# Challenge 04: Analyze Network Diagnostics Using Foundry Playground

## Introduction

With network telemetry and incident data indexed, the next step is to validate AI-powered diagnostics using Foundry Playground.

In this challenge, you will connect Azure AI Search to Foundry Playground and test diagnostics-focused prompts. The AI agent will retrieve telemetry data and generate explanations and recommendations using RAG.

## Challenge Objectives

- Connect Azure AI Search to Foundry Playground  
- Analyze network issues using natural-language prompts  
- Validate explainable AI-driven diagnostics  

## Steps to Complete

1. Open **Microsoft Foundry** from the Azure Portal.

1. Navigate to the project:
   **telecom-proj-<inject key="DeploymentID"></inject>**

1. Select the deployed model:
   **gpt-4.1-mini**

1. Select **Playground** and click on **Open Chat Playground**.

1. Under **Add your data**, select **Add a data source**.

1. Configure the data source:

   - Data source type: **Azure AI Search**
   - Subscription: **default Subscription**
   - Azure AI Search service: **telecom-search-<inject key="DeploymentID"></inject>**
   - Azure AI Search index: Select the default index
   - Click **Next**

1. In **Data management**:
   - Search type: **semantic**
   - Semantic configuration: **Use existing**
   - Click **Next**

1. In **Data connection**:
   - Authentication type: **API key**
   - Click **Next**

1. Review and click **Save and close**.

1. Test the following prompts:

   - `Why is network latency high in this Downtown LA Sports Bar District?`

   - `What remediation actions are recommended for congestion issues?`

1. Observe how the AI explains root causes and suggests optimizations.

## Success Criteria

- Azure AI Search successfully connected  
- AI responses are grounded in telemetry data  
- Diagnostics explanations are clear and actionable  

## Additional Resources

- [Azure AI Foundry Playground](https://learn.microsoft.com/azure/ai-foundry/)
- [AI for Network Operations](https://learn.microsoft.com/azure/architecture/industries/telecommunications/)

Now, click **Next** to continue to **Challenge 05**.
