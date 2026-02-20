# Challenge 05: Run the Streamlit Application Locally

## Introduction

Your three-agent pipeline is operational! All the code has been built for you. In this challenge, you'll configure and run a Streamlit web application locally that provides a beautiful interface for your SQL modernization system.

## Prerequisites

- Completed Challenge 4 (all three agents created and connected)
- Visual Studio Code installed
- Python 3.11+ installed
- Azure CLI installed and authenticated (`az login`)

## Challenge Objectives

- Configure environment variables with your agent credentials
- Authenticate with Azure CLI
- Install Python dependencies
- Run the Streamlit application locally
- Test the multi-agent pipeline through the web UI
- Upload SQL files and process them
- View translation history from Cosmos DB

## Steps to Complete

### Part 1: Download and Extract Code Files

The application code is provided in a pre-built package.

1. **Download the code package**:
   
   Visit this link in your browser:
   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/modernize-your-code.zip
   ```

2. **Extract the ZIP file**:
   
   - Right-click the downloaded `modernize-your-code.zip` file
   - Select **Extract All...**
   - Choose a location like `C:\LabFiles\` or your Desktop
   - Click **Extract**

3. **Navigate to the codefiles folder**:
   
   Open File Explorer and go to:
   ```
   [extraction-path]\hack-in-a-day-challenges-modernize-your-code\modernize-your-code\codefiles
   ```

### Part 2: Install and Authenticate with Azure CLI

The application uses Azure CLI authentication to connect to your agents.

1. Open the **Windows Powershell** as an admin.

1. **Install Azure CLI** (if not already installed):
   
   For Windows:
   ```powershell
   Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
   Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi'
   ```

1. Accept the terms and license agreement and select **Install**. Once done select **Finish**.

1. **Login to Azure**:
   ```bash
   az login
   ```
   
1. This will open a pop-up for authentication. Sign in with your Azure credentials.

1. Don't change the subscription or tenant, hit enter.

### Part 3: Get Your Agent Credentials

You need three values to connect to your agents:

1. Go to **Microsoft Foundry Studio** → Your project.

1. In the Overview section, find the **Microsoft Foundry project endpoint**:

   - Example format: `https://sql-modernize-2034545.services.ai.azure.com/api/projects/proj-default`
   - **CRITICAL:** The project name at the end is always `proj-default` (not sql-modernize-XXXX)
   - Make sure it ends with `/api/projects/proj-default`

1. Navigate to **Agents** in the left menu.

1. Click on your **SQL-Translation-Agent**.

1. In the Setup panel on the right, copy the **Agent ID** (starts with `asst_`).

1. From Challenge 1, get your **Cosmos DB** connection details:
   - Go to Azure Portal → Your Cosmos DB account
   - Click **Keys** → Copy **URI** and **Primary Key**

### Part 4: Configure the Application

1. Navigate to the `codefiles` folder you extracted in Part 1.

2. Locate the `.env.example` file.

3. **Copy** `.env.example` to create a new file named `.env`

4. Open `.env` and replace the placeholder values:

    ```env
    # Microsoft Foundry Agent API Configuration
    # IMPORTANT: Use proj-default as the project name (not sql-modernize-XXXX)
    AGENT_API_ENDPOINT=https://sql-modernize-<DeploymentID>.services.ai.azure.com/api/projects/proj-default
    AGENT_ID=asst_<your-agent-id>

    # Cosmos DB Configuration
    COSMOS_ENDPOINT=https://sql-modernization-cosmos-<DeploymentID>.documents.azure.com:443/
    COSMOS_KEY=<your-cosmos-primary-key>
    DATABASE_NAME=SQLModernizationDB
    ```

**Important Notes:**
- Replace `<DeploymentID>` with your actual deployment ID (e.g., 2034545)
- **CRITICAL:** Endpoint must end with `/api/projects/proj-default` (the project name is always `proj-default`)
- Replace `<your-agent-id>` with your Translation Agent ID from step 6 (starts with `asst_`)
- Replace `<your-cosmos-primary-key>` with your Cosmos DB Primary Key
- The app uses Azure CLI authentication (`az login`), so no API key is needed for agents

5. Save the file.

### Part 5: Review the Code (Optional but Recommended)

Before running, take a moment to explore the application code:

**app.py** - Main Streamlit application
- **Lines 1-50**: Imports and Azure SDK configuration
- **Lines 51-169**: Custom CSS styling for premium UI
- **Lines 171-186**: Cosmos DB connection
- **Lines 188-228**: Agent response parsing logic
- **Lines 230-350**: Agent API calling with Azure AI Projects SDK
- **Lines 352-687**: Streamlit UI with 3 tabs (Modernize SQL, Results, History)

**Key features to notice:**
- Azure CLI authentication using `DefaultAzureCredential`
- File upload support (upload .sql files)
- Sample query templates
- Real-time progress tracking
- Professional gradient completion banner
- Three-column results display
- History from Cosmos DB
- Error handling and validation
- Production-ready premium styling
- Auto-switch to Results tab after completion

### Part 6: Install Dependencies

Open a terminal in the `codefiles` folder and run:

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit` - Web framework
- `azure-ai-agents` - Azure AI Agents SDK (for thread/message/run operations)
- `azure-ai-projects` - Microsoft Foundry SDK (for project management)
- `azure-identity` - Azure authentication
- `azure-cosmos` - Cosmos DB SDK
- `python-dotenv` - Environment variables
- `pandas` - Data processing

### Part 7: Run the Application

1. Start the Streamlit app with Azure CLI in PATH:

    **Windows PowerShell:**

    ```powershell
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

    streamlit run app.py
    ```

1. Enter the email as **<inject key="AzureAdUserEmail"></inject>** and hit enter.



**macOS/Linux:**
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501` or `http://localhost:8502`

### Part 8: Test the Multi-Agent Pipeline

1. You'll see a premium blue gradient header: **"SQL Modernization Assistant"**

2. In the **sidebar**, verify all agents show green checkmarks:
   - Translation Agent
   - Validation Agent
   - Optimization Agent

3. **Option A: Use a Sample Query**
   - On the right side, select a sample from the dropdown (e.g., "Hierarchical Query (CONNECT BY)")
   - Click **"Load Sample"**

4. **Option B: Upload a SQL File**
   - Click the file upload area
   - Upload a .sql file with Oracle SQL code

5. **Option C: Paste SQL Directly**
   - Paste your Oracle SQL in the text area

6. Click the **"Modernize SQL"** button

7. Watch the progress indicators as your query flows through all three agents:
   - Creating conversation thread...
   - Sending Oracle SQL to Translation Agent...
   - Starting multi-agent pipeline...
   - Agent Status: RUNNING...
   - Agent processing completed!

8. After completion, you'll see a **professional gradient completion banner** and the app will automatically switch to the **"Results"** tab.

9. View the **three-column output**:

   **Column 1: Translation**
   - Azure SQL T-SQL translation
   - Copy button for easy use

   **Column 2: Validation**
   - Validation status (Pass/Fail)
   - Syntax errors (if any)
   - Semantic warnings
   - Raw JSON data

   **Column 3: Optimization**
   - Optimization score (0-100)
   - Performance recommendations
   - Suggested indexes
   - Raw JSON data

10. Click the **"History"** tab to see all past translations from Cosmos DB

### Part 9: Test Complex Scenarios

Try these test cases to verify everything works:

**Test 1: Simple ROWNUM Query**
```sql
SELECT emp_id, emp_name, salary
FROM employees
WHERE ROWNUM <= 10
ORDER BY salary DESC;
```

Expected: Should convert `ROWNUM <= 10` to `TOP 10`

---

**Test 2: NVL and Date Functions**
```sql
SELECT emp_name, NVL(commission, 0) as comm
FROM employees
WHERE hire_date > SYSDATE - 30;
```

Expected: Should convert `NVL` to `ISNULL`, `SYSDATE` to `GETDATE()`

---

**Test 3: Hierarchical Query** (Most Complex)
```sql
SELECT emp_id, emp_name, manager_id, LEVEL as emp_level
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR emp_id = manager_id;
```

Expected:
- Translation: Recursive CTE with `WITH` clause
- Validation: Should flag if indexes missing
- Optimization: Should suggest indexes on `manager_id` and `emp_id`

---

**Test 4: Invalid SQL** (Test Validation Agent)
```sql
SELECT emp_id, emp_name
FROM employees
WHERE dept_id = 10
GROUP BY -- Missing column list
```
```

Expected:
- Validation: Should show error with syntax error
- Details: Missing GROUP BY columns

---

**Test 5: File Upload**
1. Create a file `test.sql` with any Oracle SQL
2. Upload it using the file uploader
3. Click "Modernize SQL"
4. Verify it processes correctly

## Success Criteria

- [ ] Code package downloaded and extracted successfully
- [ ] Azure CLI installed and authenticated (`az login` completed)
- [ ] `.env` file configured with correct credentials
- [ ] All dependencies installed successfully (`azure-ai-agents==1.1.0` included)
- [ ] Streamlit app runs without errors
- [ ] Browser opens to `http://localhost:8501` or `http://localhost:8502`
- [ ] Sidebar shows green checkmarks for all 3 agents
- [ ] Can process sample queries successfully
- [ ] Can upload and process .sql files
- [ ] Results tab shows translation + validation + optimization
- [ ] Professional gradient completion banner displays after processing
- [ ] App automatically switches to Results tab after completion
- [ ] History tab shows previous translations from Cosmos DB
- [ ] Cosmos DB saves results (verify in Azure Portal)
- [ ] UI is responsive and visually premium

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'azure'`

**Solution**: Run `pip install -r requirements.txt` in the codefiles folder. Ensure `azure-ai-agents==1.1.0` is installed.

---

**Issue**: `DefaultAzureCredential failed to retrieve a token`

**Solution**: 
- Run `az login` in terminal to authenticate
- If on Windows, restart terminal after Azure CLI installation to refresh PATH
- Run this in PowerShell before starting app:
  ```powershell
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  ```

---

**Issue**: `404 Resource not found` or `The project does not exist`

**Solution**: 
- **CRITICAL:** Verify endpoint ends with `/api/projects/proj-default` (the project name is always `proj-default`)
- Do NOT use `sql-modernize-XXXX` as the project name in the endpoint
- Example correct endpoint: `https://sql-modernize-2034545.services.ai.azure.com/api/projects/proj-default`
- Verify `AGENT_ID` is copied correctly from Microsoft Foundry Studio (starts with `asst_`)

---

**Issue**: Sidebar shows "Configuration missing"

**Solution**: 
- Check `.env` file exists (not `.env.example`)
- Verify all values are filled in (no `<DeploymentID>` or `<your-agent-id>` placeholders)
- Restart the Streamlit app

---

**Issue**: "Thread timeout" or "Agent run timed out"

**Solution**: 
- Complex queries can take 1-2 minutes with 3 agents
- Refresh the page and try again
- If it persists, check Microsoft Foundry project quota

---

**Issue**: No validation or optimization results

**Solution**:
- Verify Connected agents are configured in Microsoft Foundry (from Challenges 4-5)
- Check Translation Agent has `validation_agent` and `optimization_agent` in Connected agents
- Ensure activation details are in Translation Agent instructions
- Verify the Translation Agent instructions do NOT contain "Return ONLY" which can prevent hand-offs

---

**Issue**: Cosmos DB errors

**Solution**:
- Verify `COSMOS_ENDPOINT` and `COSMOS_KEY` are correct in `.env`
- Check Cosmos DB database `SQLModernizationDB` exists
- Verify container `TranslationResults` exists
- If missing, create them manually or re-run Challenge 1

---

**Issue**: App is slow or unresponsive

**Solution**:
- Check your internet connection
- Verify Microsoft Foundry quota hasn't been exceeded
- Try with a simpler SQL query first
- Complex hierarchical queries can take 60-90 seconds with 3 agents

---

**Issue**: "Azure CLI not found" error on Windows

**Solution**:
- After installing Azure CLI, close and reopen terminal
- Or refresh PATH in current PowerShell session:
  ```powershell
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  ```

## Technical Notes

### Authentication Architecture

The application uses **Azure CLI authentication** instead of API keys:

1. **DefaultAzureCredential** from `azure-identity` automatically discovers credentials
2. When you run `az login`, credentials are cached locally
3. The app reads these cached credentials to authenticate API calls
4. No API key is stored in code or environment variables (more secure)

### SDK Details

- **Package**: `azure-ai-agents==1.1.0` (provides `AgentsClient` with `.threads`, `.messages`, `.runs` sub-clients)
- **Project SDK**: `azure-ai-projects==2.0.0b3` (for project-level management)
- **Agent Message Role**: Uses `agent` or `assistant` role string from agent responses
- **Thread Management**: Automatic thread creation and message polling via `AgentsClient`

### Endpoint Format

Foundry services endpoint structure:
```
https://ai-project-<ID>.services.ai.azure.com/api/projects/<project-name>-<ID>
```

Key differences from OpenAI endpoint:
- Domain: `.services.ai.azure.com` (not `.openai.azure.com`)
- Path: Includes `/api/projects/<project-name>`
- Authentication: Entra ID only (API keys won't work)
- Agents: Only Foundry-created agents are accessible

## Bonus Challenges

1. **Custom Query Builder**: Modify [app.py](app.py) to add a query builder with dropdown menus for common Oracle patterns

2. **Export Feature**: Add a "Download Report" button that exports results as PDF or Word document

3. **Batch Processing**: Add functionality to upload multiple .sql files and process them all at once

4. **Real-time Comparison**: Add a diff view showing Oracle vs Azure SQL side-by-side with syntax highlighting

5. **Agent Metrics Dashboard**: Create a new tab showing statistics:
   - Average optimization score
   - Most common syntax errors
   - Processing time trends
   - Success rate over time

## Next Steps

Congratulations! You've successfully:
- Built a 3-agent AI system in Microsoft Foundry
- Connected agents in a pipeline (Translation → Validation, Optimization)
- Run a Streamlit web application locally
- Integrated with Cosmos DB for persistence
- Created a complete SQL modernization platform

**What you've learned:**
- Microsoft Foundry Agents visual builder
- Multi-agent orchestration and hand-offs
- Azure AI Projects SDK integration with Entra ID authentication
- Streamlit for web applications
- Cosmos DB for NoSQL storage
- End-to-end AI application development

**Where to go from here:**
1. Add more specialized agents (Security Analyzer, Performance Tester)
2. Integrate with Azure DevOps for automated migration PRs
3. Build a feedback loop for continuous agent improvement
4. Extend to support other databases (MySQL, PostgreSQL, etc.)
5. Deploy to Azure Container Apps for production access (optional)
        "content": sql_input
    }
)
```

**Step 3: Run the Agent**
```python
# Start the Translation Agent
run_response = requests.post(
    f"{endpoint}/openai/threads/{thread_id}/runs?api-version=2024-02-15-preview",
    headers=headers,
    json={
        "assistant_id": agent_id  # Your Translation Agent ID
    }
)
run_id = run_response.json()["id"]
```

**Step 4: Poll for Completion**
```python
# Wait for agent to finish (including connected agents)
import time
while True:
    status_response = requests.get(
        f"{endpoint}/openai/threads/{thread_id}/runs/{run_id}?api-version=2024-02-15-preview",
        headers=headers
    )
    status = status_response.json()["status"]
    
    if status == "completed":
        break
    elif status in ["failed", "cancelled", "expired"]:
        raise Exception(f"Run {status}")
    
    time.sleep(2)
```

**Step 5: Get the Response**
```python
# Retrieve messages from the thread
messages_response = requests.get(
    f"{endpoint}/openai/threads/{thread_id}/messages?api-version=2024-02-15-preview",
    headers=headers
)
messages = messages_response.json()["data"]

# Get the assistant's response (includes all 3 agents' outputs)
assistant_messages = [m for m in messages if m["role"] == "assistant"]
response_text = assistant_messages[0]["content"][0]["text"]["value"]
```

> **Key Point**: When you call the Translation Agent, it automatically calls the connected Validation and Optimization agents. The response includes all three outputs in one message.

### Part 9: Response Parsing

The app uses regex to extract the three agent outputs:

```python
def parse_agent_response(response_text):
    result = {
        'translation': '',
        'validation': None,
        'optimization': None
    }
    
    # Extract SQL code block
    sql_match = re.search(r'```sql\n(.*?)```', response_text, re.DOTALL)
    if sql_match:
        result['translation'] = sql_match.group(1).strip()
    
    # Extract JSON blocks for validation/optimization
    json_matches = re.findall(r'```json\n(.*?)```', response_text, re.DOTALL)
    for json_text in json_matches:
        data = json.loads(json_text)
        if 'valid' in data or 'syntax_errors' in data:
            result['validation'] = data
        elif 'optimization_score' in data:
            result['optimization'] = data
    
    return result
```

### Part 10: Deploy to Azure Container Apps

Now that your app works locally, let's deploy it to Azure for production use.

1. Create a **Dockerfile** in your project folder:

    ```dockerfile
    FROM python:3.11-slim

    WORKDIR /app

    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    COPY app.py .
    COPY .env .

    EXPOSE 8501

    CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
    ```

2. Build and test Docker image locally:

    ```bash
    docker build -t sql-modernization-app .
    docker run -p 8501:8501 sql-modernization-app
    ```

3. Visit `http://localhost:8501` to test the containerized app.

4. Push to Azure Container Registry:

    ```bash
    # Login to Azure
    az login

    # Create Azure Container Registry (if not exists)
    az acr create --resource-group challenge-rg-<inject key="DeploymentID" enableCopy="false"/> --name sqlmodernizationacr<inject key="DeploymentID" enableCopy="false"/> --sku Basic

    # Login to ACR
    az acr login --name sqlmodernizationacr<inject key="DeploymentID" enableCopy="false"/>

    # Tag and push image
    docker tag sql-modernization-app sqlmodernizationacr<inject key="DeploymentID" enableCopy="false"/>.azurecr.io/sql-modernization-app:v1
    docker push sqlmodernizationacr<inject key="DeploymentID" enableCopy="false"/>.azurecr.io/sql-modernization-app:v1
    ```

5. Create Azure Container App:

    ```bash
    az containerapp create \
    --name sql-modernization-app \
    --resource-group challenge-rg-<inject key="DeploymentID" enableCopy="false"/> \
    --environment sql-modernization-env \
    --image sqlmodernizationacr<inject key="DeploymentID" enableCopy="false"/>.azurecr.io/sql-modernization-app:v1 \
    --target-port 8501 \
    --ingress external \
    --registry-server sqlmodernizationacr<inject key="DeploymentID" enableCopy="false"/>.azurecr.io \
    --env-vars \
        AGENT_API_ENDPOINT="<your-endpoint>" \
        AGENT_API_KEY="<your-api-key>" \
        AGENT_ID="<your-agent-id>" \
        COSMOS_ENDPOINT="<your-cosmos-endpoint>" \
        COSMOS_KEY="<your-cosmos-key>" \
        DATABASE_NAME="SQLModernizationDB"
    ```

6. Get the public URL:

    ```bash
    az containerapp show --name sql-modernization-app --resource-group challenge-rg-<inject key="DeploymentID" enableCopy="false"/> --query properties.configuration.ingress.fqdn -o tsv
    ```

7. Visit the URL and test your deployed app!

### Part 11: Verify Complete Pipeline

Test with this complex Oracle query to verify all 3 agents work:

```sql
SELECT emp_id, emp_name, manager_id, LEVEL as emp_level
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR emp_id = manager_id
ORDER BY LEVEL, emp_name;
```

Expected results:

**Translation Agent**: Should convert to recursive CTE with T-SQL syntax

```sql
WITH EmployeeHierarchy AS (
    SELECT emp_id, emp_name, manager_id, 1 as emp_level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.emp_id, e.emp_name, e.manager_id, eh.emp_level + 1
    FROM employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.emp_id
)
SELECT emp_id, emp_name, manager_id, emp_level
FROM EmployeeHierarchy
ORDER BY emp_level, emp_name;
```

**Validation Agent**: Should return JSON

```json
{
  "valid": true,
  "syntax_errors": [],
  "semantic_warnings": ["Ensure employees table has necessary indexes on emp_id and manager_id"]
}
```

**Optimization Agent**: Should return JSON

```json
{
  "optimization_score": 78,
  "recommendations": [
    "Consider adding MAXRECURSION hint if hierarchy is deep",
    "Add index on (manager_id, emp_id) for better CTE performance"
  ],
  "indexes": [
    "CREATE INDEX IX_Employees_ManagerId ON employees(manager_id) INCLUDE (emp_id, emp_name);"
  ]
}
```

## Success Criteria

- Retrieved agent API credentials from Microsoft Foundry project
- Configured .env file with AGENT_API_ENDPOINT, AGENT_API_KEY, AGENT_ID
- Streamlit app runs locally and calls Translation Agent
- App displays results from all 3 connected agents (Translation, Validation, Optimization)
- Results saved to Cosmos DB TranslationResults container
- App deployed to Azure Container Apps with public URL
- Can test production app with complex Oracle SQL and see 3-phase results

## Troubleshooting

**Issue**: `401 Unauthorized` error

**Solution**: Verify your AGENT_API_KEY is the Primary Key from your AI Foundry project (not the model deployment key)

---

**Issue**: Response doesn't include validation/optimization

**Solution**: 
- Check Translation Agent has Connected agents configured (validation_agent and optimization_agent)
- Verify activation details in Translation Agent instructions
- Check that hand-off instructions are in the Translation Agent's Instructions field

---

**Issue**: Timeout waiting for agent response

**Solution**: Increase `max_attempts` in app.py from 60 to 120 (complex queries with 3 agents can take 2-3 minutes)

---

**Issue**: Can't find Agent ID

**Solution**: 
1. Go to Microsoft Foundry portal
2. Click on your Translation Agent
3. Look in the Setup panel on the right
4. Copy the value from "Agent ID:" field (starts with `asst_`)

## Next Steps

Congratulations! You've built a complete multi-agent SQL modernization platform. You can:

1. Add more specialized agents (Security Analyzer, Cost Optimizer, Performance Tester)
2. Create a feedback loop where validation failures trigger automatic retranslation
3. Build an agent that generates test data and runs the T-SQL to verify correctness
4. Integrate with Azure DevOps to auto-generate migration PRs
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
            output.append("[PASS] Syntax validation passed")
        else:
            output.append("[FAIL] Syntax validation failed")
        
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

    - In Azure Portal:

        - Search for **Container Registry**
        - Click **+ Create**
        - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
        - **Registry name**: **sqlmodacr<inject key="DeploymentID" enableCopy="false"/>**
        - **SKU**: **Basic**
        - Click **Review + Create**

6. Push image to ACR:

    ```bash
    az acr login --name sqlmodacr<inject key="DeploymentID" enableCopy="false"/>
    docker tag sql-modernization-app sqlmodacr<inject key="DeploymentID" enableCopy="false"/>.azurecr.io/sql-modernization-app:v1
    docker push sqlmodacr<inject key="DeploymentID" enableCopy="false"/>.azurecr.io/sql-modernization-app:v1
    ```

7. Create **Azure Container App**:

    - Search for **Container Apps**
    - Click **+ Create**
    - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
    - **Container app name**: **sql-mod-app**
    - **Region**: **<inject key="Region"></inject>**
    - **Container Apps Environment**: Create new
    - **Container**: Select from Azure Container Registry
    - **Registry**: **sqlmodacr<inject key="DeploymentID" enableCopy="false"/>**
    - **Image**: **sql-modernization-app**
    - **Tag**: **v1**
    - **Ingress**: Enabled
    - **Target port**: **8501**
    - **Ingress traffic**: **Accept from anywhere**
    - Click **Review + Create**

8. Add environment variables:

    - After creation:
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

<validation step="34d75f14-cc71-4256-b6a1-731aeff9dca9" />

 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

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
