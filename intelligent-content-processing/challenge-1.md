# Challenge 01: Document Ingestion & OCR Setup

## Introduction

Contoso Finance, a leading enterprise, processes hundreds of invoices daily. Manual data entry from PDFs and scans causes frequent errors and delays.  
To solve this, Contoso plans to implement an **AI-based invoice automation solution** using **Azure AI Document Intelligence**.  
This service extracts structured data such as invoice numbers, totals, vendor names, and dates, saving hours of repetitive manual effort.

In this challenge, you’ll create the **Azure AI Document Intelligence** resource, the foundation for the rest of your Intelligent Document Processing solution.

## Accessing the Datasets

Please download and extract the datasets required for this challenge here - [Datasets](https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/content-processing-files.zip)

   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/content-processing-files.zip
   ```

## Challenge Objectives

- Create an **Azure Blob Storage account** for document ingestion.

- Create a **Blob container** to upload files.

- Upload sample documents (invoice.pdf, handwritten_note.jpg) to Blob Storage.

- Create an **Azure Document Intelligence** resource.

- Use **Document Intelligence Studio** to analyze uploaded documents.

- Perform **OCR extraction** on PDF and image documents.

- Validate extracted **text, tables, and key-value pairs** from OCR.

- Capture and review OCR output for downstream processing.

## Steps to Complete

   1. In the **Azure Portal**, search for **Storage accounts** and click **Create**.

   1. Under **Basics**, provide:

      * **Subscription:** Use the available subscription
      * **Resource Group:** Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      * **Storage account name:** **docstore<inject key="DeploymentID" enableCopy="false"/>**
      * **Region**: **<inject key="Region"></inject>**
      * **Performance:** Standard
      * **Redundancy:** Locally-redundant storage (LRS)

   1. Click **Review + Create** → **Create**.

   1. After deployment succeeds, open the **Storage account**.

### Create a Blob Container

   1. In the storage account, go to **Containers**.

   1. Click **+ Add container** and provide:

      * **Name:** `documents`
      * **Public access level:** Private (no anonymous access)

   1. Click **Create**.

### Upload Sample Documents

   1. Open the `documents` container.

   1. Click **Upload** and upload:

      * `invoice.pdf`
      * `handwritten_note.jpg`

   1. Click **Upload** and confirm the files appear in the list.

### Create Azure Document Intelligence

   1. In the **Azure Portal**, search for **Document Intelligence** and click **Create**.

   1. Under **Basics**, provide:

      * **Subscription:** Use the available subscription
      * **Resource Group:** Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      * **Region:** Same region as storage
      * **Name:** **doc-intel-<inject key="DeploymentID" enableCopy="false"/>**
      * **Pricing Tier:** Free (F0) *(or Standard if F0 is unavailable)*

   1. Click **Review + Create** → **Create**.

   1. After deployment succeeds, open the **Document Intelligence** resource.

### Run OCR Using Document Intelligence Studio

   1. In the Document Intelligence resource, click **Go to Document Intelligence Studio**.

   1. Select **Document analysis**.

   1. On the **Welcome to Document Intelligence Studio**, select the following:

      * **Subscription:** Use the available subscription
      * **Resource Group:** Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      * **Document Intelligence:** **doc-intel-<inject key="DeploymentID" enableCopy="false"/>**
      * Select **Create** → **Finish**

   1. Choose the **Layout** (or **General Document**) model.

   1. Click **Upload file**, select `invoice.pdf`, and click **Analyze**.

   1. Repeat the same steps for `handwritten_note.jpg`.

### Validate OCR Output

   1. Confirm that:

   * Text is extracted from both documents
   * Tables are detected in the invoice
   * Handwritten text is partially recognized

<validation step="67fcae6d-e490-4215-8b86-e1cdc1722cc2" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Success Criteria

You have successfully completed the Challenge 1:

* Documents are uploaded to Blob Storage
* OCR runs successfully on PDF and image files
* Extracted text is visible in Document Intelligence Studio 

### Additional Resources

- [Azure AI Document Intelligence Overview](https://learn.microsoft.com/azure/ai-services/document-intelligence/overview)  
- [Quickstart: Create Document Intelligence Resource](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/create-resource)

Now, click **Next** to continue to **Challenge 02**.
