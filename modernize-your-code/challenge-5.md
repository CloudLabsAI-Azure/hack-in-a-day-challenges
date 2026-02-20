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

### Task 1: Download and Extract Code Files

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

### Task 2: Install and Authenticate with Azure CLI

The application uses Azure CLI authentication to connect to your agents.

1. Open the **Windows Powershell** as an admin.

1. **Install Azure CLI** (if not already installed):
   
   For Windows:
   ```powershell
   Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
   Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi'
   ```

1. Accept the terms and license agreement and select **Install**. Once done, select **Finish**.

1. **Login to Azure**:
   ```bash
   az login
   ```
   
1. This will open a pop-up for authentication. Sign in with your Azure credentials.

1. Don't change the subscription or tenant, hit enter.

### Task 3: Get Your Agent Credentials

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

### Task 4: Configure the Application

1. Navigate to the `codefiles` folder you extracted in Task 1.

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

    - **Important Notes:**
        - Replace `<DeploymentID>` with your actual deployment ID (e.g., 2034545)
        - **CRITICAL:** Endpoint must end with `/api/projects/proj-default` (the project name is always `proj-default`)
        - Replace `<your-agent-id>` with your Translation Agent ID from step 6 (starts with `asst_`)
        - Replace `<your-cosmos-primary-key>` with your Cosmos DB Primary Key
        - The app uses Azure CLI authentication (`az login`), so no API key is needed for agents

5. Save the file.

### Task 5: Review the Code

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

### Task 6: Install Dependencies

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

### Task 7: Run the Application

1. Start the Streamlit app with Azure CLI in PATH:

    **Windows PowerShell:**

    ```powershell
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

    streamlit run app.py
    ```

1. Enter the email as **<inject key="AzureAdUserEmail"></inject>** and hit enter.

1. The application will automatically open in your browser at `http://localhost:8501` or `http://localhost:8502`

### Task 8: Test the Multi-Agent Pipeline

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

### Task 9: Test Complex Scenarios

Try these test cases to verify everything works:

**Test 1: Simple ROWNUM Query**
```sql
SELECT emp_id, emp_name, salary
FROM employees
WHERE ROWNUM <= 10
ORDER BY salary DESC;
```

Expected Output: Should convert `ROWNUM <= 10` to `TOP 10`

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

Expected Output:
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

<validation step="34d75f14-cc71-4256-b6a1-731aeff9dca9" />


> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Congratulations! You've successfully:

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

## Success Criteria

- Retrieved agent API credentials from the Microsoft Foundry project
- Configured .env file with AGENT_API_ENDPOINT, AGENT_API_KEY, AGENT_ID
- Streamlit app runs locally and calls the Translation Agent
- App displays results from all 3 connected agents (Translation, Validation, Optimization)
- Results saved to Cosmos DB TranslationResults container
- App deployed to Azure Container Apps with public URL
- Can test production app with complex Oracle SQL and see 3-phase results

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Container Apps](https://learn.microsoft.com/azure/container-apps/)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

Congratulations! You've completed all challenges. Your SQL modernization platform is production-ready!