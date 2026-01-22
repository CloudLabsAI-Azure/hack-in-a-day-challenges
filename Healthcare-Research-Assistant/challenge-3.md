# Challenge 03: Create Azure AI Search Index for Clinical Research Data

## Introduction

To enable evidence-based answers and citations, the Clinical Research Intelligence Assistant requires a searchable knowledge layer that can retrieve relevant medical literature on demand.

In this challenge, you will create an **Azure AI Search** service and index the uploaded clinical research documents. This indexed data will later be used by the Foundry AI agent to generate grounded, citation-backed responses using Retrieval-Augmented Generation (RAG).

## Challenge Objectives

- Create an Azure AI Search service  
- Connect Azure Blob Storage as a data source  
- Vectorize clinical research documents using embeddings  
- Validate indexed medical data  

## Steps to Complete

1. In the **Azure Portal**, search for **Azure AI Search** and select **Create**.

1. Create the Azure AI Search service with the following configuration:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - Service name: **health-search-<inject key="DeploymentID" enableCopy="false"/>**
   - Location: **<inject key="Region"></inject>**
   - Pricing tier: **Basic**
   
1. Click **Review + Create**, then select **Create**.

1. Once deployment completes, open the Azure AI Search resource.

1. From **Keys and Endpoints**, copy and note:
   - **Search service endpoint** from the overview page.
   - **Query key** from **Keys** under settings pane.
   - **Index Name** from **Indexes** under Search Management pane.

1. From the top menu, select **Import data (new)**.

1. Select Data Source as **Azure Blob Storage**.

1. When prompted for scenario, select **RAG (Retrieval-Augmented Generation)**.

1. Configure the data source:
   - Data source: **Azure Blob Storage**
   - Subscription: **default Subscription**
   - Storage account: **storage<inject key="DeploymentID" enableCopy="false"/>**
   - Blob container: **datasets**
   - Parsing mode: **Default**
   - Click **Next**

1. Configure vectorization:
   - Column to vectorize: **content**
   - Kind: **Azure AI Foundry**
   - Foundry project: **health-proj-<inject key="DeploymentID" enableCopy="false"/>**
   - Model deployment: **text-embedding-ada-002**
   - Authentication: **API key**
   - Acknowledge the checkbox and click **Next**

1. Skip advanced ranking and click **Next**.

1. Review the configuration and click **Create**.

1. After indexing completes, open **Search Explorer** and run a test query:

   ```
   glioblastoma
   ```

## Success Criteria

- Azure AI Search service created successfully  
- Clinical research documents indexed  
- Semantic queries return relevant medical literature  

## Additional Resources

- [Azure AI Search Overview](https://learn.microsoft.com/azure/search/search-what-is-azure-search)
- [RAG with Azure AI Search](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 04**.
