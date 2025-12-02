# Challenge 04: Analyze Data Using GenAI Prompts

## Introduction
With data available and LLM deployed, Contoso wants to generate natural-language insights from machine logs.  
In this challenge, you’ll use Azure OpenAI to summarize and interpret manufacturing data.

## Challenge Objectives
- Load the CSV data from Azure Blob Storage.  
- Send structured chunks of data to Azure OpenAI via prompt.  
- Generate natural-language summaries and recommendations.

## Steps to Complete
1. Open **Azure AI Studio** or **Azure OpenAI Playground**.  

2. Choose the deployed model `gpt-4.1-mini`.  

3. Prepare a prompt such as:  
   - You are an AI data analyst. Summarize key insights from the following manufacturing sensor data:
   - Provide an overview of machine performance, downtime patterns, and recommendations for improvement.

4. Run the prompt and observe the output summary.  

5. Modify the prompt to ask specific questions, for example:  
   - “Which machines showed highest temperature variance?”  
   - “Summarize possible reasons for downtime.”  

## Success Criteria
- Model produces coherent, context-aware summaries of data.  
- Insights include metrics and recommendations based on patterns.

## Additional Resources
- [Prompt Engineering Guidance](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)
- [Azure AI Studio Playground](https://oai.azure.com/portal)

Now, click **Next** to continue to **Challenge 04: Build a Summary Report and Dashboard**.