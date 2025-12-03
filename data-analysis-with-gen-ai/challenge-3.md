# Challenge 03: Create Azure AI Search Resource and Import Manufacturing Data

## Introduction

To enable context-driven insights, Contoso Manufacturing needs a **searchable data layer** that the Large Language Model (LLM) can reference.  
Azure AI Search provides this capability — it allows you to index and query structured or unstructured data, forming the foundation for **Retrieval-Augmented Generation (RAG)** scenarios.

In this challenge, you’ll create an **Azure AI Search** service and import your manufacturing dataset into an index.  
This index will serve as the contextual knowledge base that the model will later use to generate accurate, data-grounded responses.

## Challenge Objectives

- Create an **Azure AI Search** resource.  
- Upload and import your manufacturing dataset into an **index**.  
- Validate that the indexed data can be queried successfully.  

## Steps to Complete

1. In the **Azure Portal**, select **Create a resource** → search for **Azure AI Search** → click **Create**.  

2. Under **Basics**, fill in the following details:
   - **Subscription:** Select your active subscription.  
  - **Resource Group:** Use challenge-rg-<inject key="DeploymentID"></inject>.  
   - **Service Name:** mfg-search-<inject key="DeploymentID"></inject>.
   - **Region:** <inject key="Region"></inject>. 
   - **Pricing Tier:** Choose *Basic (B)* or *Free (F)*. 

3. Click **Review + Create** → **Create**.  

4. Once deployment completes, open your **Azure AI Search** resource and note:
   - **Endpoint URL**  
   - **Admin Key**

5. In the left pane, select **Import data (new)**.  

6. Choose **Azure Blob Storage** as the Data Source.  

7. When asked **What scenario are you targeting?**, choose **RAG** (Retrieval-Augmented Generation).  

8. Configure your Azure Blob Storage connection:
  - Select **Subscription** and the **Storage account** where you uploaded `datasets`.
  - Choose the **Blob container** that contains the file.
  - Set **Parsing mode** to **Delimited Text** and enable **First line contains header**.

9. When prompted to **Vectorize your text**, configure vectorization for the dataset:
  - **Column to vectorize:** `machine_id` (or `MachineID` depending on the detected field name).
  - **Kind:** **Azure AI Foundry (preview)**.
  - Select **Subscription** and choose your **Azure AI Foundry/Hub project** (for example `mfg-proj-<inject key="DeploymentID"></inject>`).
  - **Model deployment:** `text-embedding-ada-002`.
  - **Authentication type:** `API key` and provide the Foundry API key when prompted.
  - Check the acknowledgement box to accept preview terms, then click **Next**.

10. Proceed through the remaining steps, review settings, and click **Create** to build the index and vector store.

  - On the **Review and create** page, Azure will show a summary of the resources and object names that will be created. By default there will be an **Objects name prefix** or similar generated name. Review this prefix (it is used to name the index/vector objects) and click **Create**.

12. Once the index builds successfully, test it:  
    - In the **Search Explorer**, enter a query to Get all RUNNING records for MACHINE_001:  
    
      ```
      search=machine_id:"MACHINE_001"&$filter=status eq 'RUNNING'
      ```  
    - Observe returned data (Json).

## Success Criteria

- Azure AI Search resource created successfully.  
- Manufacturing dataset indexed and searchable.  
- Queries return relevant data from your uploaded dataset.

## Additional Resources

- [Azure AI Search Overview](https://learn.microsoft.com/azure/search/search-what-is-azure-search)  
- [Import Data into Azure AI Search](https://learn.microsoft.com/azure/search/search-import-data-portal)  
- [Use Search Explorer](https://learn.microsoft.com/azure/search/search-explorer)

Now, click **Next** (bottom right corner) to continue to **Challenge 04: Analyze Data Using GenAI Prompts**.
