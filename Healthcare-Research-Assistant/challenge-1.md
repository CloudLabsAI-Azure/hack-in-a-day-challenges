# Challenge 01: Upload and Review Clinical Research Datasets

## Introduction

Clinical researchers rely on vast amounts of unstructured medical literature and patient case studies to evaluate treatment effectiveness and design trials.  
Before enabling Generative AI–powered analysis, this data must first be securely stored and reviewed.

In this challenge, you will upload synthetic clinical research documents into Azure Blob Storage, forming the foundational data layer for the Clinical Research Intelligence Assistant.

## Challenge Objectives

- Create an Azure Storage Account for healthcare research data  
- Upload synthetic medical literature and case study documents  
- Review the dataset structure to ensure it is ready for AI indexing

## Accessing the Datasets

Please download and extract the synthetic datasets and code files required for this challenge by using this below labfiles link in your LabVM browser tab:

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/healthcare-labfiles.zip
```

> Once the file is downloaded, please extract it in any desired path in the LabVM. You will be able to see `code-files` and `datasets` folders.

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Storage accounts** and select **Create**.

1. Create a **Storage Account** with the following configuration:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - Storage account name: **storage<inject key="DeploymentID" enableCopy="false"/>**
   - Region: **<inject key="Region"></inject>**
   - Performance: **Standard**
   - Redundancy: **Locally-redundant storage (LRS)**

1. Click **Review + Create**, then select **Create**.

1. Once deployment completes, open the Storage Account.

1. Under **Data storage**, select **Containers** and click **+ Add Container**.

1. Create a container with the following details:

   - Name: **datasets**
   - Public access level: **Private (no anonymous access)**\

1. In the extracted labfiles folder, which you have performed earlier in this challenge, you will find a datasets folder, inside which you will be able to find the documents.

1. Upload the synthetic healthcare research documents (PDF or text files) into the **datasets** container.

   > These documents simulate medical literature, clinical trials, and patient case studies.

1. Review a few uploaded files to understand their structure and content.

<validation step="ea21cb22-643d-4ee8-92d7-8c64dc5c7f48" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Storage Account created successfully  
- **datasets** container created  
- Clinical research documents uploaded and accessible  
- Dataset ready for indexing in Azure AI Search  

## Additional Resources

- [Quickstart: Upload data to Azure Blob Storage](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)
- [Azure Blob Storage Overview](https://learn.microsoft.com/azure/storage/blobs/)

Now, click **Next** to continue to **Challenge 02**.
