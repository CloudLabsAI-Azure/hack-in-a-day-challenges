# Challenge 03: Deploy Azure OpenAI Service for Commentary Generation
**Estimated Time:** 30 Minutes

## Introduction
After detecting visual features and anomalies, Contoso wants the AI to automatically describe findings in natural language.  
Azure OpenAI’s gpt-35-turbo model can interpret detection results and generate insightful commentary for operators.

## Challenge Objectives
- Deploy an **Azure OpenAI** resource.  
- Deploy the **gpt-35-turbo** model with 20K TPM.  
- Record endpoint and key for integration.

## Steps to Complete
1. In the Azure Portal, search **Azure OpenAI** → **Create**.  
2. Configure:  
   - **Subscription:** Your assigned one.  
   - **Resource Group:** `MFG-VIS-ASSIST-RG`.  
   - **Region:** *East US* or *West Europe*.  
   - **Name:** `openai-vis-<uniqueID>`.  
   - **Pricing Tier:** *Standard S0*.  
3. After deployment, go to **Model Deployments** → **+ Create new deployment**.  
4. Choose **gpt-35-turbo**, version *0125*, and set 20K TPM.  
5. Copy **Endpoint URL** and **API Key 1**.

## Success Criteria
- Azure OpenAI resource deployed successfully.  
- `gpt-35-turbo` model ready for API calls.

## Additional Resources
- [Azure OpenAI Service Overview](https://learn.microsoft.com/azure/ai-services/openai/overview)
- [Deploy Models in Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource)

Now, click **Next** to continue to **Challenge 04: Generate Visual Inspection Reports**.
