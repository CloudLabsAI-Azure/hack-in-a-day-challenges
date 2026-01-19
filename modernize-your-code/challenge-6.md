# Challenge 06: Build and Deploy the Streamlit Application

## Introduction

In this final challenge, you will build a complete web application using Streamlit that integrates all three agents (Translation, Validation, Optimization) into a cohesive user experience. Users will upload Oracle SQL files, view translation results in real-time, review validation reports, and receive optimization recommendations. The application will be deployed locally first, then containerized for cloud deployment.

## Challenge Objectives

- Build a Streamlit web interface for SQL modernization
- Integrate Translation, Validation, and Optimization agents
- Implement file upload functionality for batch processing
- Display results with syntax highlighting and downloadable reports
- Add progress tracking for long-running operations
- Containerize the application with Docker
- Deploy the application to Azure Container Apps

## Steps to Complete

### Part 1: Set Up Streamlit Development Environment

1. In **Azure AI Foundry Studio**, open a terminal and create a project directory:

```bash
mkdir sql-modernization-app
cd sql-modernization-app
```

2. Create a `requirements.txt` file:

```text
streamlit==1.30.0
openai==1.12.0
azure-cosmos==4.5.1
azure-identity==1.15.0
sqlparse==0.4.4
pyodbc==5.0.1
pandas==2.1.4
python-dotenv==1.0.0
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Part 2: Create Configuration File

1. Create a `.env` file for configuration:

```text
# AI Foundry Configuration
AZURE_OPENAI_ENDPOINT=https://your-ai-foundry-endpoint.openai.azure.com/
AZURE_OPENAI_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=gpt-4-sql-translator
AZURE_OPENAI_API_VERSION=2024-02-15-preview

COSMOS_ENDPOINT=https://your-cosmos-account.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key-here
DATABASE_NAME=SQLModernization

AZURE_SQL_CONNECTION_STRING=Server=tcp:sql-modernization-server.database.windows.net,1433;Database=ValidationDB;User ID=sqladmin;Password=YourPassword123!;Encrypt=yes;
```

2. Add `.env` to `.gitignore` to protect secrets:

```text
.env
__pycache__/
*.pyc
.vscode/
```

### Part 3: Create Agent Helper Module

1. Create `agents.py` with all agent functions:

```python
from openai import AzureOpenAI
import json
from datetime import datetime
import sqlparse

class SQLModernizationAgent:
    """Multi-agent system for SQL modernization"""
    
    def __init__(self, openai_endpoint: str, openai_key: str, deployment: str, api_version: str):
        self.client = AzureOpenAI(
            azure_endpoint=openai_endpoint,
            api_key=openai_key,
            api_version=api_version
        )
        self.deployment = deployment
    
    def translate_oracle_to_azure_sql(self, oracle_sql: str) -> dict:
        """Translates Oracle SQL to Azure SQL T-SQL"""
        
        system_prompt = """You are an expert SQL translator specializing in Oracle to Azure SQL conversions.
        
Translation Rules:
1. Oracle SYSDATE -> Azure SQL GETDATE()
2. Oracle NVL() -> Azure SQL ISNULL() or COALESCE()
3. Oracle ROWNUM -> Azure SQL ROW_NUMBER() or TOP
4. Oracle sequence.NEXTVAL -> Azure SQL NEXT VALUE FOR sequence
5. Oracle DECODE() -> Azure SQL CASE WHEN
6. Oracle (+) outer join syntax -> Azure SQL LEFT/RIGHT JOIN
7. Oracle CONNECT BY -> Azure SQL recursive CTE
8. Oracle TO_DATE() -> Azure SQL CONVERT() or CAST()
9. Oracle dual table -> Not needed in Azure SQL
10. Oracle packages/procedures -> Azure SQL stored procedures with modifications

Return ONLY valid Azure SQL T-SQL code without explanations."""

        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Translate this Oracle SQL to Azure SQL:\n\n{oracle_sql}"}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            translated_sql = response.choices[0].message.content.strip()
            
            # Remove code block markers if present
            if translated_sql.startswith("```sql"):
                translated_sql = translated_sql[6:]
            if translated_sql.startswith("```"):
                translated_sql = translated_sql[3:]
            if translated_sql.endswith("```"):
                translated_sql = translated_sql[:-3]
            
            return {
                "success": True,
                "translated_sql": translated_sql.strip(),
                "tokens_used": response.usage.total_tokens,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "translated_sql": "",
                "timestamp": datetime.now().isoformat()
            }
    
    def validate_sql(self, sql_code: str) -> dict:
        """Validates SQL code using AI and parser"""
        
        validation_prompt = """You are a SQL validation expert. Analyze the Azure SQL T-SQL code for:
1. Syntax correctness
2. Semantic validity
3. Best practice compliance
4. Potential runtime errors

Return JSON:
{
  "valid": true/false,
  "confidence": 0.0-1.0,
  "issues": [{"severity": "error/warning", "message": "description"}],
  "suggestions": ["improvement suggestion"]
}"""

        results = {
            "overall_valid": False,
            "validations": {},
            "timestamp": datetime.now().isoformat()
        }
        
        # AI-based validation
        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": validation_prompt},
                    {"role": "user", "content": sql_code}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            ai_result = json.loads(response.choices[0].message.content)
            results["validations"]["ai"] = ai_result
        except Exception as e:
            results["validations"]["ai"] = {"valid": False, "error": str(e)}
        
        # Parser-based validation
        try:
            parsed = sqlparse.parse(sql_code)
            parser_valid = len(parsed) > 0 and not any(stmt.token_first().ttype is sqlparse.tokens.Error for stmt in parsed)
            
            results["validations"]["parser"] = {
                "valid": parser_valid,
                "statement_count": len(parsed)
            }
        except Exception as e:
            results["validations"]["parser"] = {"valid": False, "error": str(e)}
        
        # Determine overall validity
        ai_valid = results["validations"].get("ai", {}).get("valid", False)
        parser_valid = results["validations"].get("parser", {}).get("valid", False)
        results["overall_valid"] = ai_valid and parser_valid
        
        return results
    
    def optimize_sql(self, sql_code: str) -> dict:
        """Provides optimization recommendations"""
        
        optimization_prompt = """Analyze Azure SQL T-SQL for performance optimizations.

Return JSON:
{
  "overall_score": 0-100,
  "priority_optimizations": [
    {
      "priority": "HIGH/MEDIUM/LOW",
      "category": "Index/Query/Azure Feature",
      "recommendation": "specific suggestion",
      "reason": "why this helps",
      "estimated_impact": "expected improvement"
    }
  ],
  "index_recommendations": [
    {
      "index_name": "IX_TableName_Columns",
      "columns": "column_list",
      "reason": "usage pattern"
    }
  ],
  "azure_features": [
    {
      "feature_name": "Azure SQL feature",
      "benefit": "performance benefit",
      "implementation_notes": "how to enable"
    }
  ]
}"""

        try:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": optimization_prompt},
                    {"role": "user", "content": f"Analyze this Azure SQL code:\n\n{sql_code}"}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            optimization_result = json.loads(response.choices[0].message.content)
            optimization_result["timestamp"] = datetime.now().isoformat()
            optimization_result["success"] = True
            
            return optimization_result
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "overall_score": 0,
                "timestamp": datetime.now().isoformat()
            }

print("Agent module loaded")
```

2. Save the file.

### Part 4: Create Cosmos DB Helper Module

1. Create `cosmos_helper.py`:

```python
from azure.cosmos import CosmosClient, exceptions
import uuid
from datetime import datetime

class CosmosDBHelper:
    """Helper for Cosmos DB operations"""
    
    def __init__(self, endpoint: str, key: str, database_name: str):
        self.client = CosmosClient(endpoint, credential=key)
        self.database = self.client.get_database_client(database_name)
        self.translation_container = self.database.get_container_client("TranslationResults")
        self.validation_container = self.database.get_container_client("ValidationLogs")
        self.optimization_container = self.database.get_container_client("OptimizationResults")
    
    def save_translation(self, source_sql: str, translated_sql: str, metadata: dict = None):
        """Save translation result"""
        item = {
            "id": str(uuid.uuid4()),
            "source_sql": source_sql,
            "translated_sql": translated_sql,
            "source_dialect": "Oracle",
            "target_dialect": "Azure SQL",
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        
        try:
            created = self.translation_container.create_item(body=item)
            return created["id"]
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error saving translation: {e.message}")
            return None
    
    def save_validation(self, translation_id: str, validation_results: dict):
        """Save validation log"""
        item = {
            "id": str(uuid.uuid4()),
            "translation_id": translation_id,
            "validation_results": validation_results,
            "is_valid": validation_results.get("overall_valid", False),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        try:
            created = self.validation_container.create_item(body=item)
            return created["id"]
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error saving validation: {e.message}")
            return None
    
    def save_optimization(self, translation_id: str, optimization_results: dict):
        """Save optimization result"""
        item = {
            "id": str(uuid.uuid4()),
            "translation_id": translation_id,
            "optimization_score": optimization_results.get("overall_score", 0),
            "optimization_results": optimization_results,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        try:
            created = self.optimization_container.create_item(body=item)
            return created["id"]
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error saving optimization: {e.message}")
            return None
    
    def get_recent_translations(self, limit: int = 10):
        """Get recent translations"""
        query = "SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT @limit"
        items = list(self.translation_container.query_items(
            query=query,
            parameters=[{"name": "@limit", "value": limit}]
        ))
        return items

print("Cosmos helper module loaded")
```

2. Save the file.

### Part 5: Build Streamlit Application

1. Create `streamlit_app.py`:

```python
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
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = SQLModernizationAgent(
        openai_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        openai_key=os.getenv("AZURE_OPENAI_KEY"),
        deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )

if 'cosmos' not in st.session_state:
    st.session_state.cosmos = CosmosDBHelper(
        endpoint=os.getenv("COSMOS_ENDPOINT"),
        key=os.getenv("COSMOS_KEY"),
        database_name=os.getenv("DATABASE_NAME")
    )

# Header
st.title("SQL Modernization Platform")
st.markdown("Translate Oracle SQL to Azure SQL with AI-powered validation and optimization")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select Page", ["Translate SQL", "Batch Processing", "History"])
    
    st.markdown("---")
    st.header("About")
    st.info("This platform uses Azure OpenAI to modernize Oracle SQL to Azure SQL T-SQL with automated validation and optimization recommendations.")

# Main content
if page == "Translate SQL":
    st.header("Translate Oracle SQL to Azure SQL")
    
    # Input
    oracle_sql = st.text_area("Oracle SQL Code", height=200, placeholder="Enter Oracle SQL here...")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        translate_btn = st.button("Translate", type="primary", use_container_width=True)
    with col2:
        validate_btn = st.button("Validate", disabled=True, use_container_width=True)
    with col3:
        optimize_btn = st.button("Optimize", disabled=True, use_container_width=True)
    
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
                
                st.success("Translation completed successfully!")
                
                # Display results
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Oracle SQL (Original)")
                    st.code(oracle_sql, language="sql")
                
                with col2:
                    st.subheader("Azure SQL (Translated)")
                    st.code(result["translated_sql"], language="sql")
                
                # Download button
                st.download_button(
                    label="Download Translated SQL",
                    data=result["translated_sql"],
                    file_name="translated_query.sql",
                    mime="text/plain"
                )
                
                # Enable validation button
                validate_btn = st.button("Validate Translation", use_container_width=True)
            else:
                st.error(f"Translation failed: {result.get('error', 'Unknown error')}")
    
    # Validation
    if 'translated_sql' in st.session_state:
        if st.button("Validate Translation", use_container_width=True):
            with st.spinner("Validating SQL..."):
                validation_result = st.session_state.agent.validate_sql(st.session_state.translated_sql)
                
                st.session_state.cosmos.save_validation(
                    translation_id=st.session_state.translation_id,
                    validation_results=validation_result
                )
                
                # Display validation results
                st.subheader("Validation Results")
                
                if validation_result["overall_valid"]:
                    st.success("SQL is valid!")
                else:
                    st.error("SQL validation failed")
                
                # Show AI validation details
                ai_validation = validation_result.get("validations", {}).get("ai", {})
                if ai_validation:
                    st.metric("AI Confidence", f"{ai_validation.get('confidence', 0):.0%}")
                    
                    issues = ai_validation.get("issues", [])
                    if issues:
                        st.warning(f"Found {len(issues)} issues:")
                        for issue in issues:
                            st.write(f"- [{issue.get('severity', 'info').upper()}] {issue.get('message', '')}")
                
                # Enable optimization button
                st.session_state.validation_complete = True
    
    # Optimization
    if 'validation_complete' in st.session_state and st.session_state.validation_complete:
        if st.button("Optimize SQL", use_container_width=True):
            with st.spinner("Analyzing optimization opportunities..."):
                optimization_result = st.session_state.agent.optimize_sql(st.session_state.translated_sql)
                
                st.session_state.cosmos.save_optimization(
                    translation_id=st.session_state.translation_id,
                    optimization_results=optimization_result
                )
                
                # Display optimization results
                st.subheader("Optimization Recommendations")
                
                score = optimization_result.get("overall_score", 0)
                st.metric("Optimization Score", f"{score}/100")
                
                # Priority optimizations
                priorities = optimization_result.get("priority_optimizations", [])
                if priorities:
                    st.write("**High Priority Recommendations:**")
                    for opt in priorities:
                        with st.expander(f"[{opt.get('priority', 'MEDIUM')}] {opt.get('category', 'General')}"):
                            st.write(f"**Recommendation:** {opt.get('recommendation', '')}")
                            st.write(f"**Reason:** {opt.get('reason', '')}")
                            st.write(f"**Estimated Impact:** {opt.get('estimated_impact', 'Unknown')}")
                
                # Index recommendations
                indexes = optimization_result.get("index_recommendations", [])
                if indexes:
                    st.write("**Index Recommendations:**")
                    for idx in indexes:
                        st.write(f"- {idx.get('index_name', 'Index')}: {idx.get('columns', '')} ({idx.get('reason', '')})")

elif page == "Batch Processing":
    st.header("Batch SQL File Processing")
    
    uploaded_files = st.file_uploader(
        "Upload Oracle SQL files",
        type=['sql'],
        accept_multiple_files=True
    )
    
    if uploaded_files:
        process_batch = st.button("Process All Files", type="primary")
        
        if process_batch:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            results = []
            
            for idx, file in enumerate(uploaded_files):
                status_text.text(f"Processing {file.name}...")
                
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
                        translated_sql=translation["translated_sql"]
                    )
                    
                    results.append({
                        "file": file.name,
                        "status": "Success",
                        "valid": validation.get("overall_valid", False),
                        "score": optimization.get("overall_score", 0)
                    })
                else:
                    results.append({
                        "file": file.name,
                        "status": "Failed",
                        "error": translation.get("error", "Unknown")
                    })
                
                progress_bar.progress((idx + 1) / len(uploaded_files))
            
            status_text.text("Processing complete!")
            
            # Display results table
            st.subheader("Batch Processing Results")
            st.table(results)

elif page == "History":
    st.header("Translation History")
    
    recent_translations = st.session_state.cosmos.get_recent_translations(limit=20)
    
    if recent_translations:
        for trans in recent_translations:
            with st.expander(f"{trans['timestamp']} - {trans['source_dialect']} to {trans['target_dialect']}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Source SQL:**")
                    st.code(trans['source_sql'][:200] + "...", language="sql")
                
                with col2:
                    st.write("**Translated SQL:**")
                    st.code(trans['translated_sql'][:200] + "...", language="sql")
    else:
        st.info("No translation history available")
```

2. Save the file.

### Part 6: Test Streamlit Application Locally

1. In the terminal, run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

2. Open the browser at the displayed URL (typically `http://localhost:8501`).

3. Test the translation workflow with a sample Oracle query.

### Part 7: Create Dockerfile

1. Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY agents.py .
COPY cosmos_helper.py .
COPY streamlit_app.py .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Save the file.

### Part 8: Build and Test Docker Container

1. Build the Docker image:

```bash
docker build -t sql-modernization-app .
```

2. Run the container locally:

```bash
docker run -p 8501:8501 --env-file .env sql-modernization-app
```

3. Test the containerized application at `http://localhost:8501`.

### Part 9: Deploy to Azure Container Apps

1. Login to Azure CLI:

```bash
az login
```

2. Create Azure Container Registry (if not exists):

```bash
az acr create --resource-group SQL-Modernization-RG --name sqlmodernizationacr --sku Basic
```

3. Build and push image to ACR:

```bash
az acr build --registry sqlmodernizationacr --image sql-modernization-app:v1 .
```

4. Create Container App environment:

```bash
az containerapp env create --name sql-modernization-env --resource-group SQL-Modernization-RG --location eastus
```

5. Deploy Container App:

```bash
az containerapp create \
  --name sql-modernization-app \
  --resource-group SQL-Modernization-RG \
  --environment sql-modernization-env \
  --image sqlmodernizationacr.azurecr.io/sql-modernization-app:v1 \
  --target-port 8501 \
  --ingress external \
  --registry-server sqlmodernizationacr.azurecr.io \
  --env-vars \
    AZURE_OPENAI_ENDPOINT=secretref:openai-endpoint \
    AZURE_OPENAI_KEY=secretref:openai-key \
    COSMOS_ENDPOINT=secretref:cosmos-endpoint \
    COSMOS_KEY=secretref:cosmos-key
```

6. Get the application URL:

```bash
az containerapp show --name sql-modernization-app --resource-group SQL-Modernization-RG --query properties.configuration.ingress.fqdn
```

### Part 10: Final Testing

1. Access the deployed application using the FQDN from the previous command.

2. Upload a test Oracle SQL file.

3. Verify the complete workflow:
   - Translation completes successfully
   - Validation runs and shows results
   - Optimization provides recommendations
   - Results are saved to Cosmos DB

4. Check batch processing with multiple files.

5. Review history to confirm data persistence.

## Success Criteria

- Streamlit application created with multi-page navigation
- Translation agent integrated with user-friendly interface
- Validation results displayed with confidence scores and issues
- Optimization recommendations shown with priority ranking
- File upload functionality works for single and batch processing
- Results downloadable in SQL format
- Cosmos DB integration persists all workflow data
- Application runs locally via Streamlit
- Docker container built successfully
- Application deployed to Azure Container Apps
- Public URL accessible and functional
- Complete end-to-end workflow tested successfully

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Container Apps Overview](https://learn.microsoft.com/azure/container-apps/overview)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)

Congratulations! You have completed the SQL Modernization hackathon. You have built a complete AI-powered platform for modernizing Oracle SQL to Azure SQL with automated translation, validation, and optimization.
