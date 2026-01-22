# Challenge 01: Upload and Review B2B Account Intelligence Data

## Introduction

Sales teams depend on account intelligence from multiple sources such as CRM systems, news updates, financial reports, and sentiment analysis.  
Before enabling AI-powered insights, this information must be centralized and stored securely.

In this challenge, you will upload synthetic B2B account intelligence documents into Azure Blob Storage, forming the data foundation for the Account Intelligence Assistant.

## Challenge Objectives

- Create an Azure Storage Account for account intelligence data  
- Upload synthetic CRM and market intelligence documents  
- Review dataset structure to ensure readiness for AI search and retrieval

## Accessing the Datasets

Please download and extract the synthetic datasets and code files required for this challenge by using this below labfiles link in your LabVM browser tab:

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/crm-dataset.zip
```

> Once the file is downloaded, please extract it in any desired path in the LabVM. You will be able to see `code-files` and `datasets` folders.

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Storage accounts** and select **Create**.

1. Create a **Storage Account** using the following details:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - Storage account name: **storage<inject key="DeploymentID" enableCopy="false"/>**
   - Region: **<inject key="Region"></inject>**
   - Performance: **Standard**
   - Redundancy: **Locally-redundant storage (LRS)**

1. Click **Review + Create**, then select **Create**.

1. After deployment, open the Storage Account.

1. Navigate to **Containers** under **Data storage** and select **+ Container**.

1. Create a container with:

   - Name: **datasets**
   - Public access level: **Private (no anonymous access)**

1. In the extracted labfiles folder, which you have performed earlier in this challenge, you will find a datasets folder, inside which you will be able to find the documents.

1. Upload the synthetic account intelligence documents (company briefs, CRM summaries, news reports) into the **datasets** container.

1. Review the uploaded documents to understand the type of information available for AI-driven sales insights.

## Success Criteria

- Storage Account created successfully  
- **datasets** container created  
- Account intelligence documents uploaded  
- Dataset prepared for Azure AI Search indexing  

## Additional Resources

- [Quickstart: Upload data to Azure Blob Storage](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)
- [Designing AI-ready Business Data](https://learn.microsoft.com/azure/architecture/ai-ml/)

Now, click **Next** to continue to **Challenge 02**.
