# Challenge 04: Analyze Data Using GenAI Prompts

## Introduction
With data available and LLM deployed, Contoso wants to generate natural-language insights from machine logs.  
In this challenge, you’ll use Microsoft Foundry (LLM capabilities) to summarize and interpret manufacturing data.

## Challenge Objectives
- Load the CSV data from Azure Blob Storage.  
-- Send structured chunks of data to the Foundry LLM via prompt.  
- Generate natural-language summaries and recommendations.

## Steps to Complete
1. Open **Microsoft Foundry Studio** (or the Foundry project UI) and open your project `mfg-proj-<inject key="DeploymentID"></inject>`.

2. Choose the deployed LLM model (for example `gpt-4.1-mini`) within the Foundry project.

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
- Microsoft Foundry documentation: https://learn.microsoft.com/azure/ai-foundry/

Now, click **Next** to continue to **Challenge 04: Build a Summary Report and Dashboard**.