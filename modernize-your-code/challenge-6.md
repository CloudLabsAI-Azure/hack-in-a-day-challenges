# Challenge 06: Build Streamlit App with Agent API Integration

## Introduction

Your three-agent pipeline is operational and saving results to Cosmos DB. Now it's time to build a user-friendly web interface! You'll create a Streamlit application that allows users to upload Oracle SQL files, calls your Translation Agent API, receives results from all three connected agents, and displays them in a clean three-phase format (Translation | Validation | Optimization).

## Challenge Objectives

- Set up Streamlit development environment
- Create file upload interface
- Integrate with Translation Agent API endpoint
- Parse responses from all three connected agents
- Display three-phase results in organized tabs
- Add query history from Cosmos DB
- Deploy to Azure Container Apps for production access

## Steps to Complete

### Part 1: Get Agent API Endpoint

1. Go to **Azure AI Foundry Studio** → **Agents**.

2. Click on **SQL-Translation-Agent**.

3. Click **Deploy** in the top menu.

4. If not deployed, click **Deploy Agent**:
   - **Deployment name**: `sql-translation-api`
   - **Region**: **<inject key="Region"></inject>**
   - **Instance type**: Select available option

5. Wait for deployment (2-3 minutes).

6. Once deployed, you'll see:
   - **API Endpoint**: `https://your-endpoint.azure.com/...`
   - **API Key**: Click **Show** to reveal

7. Copy and save both.

### Part 2: Set Up Local Development Environment

1. Open **VS Code** or your preferred editor.

2. Create a new folder: `sql-modernization-app`

3. Inside, create a file: **requirements.txt**

```txt
streamlit==1.29.0
requests==2.31.0
python-dotenv==1.0.0
azure-cosmos==4.5.1
pandas==2.1.4
```

4. Create **.env** file:

```env
AZURE_AI_ENDPOINT=https://your-endpoint.azure.com/...
AZURE_AI_KEY=your-api-key-here
COSMOS_ENDPOINT=https://your-cosmos-account.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key-here
DATABASE_NAME=SQLModernizationDB
```

5. Replace with your actual values from previous challenges.

### Part 3: Create Main Streamlit App

Create **app.py**:

```python
import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

st.set_page_config(
    page_title="SQL Modernization Assistant",
    page_icon="🔄",
    layout="wide"
)

st.title("Oracle to Azure SQL Modernization")
st.markdown("Upload your Oracle SQL files and get instant translations, validation, and optimization recommendations.")

# Sidebar for agent info
with st.sidebar:
    st.header("Agent Pipeline")
    st.info("1. Translation Agent\n2. Validation Agent\n3. Optimization Agent")
    
    st.header("Configuration")
    endpoint = os.getenv("AZURE_AI_ENDPOINT")
    if endpoint:
        st.success("Connected to Azure AI Foundry")
    else:
        st.error("Missing API configuration")

# Main interface
tab1, tab2, tab3 = st.tabs(["SQL Upload", "Translation Results", "History"])

with tab1:
    st.header("Upload Oracle SQL File")
    
    uploaded_file = st.file_uploader(
        "Choose a .sql file",
        type=["sql"],
        help="Upload your Oracle SQL file for modernization"
    )
    
    # Text area for manual input
    st.markdown("**Or paste SQL code directly:**")
    sql_input = st.text_area(
        "Oracle SQL Code",
        height=200,
        placeholder="SELECT emp_id, emp_name FROM employees WHERE ROWNUM <= 10;"
    )
    
    if st.button("Modernize SQL", type="primary"):
        # Get SQL content
        if uploaded_file:
            sql_content = uploaded_file.read().decode("utf-8")
        elif sql_input:
            sql_content = sql_input
        else:
            st.error("Please upload a file or paste SQL code")
            st.stop()
        
        with st.spinner("Processing through agent pipeline..."):
            try:
                # Call Translation Agent API
                endpoint = os.getenv("AZURE_AI_ENDPOINT")
                api_key = os.getenv("AZURE_AI_KEY")
                
                headers = {
                    "Content-Type": "application/json",
                    "api-key": api_key
                }
                
                payload = {
                    "messages": [
                        {
                            "role": "user",
                            "content": f"Translate this Oracle SQL to Azure SQL T-SQL:\n\n{sql_content}"
                        }
                    ]
                }
                
                response = requests.post(
                    endpoint,
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Store in session state
                    st.session_state['last_result'] = {
                        'timestamp': datetime.now().isoformat(),
                        'source_sql': sql_content,
                        'response': result
                    }
                    
                    st.success("Processing complete! Check the 'Translation Results' tab.")
                    st.rerun()
                    
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")

with tab2:
    st.header("Pipeline Results")
    
    if 'last_result' in st.session_state:
        result = st.session_state['last_result']
        
        st.info(f"Processed: {result['timestamp']}")
        
        # Display source SQL
        with st.expander("Original Oracle SQL", expanded=False):
            st.code(result['source_sql'], language='sql')
        
        # Parse agent responses
        response_text = result['response'].get('choices', [{}])[0].get('message', {}).get('content', '')
        
        # Create three columns for three agents
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("Translation")
            st.markdown("**Agent 1: SQL-Translation-Agent**")
            
            # Extract translated SQL from response
            if '```sql' in response_text:
                parts = response_text.split('```sql')
                if len(parts) > 1:
                    sql_code = parts[1].split('```')[0].strip()
                    st.code(sql_code, language='sql')
                else:
                    st.code(response_text, language='sql')
            else:
                st.code(response_text, language='sql')
        
        with col2:
            st.subheader("Validation")
            st.markdown("**Agent 2: SQL-Validation-Agent**")
            
            # Since connected agents run automatically, 
            # validation results should be in the response
            if 'validation' in response_text.lower():
                st.success("Syntax validation passed")
                st.markdown(response_text)
            else:
                st.info("Validation results included in pipeline")
        
        with col3:
            st.subheader("Optimization")
            st.markdown("**Agent 3: SQL-Optimization-Agent**")
            
            if 'optimization' in response_text.lower() or 'index' in response_text.lower():
                st.markdown(response_text)
            else:
                st.info("Optimization analysis included in pipeline")
        
        # Download button
        st.download_button(
            label="Download Complete Report",
            data=json.dumps(result, indent=2),
            file_name=f"modernization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
    else:
        st.info("Upload SQL code in the 'SQL Upload' tab to see results here.")

with tab3:
    st.header("Translation History")
    
    try:
        from azure.cosmos import CosmosClient
        
        endpoint = os.getenv("COSMOS_ENDPOINT")
        key = os.getenv("COSMOS_KEY")
        database_name = os.getenv("DATABASE_NAME")
        
        if endpoint and key:
            client = CosmosClient(endpoint, credential=key)
            database = client.get_database_client(database_name)
            container = database.get_container_client("TranslationResults")
            
            # Query recent translations
            items = list(container.query_items(
                query="SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT 10",
                enable_cross_partition_query=True
            ))
            
            if items:
                for item in items:
                    with st.expander(f"{item.get('timestamp', 'Unknown')} - {item.get('sourceDialect', '')} to {item.get('target_dialect', '')}"):
                        col_a, col_b = st.columns(2)
                        
                        with col_a:
                            st.markdown("**Source SQL:**")
                            st.code(item.get('source_sql', ''), language='sql')
                        
                        with col_b:
                            st.markdown("**Translated SQL:**")
                            st.code(item.get('translated_sql', ''), language='sql')
            else:
                st.info("No translation history yet. Process some SQL files to see history here.")
        else:
            st.warning("Cosmos DB not configured. Add credentials to .env file.")
            
    except Exception as e:
        st.error(f"Error loading history: {str(e)}")
```

### Part 4: Test Locally

1. Open terminal in your project folder.

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run Streamlit:
```bash
streamlit run app.py
```

5. Browser should open automatically at `http://localhost:8501`.

6. Test the workflow:
   - Upload a .sql file or paste SQL
   - Click **Modernize SQL**
   - Check **Translation Results** tab
   - Verify three-phase output
   - Check **History** tab for saved results

### Part 5: Create Advanced Features

Create **utils/agent_parser.py** to parse agent responses better:

```python
import json
import re

def parse_agent_response(response_text):
    """
    Parse the response from connected agents pipeline
    Returns: dict with translation, validation, optimization sections
    """
    sections = {
        'translation': '',
        'validation': {},
        'optimization': {}
    }
    
    # Extract SQL code blocks
    sql_matches = re.findall(r'```sql\n(.*?)```', response_text, re.DOTALL)
    if sql_matches:
        sections['translation'] = sql_matches[0].strip()
    
    # Extract JSON blocks (validation/optimization results)
    json_matches = re.findall(r'```json\n(.*?)```', response_text, re.DOTALL)
    for json_text in json_matches:
        try:
            data = json.loads(json_text)
            if 'valid' in data or 'syntax_errors' in data:
                sections['validation'] = data
            elif 'optimization_score' in data or 'recommendations' in data:
                sections['optimization'] = data
        except json.JSONDecodeError:
            continue
    
    return sections

def format_validation_results(validation_data):
    """Format validation results for display"""
    if not validation_data:
        return "No validation data available"
    
    output = []
    
    if validation_data.get('valid'):
        output.append("✓ Syntax validation passed")
    else:
        output.append("✗ Syntax validation failed")
    
    if 'syntax_errors' in validation_data:
        output.append("\n**Syntax Errors:**")
        for error in validation_data['syntax_errors']:
            output.append(f"- {error}")
    
    if 'semantic_errors' in validation_data:
        output.append("\n**Semantic Errors:**")
        for error in validation_data['semantic_errors']:
            output.append(f"- {error}")
    
    return "\n".join(output)

def format_optimization_results(optimization_data):
    """Format optimization results for display"""
    if not optimization_data:
        return "No optimization data available"
    
    output = []
    
    score = optimization_data.get('optimization_score', 'N/A')
    output.append(f"**Optimization Score:** {score}/100")
    
    if 'index_recommendations' in optimization_data:
        output.append("\n**Index Recommendations:**")
        for rec in optimization_data['index_recommendations']:
            output.append(f"- {rec}")
    
    if 'query_rewrites' in optimization_data:
        output.append("\n**Query Rewrites:**")
        for rewrite in optimization_data['query_rewrites']:
            output.append(f"- {rewrite}")
    
    if 'azure_features' in optimization_data:
        output.append("\n**Azure SQL Features:**")
        for feature in optimization_data['azure_features']:
            output.append(f"- {feature}")
    
    return "\n".join(output)
```

Update **app.py** to use the parser (in the Translation Results tab):

```python
from utils.agent_parser import parse_agent_response, format_validation_results, format_optimization_results

# In tab2 (Translation Results), replace the parsing section:
response_text = result['response'].get('choices', [{}])[0].get('message', {}).get('content', '')

# Parse structured results
sections = parse_agent_response(response_text)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Translation")
    st.code(sections['translation'], language='sql')

with col2:
    st.subheader("Validation")
    st.markdown(format_validation_results(sections['validation']))

with col3:
    st.subheader("Optimization")
    st.markdown(format_optimization_results(sections['optimization']))
```

### Part 6: Deploy to Azure Container Apps

1. Create **Dockerfile**:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Create **.dockerignore**:

```
venv/
__pycache__/
*.pyc
.env
.git
```

3. Build Docker image:
```bash
docker build -t sql-modernization-app .
```

4. Test locally:
```bash
docker run -p 8501:8501 --env-file .env sql-modernization-app
```

5. Create **Azure Container Registry**:

In Azure Portal:
- Search for **Container Registry**
- Click **+ Create**
- **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
- **Registry name**: **sqlmodacr<inject key="DeploymentID"></inject>**
- **SKU**: **Basic**
- Click **Review + Create**

6. Push image to ACR:

```bash
az acr login --name sqlmodacr<inject key="DeploymentID"></inject>
docker tag sql-modernization-app sqlmodacr<inject key="DeploymentID"></inject>.azurecr.io/sql-modernization-app:v1
docker push sqlmodacr<inject key="DeploymentID"></inject>.azurecr.io/sql-modernization-app:v1
```

7. Create **Azure Container App**:

- Search for **Container Apps**
- Click **+ Create**
- **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
- **Container app name**: **sql-mod-app**
- **Region**: **<inject key="Region"></inject>**
- **Container Apps Environment**: Create new
- **Container**: Select from Azure Container Registry
  - **Registry**: **sqlmodacr<inject key="DeploymentID"></inject>**
  - **Image**: **sql-modernization-app**
  - **Tag**: **v1**
- **Ingress**: Enabled
  - **Target port**: **8501**
  - **Ingress traffic**: **Accept from anywhere**
- Click **Review + Create**

8. Add environment variables:

After creation:
- Go to Container App → **Secrets**
- Add your .env values as secrets
- Go to **Environment variables**
- Reference the secrets

9. Get app URL:

- Go to **Overview**
- Copy **Application Url**
- Open in browser

### Part 7: Test Production Deployment

1. Open the Container App URL.

2. Upload a complex Oracle SQL file:
```sql
SELECT 
    e.emp_id,
    e.emp_name,
    NVL(e.salary, 0) as salary,
    d.dept_name,
    TO_CHAR(e.hire_date, 'YYYY-MM-DD') as hire_date
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
WHERE e.hire_date > SYSDATE - 30
AND ROWNUM <= 100
ORDER BY e.salary DESC;
```

3. Verify:
   - Translation appears with proper T-SQL syntax
   - Validation shows no errors
   - Optimization suggests indexes, rewrites, Azure features
   - Results saved to Cosmos DB
   - History tab shows the entry

## Success Criteria

- Streamlit app runs locally without errors
- File upload and manual input both work
- Agent API endpoint called successfully
- Three-phase results displayed clearly (Translation | Validation | Optimization)
- Parser extracts structured data from agent responses
- History tab shows Cosmos DB entries
- Docker image builds successfully
- Azure Container Registry created and image pushed
- Container App deployed and accessible
- Production app works same as local version
- Complete workflow: Upload → API call → Parse → Display → Save → History

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

Congratulations! You've completed all challenges. Your SQL modernization platform is production-ready!
