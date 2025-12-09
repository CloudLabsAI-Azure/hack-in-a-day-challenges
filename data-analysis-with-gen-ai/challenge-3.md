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

1. Under **Basics**, fill in the following details:
   - **Subscription:** Select your active subscription.  
  - **Resource Group:** Use challenge-rg-<inject key="DeploymentID"></inject>.  
   - **Service Name:** mfg-search-<inject key="DeploymentID"></inject>.
   - **Region:** <inject key="Region"></inject>. 
   - **Pricing Tier:** Choose *Basic (B)* or *Free (F)*. 

1. Click **Review + Create** → **Create**.  

1. Once deployment completes, open your **Azure AI Search** resource and note:
   - **Endpoint URL**  
   - **Admin Key**

1. In the left pane, select **Import data (new)**.  

1. Choose **Azure Blob Storage** as the Data Source.  

1. When asked **What scenario are you targeting?**, choose **RAG** (Retrieval-Augmented Generation).  

1. Configure your Azure Blob Storage connection:
  - Select **Subscription** and the **Storage account** where you uploaded `datasets`.
  - Choose the **Blob container** that contains the file.
  - Set **Parsing mode** to **Delimited Text** and enable **First line contains header**.

1. When prompted to **Vectorize your text**, configure vectorization for the dataset:
  - **Column to vectorize:** `machine_id` (or `MachineID` depending on the detected field name).
  - **Kind:** **Azure AI Foundry (preview)**.
  - Select **Subscription** and choose your **Azure AI Foundry/Hub project**,**mfg-proj-<inject key="DeploymentID"></inject>**).
  - **Model deployment:** `text-embedding-ada-002`.
  - **Authentication type:** `API key` and provide the Foundry API key when prompted.
  - Check the acknowledgement box to accept preview terms, then click **Next**.

1. Proceed through the remaining steps, review settings, and click **Create** to build the index and vector store.

  - On the **Review and create** page, Azure will show a summary of the resources and object names that will be created. By default there will be an **Objects name prefix** or similar generated name. Review this prefix (it is used to name the index/vector objects) and click **Create**.

1. Once the index builds successfully, test it:  
    - In the **Search Explorer**, enter a query to Get all RUNNING records for MACHINE_001:  
    
      ```
      search=machine_id:"MACHINE_001"&$filter=status eq 'RUNNING'
      ```  
    - Observe returned data (Json).

<validation step="c0d4027b-c42a-4776-861a-3368fdb6f29c" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Azure AI Search resource created successfully.  
- Manufacturing dataset indexed and searchable.  
- Queries return relevant data from your uploaded dataset.

## Additional Resources

- [Azure AI Search Overview](https://learn.microsoft.com/azure/search/search-what-is-azure-search)  
- [Import Data into Azure AI Search](https://learn.microsoft.com/azure/search/search-import-data-portal)  
- [Use Search Explorer](https://learn.microsoft.com/azure/search/search-explorer)

Now, click **Next** (bottom right corner) to continue to **Challenge 04: Analyze Data Using GenAI Prompts**.
