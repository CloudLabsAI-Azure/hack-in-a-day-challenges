"""
SQL Modernization Platform - Streamlit Application
Complete web application for Oracle to Azure SQL migration with AI-powered translation, validation, and optimization.
"""

import streamlit as st
from agents import SQLModernizationAgent
from cosmos_helper import CosmosDBHelper
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="SQL Modernization Platform",
    page_icon="💾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0078D4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.agent = None
    st.session_state.cosmos = None
    st.session_state.translated_sql = None
    st.session_state.translation_id = None
    st.session_state.validation_complete = False
    st.session_state.optimization_complete = False

# Initialize connections
def initialize_connections():
    """Initialize Azure OpenAI and Cosmos DB connections"""
    try:
        # Initialize agent
        st.session_state.agent = SQLModernizationAgent(
            openai_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            openai_key=os.getenv("AZURE_OPENAI_KEY"),
            deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION")
        )
        
        # Initialize Cosmos DB
        st.session_state.cosmos = CosmosDBHelper(
            endpoint=os.getenv("COSMOS_ENDPOINT"),
            key=os.getenv("COSMOS_KEY"),
            database_name=os.getenv("DATABASE_NAME")
        )
        
        st.session_state.initialized = True
        return True
    except Exception as e:
        st.error(f"Failed to initialize connections: {str(e)}")
        st.error("Please check your .env file configuration.")
        return False

# Initialize on first run
if not st.session_state.initialized:
    with st.spinner("Initializing connections to Azure services..."):
        initialize_connections()

# Header
st.markdown('<div class="main-header">SQL Modernization Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Translate Oracle SQL to Azure SQL with AI-powered validation and optimization</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select Page", ["🔄 Translate SQL", "📁 Batch Processing", "📊 History"])
    
    st.markdown("---")
    
    st.header("About")
    st.info("This platform uses Azure OpenAI GPT-4 to modernize Oracle SQL to Azure SQL T-SQL with automated validation and optimization recommendations.")
    
    st.markdown("---")
    
    st.header("Quick Stats")
    if st.session_state.cosmos:
        try:
            recent = st.session_state.cosmos.get_recent_translations(limit=1000)
            st.metric("Total Translations", len(recent))
        except:
            st.metric("Total Translations", "N/A")
    
    st.markdown("---")
    
    if st.button("Reset Session", type="secondary"):
        st.session_state.translated_sql = None
        st.session_state.translation_id = None
        st.session_state.validation_complete = False
        st.session_state.optimization_complete = False
        st.success("Session reset!")
        st.rerun()

# Main content
if page == "🔄 Translate SQL":
    st.header("Translate Oracle SQL to Azure SQL")
    
    # Sample queries for quick testing
    with st.expander("📋 Load Sample Oracle Query"):
        sample_choice = st.selectbox(
            "Select a sample query",
            [
                "Select with SYSDATE and ROWNUM",
                "NVL and DECODE usage",
                "Cursor-based update",
                "CONNECT BY hierarchical query"
            ]
        )
        
        samples = {
            "Select with SYSDATE and ROWNUM": "SELECT emp_id, emp_name, hire_date\nFROM employees\nWHERE hire_date > SYSDATE - 30\nAND ROWNUM <= 10;",
            "NVL and DECODE usage": "SELECT emp_id,\n       NVL(commission, 0) as commission,\n       DECODE(dept_id, 10, 'Sales', 20, 'Marketing', 'Other') as department\nFROM employees;",
            "Cursor-based update": "DECLARE\n  CURSOR emp_cursor IS\n    SELECT emp_id, salary FROM employees WHERE dept_id = 10;\nBEGIN\n  FOR emp_rec IN emp_cursor LOOP\n    UPDATE employees\n    SET bonus = emp_rec.salary * 0.1\n    WHERE emp_id = emp_rec.emp_id;\n  END LOOP;\n  COMMIT;\nEND;",
            "CONNECT BY hierarchical query": "SELECT emp_id, emp_name, manager_id, LEVEL\nFROM employees\nSTART WITH manager_id IS NULL\nCONNECT BY PRIOR emp_id = manager_id;"
        }
        
        if st.button("Load Sample"):
            st.session_state.sample_sql = samples[sample_choice]
    
    # Input
    oracle_sql = st.text_area(
        "Oracle SQL Code",
        height=250,
        placeholder="Enter Oracle SQL here or load a sample query...",
        value=st.session_state.get('sample_sql', '')
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        translate_btn = st.button("🔄 Translate", type="primary", use_container_width=True)
    with col2:
        validate_btn = st.button("✓ Validate", disabled=not st.session_state.translated_sql, use_container_width=True)
    with col3:
        optimize_btn = st.button("⚡ Optimize", disabled=not st.session_state.validation_complete, use_container_width=True)
    
    # Translation
    if translate_btn and oracle_sql:
        with st.spinner("Translating SQL..."):
            result = st.session_state.agent.translate_oracle_to_azure_sql(oracle_sql)
            
            if result["success"]:
                st.session_state.translated_sql = result["translated_sql"]
                st.session_state.translation_id = st.session_state.cosmos.save_translation(
                    source_sql=oracle_sql,
                    translated_sql=result["translated_sql"],
                    metadata={"tokens_used": result["tokens_used"]}
                )
                
                st.markdown('<div class="success-box">✓ Translation completed successfully!</div>', unsafe_allow_html=True)
                
                # Display results side by side
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Oracle SQL (Original)")
                    st.code(oracle_sql, language="sql", line_numbers=True)
                
                with col2:
                    st.subheader("Azure SQL (Translated)")
                    st.code(result["translated_sql"], language="sql", line_numbers=True)
                
                # Metrics
                metric_col1, metric_col2, metric_col3 = st.columns(3)
                with metric_col1:
                    st.metric("Tokens Used", result["tokens_used"])
                with metric_col2:
                    st.metric("Source Lines", len(oracle_sql.split('\n')))
                with metric_col3:
                    st.metric("Target Lines", len(result["translated_sql"].split('\n')))
                
                # Download button
                st.download_button(
                    label="📥 Download Translated SQL",
                    data=result["translated_sql"],
                    file_name="translated_query.sql",
                    mime="text/plain",
                    use_container_width=True
                )
            else:
                st.markdown(f'<div class="error-box">✗ Translation failed: {result.get("error", "Unknown error")}</div>', unsafe_allow_html=True)
    
    # Validation
    if validate_btn and st.session_state.translated_sql:
        with st.spinner("Validating SQL..."):
            validation_result = st.session_state.agent.validate_sql(st.session_state.translated_sql)
            
            st.session_state.cosmos.save_validation(
                translation_id=st.session_state.translation_id,
                validation_results=validation_result
            )
            
            # Display validation results
            st.subheader("Validation Results")
            
            if validation_result["overall_valid"]:
                st.markdown('<div class="success-box">✓ SQL validation passed!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error-box">✗ SQL validation failed</div>', unsafe_allow_html=True)
            
            # Show AI validation details
            ai_validation = validation_result.get("validations", {}).get("ai", {})
            parser_validation = validation_result.get("validations", {}).get("parser", {})
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### AI-Based Validation")
                if ai_validation.get("valid"):
                    st.success(f"✓ Valid (Confidence: {ai_validation.get('confidence', 0):.0%})")
                else:
                    st.error("✗ Invalid")
                
                issues = ai_validation.get("issues", [])
                if issues:
                    st.warning(f"Found {len(issues)} issues:")
                    for issue in issues:
                        severity = issue.get('severity', 'info').upper()
                        message = issue.get('message', '')
                        st.write(f"- [{severity}] {message}")
                
                suggestions = ai_validation.get("suggestions", [])
                if suggestions:
                    st.info("Suggestions:")
                    for suggestion in suggestions:
                        st.write(f"- {suggestion}")
            
            with col2:
                st.markdown("#### Parser-Based Validation")
                if parser_validation.get("valid"):
                    st.success("✓ Syntax Valid")
                else:
                    st.error("✗ Syntax Invalid")
                
                st.metric("Statements", parser_validation.get("statement_count", 0))
                
                if parser_validation.get("formatted"):
                    with st.expander("View Formatted SQL"):
                        st.code(parser_validation["formatted"], language="sql")
            
            st.session_state.validation_complete = True
    
    # Optimization
    if optimize_btn and st.session_state.validation_complete:
        with st.spinner("Analyzing optimization opportunities..."):
            optimization_result = st.session_state.agent.optimize_sql(st.session_state.translated_sql)
            
            st.session_state.cosmos.save_optimization(
                translation_id=st.session_state.translation_id,
                optimization_results=optimization_result
            )
            
            # Display optimization results
            st.subheader("Optimization Recommendations")
            
            score = optimization_result.get("overall_score", 0)
            
            # Score with color coding
            if score >= 80:
                st.success(f"Optimization Score: {score}/100 - Excellent!")
            elif score >= 60:
                st.warning(f"Optimization Score: {score}/100 - Good, but improvements possible")
            else:
                st.error(f"Optimization Score: {score}/100 - Needs optimization")
            
            # Priority optimizations
            priorities = optimization_result.get("priority_optimizations", [])
            if priorities:
                st.markdown("#### High Priority Recommendations")
                for idx, opt in enumerate(priorities, 1):
                    priority = opt.get('priority', 'MEDIUM')
                    category = opt.get('category', 'General')
                    
                    with st.expander(f"{idx}. [{priority}] {category}: {opt.get('recommendation', '')[:50]}..."):
                        st.write(f"**Recommendation:** {opt.get('recommendation', '')}")
                        st.write(f"**Reason:** {opt.get('reason', '')}")
                        st.write(f"**Estimated Impact:** {opt.get('estimated_impact', 'Unknown')}")
            
            # Index recommendations
            indexes = optimization_result.get("index_recommendations", [])
            if indexes:
                st.markdown("#### Index Recommendations")
                for idx in indexes:
                    st.write(f"- **{idx.get('index_name', 'Recommended Index')}** on {idx.get('table', 'table')}({idx.get('columns', '')})")
                    st.write(f"  Type: {idx.get('index_type', 'Non-clustered')} - {idx.get('reason', '')}")
            
            # Azure features
            azure_features = optimization_result.get("azure_features", [])
            if azure_features:
                st.markdown("#### Azure SQL Features to Consider")
                for feature in azure_features:
                    with st.expander(f"🔹 {feature.get('feature_name', 'Feature')}"):
                        st.write(f"**Benefit:** {feature.get('benefit', '')}")
                        st.write(f"**Implementation:** {feature.get('implementation_notes', '')}")
            
            # Query rewrites
            rewrites = optimization_result.get("query_rewrites", [])
            if rewrites:
                st.markdown("#### Query Rewrite Suggestions")
                for rewrite in rewrites:
                    st.write(f"- {rewrite.get('suggested_rewrite', '')}")
                    if 'example' in rewrite:
                        st.code(rewrite['example'], language="sql")
            
            st.session_state.optimization_complete = True

elif page == "📁 Batch Processing":
    st.header("Batch SQL File Processing")
    
    st.info("Upload multiple Oracle SQL files for batch translation, validation, and optimization.")
    
    uploaded_files = st.file_uploader(
        "Upload Oracle SQL files",
        type=['sql', 'txt'],
        accept_multiple_files=True,
        help="Select one or more SQL files to process"
    )
    
    if uploaded_files:
        st.success(f"Loaded {len(uploaded_files)} file(s)")
        
        # Preview files
        with st.expander("Preview uploaded files"):
            for file in uploaded_files:
                st.write(f"**{file.name}** ({file.size} bytes)")
        
        process_batch = st.button("🚀 Process All Files", type="primary", use_container_width=True)
        
        if process_batch:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            results = []
            
            for idx, file in enumerate(uploaded_files):
                status_text.text(f"Processing {file.name}... ({idx + 1}/{len(uploaded_files)})")
                
                try:
                    oracle_sql = file.read().decode('utf-8')
                    
                    # Translate
                    translation = st.session_state.agent.translate_oracle_to_azure_sql(oracle_sql)
                    
                    if translation["success"]:
                        # Validate
                        validation = st.session_state.agent.validate_sql(translation["translated_sql"])
                        
                        # Optimize
                        optimization = st.session_state.agent.optimize_sql(translation["translated_sql"])
                        
                        # Save to Cosmos
                        translation_id = st.session_state.cosmos.save_translation(
                            source_sql=oracle_sql,
                            translated_sql=translation["translated_sql"],
                            metadata={"filename": file.name}
                        )
                        
                        if translation_id:
                            st.session_state.cosmos.save_validation(translation_id, validation)
                            st.session_state.cosmos.save_optimization(translation_id, optimization)
                        
                        results.append({
                            "File": file.name,
                            "Status": "✓ Success",
                            "Valid": "✓" if validation.get("overall_valid", False) else "✗",
                            "Opt Score": f"{optimization.get('overall_score', 0)}/100"
                        })
                    else:
                        results.append({
                            "File": file.name,
                            "Status": "✗ Failed",
                            "Valid": "N/A",
                            "Opt Score": "N/A"
                        })
                
                except Exception as e:
                    results.append({
                        "File": file.name,
                        "Status": f"✗ Error: {str(e)[:30]}...",
                        "Valid": "N/A",
                        "Opt Score": "N/A"
                    })
                
                progress_bar.progress((idx + 1) / len(uploaded_files))
            
            status_text.text("✓ Processing complete!")
            
            # Display results table
            st.subheader("Batch Processing Results")
            st.table(results)
            
            # Summary metrics
            col1, col2, col3 = st.columns(3)
            success_count = sum(1 for r in results if "Success" in r["Status"])
            valid_count = sum(1 for r in results if r["Valid"] == "✓")
            
            with col1:
                st.metric("Total Processed", len(results))
            with col2:
                st.metric("Successful", success_count)
            with col3:
                st.metric("Valid SQL", valid_count)

elif page == "📊 History":
    st.header("Translation History")
    
    # Refresh button
    if st.button("🔄 Refresh History"):
        st.rerun()
    
    recent_translations = st.session_state.cosmos.get_recent_translations(limit=50)
    
    if recent_translations:
        st.info(f"Showing {len(recent_translations)} most recent translations")
        
        for trans in recent_translations:
            timestamp = trans.get('timestamp', 'Unknown time')
            source_dialect = trans.get('sourceDialect', 'Oracle')
            target_dialect = trans.get('target_dialect', 'Azure SQL')
            
            with st.expander(f"📝 {timestamp} - {source_dialect} to {target_dialect}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Source SQL:**")
                    source_preview = trans.get('source_sql', '')[:300]
                    st.code(source_preview + ("..." if len(trans.get('source_sql', '')) > 300 else ""), language="sql")
                
                with col2:
                    st.write("**Translated SQL:**")
                    translated_preview = trans.get('translated_sql', '')[:300]
                    st.code(translated_preview + ("..." if len(trans.get('translated_sql', '')) > 300 else ""), language="sql")
                
                # Show metadata if available
                metadata = trans.get('metadata', {})
                if metadata:
                    st.write(f"**Metadata:** {metadata}")
                
                # Download full translation
                st.download_button(
                    label="Download Full Translation",
                    data=trans.get('translated_sql', ''),
                    file_name=f"translation_{trans['id'][:8]}.sql",
                    mime="text/plain",
                    key=f"download_{trans['id']}"
                )
    else:
        st.info("No translation history available. Start by translating some SQL queries!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        SQL Modernization Platform | Powered by Azure OpenAI GPT-4 | Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
