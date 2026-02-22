# Challenge 01: Set Up Azure Infrastructure

## Introduction

Before building your AI-powered document processing pipeline, you need to provision the Azure services that form its backbone. In this challenge, you will set up four key services: Azure Blob Storage for document ingestion, Azure AI Document Intelligence for OCR extraction, Microsoft Foundry for the multi-agent AI pipeline, and Azure Cosmos DB for dual-container persistence.

You will also upload sample documents and test Document Intelligence's OCR capabilities to see raw extraction in action, setting the stage for the intelligent agents you will build in upcoming challenges.

## Challenge Objectives

- Create an Azure Storage Account with a blob container for document ingestion
- Upload 5 sample documents (invoice, receipt, medical form, insurance claim, ID)
- Create an Azure AI Document Intelligence resource
- Test OCR extraction in Document Intelligence Studio
- Create a Microsoft Foundry project and deploy a GPT model
- Create an Azure Cosmos DB account with two containers: ProcessedDocuments and ReviewQueue

## Steps to Complete

### Task 1: Create Azure Storage Account

1. In the Azure portal, click **+ Create a resource** and search for **Storage account**.

1. Click on **Create** and configure with the following settings:

   - **Subscription**: Select the available **Azure subscription**
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Storage account name**: **docstore<inject key="DeploymentID" enableCopy="false"/>**
   - **Region**: **<inject key="Region" />**
   - **Performance**: **Standard**
   - **Redundancy**: **Locally-redundant storage (LRS)**

1. Click on **Review + Create**, then **Create**. Wait for the deployment to complete.

1. Navigate to your new Storage Account. In the left menu, click **Containers** under **Data storage**.

1. Click on **+ Add container** and create a container named **documents**.

1. Click on **+ Add container** again and create a second container named **processed**.

### Task 2: Download and Extract Sample Documents and Code Files

The application code is provided in a pre-built package.

1. On your lab VM, open a terminal PowerShell.

1. Create a working directory:

   ```powershell
   mkdir C:\Code
   ```

1. **Download the code package**:
   
   Access the link mentioned below using browser:
   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/content-processing-files.zip
   ```

1. **Extract the ZIP file**:
   
   - Right-click on the downloaded `content-processing-files.zip` file
   - Select the **Extract All...** option
   - Choose a location `C:\Code`
   - Click on **Extract**

1. Extract the ZIP file. You should see 5 sample documents inside the **sample_data** folder:

   - **invoice_contoso.pdf** - Commercial invoice from Contoso Ltd with line items, amounts, and payment terms
   - **receipt_cafe.jpg** - Cafe receipt with items, tax, and total
   - **medical_form.pdf** - Patient intake form with personal details and medical history
   - **insurance_claim.pdf** - Auto insurance claim with incident details and cost estimates
   - **drivers_license.jpg** - Sample driver's license with personal information

### Task 3: Create Azure AI Document Intelligence Resource

1. In the Azure portal, search for **Document Intelligence** and **Select it**.

1. Click on **Create** and configure:

   - **Subscription**: Select the available **Azure subscription**
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Region**: **<inject key="Region" />**
   - **Name**: **doc-intel-<inject key="DeploymentID" enableCopy="false"/>**
   - **Pricing tier**: **Standard S0**.

1. Click **Review + Create**, then **Create**. Wait for deployment to complete.

### Task 4: Test OCR in Document Intelligence Studio

1. In the Azure portal, navigate to your deployed **doc-intel-<inject key="DeploymentID" enableCopy="false"/>** Document Intelligence.

1. On the **Overview** page, select **Go to Document Intelligence Studio** to open the studio in a new tab.

1. Select **Start with Document Intelligence**.

1. Under **Document analysis**, select **OCR/Read** by clicking on **Try it out**.

1. If prompted on the **Sign into Microsoft Azure** tab, enter the provided credentials and select **Sign in**.

   - **Email**: **<inject key="AzureAdUserEmail" />**
   - **Password**: **<inject key="AzureAdUserPassword" />**

1. In the top bar, click **Configure** and select:

   - **Subscription**: Select the available **Azure subscription**
   - **Resource**: Select **doc-intel-<inject key="DeploymentID" enableCopy="false"/>**
   - click **Continue** and click on **Finish**.

1. Click **Browse for files** and upload **invoice_contoso.pdf** from your sample documents.

1. Click **Run analysis** and wait for results.

1. Observe the extracted content:

   - **Text** - The full text extracted from the document, preserving reading order
   - **Words and Lines** - Individual words and lines detected with confidence scores
   - **Pages** - Page-level metadata, including dimensions and language

      > **Note:** The OCR/Read model focuses on text extraction, which is exactly what our AI agents need. The agents downstream will handle classification, structured data extraction, and validation. We don't need Layout's table/structure detection because the agents are smart enough to understand the text format.

1. Try analysing **Images** as well. Notice how Document Intelligence handles different document formats (PDF vs image) and layouts.

### Task 5: Create Microsoft Foundry Resource and Deploy GPT Model

1. In the Azure portal, search for **Microsoft Foundry** in the top search bar.

1. In the left menu under **Use with Foundry**, click **Foundry**.

1. Click **+ Create**.

1. On the **Create a Foundry resource** page, fill in the following:

   - **Subscription**: Select the available **Azure subscription**
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Name**: **openai-doc-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - **Region**: **<inject key="Region" />**
   - **Default project name**: Keep it as **proj-default**

      > **Important:** Keep the default project name as **proj-default** - this is used in the application's endpoint URL.

1. Click **Review + Create**, then **Create**. Wait for the deployment to complete (this may take 2-3 minutes).

1. Once deployed, navigate to the **Microsoft Foundry** resource you just created.

1. On the **Overview** page of the Microsoft Foundry resource, select **Go to Foundry**.

1. In the left menu, navigate to **Models + endpoints**.

1. Click **+ Deploy model** and select **Deploy base model**.

1. Search for and select **GPT-4.1** from the model catalog and click on **Confirm** button.

1. Configure the deployment:

   - **Deployment name**: `doc-processor`
   - **Deployment type**: **Standard**
   - **Tokens per Minute Rate Limit**: **40K**

      > **Note:** Do not set the Tokens per Minute rate limit above **40K**, as exceeding this limit may cause deployment or quota issues.

1. Click **Deploy** and wait for the model to be ready.

### Task 6: Create Azure Cosmos DB Account

1. In the Azure portal, click **+ Create a resource** and search for **Azure Cosmos DB**.

1. Select **Azure Cosmos DB for NoSQL** and click **Create**.

1. Configure:

   - **Subscription**: Select the available **Azure subscription**
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Account Name**: **cosmos-docs-<inject key="DeploymentID" enableCopy="false"/>**
   - **Region**: **<inject key="Region" />**
   - **Capacity mode**: **Serverless**

1. Click **Review + Create**, then **Create**. Wait for deployment (this may take 3-5 minutes).

1. Navigate to the Cosmos DB account. In the left menu, click **Data Explorer**.

1. Click **New Database** and enter:

   - **Database id**: `ContentProcessingDB`

1. Click **OK** to create the database.

1. Expand the **ContentProcessingDB** database and click **New Container**:

   - **Database id**: Select **Use existing** and choose **ContentProcessingDB**
   - **Container id**: `ProcessedDocuments`
   - **Partition key**: `/docType`

1. Click **OK**, then create a second container:

   - **Database id**: Select **Use existing** and choose **ContentProcessingDB**
   - **Container id**: `ReviewQueue`
   - **Partition key**: `/documentId`

1. Verify you have:

   - Database: `ContentProcessingDB`
   - Container: `ProcessedDocuments` (partition key: `/docType`)
   - Container: `ReviewQueue` (partition key: `/documentId`)

<validation step="67fcae6d-e490-4215-8b86-e1cdc1722cc2" />
 
> **Congratulations** on completing the Task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Task. If you receive a success message, you can proceed to the next Task.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Additional Resources

- [Azure Blob Storage Documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/)
- [Azure AI Document Intelligence Overview](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)
- [Microsoft Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/)

Now, click **Next** to continue to **Challenge 02**.
