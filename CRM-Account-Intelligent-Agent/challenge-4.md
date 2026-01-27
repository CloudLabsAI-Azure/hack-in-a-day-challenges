# Challenge 04: Generate Account Insights Using Foundry Playground

## Introduction

With account intelligence documents indexed and models deployed, you will now validate AI-driven account insights using Foundry Playground.

In this challenge, you will connect Azure AI Search to Foundry Playground and test sales-focused prompts. The AI agent will retrieve account intelligence documents and generate contextual sales briefings using RAG.

## Challenge Objectives

- Connect Azure AI Search to Foundry Playground  
- Generate contextual B2B account insights  
- Validate RAG-based responses for sales scenarios  

## Steps to Complete

1. Open **Microsoft Foundry** from the Azure Portal.

1. Navigate to the project:
   **crm-proj-<inject key="DeploymentID" enableCopy="false"/>**

1. Select the deployed model:
   **gpt-4.1-mini**

1. Select **Playground** and click on **Open Chat Playground**.

1. Select **Add a data source** under **Add your data**.

1. Configure the data source:

   - Data source type: **Azure AI Search**
   - Subscription: **default Subscription**
   - Azure AI Search service: **crm-search-<inject key="DeploymentID" enableCopy="false"/>**
   - Azure AI Search index: Select the default index
   - Click **Next**

1. In **Data management**:
   - Search type: **Semantic**
   - Semantic configuration: **Use existing**
   - Click **Next**

1. In **Data connection**:
   - Authentication type: **API key**
   - Click **Next**

1. Review and click **Save and close**.

1. Test the following prompts in Playground:

   - `Summarize recent changes for ConnectWave account`

   - `What risks and opportunities exist for VitalHealth customer?`

1. Observe how the model produces concise, actionable sales insights.

<validation step="999ba887-39bc-4f78-be46-310a1abfa255" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Azure AI Search connected successfully  
- AI responses are grounded in indexed account data  
- Insights are relevant and actionable for sales teams  

## Additional Resources

- [Azure AI Foundry Playground](https://learn.microsoft.com/azure/ai-foundry/)
- [RAG for Business Intelligence](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 05**.
