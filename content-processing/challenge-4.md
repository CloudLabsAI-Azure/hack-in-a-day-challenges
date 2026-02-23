# Challenge 04: Run the Content Processing Application

## Introduction

You have built the infrastructure, created three specialized AI agents, and connected them into an automated pipeline. Now it's time to bring everything together with a **Streamlit application** that orchestrates the full document processing workflow:

1. **Upload** documents via the web interface
2. **Store** them in Azure Blob Storage
3. **Analyse** them with Azure AI Document Intelligence (OCR extraction)
4. **Process** the extracted text through your 3-agent AI pipeline
5. **Route** results to the appropriate Cosmos DB container based on confidence

In this challenge, you will configure and run the pre-built application, then test it with your sample documents.

## Challenge Objectives

- Download and configure the application codefiles
- Set up environment variables for all Azure services
- Authenticate with Azure CLI
- Run the Streamlit application locally
- Process documents through the full pipeline and verify results in Cosmos DB

## Steps to Complete

### Task 1: Authenticate with Azure CLI

The application uses Azure CLI authentication to connect to your agents.

1. From the **Desktop**, open **Visual Studio Code**.

1. In **Visual Studio Code**, select **File** > **Open Folder**.

1. Browse to **C:\Code**, open the **hack-in-a-day-challenges-modernize-your-code** folder, select the **codefiles** folder, and then choose **Select Folder**.
   
1. In the **Trust the authors of the files in this folder?** pop-up, select **Yes, I trust the authors**.

1. Select **Terminal** from the top menu, and then choose **New Terminal**.

1. In the opened terminal, log in to Azure by running the following command:

   ```bash
   az login
   ```

   > **Note:** This will open a browser pop-up for authentication; minimize **Visual Studio Code** to view the sign-in window.

1. On the **Sign in** page, select **Work or school account**, and then click **Continue**.

1. On the **Sign into Microsoft Azure** page, enter the below provided email and password, to login.

   - Email/Username: **<inject key="AzureAdUserEmail"></inject>**

   - Password: **<inject key="AzureAdUserPassword"></inject>**

1. In the **Stay signed in to all your apps?** window, select **No, sign in to this app only**.

1. Return to **Visual Studio Code**, enter **1** to select the subscription, and then press **Enter**.

### Task 2: Get Your Service Credentials

You need these below values to connect to your Azure services:

1. Open **Notepad**, and keep it ready to paste the required values that you will copy in the following steps.

1. Go to **Microsoft Foundry** and open the project that you created in an earlier challenge (**proj-default**).

1. In the Overview section, find the **Microsoft Foundry project endpoint** which would look like the below mentioned example:

   - Example format: `https://content-hub-<inject key="DeploymentID" enableCopy="false"/>.services.ai.azure.com/api/projects/proj-default`
   - **Important:** The project name at the end is always `proj-default`
   - Make sure it ends with `/api/projects/proj-default`

1. Navigate to **Agents** in the left menu.

1. Click on your **Document-Classification-Agent**.

1. In the Setup panel on the right, copy the **Agent ID** (starts with `asst_`).

1. Retrieve your **Azure AI Document Intelligence** details:
   - Go to Azure Portal and open your Document Intelligence resource **doc-intelligence-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Keys and Endpoint**, Copy the **Endpoint** and **Key 1**

1. Retrieve your **Azure Blob Storage** connection string:
   - Go to Azure Portal > Storage Account **contentstore<inject key="DeploymentID" enableCopy="false"/>**
   - Click on **Access keys** > Copy **Connection string** for Key 1

1. Retrieve your **Cosmos DB** connection details:
   - Go to Azure Portal and Cosmos DB account **content-cosmos-<inject key="DeploymentID" enableCopy="false"/>**
   - Click on **Keys**, Copy the **URI** and **Primary Key**

### Task 3: Configure the Application

1. Navigate back to **Visual Studio Code**.

1. Locate the `.env.example` file.

1. Rename the **.env.example** file to **.env**.

1. Open the **.env** file and replace the placeholders with the values you copied earlier:

1. Save the file.

### Task 4: Run the Application

1. In the terminal run:

   ```bash
   pip install -r requirements.txt
   ```

1. Start the Streamlit application:

   ```powershell
   streamlit run app.py
   ```

1. The application should open in your browser at `http://localhost:8501`. You should see:

   - A gradient header: **Intelligent Content Processing**
   - A sidebar showing connection status for all services (Agents, Document Intelligence, Blob Storage, Cosmos DB)
   - Four tabs: **Process Documents**, **Processing Results**, **Review Queue**, **Analytics**

1. If any service shows a red status indicator in the sidebar, check your `.env` configuration for that service.

### Task 5: Process Your First Document

1. In the **Process Documents** tab:

   - **Upload a file** - drag and drop or browse for a document

1. Click **Process Document**.

1. Watch the processing pipeline execute:

   - **Step 1 - Upload**: Document is uploaded
   - **Step 2 - OCR**: Document Intelligence extracts text, tables, and key-value pairs
   - **Step 3 - Classification**: Agent classifies the document type (INVOICE)
   - **Step 4 - Extraction**: Agent extracts structured data (vendor, line items, totals)
   - **Step 5 - Validation**: Agent validates data quality and assigns confidence score
   - **Step 6 - Routing**: Based on confidence: auto-approved to `ProcessedDocuments` or review needed to `ReviewQueue`

1. The results panel should show:

   - **Classification**: INVOICE with high confidence
   - **Extracted Data**: Structured JSON with vendor info, invoice details, line items, totals
   - **Validation**: Confidence score >= 0.85, routing: AUTO_APPROVE
   - **Status**: Saved to `ProcessedDocuments` container

1. Process two more documents - select `receipt_cafe` and `identity_doc` from the sample data and process them.

### Task 6: Verify Data in Cosmos DB

1. Go to the Azure portal, open Cosmos DB account **content-cosmos-<inject key="DeploymentID" enableCopy="false"/>**, and click on **Data Explorer**.

1. Expand **ContentProcessingDB** and open **ProcessedDocuments** container.

1. Click on **Items** to see the auto-approved documents. You should see at least one item with:

   - A `docType` field (e.g., "INVOICE")
   - Classification, extraction, and validation results
   - `routing_decision`: "AUTO_APPROVE"
   - `confidence_score` >= 0.85

1. Expand **ReviewQueue** and check if any documents were routed for human review.

<validation step="91273538-4019-4887-8d59-87c8bda31f27" />

> **Congratulations** on completing the Task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Task. If you receive a success message, you can proceed to the next Task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Task 7: Test Smart Routing

1. To test that low-confidence documents are routed correctly, use the **Upload a file** option.

1. Create a text file named `poor_scan.txt` on your desktop with deliberately messy content:

   ```
   [SCAN QUALITY: VERY POOR]
   
   ...Cont[illegible]...
   Date: ??/??/2025
   
   Amount... $[smudged]...
   Reference: [cut off]
   
   [Rest of page is blank or illegible]
   ```

1. Upload this file and process it. The pipeline should:

   - Struggle to classify (lower confidence)
   - Extract minimal data (many null fields)
   - **Route to ReviewQueue** with `MANUAL_REVIEW` and clear review reasons

1. Verify in Cosmos DB that this document appears in the **ReviewQueue** container.

## Additional Resources

- [Azure AI Agents SDK Documentation](https://learn.microsoft.com/en-us/python/api/azure-ai-agents/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Blob Storage Python SDK](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)

Now, click **Next** to continue to **Challenge 05**.
