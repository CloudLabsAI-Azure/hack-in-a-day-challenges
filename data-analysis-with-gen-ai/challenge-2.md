# Challenge 02: Deploy Azure OpenAI Service

## Introduction
Contoso wants to use a Large Language Model (LLM) to summarize machine logs and generate human-readable insights.  
Azure OpenAI Service provides API access to models like gpt-35-turbo, which can analyze data and produce natural language reports.

## Challenge Objectives
- Create an **Azure OpenAI** resource in your subscription.  
- Deploy the **gpt-35-turbo** model with 20 K TPM capacity.  
- Record the endpoint and API key for later use.

## Steps to Complete
1. In the Azure Portal, select **Create a resource** → search for **Azure OpenAI**.  
2. Click **Create**, then fill in the following:  
   - **Subscription:** Your active subscription.  
   - **Resource Group:** ODL-demolab-<inject key="DeploymentID"></inject>.  
   - **Region:** <inject key="Region"></inject>. 
   - **Name:** openai-mfg-<inject key="DeploymentID"></inject>.  
   - **Pricing Tier:** *Standard S0*.  
3. After deployment, navigate to the resource → select **Model Deployments**.  
4. Deploy the following models:  
   - **gpt-4.1-mini** (version Global Standard) with 20 K TPM.  
   - *(Optional)* `text-embedding-ada-002` for semantic search use later.  
5. Note the **Endpoint URL** and **API Key 1**.

## Success Criteria
- Azure OpenAI resource deployed successfully.  
- `gpt-4.1-mini` model available for prompt testing.  
- Endpoint and API key ready for subsequent use.

## Additional Resources
- [Azure OpenAI Service Overview](https://learn.microsoft.com/azure/ai-services/openai/overview)
- [Deploy a model in Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource)

Now, click **Next** to continue to **Challenge 03: Analyze Data Using GenAI Prompts**.
