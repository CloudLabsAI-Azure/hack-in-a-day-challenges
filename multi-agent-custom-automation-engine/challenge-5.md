# Challenge 05: Production Dashboard & End-to-End Validation

## Introduction

In this final challenge, you will run a **Streamlit dashboard** that brings together the complete Multi-Agent Automation Engine built throughout the hackathon. Instead of running scripts in the terminal, you will use a professional web interface to submit workflow requests, watch agents collaborate in real time, view structured results, and review execution history from Cosmos DB.

The pre-built application wraps your Semantic Kernel agents and orchestrator in an interactive dashboard with sample data, file upload support, and full audit traceability, demonstrating a production-ready AI orchestration pattern suitable for enterprise automation.

## Challenge Objectives

- Download and configure the pre-built Streamlit application
- Authenticate with Azure CLI
- Run the production dashboard locally
- Test the multi-agent pipeline through the web UI with sample enterprise scenarios
- Process multiple workflow requests and review agent outputs
- Verify execution history in Cosmos DB

## Steps to Complete

### Task 1: Download the Application Code

The application code is provided in the lab repository.

1. On your lab VM, open a terminal (**PowerShell** or **Command Prompt**).

2. Create a working directory and download the application code:

   ```powershell
   mkdir C:\LabFiles
   cd C:\LabFiles
   ```

3. Download  the ZIP from `https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/multi-agent-custom-automation-engine.zip` and extract it to `C:\LabFiles`.

### Task 2: Authenticate with Azure CLI

The application uses Azure CLI authentication to connect to Azure services.

1. Open **Windows PowerShell** as an administrator.

1. **Install Azure CLI** (if not already installed):

   ```powershell
   Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
   Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi'
   ```

1. Accept the terms and license agreement and select **Install**. Once done, select **Finish**.

1. **Login to Azure**:
   ```powershell
   az login
   ```

1. This will open a pop-up for authentication. Sign in with your Azure credentials.

1. Don't change the subscription or tenant, hit enter.

### Task 3: Get Your Configuration Values

You need the following values from your Azure resources:

1. **Microsoft Foundry API Key and Endpoint**:

   - Go to **Azure Portal** and open your Microsoft Foundry resource: **agent-foundry-<inject key="DeploymentID" enableCopy="false"/>**
   - Navigate to **Keys and Endpoint**
   - Copy the **Key** and **Endpoint**

2. **Cosmos DB Connection Details** (from Challenge 1):

   - Go to **Azure Portal** and open your Cosmos DB account: **agent-cosmos-<inject key="DeploymentID" enableCopy="false"/>**
   - Navigate to **Settings** and then select **Keys**
   - Copy the **URI** and **PRIMARY KEY**

### Task 4: Configure the Application

1. Navigate to the `codefiles` folder you extracted in Task 1.

2. Locate the `.env.example` file.

3. **Copy** `.env.example` to create a new file named `.env`:

   ```powershell
   copy .env.example .env
   ```

4. Open `.env` and replace the placeholder values:

   ```env
   # Azure OpenAI / Microsoft Foundry Configuration
   AZURE_OPENAI_ENDPOINT=https://<your-foundry-resource>.openai.azure.com/
   MICROSOFT_FOUNDRY_API_KEY=<your-foundry-key>
   AZURE_DEPLOYMENT_NAME=agent-gpt-4o-mini

   # Cosmos DB Configuration
   COSMOS_DB_ENDPOINT=https://agent-cosmos-<DeploymentID>.documents.azure.com:443/
   COSMOS_DB_KEY=<your-cosmos-primary-key>
   COSMOS_DB_DATABASE=agent-memory-db
   COSMOS_DB_CONTAINER=agent-state
   ```

   - **Important Notes:**
     - Replace `<your-foundry-resource>` with your Foundry resource name
     - Replace `<your-foundry-key>` with the API key from Task 3
     - Replace `<DeploymentID>` with your actual deployment ID
     - Replace `<your-cosmos-primary-key>` with your Cosmos DB Primary Key
     - Keep `AZURE_DEPLOYMENT_NAME=agent-gpt-4o-mini` (the model deployment from Challenge 1)

5. Save the file.

### Task 5: Review the Application Code

Before running, take a moment to explore the application code:

**app.py** - Main Streamlit application
- Custom CSS styling for premium enterprise UI
- Three-tab layout: Process Workflow, Results, History
- Sample data selection and file upload support
- Real-time pipeline progress tracking
- Professional result display with agent-specific cards

**orchestrator.py** - Multi-agent orchestrator
- Semantic Kernel initialization and agent definitions
- Sequential agent execution: Extraction, Validation, Communication, and Reporting
- Shared state management and workflow tracking
- Structured JSON output from each agent

**cosmos_helper.py** - Cosmos DB persistence
- Save and retrieve workflow states
- Query execution history
- Error handling and retry logic

**Key features:**
- Rich enterprise-style UI with gradient headers and status cards
- 5 sample enterprise scenarios (employee onboarding, expense reports, compliance, etc.)
- File upload support for `.txt` files
- Real-time progress indicators for each pipeline stage
- Structured result display showing all four agent outputs
- Execution history tab with Cosmos DB integration
- Error handling and input validation

### Task 6: Install Dependencies

1. Open a terminal in VS Code or PowerShell.

2. Navigate to the `codefiles` folder:

   ```powershell
   cd C:\LabFiles\hack-in-a-day-challenges\multi-agent-custom-automation-engine\codefiles
   ```

3. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

   > **Note:** This may take 3-5 minutes to complete.

### Task 7: Run the Application

1. Start the Streamlit app:

   ```powershell
   .venv\Scripts\python.exe -m streamlit run app.py
   ```

1. Enter the email as **<inject key="AzureAdUserEmail"></inject>** and hit enter.

1. The application will automatically open in your browser at `http://localhost:8501`

### Task 8: Test the Multi-Agent Pipeline

1. You'll see the **Multi-Agent Automation Engine** dashboard with a blue gradient header.

2. In the **sidebar**, verify all agents show green checkmarks:
   - Extraction Agent
   - Validation Agent
   - Communication Agent
   - Reporting Agent

3. **Option A: Use a Sample Scenario**
   - On the right side, select a sample from the dropdown (e.g., "Employee Onboarding")
   - Click **"Load Sample"**

4. **Option B: Upload a Text File**
   - Click the file upload area
   - Upload a `.txt` file with enterprise workflow text

5. **Option C: Type Directly**
   - Paste or type your workflow request in the text area

6. Click the **"Run Pipeline"** button

7. Watch the progress indicators as your request flows through all four agents:
   - Extraction Agent processing...
   - Validation Agent processing...
   - Communication Agent processing...
   - Reporting Agent processing...
   - Pipeline completed!

8. After completion, you'll see a completion banner and the app will automatically switch to the **"Results"** tab.

9. View the **four-section output**:

   **Section 1: Extraction**
   - Structured JSON data extracted from the input text

   **Section 2: Validation**
   - Validation status and any flagged issues

   **Section 3: Communication**
   - Generated email with subject and body

   **Section 4: Reporting**
   - Workflow execution summary

10. Click the **"History"** tab to see all past workflows from Cosmos DB.

### Task 9: Test Multiple Scenarios

Try each of the 5 sample scenarios to verify the pipeline handles different enterprise workflows:

**Test 1: Employee Onboarding**
- Select "Employee Onboarding" from the dropdown
- Expected: Extracts employee name, department, start date, manager, etc.

**Test 2: Expense Report**
- Select "Expense Report" from the dropdown
- Expected: Extracts expense items, amounts, dates, and approval fields

**Test 3: Compliance Report**
- Select "Compliance Report" from the dropdown
- Expected: Extracts audit findings, risk levels, and action items

**Test 4: Leave Request**
- Select "Leave Request" from the dropdown
- Expected: Extracts employee info, leave dates, type, and approval chain

**Test 5: Vendor Contract**
- Select "Vendor Contract" from the dropdown
- Expected: Extracts vendor details, contract terms, and financial amounts

## Success Criteria

- Streamlit application runs locally and displays the Multi-Agent Automation Engine dashboard
- All four agents show green status in the sidebar
- At least 3 sample scenarios are processed successfully through the full pipeline
- Results tab displays structured output from all four agents (Extraction, Validation, Communication, Reporting)
- Each workflow shows `status: COMPLETED` in the Results tab
- Cosmos DB contains complete workflow records with `agentData` and `history` entries
- History tab displays past workflow executions retrieved from Cosmos DB

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Semantic Kernel Python SDK](https://learn.microsoft.com/semantic-kernel/overview/)
- [Azure Cosmos DB Data Explorer](https://learn.microsoft.com/azure/cosmos-db/data-explorer)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

Congratulations! You've completed all challenges. Your Multi-Agent Automation Engine is production-ready!
