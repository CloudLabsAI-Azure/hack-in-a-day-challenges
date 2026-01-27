# Challenge 04: Analyze Clinical Research Data Using Foundry Playground

## Introduction

With clinical research documents indexed in Azure AI Search and Foundry models deployed, the next step is to validate Retrieval-Augmented Generation (RAG).

In this challenge, you will connect Azure AI Search as a data source in **Microsoft Foundry Playground** and test natural-language prompts. The AI model will retrieve relevant medical literature and generate grounded, citation-aware responses.

## Challenge Objectives

- Connect Azure AI Search to Foundry Playground  
- Enable RAG for clinical research queries  
- Validate grounded responses from indexed medical data  

## Steps to Complete

1. Open **Microsoft Foundry** from the Azure Portal.

1. Navigate to the project:
   **health-proj-<inject key="DeploymentID" enableCopy="false"/>**

1. Select **Playground** and click on **Open Chat Playground**.

1. In the Playground, select **Add a data source** under **Add your data**.

1. Configure the data source:

   - Data source type: **Azure AI Search**
   - Subscription: **default Subscription**
   - Azure AI Search service: **health-search-<inject key="DeploymentID" enableCopy="false"/>**
   - Azure AI Search index: Select the default index created in Challenge 03
   - Click **Next**

1. In **Data management**:
   - Search type: **Semantic**
   - Semantic configuration: **Use existing**
   - Click **Next**

1. In **Data connection**:
   - Authentication type: **API key**
   - Click **Next**

1. Review settings and click **Save and close**.

1. In the Playground prompt window, test the following queries:

   - `What are the latest treatments for glioblastoma in patients over 60?`

   - `Compare chemotherapy and immunotherapy outcomes for glioblastoma`

1. Observe how the model retrieves information from indexed documents and generates grounded responses.

<validation step="7f21dea7-cad6-427f-a596-1cdc1511e2cd" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Azure AI Search connected successfully to Foundry Playground  
- Model responses reference indexed clinical data  
- Answers are coherent, relevant, and grounded  

## Additional Resources

- [Prompt Engineering Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [RAG with Azure AI Search](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 05**.
