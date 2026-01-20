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
   **health-proj-<inject key="DeploymentID"></inject>**

1. Select the deployed model:
   **gpt-4.1-mini**

1. Click **Open in Playground**.

1. In the Playground, select **Add a data source** under **Add your data**.

1. Configure the data source:

   - Data source type: **Azure AI Search**
   - Subscription: **default Subscription**
   - Azure AI Search service: **health-search-<inject key="DeploymentID"></inject>**
   - Azure AI Search index: Select the default index created in Challenge 03
   - Click **Next**

1. In **Data management**:
   - Search type: **Azure AI Search**
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

## Success Criteria

- Azure AI Search connected successfully to Foundry Playground  
- Model responses reference indexed clinical data  
- Answers are coherent, relevant, and grounded  

## Additional Resources

- [Prompt Engineering Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [RAG with Azure AI Search](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 05**.
