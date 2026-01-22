# Challenge 03: Create Azure AI Search Index for Account Intelligence Data

## Introduction

To deliver meaningful account briefings, the B2B Account Intelligence Assistant requires fast, semantic access to account intelligence documents.

In this challenge, you will create an **Azure AI Search** service and index synthetic CRM and market intelligence documents. This index will serve as the retrieval layer for the AI-powered sales assistant.

## Challenge Objectives

- Create an Azure AI Search service  
- Index account intelligence documents from Blob Storage  
- Enable vector-based semantic search for RAG  

## Steps to Complete

1. In the **Azure Portal**, search for **Azure AI Search** and select **Create**.

1. Configure the Azure AI Search service:

   - Subscription: **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - Service name: **crm-search-<inject key="DeploymentID" enableCopy="false"/>**
   - Location: **<inject key="Region"></inject>**
   - Pricing tier: **Basic**

1. Click **Review + Create**, then **Create**.

1. Open the Azure AI Search resource once deployment completes.

1. From **Keys and Endpoints**, copy and note:
   - **Search service endpoint** from the overview page.
   - **Query key** from **Keys** under settings pane.
   - **Index Name** from **Indexes** under Search Management pane.

1. Select **Import data (new)**.

1. Select Data Source as **Azure Blob Storage**.

1. When prompted for scenario, select **RAG (Retrieval-Augmented Generation)**.

1. Configure the data source:
   - Data source: **Azure Blob Storage**
   - Storage account: **storage<inject key="DeploymentID" enableCopy="false"/>**
   - Container: **datasets**
   - Parsing mode: **Default**
   - Click **Next**

1. Configure vectorization:
   - Column to vectorize: **content**
   - Kind: **Azure AI Foundry**
   - Foundry project: **crm-proj-<inject key="DeploymentID" enableCopy="false"/>**
   - Model deployment: **text-embedding-ada-002**
   - Authentication type: **API key**
   - Click **Next**

1. Skip ranking options and proceed.

1. Review settings and click **Create**.

1. Validate indexing using **Search Explorer**:

   ```
   account risk
   ```

## Success Criteria

- Azure AI Search service created  
- Account intelligence documents indexed  
- Semantic search returns relevant account insights  

## Additional Resources

- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Semantic Search Concepts](https://learn.microsoft.com/azure/search/semantic-search-overview)

Now, click **Next** to continue to **Challenge 04**.
