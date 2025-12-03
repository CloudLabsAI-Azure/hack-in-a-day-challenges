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
   - **Resource Group:** Use ODL-demolab-<inject key="DeploymentID"></inject>.  
   - **Service Name:** mfg-search-<inject key="DeploymentID"></inject>.
   - **Region:** <inject key="Region"></inject>. 
   - **Pricing Tier:** Choose *Basic (B)* or *Free (F)*. 

3. Click **Review + Create** → **Create**.  

4. Once deployment completes, open your **Azure AI Search** resource and note:
   - **Endpoint URL**  
   - **Admin Key**

5. In the left pane, select **Import data**.  

6. For **Data Source**, choose **Azure Blob Storage**.  

7. Select the same Storage Account where you uploaded your manufacturing dataset (`machine_sensor_data.csv`).  

8. Name your data source: mfg-datasource-<inject key="DeploymentID"></inject>. 

9. On the **Add cognitive skills (optional)** page, skip and click **Next**.  

10. On **Create an index**, name it mfg-index-<inject key="DeploymentID"></inject>.  
    - Confirm that fields such as `MachineID`, `Temperature`, `Downtime`, and `Timestamp` are detected.  

11. Complete the wizard and click **Submit**.  

12. Once the index builds successfully, test it:  
    - In the **Search Explorer**, enter a query to Get all RUNNING records for MACHINE_001:  
    
      ```
      search=machine_id:"MACHINE_001"&$filter=status eq 'RUNNING'
      ```  
    - Observe returned documents.

## Success Criteria

- Azure AI Search resource created successfully.  
- Manufacturing dataset indexed and searchable.  
- Queries return relevant data from your uploaded dataset.

## Additional Resources

- [Azure AI Search Overview](https://learn.microsoft.com/azure/search/search-what-is-azure-search)  
- [Import Data into Azure AI Search](https://learn.microsoft.com/azure/search/search-import-data-portal)  
- [Use Search Explorer](https://learn.microsoft.com/azure/search/search-explorer)

Now, click **Next** (bottom right corner) to continue to **Challenge 04: Analyze Data Using GenAI Prompts**.
