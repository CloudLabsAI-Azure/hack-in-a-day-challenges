"""
SQL Modernization Platform - Streamlit Application
Web interface for Oracle to Azure SQL migration using Azure AI Foundry Agents
"""

import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from azure.cosmos import CosmosClient, exceptions
import uuid
import re

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="SQL Modernization Assistant",
    page_icon="🔄",
    layout="wide"
)

# Initialize Cosmos DB connection
@st.cache_resource
def get_cosmos_client():
    """Initialize Cosmos DB client"""
    try:
        endpoint = os.getenv("COSMOS_ENDPOINT")
        key = os.getenv("COSMOS_KEY")
        database_name = os.getenv("DATABASE_NAME")
        
        if not all([endpoint, key, database_name]):
            return None, None, None
            
        client = CosmosClient(endpoint, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client("TranslationResults")
        return client, database, container
    except Exception as e:
        st.error(f"Cosmos DB Error: {str(e)}")
        return None, None, None

def save_to_cosmos(source_sql, translated_sql, validation_result, optimization_result):
    """Save translation results to Cosmos DB"""
    try:
        _, _, container = get_cosmos_client()
        if container:
            item = {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.utcnow().isoformat(),
                "source_sql": source_sql,
                "translated_sql": translated_sql,
                "validation": validation_result,
                "optimization": optimization_result,
                "sourceDialect": "Oracle",
                "targetDialect": "Azure SQL"
            }
            container.create_item(body=item)
            return item["id"]
    except Exception as e:
        st.warning(f"Could not save to Cosmos DB: {str(e)}")
    return None

def get_history():
    """Get translation history from Cosmos DB"""
    try:
        _, _, container = get_cosmos_client()
        if container:
            items = list(container.query_items(
                query="SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT 10",
                enable_cross_partition_query=True
            ))
            return items
    except Exception as e:
        st.warning(f"Could not fetch history: {str(e)}")
    return []

def parse_agent_response(response_text):
    """Extract translation, validation, and optimization from agent response"""
    result = {
        'translation': '',
        'validation': None,
        'optimization': None
    }
    
    # Extract SQL code
    sql_match = re.search(r'```sql\n(.*?)```', response_text, re.DOTALL)
    if sql_match:
        result['translation'] = sql_match.group(1).strip()
    else:
        # If no code block, take first line as translation
        result['translation'] = response_text.split('\n')[0].strip()
    
    # Extract JSON blocks for validation/optimization
    json_matches = re.findall(r'```json\n(.*?)```', response_text, re.DOTALL)
    for json_text in json_matches:
        try:
            data = json.loads(json_text)
            if 'valid' in data or 'syntax_errors' in data:
                result['validation'] = data
            elif 'optimization_score' in data or 'recommendations' in data:
                result['optimization'] = data
        except:
            continue
    
    # Look for plain text validation/optimization
    if 'Validation:' in response_text:
        val_match = re.search(r'Validation:(.*?)(?:Optimization|$)', response_text, re.DOTALL)
        if val_match:
            result['validation'] = {'summary': val_match.group(1).strip()}
    
    if 'Optimization' in response_text or 'recommendations' in response_text.lower():
        opt_match = re.search(r'Optimization.*?:(.*?)$', response_text, re.DOTALL)
        if opt_match:
            result['optimization'] = {'summary': opt_match.group(1).strip()}
    
    return result

# Main UI
st.title("Oracle to Azure SQL Modernization")
st.markdown("Transform your Oracle SQL using AI-powered agents for translation, validation, and optimization.")

# Sidebar
with st.sidebar:
    st.header("Agent Pipeline")
    st.info("1. Translation Agent\n2. Validation Agent\n3. Optimization Agent")
    
    st.header("Configuration")
    endpoint = os.getenv("AGENT_API_ENDPOINT")
    if endpoint:
        st.success("✓ Connected to Azure AI Foundry")
    else:
        st.error("✗ Missing Agent API configuration")
    
    cosmos_status = get_cosmos_client()[0] is not None
    if cosmos_status:
        st.success("✓ Connected to Cosmos DB")
    else:
        st.warning("✗ Cosmos DB not configured")

# Tabs
tab1, tab2, tab3 = st.tabs(["SQL Modernization", "Translation Results", "History"])

with tab1:
    st.header("Input Oracle SQL")
    
    # Sample queries
    with st.expander("📋 Load Sample Query"):
        sample = st.selectbox("Choose a sample:", [
            "Simple SELECT with ROWNUM",
            "NVL and Date Functions",
            "Hierarchical Query (CONNECT BY)",
            "Cursor-based Update"
        ])
        
        samples = {
            "Simple SELECT with ROWNUM": "SELECT emp_id, emp_name, hire_date, salary\nFROM employees\nWHERE hire_date > SYSDATE - 30\n  AND ROWNUM <= 10\nORDER BY salary DESC;",
            "NVL and Date Functions": "SELECT emp_id, emp_name, NVL(commission, 0) as commission\nFROM employees\nWHERE hire_date > SYSDATE - 90\n  AND ROWNUM <= 20\nORDER BY commission DESC;",
            "Hierarchical Query (CONNECT BY)": "SELECT emp_id, emp_name, manager_id, LEVEL as emp_level\nFROM employees\nSTART WITH manager_id IS NULL\nCONNECT BY PRIOR emp_id = manager_id;",
            "Cursor-based Update": "DECLARE\n  CURSOR emp_cursor IS SELECT emp_id, salary FROM employees WHERE dept_id = 10;\nBEGIN\n  FOR emp_rec IN emp_cursor LOOP\n    UPDATE employees SET bonus = emp_rec.salary * 0.1 WHERE emp_id = emp_rec.emp_id;\n  END LOOP;\n  COMMIT;\nEND;"
        }
        
        if st.button("Load Sample"):
            st.session_state['sample_sql'] = samples[sample]
    
    sql_input = st.text_area(
        "Oracle SQL Code",
        height=250,
        placeholder="SELECT emp_id, emp_name FROM employees WHERE ROWNUM <= 10;",
        value=st.session_state.get('sample_sql', '')
    )
    
    if st.button("🔄 Modernize SQL", type="primary"):
        if not sql_input:
            st.error("Please enter some SQL code")
        else:
            with st.spinner("Processing through 3-agent pipeline..."):
                try:
                    endpoint = os.getenv("AGENT_API_ENDPOINT")
                    api_key = os.getenv("AGENT_API_KEY")
                    
                    if not endpoint or not api_key:
                        st.error("Missing AGENT_API_ENDPOINT or AGENT_API_KEY in .env file")
                        st.stop()
                    
                    headers = {
                        "Content-Type": "application/json",
                        "api-key": api_key
                    }
                    
                    payload = {
                        "messages": [
                            {
                                "role": "user",
                                "content": sql_input
                            }
                        ]
                    }
                    
                    response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
                    
                    if response.status_code == 200:
                        result = response.json()
                        response_text = result.get('choices', [{}])[0].get('message', {}).get('content', '')
                        
                        # Parse the response
                        parsed = parse_agent_response(response_text)
                        
                        # Save to session state
                        st.session_state['last_result'] = {
                            'timestamp': datetime.now().isoformat(),
                            'source_sql': sql_input,
                            'translation': parsed['translation'],
                            'validation': parsed['validation'],
                            'optimization': parsed['optimization'],
                            'raw_response': response_text
                        }
                        
                        # Save to Cosmos DB
                        save_to_cosmos(sql_input, parsed['translation'], parsed['validation'], parsed['optimization'])
                        
                        st.success("✓ Processing complete! Check the 'Translation Results' tab.")
                        st.rerun()
                    else:
                        st.error(f"API Error {response.status_code}: {response.text}")
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")

with tab2:
    st.header("Pipeline Results")
    
    if 'last_result' in st.session_state:
        result = st.session_state['last_result']
        
        st.info(f"⏱ Processed: {result['timestamp']}")
        
        # Source SQL
        with st.expander("📄 Original Oracle SQL", expanded=False):
            st.code(result['source_sql'], language='sql')
        
        # Three-column layout
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("🔄 Translation")
            st.markdown("**SQL-Translation-Agent**")
            st.code(result['translation'], language='sql')
        
        with col2:
            st.subheader("✓ Validation")
            st.markdown("**SQL-Validation-Agent**")
            if result['validation']:
                if isinstance(result['validation'], dict):
                    if result['validation'].get('valid'):
                        st.success("Valid SQL")
                    else:
                        st.error("Invalid SQL")
                    st.json(result['validation'])
                else:
                    st.markdown(str(result['validation']))
            else:
                st.info("See raw response below")
        
        with col3:
            st.subheader("⚡ Optimization")
            st.markdown("**SQL-Optimization-Agent**")
            if result['optimization']:
                if isinstance(result['optimization'], dict):
                    score = result['optimization'].get('optimization_score', 'N/A')
                    st.metric("Optimization Score", f"{score}/100")
                    st.json(result['optimization'])
                else:
                    st.markdown(str(result['optimization']))
            else:
                st.info("See raw response below")
        
        # Raw response
        with st.expander("📋 Raw Agent Response"):
            st.text(result['raw_response'])
        
        # Download
        st.download_button(
            label="📥 Download Complete Report",
            data=json.dumps(result, indent=2),
            file_name=f"modernization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    else:
        st.info("No results yet. Go to 'SQL Modernization' tab to process a query.")

with tab3:
    st.header("Translation History")
    
    history = get_history()
    
    if history:
        for item in history:
            with st.expander(f"{item.get('timestamp', 'Unknown')} - {item.get('sourceDialect', '')} → {item.get('targetDialect', '')}"):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown("**Source SQL:**")
                    st.code(item.get('source_sql', ''), language='sql')
                
                with col_b:
                    st.markdown("**Translated SQL:**")
                    st.code(item.get('translated_sql', ''), language='sql')
                
                if item.get('validation'):
                    st.markdown("**Validation:**")
                    st.json(item['validation'])
                
                if item.get('optimization'):
                    st.markdown("**Optimization:**")
                    st.json(item['optimization'])
    else:
        st.info("No translation history yet. Process some SQL to see history here.")
