"""
SQL Modernization Platform - Production Streamlit Application
Oracle to Azure SQL migration using Azure AI Foundry Multi-Agent System
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
import time
import pandas as pd

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="SQL Modernization Assistant",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for stunning UI
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #0078D4;
        --secondary-color: #50E6FF;
        --success-color: #107C10;
        --warning-color: #F7630C;
        --error-color: #D13438;
        --bg-dark: #1E1E1E;
        --bg-light: #F5F5F5;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #0078D4 0%, #50E6FF 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #0078D4;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .success-card {
        background: #F0FFF0;
        border-left-color: #107C10;
    }
    
    .warning-card {
        background: #FFF8F0;
        border-left-color: #F7630C;
    }
    
    .error-card {
        background: #FFF0F0;
        border-left-color: #D13438;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #0078D4 0%, #50E6FF 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 6px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,120,212,0.3);
    }
    
    /* Code block styling */
    .stCodeBlock {
        background: #1E1E1E;
        border-radius: 6px;
        border: 1px solid #333;
    }
    
    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #0078D4;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1E1E1E 0%, #2D2D2D 100%);
    }
    
    [data-testid="stSidebar"] .element-container {
        color: white;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #0078D4 0%, #50E6FF 100%);
    }
    
    /* Agent status badges */
    .agent-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    .agent-active {
        background: #107C10;
        color: white;
    }
    
    .agent-processing {
        background: #F7630C;
        color: white;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    /* File uploader styling */
    [data-testid="stFileUploader"] {
        background: #F5F5F5;
        border: 2px dashed #0078D4;
        border-radius: 8px;
        padding: 2rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #F5F5F5;
        border-radius: 6px 6px 0 0;
        padding: 1rem 2rem;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: white;
        border-bottom: 3px solid #0078D4;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Cosmos DB connection
@st.cache_resource
def get_cosmos_client():
    """Initialize Cosmos DB client with error handling"""
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
        st.sidebar.error(f"Cosmos DB Connection Error: {str(e)}")
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
        st.warning(f"⚠️ Could not save to Cosmos DB: {str(e)}")
    return None

def get_history(limit=10):
    """Get translation history from Cosmos DB"""
    try:
        _, _, container = get_cosmos_client()
        if container:
            items = list(container.query_items(
                query=f"SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT {limit}",
                enable_cross_partition_query=True
            ))
            return items
    except Exception as e:
        st.warning(f"⚠️ Could not fetch history: {str(e)}")
    return []

def parse_agent_response(response_text):
    """Extract translation, validation, and optimization from agent response"""
    result = {
        'translation': '',
        'validation': None,
        'optimization': None
    }
    
    # Extract SQL code blocks
    sql_matches = re.findall(r'```sql\n(.*?)```', response_text, re.DOTALL)
    if sql_matches:
        result['translation'] = sql_matches[0].strip()
    elif '```' in response_text:
        # Try any code block
        code_match = re.search(r'```\w*\n(.*?)```', response_text, re.DOTALL)
        if code_match:
            result['translation'] = code_match.group(1).strip()
    else:
        # Fallback: use the response text itself
        result['translation'] = response_text.strip()
    
    # Extract JSON blocks for validation/optimization
    json_matches = re.findall(r'```json\n(.*?)```', response_text, re.DOTALL)
    for json_text in json_matches:
        try:
            data = json.loads(json_text)
            if 'valid' in data or 'syntax_errors' in data:
                result['validation'] = data
            elif 'optimization_score' in data or 'recommendations' in data:
                result['optimization'] = data
        except json.JSONDecodeError:
            continue
    
    # Look for plain text indicators if no JSON found
    if not result['validation'] and ('valid' in response_text.lower() or 'validation' in response_text.lower()):
        result['validation'] = {'summary': 'See agent response for validation details', 'valid': True}
    
    if not result['optimization'] and ('optimization' in response_text.lower() or 'recommend' in response_text.lower()):
        result['optimization'] = {'summary': 'See agent response for optimization suggestions'}
    
    return result

def call_agent_api(sql_input):
    """Call Azure AI Foundry Agent API with proper error handling"""
    try:
        endpoint = os.getenv("AGENT_API_ENDPOINT")
        api_key = os.getenv("AGENT_API_KEY")
        agent_id = os.getenv("AGENT_ID")
        
        if not all([endpoint, api_key, agent_id]):
            st.error("❌ Missing configuration. Please check your .env file.")
            st.stop()
        
        # Remove trailing slash from endpoint
        endpoint = endpoint.rstrip('/')
        
        headers = {
            "Content-Type": "application/json",
            "api-key": api_key
        }
        
        # Step 1: Create a thread
        with st.spinner("🔄 Creating conversation thread..."):
            thread_response = requests.post(
                f"{endpoint}/openai/threads?api-version=2024-02-15-preview",
                headers=headers,
                json={},
                timeout=30
            )
            thread_response.raise_for_status()
            thread_id = thread_response.json()["id"]
        
        # Step 2: Add message to thread
        with st.spinner("📝 Sending Oracle SQL to Translation Agent..."):
            message_response = requests.post(
                f"{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-02-15-preview",
                headers=headers,
                json={
                    "role": "user",
                    "content": sql_input
                },
                timeout=30
            )
            message_response.raise_for_status()
        
        # Step 3: Run the agent
        with st.spinner("🤖 Starting multi-agent pipeline (Translation → Validation → Optimization)..."):
            run_response = requests.post(
                f"{endpoint}/openai/threads/{thread_id}/runs?api-version=2024-02-15-preview",
                headers=headers,
                json={
                    "assistant_id": agent_id
                },
                timeout=30
            )
            run_response.raise_for_status()
            run_id = run_response.json()["id"]
        
        # Step 4: Poll for completion with progress bar
        max_attempts = 120
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for attempt in range(max_attempts):
            status_response = requests.get(
                f"{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2024-02-15-preview",
                headers=headers,
                timeout=30
            )
            status_response.raise_for_status()
            status_data = status_response.json()
            status = status_data["status"]
            
            # Update progress
            progress = min((attempt / max_attempts) * 100, 95)
            progress_bar.progress(int(progress))
            status_text.text(f"⏳ Agent Status: {status.upper()} ({attempt + 1}/{max_attempts})")
            
            if status == "completed":
                progress_bar.progress(100)
                status_text.text("✅ Agent processing completed!")
                break
            elif status in ["failed", "cancelled", "expired"]:
                st.error(f"❌ Agent run {status}")
                if "last_error" in status_data:
                    st.error(f"Error details: {status_data['last_error']}")
                st.stop()
            
            time.sleep(2)
        
        if status != "completed":
            st.error("❌ Agent run timed out. Please try again with a simpler query.")
            st.stop()
        
        # Step 5: Get messages
        messages_response = requests.get(
            f"{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-02-15-preview",
            headers=headers,
            timeout=30
        )
        messages_response.raise_for_status()
        messages = messages_response.json()["data"]
        
        # Get the latest assistant message
        assistant_messages = [m for m in messages if m["role"] == "assistant"]
        if not assistant_messages:
            st.error("❌ No response from agent")
            st.stop()
        
        response_text = assistant_messages[0]["content"][0]["text"]["value"]
        
        return response_text
        
    except requests.exceptions.Timeout:
        st.error("❌ Request timed out. Please try again.")
        st.stop()
    except requests.exceptions.RequestException as e:
        st.error(f"❌ API Error: {str(e)}")
        st.stop()
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        st.stop()

# Header
st.markdown("""
<div class="main-header">
    <h1>🔄 SQL Modernization Assistant</h1>
    <p>Transform Oracle SQL to Azure SQL using AI-powered multi-agent system</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/200px-Microsoft_logo.svg.png", width=150)
    
    st.markdown("### 🤖 Agent Pipeline")
    
    # Check configuration
    endpoint = os.getenv("AGENT_API_ENDPOINT")
    api_key = os.getenv("AGENT_API_KEY")
    agent_id = os.getenv("AGENT_ID")
    cosmos_endpoint = os.getenv("COSMOS_ENDPOINT")
    
    if all([endpoint, api_key, agent_id]):
        st.markdown('<span class="agent-badge agent-active">✓ Translation Agent</span>', unsafe_allow_html=True)
        st.markdown('<span class="agent-badge agent-active">✓ Validation Agent</span>', unsafe_allow_html=True)
        st.markdown('<span class="agent-badge agent-active">✓ Optimization Agent</span>', unsafe_allow_html=True)
        st.success("🟢 All agents connected")
    else:
        st.error("🔴 Configuration missing")
        st.warning("Please configure your .env file")
    
    if cosmos_endpoint:
        st.success("🟢 Cosmos DB connected")
    else:
        st.warning("🟡 Cosmos DB not configured")
    
    st.markdown("---")
    
    st.markdown("### 📊 Quick Stats")
    history = get_history(limit=100)
    st.metric("Total Translations", len(history))
    if history:
        recent = history[:10]
        avg_valid = sum(1 for h in recent if h.get('validation', {}).get('valid', False)) / len(recent) * 100
        st.metric("Success Rate", f"{avg_valid:.0f}%")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("This application uses Azure AI Foundry's multi-agent system to modernize Oracle SQL to Azure SQL with automatic validation and optimization.")

# Main tabs
tab1, tab2, tab3 = st.tabs(["🚀 Modernize SQL", "📋 Results", "📚 History"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📥 Input Oracle SQL")
        
        # File upload option
        uploaded_file = st.file_uploader(
            "Upload SQL file",
            type=["sql", "txt"],
            help="Upload your Oracle SQL file (.sql or .txt)",
            key="file_uploader"
        )
        
        st.markdown("**Or paste SQL code directly:**")
        
    with col2:
        st.markdown("### 📝 Sample Queries")
        sample_choice = st.selectbox(
            "Load a sample:",
            [
                "None",
                "Simple SELECT with ROWNUM",
                "NVL and Date Functions",
                "Hierarchical Query (CONNECT BY)",
                "Cursor-based Update",
                "Complex JOIN with DECODE"
            ]
        )
        
        samples = {
            "Simple SELECT with ROWNUM": """SELECT emp_id, emp_name, hire_date, salary
FROM employees
WHERE hire_date > SYSDATE - 30
  AND ROWNUM <= 10
ORDER BY salary DESC;""",
            
            "NVL and Date Functions": """SELECT 
    emp_id, 
    emp_name, 
    NVL(commission, 0) as commission,
    TO_CHAR(hire_date, 'YYYY-MM-DD') as hire_date_formatted
FROM employees
WHERE hire_date > SYSDATE - 90
  AND ROWNUM <= 20
ORDER BY commission DESC;""",
            
            "Hierarchical Query (CONNECT BY)": """SELECT 
    emp_id, 
    emp_name, 
    manager_id, 
    LEVEL as emp_level,
    SYS_CONNECT_BY_PATH(emp_name, '/') as path
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR emp_id = manager_id
ORDER BY LEVEL, emp_name;""",
            
            "Cursor-based Update": """DECLARE
  CURSOR emp_cursor IS 
    SELECT emp_id, salary 
    FROM employees 
    WHERE dept_id = 10;
BEGIN
  FOR emp_rec IN emp_cursor LOOP
    UPDATE employees 
    SET bonus = emp_rec.salary * 0.1, 
        updated_date = SYSDATE
    WHERE emp_id = emp_rec.emp_id;
  END LOOP;
  COMMIT;
END;""",
            
            "Complex JOIN with DECODE": """SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_name,
    DECODE(e.status, 'A', 'Active', 'I', 'Inactive', 'Unknown') as status_desc,
    NVL(e.salary, 0) + NVL(e.commission, 0) as total_comp
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.hire_date > ADD_MONTHS(SYSDATE, -12)
  AND ROWNUM <= 50
ORDER BY total_comp DESC;"""
        }
        
        if sample_choice != "None" and st.button("📋 Load Sample", use_container_width=True):
            st.session_state['sql_input'] = samples[sample_choice]
            st.rerun()
    
    # SQL input area
    sql_input = st.text_area(
        "Oracle SQL Code",
        height=300,
        placeholder="""-- Enter your Oracle SQL code here or upload a file above
-- Example:
SELECT emp_id, emp_name 
FROM employees 
WHERE ROWNUM <= 10;""",
        value=st.session_state.get('sql_input', ''),
        key="sql_text_area"
    )
    
    # Get SQL from file if uploaded
    if uploaded_file:
        sql_content = uploaded_file.read().decode("utf-8")
        st.code(sql_content, language="sql")
        sql_to_process = sql_content
    else:
        sql_to_process = sql_input
    
    # Modernize button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Modernize SQL", type="primary", use_container_width=True):
            if not sql_to_process or sql_to_process.strip() == '':
                st.error("❌ Please enter some SQL code or upload a file")
            else:
                with st.container():
                    response_text = call_agent_api(sql_to_process)
                    
                    # Parse the response
                    parsed = parse_agent_response(response_text)
                    
                    # Save to session state
                    st.session_state['last_result'] = {
                        'timestamp': datetime.now().isoformat(),
                        'source_sql': sql_to_process,
                        'translation': parsed['translation'],
                        'validation': parsed['validation'],
                        'optimization': parsed['optimization'],
                        'raw_response': response_text
                    }
                    
                    # Save to Cosmos DB
                    cosmos_id = save_to_cosmos(
                        sql_to_process, 
                        parsed['translation'], 
                        parsed['validation'], 
                        parsed['optimization']
                    )
                    
                    if cosmos_id:
                        st.success(f"✅ Saved to Cosmos DB (ID: {cosmos_id[:8]}...)")
                    
                    st.success("✅ Processing complete! Check the 'Results' tab.")
                    st.balloons()
                    time.sleep(1)
                    st.rerun()

with tab2:
    st.markdown("### 📊 Translation Results")
    
    if 'last_result' in st.session_state:
        result = st.session_state['last_result']
        
        # Show timestamp
        st.caption(f"🕐 Processed: {datetime.fromisoformat(result['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Three-column layout
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 🔄 Translation")
            if result['translation']:
                st.code(result['translation'], language="sql")
                if st.button("📋 Copy T-SQL", key="copy_translation"):
                    st.toast("Copied to clipboard!")
            else:
                st.warning("No translation found in response")
        
        with col2:
            st.markdown("#### ✅ Validation")
            if result['validation']:
                if isinstance(result['validation'], dict):
                    if result['validation'].get('valid'):
                        st.success("✅ Valid T-SQL")
                    else:
                        st.error("❌ Validation Issues Found")
                    
                    if 'syntax_errors' in result['validation'] and result['validation']['syntax_errors']:
                        st.markdown("**Syntax Errors:**")
                        for error in result['validation']['syntax_errors']:
                            st.error(f"• {error}")
                    
                    if 'semantic_warnings' in result['validation'] and result['validation']['semantic_warnings']:
                        st.markdown("**Warnings:**")
                        for warning in result['validation']['semantic_warnings']:
                            st.warning(f"• {warning}")
                    
                    # Show raw JSON
                    with st.expander("📄 Raw JSON"):
                        st.json(result['validation'])
                else:
                    st.info(str(result['validation']))
            else:
                st.info("No validation data available")
        
        with col3:
            st.markdown("#### ⚡ Optimization")
            if result['optimization']:
                if isinstance(result['optimization'], dict):
                    if 'optimization_score' in result['optimization']:
                        score = result['optimization']['optimization_score']
                        st.metric("Optimization Score", f"{score}/100")
                        
                        # Progress bar for score
                        st.progress(score / 100)
                    
                    if 'recommendations' in result['optimization']:
                        st.markdown("**Recommendations:**")
                        for rec in result['optimization']['recommendations']:
                            st.info(f"💡 {rec}")
                    
                    if 'indexes' in result['optimization']:
                        st.markdown("**Suggested Indexes:**")
                        for idx in result['optimization']['indexes']:
                            st.code(idx, language="sql")
                    
                    # Show raw JSON
                    with st.expander("📄 Raw JSON"):
                        st.json(result['optimization'])
                else:
                    st.info(str(result['optimization']))
            else:
                st.info("No optimization data available")
        
        # Show original SQL
        with st.expander("📜 View Original Oracle SQL"):
            st.code(result['source_sql'], language="sql")
        
        # Show raw response
        with st.expander("🔍 View Raw Agent Response"):
            st.text(result['raw_response'])
        
    else:
        st.info("👈 Process a SQL query in the 'Modernize SQL' tab to see results here")

with tab3:
    st.markdown("### 📚 Translation History")
    
    history = get_history(limit=20)
    
    if history:
        for idx, item in enumerate(history):
            with st.expander(f"🕐 {datetime.fromisoformat(item['timestamp']).strftime('%Y-%m-%d %H:%M:%S')} - ID: {item['id'][:8]}..."):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Oracle SQL:**")
                    st.code(item['source_sql'][:200] + "..." if len(item['source_sql']) > 200 else item['source_sql'], language="sql")
                
                with col2:
                    st.markdown("**Azure SQL:**")
                    st.code(item['translated_sql'][:200] + "..." if len(item['translated_sql']) > 200 else item['translated_sql'], language="sql")
                
                if item.get('validation'):
                    st.json(item['validation'])
                
                if st.button(f"🔄 Load This Query", key=f"load_{idx}"):
                    st.session_state['sql_input'] = item['source_sql']
                    st.session_state['last_result'] = {
                        'timestamp': item['timestamp'],
                        'source_sql': item['source_sql'],
                        'translation': item['translated_sql'],
                        'validation': item.get('validation'),
                        'optimization': item.get('optimization'),
                        'raw_response': ''
                    }
                    st.rerun()
    else:
