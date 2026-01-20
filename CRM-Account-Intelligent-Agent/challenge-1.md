# Challenge 01: Upload and Review B2B Account Intelligence Data

## Introduction

Sales teams depend on account intelligence from multiple sources such as CRM systems, news updates, financial reports, and sentiment analysis.  
Before enabling AI-powered insights, this information must be centralized and stored securely.

In this challenge, you will upload synthetic B2B account intelligence documents into Azure Blob Storage, forming the data foundation for the Account Intelligence Assistant.

## Challenge Objectives

- Create an Azure Storage Account for account intelligence data  
- Upload synthetic CRM and market intelligence documents  
- Review dataset structure to ensure readiness for AI search and retrieval  

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Storage accounts** and select **Create**.

1. Create a **Storage Account** using the following details:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID"></inject>**
   - Storage account name: **storage<inject key="DeploymentID"></inject>**
   - Region: **<inject key="Region"></inject>**
   - Performance: **Standard**
   - Redundancy: **Locally-redundant storage (LRS)**

1. Click **Review + Create**, then select **Create**.

1. After deployment, open the Storage Account.

1. Navigate to **Containers** under **Data storage** and select **+ Container**.

1. Create a container with:

   - Name: **datasets**
   - Public access level: **Private (no anonymous access)**

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
