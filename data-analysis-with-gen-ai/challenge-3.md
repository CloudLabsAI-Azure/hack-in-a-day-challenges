# Challenge 03: Create Azure AI Search Resource and Import Manufacturing Data

## Introduction

To enable context-driven insights, Contoso Manufacturing needs a **searchable data layer** that the Large Language Model (LLM) can reference.  
Azure AI Search provides this capability, it allows you to index and query structured or unstructured data, forming the foundation for **Retrieval-Augmented Generation (RAG)** scenarios.

In this challenge, you’ll create an **Azure AI Search** service and import your manufacturing dataset into an index.  
This index will serve as the contextual knowledge base that the model will later use to generate accurate, data-grounded responses.

## Challenge Objectives

- Create an **Azure AI Search** resource.  
- Upload and import your manufacturing dataset into an **index**.  
- Validate that the indexed data can be queried successfully.  

## Steps to Complete

1. In the **Azure Portal**, search for **Azure AI Search**.

1. Create an **Azure AI Search** resource with the following details:

   - Subscription: **Select the defualt Subscription**.  
   - Resource Group: **Use challenge-rg-<inject key="DeploymentID"></inject>**.  
   - Service Name: **mfg-search-<inject key="DeploymentID"></inject>**.
   - Location: **<inject key="Region"></inject>**. 
   - Pricing Tier: Choose **Basic**. 

1. Click **Review + Create** → **Create**.  

1. Once deployment completes, open your **Azure AI Search** resource and from Keys and Endpoints pane, copy and note these values safely in notepad:

   - **Endpoint URL**  
   - **Admin Key**

   > **Hint:** The Azure AI Search URL shown on the **Overview** page is your endpoint.

1. In the top pane, select **Import data (new)**.  

1. Choose **Azure Blob Storage** as the Data Source.  

1. When asked **What scenario are you targeting?**, choose **RAG** (Retrieval-Augmented Generation).  

1. Configure your Azure Blob Storage connection with:

   - Subscription: **Select the defualt Subscription**.  
   - Storage account: **mfgdatagenai<inject key="DeploymentID"></inject>**.  
   - Blob container: **manufacturing-logs-<inject key="DeploymentID"></inject>**.
   - Parsing mode: **Delimited text**. 
   - Check the option **First line contains headers**.
   - Click **Next**.

1. Vectorize your text with:

   - Column to vectorize: **machine_id**.  
   - Kind: **Azure AI Foundary (Preview)**.  
   - Subscription: **Select the defualt Subscription**.
   - Azure AI Foundry/Hub project: **openai-mfg-<inject key="DeploymentID"></inject>**. 
   - Model deployment: **text-embedding-ada-002**.
   - Authentication type: **API key**.
   - Check the **Acknowledge** checkbox.
   - Click **Next**.

1. Advanced ranking and relevancy:

   - Click **Next**.

1. On the **Review and create** page, Azure will show a summary of the resources and object names that will be created. By default there will be an **Objects name prefix**. Review this prefix (it is used to name the index/vector objects) and click **Create**.

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

Now, click **Next** to continue to **Challenge 04**.
