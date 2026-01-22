# Challenge 03: Create Azure AI Search Index for Network Diagnostics Data

## Introduction

To support proactive network monitoring and diagnostics, the AI agent must retrieve relevant telemetry and incident data efficiently.

In this challenge, you will create an **Azure AI Search** service and index synthetic network telemetry and incident reports. This indexed data will power AI-driven diagnostics and recommendations using RAG.

## Challenge Objectives

- Create an Azure AI Search service  
- Index network telemetry and incident data  
- Enable semantic retrieval for diagnostics  

## Steps to Complete

1. In the **Azure Portal**, search for **Azure AI Search** and select **Create**.

1. Create the Azure AI Search service with:

   - Subscription: **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID"></inject>**
   - Service name: **telecom-search-<inject key="DeploymentID"></inject>**
   - Location: **<inject key="Region"></inject>**
   - Pricing tier: **Basic**

1. Click **Review + Create** → **Create**.

1. Open the Azure AI Search resource after deployment.

1. From **Keys and Endpoints**, copy and note:
   - **Search service endpoint** from the overview page.
   - **Query key** from **Keys** under settings pane.
   - **Index Name** from **Indexes** under Search Management pane.

1. Select **Import data (new)**.

1. Select Data Source as **Azure Blob Storage**.

1. When prompted for scenario, select **RAG (Retrieval-Augmented Generation)**.

1. Configure the data source:
   - Storage account: **storage<inject key="DeploymentID"></inject>**
   - Container: **datasets**
   - Parsing mode: **Default**
   - Click **Next**

1. Choose **RAG (Retrieval-Augmented Generation)**.

1. Configure vectorization:
   - Kind: **Azure AI Foundry**
   - Foundry project: **telecom-proj-<inject key="DeploymentID"></inject>**
   - Model deployment: **text-embedding-ada-002**
   - Authentication: **API key**
   - Click **Next**

1. Skip ranking configuration and proceed.

1. Review and click **Create**.

1. Test indexing using **Search Explorer**:

   ```
   network congestion
   ```

## Success Criteria

- Azure AI Search service deployed  
- Network diagnostics documents indexed  
- Semantic queries return telemetry-related insights  

## Additional Resources

- [Azure AI Search Overview](https://learn.microsoft.com/azure/search/)
- [RAG for Operational Intelligence](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 04**.
