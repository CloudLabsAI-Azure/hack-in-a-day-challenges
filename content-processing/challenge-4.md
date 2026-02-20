# Challenge 4: Run the Content Processing Application

## Introduction

You've built the infrastructure, created three specialized AI agents, and connected them into an automated pipeline. Now it's time to bring everything together with a **production-grade Streamlit application** that orchestrates the full document processing workflow:

1. **Upload** documents via the web interface
2. **Store** them in Azure Blob Storage
3. **Analyse** them with Azure AI Document Intelligence (OCR extraction)
4. **Process** the extracted text through your 3-agent AI pipeline
5. **Route** results to the appropriate Cosmos DB container based on confidence

In this challenge, you'll configure and run the pre-built application, then test it with your sample documents.

## Challenge Objectives

- Download and configure the application codefiles
- Set up environment variables for all Azure services
- Authenticate with Azure CLI
- Run the Streamlit application locally
- Process documents through the full pipeline and verify results in Cosmos DB

## Steps to Complete

### Task 1: Download the Application Code

1. On your lab VM, open a terminal (PowerShell or Command Prompt).

1. Create a working directory and download the application code:

   ```powershell
   mkdir C:\ContentProcessing
   cd C:\ContentProcessing
   ```

1. Download the codefiles from the repository:

   ```powershell
   git clone https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges.git --depth 1
   cd hack-in-a-day-challenges\content-processing\codefiles
   ```

   > **Note:** If git is not available, you can download the ZIP from `https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/main.zip` and extract it to `C:\ContentProcessing`.

1. Verify you have the following files:

   ```
   codefiles/
   ├── app.py                  # Main Streamlit application
   ├── doc_processor.py        # Document Intelligence SDK integration
   ├── cosmos_helper.py        # Cosmos DB operations (dual container)
   ├── requirements.txt        # Python dependencies
   ├── .env.example            # Environment variable template
   ├── Dockerfile              # Container deployment (optional)
   ├── README.md               # Code documentation
   └── sample_data/            # Sample OCR outputs for testing
       ├── invoice_ocr.txt
       ├── receipt_ocr.txt
       ├── medical_form_ocr.txt
       ├── insurance_claim_ocr.txt
       └── identity_doc_ocr.txt
   ```

### Task 2: Configure Environment Variables

1. Copy the environment template:

   ```powershell
   copy .env.example .env
   ```

1. Open `.env` in VS Code:

   ```powershell
   code .env
   ```

1. Fill in the following values:

   **Azure AI Foundry Agent Configuration:**

   - **AGENT_API_ENDPOINT** — Go to [Azure AI Foundry](https://ai.azure.com) → Your project (**proj-default**) → **Settings** → **Overview**. Copy the **Project endpoint**.
     - Format: **https://content-hub-<inject key="DeploymentID" enableCopy="false"/>.services.ai.azure.com/api/projects/proj-default**

   - **AGENT_ID** — Go to **Agents** → Open **Document-Classification-Agent** → Copy the **Agent ID** from the Setup panel (starts with `asst_`).

   **Azure AI Document Intelligence:**

   - **DOC_INTELLIGENCE_ENDPOINT** — Go to Azure portal → your Document Intelligence resource **doc-intelligence-<inject key="DeploymentID" enableCopy="false"/>** → **Keys and Endpoint** → Copy **Endpoint**.
   - **DOC_INTELLIGENCE_KEY** — Same page → Copy **Key 1**.

   **Azure Blob Storage:**

   - **STORAGE_CONNECTION_STRING** — Go to Azure portal → Storage Account **contentstore<inject key="DeploymentID" enableCopy="false"/>** → **Access keys** → Copy **Connection string** for Key 1.

   **Azure Cosmos DB:**

   - **COSMOS_ENDPOINT** — Go to Azure portal → Cosmos DB account **content-cosmos-<inject key="DeploymentID" enableCopy="false"/>** → **Keys** → Copy **URI**.
   - **COSMOS_KEY** — Same page → Copy **Primary Key**.

1. Your `.env` file should look like this (with your actual values):

   ```env
   # Azure AI Foundry
   AGENT_API_ENDPOINT=https://content-hub-XXXXX.services.ai.azure.com/api/projects/proj-default
   AGENT_ID=asst_XXXXXXXXXXXX

   # Document Intelligence
   DOC_INTELLIGENCE_ENDPOINT=https://doc-intelligence-XXXXX.cognitiveservices.azure.com/
   DOC_INTELLIGENCE_KEY=your-key-here

   # Blob Storage
   STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=...

   # Cosmos DB
   COSMOS_ENDPOINT=https://content-cosmos-XXXXX.documents.azure.com:443/
   COSMOS_KEY=your-cosmos-key-here
   DATABASE_NAME=ContentProcessingDB
   ```

1. Save the `.env` file.

### Task 3: Install Dependencies and Authenticate

1. Install Python dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

   > **Note:** If you encounter permission errors, try `pip install --user -r requirements.txt`.

1. Authenticate with Azure CLI (required for the AI Foundry Agents SDK):

   ```powershell
   az login
   ```

   Sign in with your lab credentials: **<inject key="AzureAdUserEmail" />**

1. Set the default subscription:

   ```powershell
   az account set --subscription "<inject key="SubscriptionID" />"
   ```

### Task 4: Run the Application

1. Start the Streamlit application:

   ```powershell
   streamlit run app.py
   ```

1. The application should open in your browser at `http://localhost:8501`. You should see:
   - A gradient header: **📄 Intelligent Content Processing**
   - A sidebar showing connection status for all services (Agents, Document Intelligence, Blob Storage, Cosmos DB)
   - Four tabs: **Process Documents**, **Processing Results**, **Review Queue**, **Analytics**

1. If any service shows a red status indicator in the sidebar, check your `.env` configuration for that service.

### Task 5: Process Your First Document

1. In the **Process Documents** tab, you have two options:
   - **Upload a file** — drag and drop or browse for a document
   - **Use sample data** — select from pre-loaded sample documents

1. Click **Use sample data** and select `invoice_contoso` from the dropdown.

1. Click **🚀 Process Document**.

1. Watch the processing pipeline execute:

   | Step | What Happens |
   |------|-------------|
   | **1. Upload** | Document is uploaded to Azure Blob Storage `documents` container |
   | **2. OCR** | Document Intelligence extracts text, tables, and key-value pairs |
   | **3. Classification** | Agent classifies the document type (INVOICE) |
   | **4. Extraction** | Agent extracts structured data (vendor, line items, totals) |
   | **5. Validation** | Agent validates data quality and assigns confidence score |
   | **6. Routing** | Based on confidence: auto-approved → `ProcessedDocuments` or review needed → `ReviewQueue` |

1. The results panel should show:
   - **Classification**: INVOICE with high confidence
   - **Extracted Data**: Structured JSON with vendor info, invoice details, line items, totals
   - **Validation**: Confidence score ≥ 0.85, routing: AUTO_APPROVE
   - **Status**: ✅ Saved to `ProcessedDocuments` container

1. Process two more documents — select `receipt_cafe` and `identity_doc` from the sample data and process them.

### Task 6: Verify Data in Cosmos DB

1. Go to the Azure portal → Cosmos DB account **content-cosmos-<inject key="DeploymentID" enableCopy="false"/>** → **Data Explorer**.

1. Expand **ContentProcessingDB** → **ProcessedDocuments**.

1. Click **Items** to see the auto-approved documents. You should see at least one item with:
   - A `docType` field (e.g., "INVOICE")
   - Classification, extraction, and validation results
   - `routing_decision`: "AUTO_APPROVE"
   - `confidence_score` ≥ 0.85

1. Expand **ReviewQueue** and check if any documents were routed for human review.

<validation step="91273538-4019-4887-8d59-87c8bda31f27" />

> **Congratulations!** Your content processing application is live and routing documents intelligently.
>
> If validation fails, verify:
> - The Streamlit app runs without errors at http://localhost:8501
> - At least one document was processed and saved to Cosmos DB
> - The sidebar shows green status for all connected services

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

## Success Criteria

- Application runs at `http://localhost:8501` with all services connected (green status)
- Successfully processed an invoice — classified as INVOICE, data extracted, auto-approved
- Successfully processed a receipt — classified as RECEIPT, data extracted, routed correctly
- At least one document appears in the `ProcessedDocuments` Cosmos DB container with full pipeline results
- A low-quality document was routed to the `ReviewQueue` container with review reasons
- The processing pipeline shows real-time status updates in the UI

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| `DefaultAzureCredential` error | Run `az login` and ensure you're signed in with lab credentials |
| Agent returns empty response | Verify `AGENT_ID` matches the Classification Agent's ID (starts with `asst_`) |
| Document Intelligence fails | Check `DOC_INTELLIGENCE_ENDPOINT` includes the trailing `/` |
| Cosmos DB write fails | Verify `COSMOS_KEY` is the Primary Key (not the Connection String) |
| Blob upload fails | Check `STORAGE_CONNECTION_STRING` is the full connection string |
| App won't start | Check for port conflicts: `streamlit run app.py --server.port 8502` |
| Pipeline runs but no routing | Ensure Validation Agent returns `routing_decision` in its JSON output |

## Additional Resources

- [Azure AI Agents SDK Documentation](https://learn.microsoft.com/en-us/python/api/azure-ai-agents/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Blob Storage Python SDK](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)

Click **Next** to continue to **Challenge 5: Review Queue & End-to-End Validation**.
