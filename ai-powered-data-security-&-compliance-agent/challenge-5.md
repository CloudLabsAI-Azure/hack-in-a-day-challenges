# Challenge 05: Configure Logic App, Run the Dashboard, and Test End-to-End

## Introduction

Your three-agent pipeline is operational. All the application code has been built for you. In this final challenge, you will create a Logic App to process Event Grid security alerts, configure and run the Streamlit web dashboard locally, and perform end-to-end testing of the complete Data Security Agent system.

## Prerequisites

- Completed Challenge 4 (all three agents created and connected)
- Event Grid Topic created in Challenge 1
- Cosmos DB and Storage Account configured with sample data

## Challenge Objectives

- Create a Logic App workflow that processes Event Grid security alerts
- Configure the Logic App to write alerts to Cosmos DB and send notifications
- Download and configure the Streamlit application
- Authenticate with Azure CLI
- Run the dashboard and test the multi-agent pipeline
- Verify end-to-end flow: Scan → Classification → Risk Detection → Compliance → Alerts

## Steps to Complete

### Task 1: Create Logic App

1. In the **Azure Portal**, search for **Logic Apps** and select it.

1. Click on **+ Add**.

1. Configure the Logic App:

   - **Subscription**: Select the available **Azure subscription**
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Logic App name**: **security-alert-processor-<inject key="DeploymentID" enableCopy="false"/>**
   - **Region**: Keep **Default**
   - **Plan type**: Select **Consumption**
   - **Zone redundancy**: Select **Disabled**

1. Click **Review + Create**, then **Create**.

1. Wait for the deployment to complete and click **Go to resource**.

### Task 2: Configure Logic App — Event Grid Trigger

1. In the Logic App, click on **Logic app designer** from the left navigation under **Development Tools**.

1. In the designer, under **Start with a common trigger**, select **When an Event Grid resource event occurs**.

   > **Note:** If you do not see this option, click **+ Add a trigger** and search for **Event Grid**.

1. If prompted to sign in, click **Sign in** and authenticate with your lab credentials:
   - Email: **<inject key="AzureAdUserEmail"></inject>**
   - Password: **<inject key="AzureAdUserPassword"></inject>**

1. Configure the Event Grid trigger:

   - **Subscription**: Select your Azure subscription
   - **Resource Type**: Select **Microsoft.EventGrid.Topics**
   - **Resource Name**: Select **security-alerts-topic-<inject key="DeploymentID" enableCopy="false"/>**
   - **Event Type Item**: Leave as default (all events)

1. Click **+ New step** to add the next action.

### Task 3: Configure Logic App — Parse Event Data

1. Search for **Parse JSON** action and select it.

1. In the **Content** field, click the dynamic content panel and select **Body** from the Event Grid trigger output.

1. In the **Schema** field, click **Use sample payload to generate schema** and paste the following sample payload:

   ```json
   [{
     "id": "sample-event-001",
     "eventType": "SecurityAlert.Critical",
     "subject": "security/risk-detection/critical",
     "data": {
       "alert_id": "ALERT-001",
       "severity": "CRITICAL",
       "risk_id": "ACT-001",
       "description": "Intern bulk-exported 48500 rows of PII/PCI data at 2:47 AM",
       "user": "jake.morrison",
       "role": "Intern",
       "affected_data": ["SSN", "CreditCardNumber", "CVV"],
       "timestamp": "2025-06-15T02:47:00Z",
       "requires_approval": true,
       "scan_id": "scan-20250615-001"
     },
     "eventTime": "2025-06-15T02:47:00Z",
     "dataVersion": "1.0"
   }]
   ```

1. Click **Done** to generate the schema.

### Task 4: Configure Logic App — Condition and Actions

1. Click **+ New step**. Search for and select **Condition** (under Control).

1. In the Condition, configure:

   - Click the left value field, select **severity** from the Parse JSON dynamic content
   - Set the operator to **is equal to**
   - Set the right value to **CRITICAL**

1. In the **If true** branch, click **Add an action**.

1. Search for **Azure Cosmos DB** and select **Create or update document (V3)**.

1. If prompted, create a new connection:

   - **Connection Name**: Enter `SecurityCosmosDB`
   - **Authentication Type**: Select **Access Key**
   - **Account ID**: Enter your Cosmos DB account name: `security-agent-cosmos-<inject key="DeploymentID" enableCopy="false"/>`
   - **Access Key to your Azure Cosmos DB account**: Paste the **PRIMARY KEY** you saved from Challenge 1
   - Click **Create**.

1. Configure the Cosmos DB action:

   - **Database ID**: Select **SecurityAgentDB** or enter `SecurityAgentDB`
   - **Container ID**: Select **SecurityAlerts** or enter `SecurityAlerts`
   - **Document**: Enter the following (use dynamic content where indicated):

     ```json
     {
       "id": "@{guid()}",
       "alertId": "@{body('Parse_JSON')?[0]?['data']?['alert_id']}",
       "severity": "@{body('Parse_JSON')?[0]?['data']?['severity']}",
       "description": "@{body('Parse_JSON')?[0]?['data']?['description']}",
       "user": "@{body('Parse_JSON')?[0]?['data']?['user']}",
       "role": "@{body('Parse_JSON')?[0]?['data']?['role']}",
       "timestamp": "@{body('Parse_JSON')?[0]?['data']?['timestamp']}",
       "scanId": "@{body('Parse_JSON')?[0]?['data']?['scan_id']}",
       "status": "OPEN",
       "processedAt": "@{utcNow()}"
     }
     ```

   - **Partition Key Value**: Enter `CRITICAL`

   > **Note:** If you see a multi-line text box, click **Switch to input text format** to enter the JSON directly. You can also use the **Code view** to paste the JSON directly.

1. In the **If false** branch (for non-CRITICAL alerts), click **Add an action**.

1. Search for **Azure Cosmos DB** and select **Create or update document (V3)** again.

1. Use the same connection and configure:

   - **Database ID**: `SecurityAgentDB`
   - **Container ID**: `SecurityAlerts`
   - **Document**:

     ```json
     {
       "id": "@{guid()}",
       "alertId": "@{body('Parse_JSON')?[0]?['data']?['alert_id']}",
       "severity": "@{body('Parse_JSON')?[0]?['data']?['severity']}",
       "description": "@{body('Parse_JSON')?[0]?['data']?['description']}",
       "user": "@{body('Parse_JSON')?[0]?['data']?['user']}",
       "role": "@{body('Parse_JSON')?[0]?['data']?['role']}",
       "timestamp": "@{body('Parse_JSON')?[0]?['data']?['timestamp']}",
       "scanId": "@{body('Parse_JSON')?[0]?['data']?['scan_id']}",
       "status": "OPEN",
       "processedAt": "@{utcNow()}"
     }
     ```

   - **Partition Key Value**: Enter `HIGH`

1. Click **Save** at the top of the Logic App designer to save the workflow.

<validation step="c1e9f5a2-8b63-4d34-e9f0-6b2c7d4e5f83" />

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 5: Download and Extract Code Files

The application code is provided in a pre-built package.

1. On your lab VM, open a terminal PowerShell.

1. Create a working directory:

   ```powershell
   mkdir C:\Code
   ```

1. **Download the code package**:

   Access the link below using your browser:

   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/ai-powered-data-security.zip
   ```

1. **Extract the ZIP file**:

   - Right-click on the downloaded `ai-powered-data-security.zip` file
   - Select the **Extract All...** option
   - Choose a location: `C:\Code`
   - Click on **Extract**

### Task 6: Authenticate with Azure CLI

The application uses Azure CLI authentication to connect to your agents.

1. From the **Desktop**, open **Visual Studio Code**.

1. In **Visual Studio Code**, select **File** > **Open Folder**.

1. Browse to **C:\Code**, open the **hack-in-a-day-challenges-ai-powered-data-security** folder, select the **codefiles** folder, and then choose **Select Folder**.

1. In the **Trust the authors of the files in this folder?** pop-up, select **Yes, I trust the authors**.

1. Select **Terminal** from the top menu, and then choose **New Terminal**.

1. In the opened terminal, log in to Azure by running the following command:

   ```bash
   az login
   ```

   > **Note:** This will open a browser pop-up for authentication; minimize Visual Studio Code to view the sign-in window.

1. On the **Sign in** page, select **Work or school account**, and then click **Continue**.

1. On the **Sign into Microsoft Azure** page, enter the below provided email and password to login.

   - Email/Username: **<inject key="AzureAdUserEmail"></inject>**
   - Password: **<inject key="AzureAdUserPassword"></inject>**

1. In the **Stay signed in to all your apps?** window, select **No, sign in to this app only**.

1. Return to **Visual Studio Code**, enter **1** to select the subscription, and then press **Enter**.

### Task 7: Get Your Agent Credentials

You need the following values to connect to your agents:

1. Open **Notepad** and keep it ready to paste the required values.

1. Go to **Microsoft Foundry** and open the project that you created in Challenge 1.

1. In the Overview section, find the **Microsoft Foundry project endpoint** which would look like:

   - Example: `https://data-security-XXXXXXX.services.ai.azure.com/api/projects/proj-default`
   - **Important:** The project name at the end is always `proj-default` (not data-security-XXXX)
   - Make sure it ends with `/api/projects/proj-default`

1. Navigate to **Agents** in the left menu.

1. Click on your **Data-Classification-Agent**.

1. In the Setup panel on the right, copy the **Agent ID** (starts with `asst_`).

1. From Challenge 1, retrieve your **Cosmos DB** connection details:
   - Go to Azure Portal → Your Cosmos DB account
   - Click **Keys** → Copy **URI** and **Primary Key**

1. From Challenge 1, retrieve your **Storage Account** details:
   - Go to Azure Portal → Your Storage Account
   - Click **Access keys** → Copy **Storage account name** and **Key**

1. From Challenge 1, retrieve your **Event Grid** details:
   - Go to Azure Portal → Your Event Grid Topic
   - Click **Access keys** → Copy **Topic Endpoint** and **Key 1**

### Task 8: Configure the Application

1. Navigate back to **Visual Studio Code**.

1. Locate the `.env.example` file.

1. Rename the **.env.example** file to **.env**.

1. Open the **.env** file and fill in the values:

   ```
   AGENT_API_ENDPOINT=https://data-security-XXXXXXX.services.ai.azure.com/api/projects/proj-default
   AGENT_ID=asst_XXXXXXXXXXXXXXXX
   COSMOS_ENDPOINT=https://security-agent-cosmos-XXXXXXX.documents.azure.com:443/
   COSMOS_KEY=your_cosmos_primary_key
   DATABASE_NAME=SecurityAgentDB
   STORAGE_ACCOUNT_NAME=securitydataXXXXXX
   STORAGE_ACCOUNT_KEY=your_storage_account_key
   EVENT_GRID_ENDPOINT=https://security-alerts-topic-XXXXXXX.region.eventgrid.azure.net/api/events
   EVENT_GRID_KEY=your_event_grid_key
   ```

1. Replace each placeholder with the actual values you copied. Save the file.

### Task 9: Review the Code

Before running the application, explore the code structure:

**app.py** — Main Streamlit application
- **Lines 1-30**: Imports, page config, and environment variable loading
- **Lines 32-200**: Custom CSS styling (animated gradient header, fade-in animations, severity badges, metric cards with hover effects, dark sidebar)
- **Lines 202-250**: Configuration validation and setup guide
- **Lines 252-310**: Cosmos DB, Event Grid, and Storage Account helper functions
- **Lines 312-370**: Agent API calling with AgentsClient and DefaultAzureCredential
- **Lines 372-430**: Response parsing for classification, risk detection, and compliance results
- **Lines 432-470**: Scan prompt builder (constructs the full data payload for the agent)
- **Lines 472-680**: Streamlit UI with 6 tabs (Scan, Classification, Risk Detection, Remediation, Alerts, History)

**Helper modules:**
- **cosmos_helper.py** — Cosmos DB operations (save scan results, save alerts, query history)
- **storage_helper.py** — Azure Blob Storage operations (read schemas, policies, logs)
- **event_grid_helper.py** — Event Grid publishing (CRITICAL and HIGH risk alerts)

**Key features:**
- Azure CLI authentication using DefaultAzureCredential
- Fast Scan (top 5 rows) and Full Scan (all rows) modes
- Real-time progress tracking with status indicators
- Animated gradient header and severity-coded badges
- Connection status dots in the sidebar (animated pulse)
- Automatic Event Grid publishing for critical/high risks
- Cosmos DB persistence for scan history and alerts
- Six-tab dashboard interface

### Task 10: Install Dependencies

1. In the terminal, run:

   ```bash
   pip install -r requirements.txt
   ```

1. This installs:

   - `streamlit` — Web framework
   - `azure-ai-agents` — Azure AI Agents SDK
   - `azure-ai-projects` — Microsoft Foundry SDK
   - `azure-identity` — Azure authentication
   - `azure-cosmos` — Cosmos DB SDK
   - `azure-storage-blob` — Blob Storage SDK
   - `azure-eventgrid` — Event Grid SDK
   - `python-dotenv` — Environment variables
   - `pandas` — Data processing

### Task 11: Run the Application

1. Start the Streamlit app:

   **Windows PowerShell:**

   ```powershell
   $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

   streamlit run app.py
   ```

1. Enter the email as **<inject key="AzureAdUserEmail"></inject>** and press Enter.

1. The application will automatically open in your browser at `http://localhost:8501` or `http://localhost:8502`.

### Task 12: Test the Security Scan Pipeline

1. You will see an animated gradient header: **"Data Security & Compliance Agent"**.

1. In the **sidebar**, verify connection status indicators:
   - Agent: Green dot (connected)
   - Cosmos DB: Green dot (connected)
   - Storage: Green dot (connected)
   - Event Grid: Green dot (connected)

1. Set the **Scan Mode** to **Fast Scan** (reads top 5 rows per table for faster results).

1. Navigate to the **Scan Data Assets** tab.

1. Click the **Run Security Scan** button.

1. Watch the progress indicators:
   - Loading data from Storage Account...
   - Building scan prompt...
   - Sending to Classification Agent...
   - Agent processing (Classification → Risk Detection → Compliance)...
   - Publishing alerts to Event Grid...
   - Saving results to Cosmos DB...
   - Scan complete.

1. After completion, a gradient completion banner appears and the results populate across tabs.

### Task 13: Explore the Results

1. Navigate to the **Classification** tab:
   - View the classification table for all columns across all datasets
   - Check the metric cards: PII Count, PHI Count, PCI Count, Confidential, Public
   - Verify SSN columns are classified as PII, card numbers as PCI, diagnoses as PHI

1. Navigate to the **Risk Detection** tab:
   - View the risk summary: Critical, High, Medium, Low counts
   - Check the access policy risks table (over-privileged roles)
   - Check the activity anomalies table (after-hours exports, foreign IPs)
   - Verify the intern's 2:47 AM bulk export is flagged as CRITICAL

1. Navigate to the **Remediation** tab:
   - View the compliance score (should be low given the sample data risks)
   - Check the remediation playbook with priorities and assigned owners
   - Review the approval queue for actions requiring human sign-off
   - Verify regulation mappings (GDPR, HIPAA, PCI-DSS)

1. Navigate to the **Alerts & Approvals** tab:
   - View alerts written to Cosmos DB by the Logic App
   - Check alert severity and status

   > **Note:** Event Grid alerts are processed by the Logic App asynchronously. Alerts may take a few moments to appear in Cosmos DB after the scan completes.

1. Navigate to the **Scan History** tab:
   - View past scan records stored in Cosmos DB
   - Verify the scan you just ran appears with its timestamp and results summary

### Task 14: Run a Full Scan

1. In the sidebar, switch to **Full Scan** mode.

1. Click **Run Security Scan** again.

1. This scan processes all sample rows (not just the top 5) and takes longer.

1. Compare the Full Scan results with the Fast Scan — the classifications should be consistent, and the risk detection may find additional patterns in the complete log data.

### Task 15: Verify Event Grid and Logic App Flow

1. Go to the **Azure Portal** and navigate to your Logic App: **security-alert-processor-<inject key="DeploymentID" enableCopy="false"/>**.

1. Click on **Overview** and check the **Runs history** section.

1. You should see one or more successful runs triggered by the Event Grid alerts from your scans.

1. Click on a run to see the execution details:
   - Event Grid trigger fired
   - JSON parsed
   - Condition evaluated (CRITICAL or not)
   - Document created in Cosmos DB

1. Navigate to **Cosmos DB** → **Data Explorer** → **SecurityAgentDB** → **SecurityAlerts**.

1. Verify that alert documents were created by the Logic App with the correct severity, description, and status.

<validation step="d2f0a6b3-9c74-4e45-f0a1-7c3d8e5f6a94" />

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Congratulations! You have successfully:

- Built a 3-agent AI system in Microsoft Foundry (Classification → Risk Detection → Compliance Advisory)
- Connected agents in a pipeline with automatic hand-off
- Created an Event Grid Topic for event-driven alerts
- Configured a Logic App to process security alerts and write to Cosmos DB
- Deployed sample datasets to Azure Blob Storage
- Run a Streamlit web dashboard with 6 interactive tabs
- Performed end-to-end security scans with Fast and Full scan modes
- Verified the complete flow from data scan to alert processing

**What you learned:**
- Microsoft Foundry Agent visual builder and multi-agent orchestration
- Azure AI Projects SDK integration with DefaultAzureCredential
- Azure Cosmos DB for NoSQL storage and querying
- Azure Blob Storage for data asset management
- Azure Event Grid for event-driven architecture
- Azure Logic Apps for no-code workflow automation
- Streamlit for interactive web dashboards
- Data classification concepts (PII, PHI, PCI)
- Security risk detection and compliance mapping (GDPR, HIPAA, PCI-DSS)

## Success Criteria

- Logic App created and configured with Event Grid trigger and Cosmos DB actions
- Streamlit app runs locally and connects to all Azure services
- Fast Scan completes and displays results across all 6 tabs
- Full Scan completes with consistent classification results
- Event Grid alerts published for CRITICAL and HIGH risks
- Logic App runs history shows successful executions
- Cosmos DB SecurityAlerts container has alert documents from Logic App
- Scan history persists in Cosmos DB ScanResults container

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Logic Apps](https://learn.microsoft.com/azure/logic-apps/)
- [Azure Event Grid](https://learn.microsoft.com/azure/event-grid/)
- [Azure AI Agents SDK](https://learn.microsoft.com/python/api/overview/azure/ai-agents-readme)

Congratulations! You have completed all challenges. Your AI-Powered Data Security & Compliance Agent is fully operational.
