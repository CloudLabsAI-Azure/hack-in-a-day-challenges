# Challenge 04: Analyze Data Using GenAI Prompts

## Introduction

With data available and LLM deployed, Contoso wants to generate natural-language insights from machine logs.  
In this challenge, you’ll use Microsoft Foundry (LLM capabilities) to summarize and interpret manufacturing data.

## Challenge Objectives

- Load the CSV data from Azure Blob Storage.  
- Send structured chunks of data to the Foundry LLM via prompt.  
- Generate natural-language summaries and recommendations.

## Steps to Complete

1. Open **Microsoft Foundry Studio** and open your project **mfg-proj-<inject key="DeploymentID"></inject>**.

1. Choose the deployed LLM model **gpt-4.1-mini** within the Foundry project.

1. Click **Open in playground**. 

1. Select **Add a data source** under the **Add your data** section.

1. In the Select or add data source pane configure:

   - Select data source: **Azure AI Search**.
   - Subscription: **Select the defualt Subscription**.  
   - Azure AI Search service: **mfg-search-<inject key="DeploymentID"></inject>**.  
   - Azure AI Search index: Select the default **index** that was created in the previous challenge.
   - Click **Next**.

1. In the Data management pane configure:

   - Search type: **Azure AI Search**.
   - Semantic search configuration: **Select the exisitng**.  
   - Click **Next**.

1. In the Data connection pane configure:

   - Azure resource authentication type: **API key**. 
   - Click **Next**.

1. Review and click **Save and close**.

1. In the Playground test with prompts such as:  

   ```
   Temprature of MACHINE_001
   ```

   ```
   All Running MACHINE
   ```

1. Observe the output summary.   

## Success Criteria

- Model produces coherent, context-aware summaries of data.  
- Insights include metrics and recommendations based on patterns.

## Additional Resources

- [Prompt Engineering Guidance](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- Microsoft Foundry documentation: https://learn.microsoft.com/azure/ai-foundry/

Now, click **Next** to continue to **Challenge 05**.