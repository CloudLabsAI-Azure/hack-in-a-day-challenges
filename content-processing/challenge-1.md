# Challenge 1: Set Up Azure Infrastructure

## Introduction

Before building your AI-powered document processing pipeline, you need to provision the Azure services that form its backbone. In this challenge, you'll set up **four key services**: Azure Blob Storage for document ingestion, Azure AI Document Intelligence for OCR extraction, Microsoft Foundry (Azure AI Foundry) for the multi-agent AI pipeline, and Azure Cosmos DB for dual-container persistence.

You'll also upload sample documents and test Document Intelligence's OCR capabilities to see raw extraction in action — setting the stage for the intelligent agents you'll build in upcoming challenges.

## Challenge Objectives

- Create an Azure Storage Account with a blob container for document ingestion
- Upload 5 sample documents (invoice, receipt, medical form, insurance claim, ID)
- Create an Azure AI Document Intelligence resource
- Test OCR extraction in Document Intelligence Studio
- Create a Microsoft Foundry project and deploy a GPT-4.1 model
- Create an Azure Cosmos DB account with two containers: `ProcessedDocuments` and `ReviewQueue`

## Steps to Complete

### Part 1: Create Azure Storage Account

1. In the Azure portal, click **+ Create a resource** and search for **Storage account**.

1. Click **Create** and configure with the following settings:

   | Setting | Value |
   |---------|-------|
   | **Subscription** | Your Azure subscription |
   | **Resource group** | challenge-rg-<inject key="DeploymentID" enableCopy="false"/> |
   | **Storage account name** | docstore<inject key="DeploymentID" enableCopy="false"/> |
   | **Region** | <inject key="Region" /> |
   | **Performance** | Standard |
   | **Redundancy** | Locally-redundant storage (LRS) |

1. Click **Review + Create**, then **Create**. Wait for the deployment to complete.

1. Navigate to your new Storage Account. In the left menu, click **Containers** under **Data storage**.

1. Click **+ Container** and create a container named **documents** with **Private** access level.

1. Click **+ Container** again and create a second container named **processed** with **Private** access level.

### Part 2: Upload Sample Documents

1. Download the sample documents from:

   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/content-processing-files.zip
   ```

1. Extract the ZIP file. You should see 5 sample documents:

   | File | Type | Description |
   |------|------|-------------|
   | `invoice_contoso.pdf` | Invoice | Commercial invoice from Contoso Ltd with line items, amounts, and payment terms |
   | `receipt_café.jpg` | Receipt | Café receipt with items, tax, and total |
   | `medical_form.pdf` | Medical Form | Patient intake form with personal details and medical history |
   | `insurance_claim.pdf` | Insurance Claim | Auto insurance claim with incident details and cost estimates |
   | `drivers_license.jpg` | Identity Document | Sample driver's license with personal information |

1. Navigate to your **documents** container in the Storage Account.

1. Click **Upload** and upload all 5 sample documents.

1. Verify all 5 documents appear in the container.

<validation step="5a1f3c2d-8e9b-4f6a-b7c1-2d3e4f5a6b7c" />

> **Congratulations!** You've created the Storage Account and uploaded sample documents.
>
> If validation fails, verify:
> - The Storage Account name is `docstore<inject key="DeploymentID" enableCopy="false"/>`
> - The `documents` container exists and contains all 5 files
> - The `processed` container exists

### Part 3: Create Azure AI Document Intelligence Resource

1. In the Azure portal, click **+ Create a resource** and search for **Document Intelligence**.

1. Click **Create** and configure:

   | Setting | Value |
   |---------|-------|
   | **Subscription** | Your Azure subscription |
   | **Resource group** | challenge-rg-<inject key="DeploymentID" enableCopy="false"/> |
   | **Region** | <inject key="Region" /> |
   | **Name** | doc-intel-<inject key="DeploymentID" enableCopy="false"/> |
   | **Pricing tier** | Free F0 (or Standard S0 if F0 is unavailable) |

1. Click **Review + Create**, then **Create**. Wait for deployment to complete.

### Part 4: Test OCR in Document Intelligence Studio

1. Navigate to [Document Intelligence Studio](https://documentintelligence.ai.azure.com/studio).

1. Sign in with your lab credentials: **<inject key="AzureAdUserEmail" />**

1. Under **Document analysis**, select **OCR/Read**.

1. In the top bar, click **Configure** and select:
   - **Subscription:** Your Azure subscription
   - **Resource:** doc-intel-<inject key="DeploymentID" enableCopy="false"/>

1. Click **Browse for files** and upload `invoice_contoso.pdf` from your sample documents.

1. Click **Run analysis** and wait for results.

1. Observe the extracted content:
   - **Text** — The full text extracted from the document, preserving reading order
   - **Words and Lines** — Individual words and lines detected with confidence scores
   - **Pages** — Page-level metadata including dimensions and language

   > **Note:** The OCR/Read model focuses on text extraction — which is exactly what our AI agents need. The agents downstream will handle classification, structured data extraction, and validation. We don't need Layout's table/structure detection because the agents are smart enough to understand the text format.

1. Try analyzing `receipt_café.jpg` and `drivers_license.jpg` as well. Notice how Document Intelligence handles different document formats (PDF vs image) and layouts.

<validation step="6b2c4d5e-9f0a-4b7c-8d1e-3f4a5b6c7d8e" />

> **Congratulations!** Document Intelligence is set up and extracting text from your documents.
>
> If validation fails, verify:
> - The Document Intelligence resource exists in your resource group
> - You can successfully analyze a document in the Studio

### Part 5: Create Microsoft Foundry Resource and Deploy GPT-4.1

1. In the Azure portal, search for **Microsoft Foundry** in the top search bar.

1. In the left menu under **Use with Foundry**, click **Foundry**.

1. Click **+ Create**.

1. On the **Create a Foundry resource** page, fill in the following:

   | Setting | Value |
   |---------|-------|
   | **Subscription** | Your Azure subscription |
   | **Resource group** | challenge-rg-<inject key="DeploymentID" enableCopy="false"/> |
   | **Name** | openai-doc-ai-<inject key="DeploymentID" enableCopy="false"/> |
   | **Region** | <inject key="Region" /> |
   | **Default project name** | Leave as `proj-default` |

   > **Important:** Keep the default project name as **proj-default** — this is used in the application's endpoint URL.

1. Click **Review + create**, then **Create**. Wait for the deployment to complete (this may take 2–3 minutes).

1. Once deployed, navigate to [Azure AI Foundry portal](https://ai.azure.com) and sign in with your lab credentials: **<inject key="AzureAdUserEmail" />**

1. You should see your project listed. Click on it to open the project.

1. In the left menu, navigate to **Models + endpoints**.

1. Click **+ Deploy model** → **Deploy base model**.

1. Search for **GPT-4.1** and select it.

1. Configure the deployment:

   | Setting | Value |
   |---------|-------|
   | **Deployment name** | doc-processor |
   | **Deployment type** | Standard |
   | **Tokens per Minute Rate Limit** | 30K (or maximum available) |

1. Click **Deploy** and wait for the model to be ready.

<validation step="7c3d5e6f-0a1b-4c8d-9e2f-4a5b6c7d8e9f" />

> **Congratulations!** Your Foundry resource, project, and GPT-4.1 model are ready.
>
> If validation fails, verify:
> - The Foundry resource `openai-doc-ai-<inject key="DeploymentID" enableCopy="false"/>` exists in your resource group
> - The default project `proj-default` is created
> - The `doc-processor` model deployment is in **Succeeded** state

### Part 6: Create Azure Cosmos DB Account

1. In the Azure portal, click **+ Create a resource** and search for **Azure Cosmos DB**.

1. Select **Azure Cosmos DB for NoSQL** and click **Create**.

1. Configure:

   | Setting | Value |
   |---------|-------|
   | **Subscription** | Your Azure subscription |
   | **Resource group** | challenge-rg-<inject key="DeploymentID" enableCopy="false"/> |
   | **Account Name** | cosmos-docs-<inject key="DeploymentID" enableCopy="false"/> |
   | **Region** | <inject key="Region" /> |
   | **Capacity mode** | Serverless |

1. Click **Review + Create**, then **Create**. Wait for deployment (this may take 3–5 minutes).

1. Navigate to the Cosmos DB account. In the left menu, click **Data Explorer**.

1. Click **New Database** and enter:
   - **Database id:** `ContentProcessingDB`

1. Click **OK** to create the database.

1. Expand the **ContentProcessingDB** database and click **New Container**:

   | Setting | Value |
   |---------|-------|
   | **Database id** | Use existing: `ContentProcessingDB` |
   | **Container id** | `ProcessedDocuments` |
   | **Partition key** | `/docType` |

1. Click **OK**, then create a second container:

   | Setting | Value |
   |---------|-------|
   | **Database id** | Use existing: `ContentProcessingDB` |
   | **Container id** | `ReviewQueue` |
   | **Partition key** | `/documentId` |

1. Verify you have:
   - Database: `ContentProcessingDB`
   - Container: `ProcessedDocuments` (partition key: `/docType`)
   - Container: `ReviewQueue` (partition key: `/documentId`)

<validation step="8d4e6f7a-1b2c-4d9e-0f3a-5b6c7d8e9f0a" />

> **Congratulations!** Your Cosmos DB is configured with dual containers for smart routing.
>
> If validation fails, verify:
> - Cosmos DB account name is `cosmos-docs-<inject key="DeploymentID" enableCopy="false"/>`
> - Both `ProcessedDocuments` and `ReviewQueue` containers exist with correct partition keys

## Success Criteria

- [ ] Storage Account `docstore<inject key="DeploymentID" enableCopy="false"/>` exists with `documents` and `processed` containers
- [ ] 5 sample documents are uploaded to the `documents` container
- [ ] Document Intelligence resource `doc-intel-<inject key="DeploymentID" enableCopy="false"/>` is provisioned
- [ ] You successfully analyzed at least one document in Document Intelligence Studio and observed extracted text/tables
- [ ] AI Foundry project `content-processor-<inject key="DeploymentID" enableCopy="false"/>` is created with `doc-processor` GPT-4.1 deployment
- [ ] Cosmos DB account `cosmos-docs-<inject key="DeploymentID" enableCopy="false"/>` has database `ContentProcessingDB` with `ProcessedDocuments` and `ReviewQueue` containers

## Additional Resources

- [Azure Blob Storage Documentation](https://learn.microsoft.com/en-us/azure/storage/blobs/)
- [Azure AI Document Intelligence Overview](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/)

Click **Next** to continue to **Challenge 2: Build the Document Classification Agent**.
