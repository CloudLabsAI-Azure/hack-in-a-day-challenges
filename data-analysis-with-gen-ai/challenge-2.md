# Challenge 02: Deploy Azure OpenAI Service

## Introduction
Contoso wants to use a Large Language Model (LLM) to summarize machine logs and generate human-readable insights.  
Azure OpenAI Service provides API access to models like gpt-4.1-mini, which can analyze data and produce natural language reports.

## Challenge Objectives
- Create an **Azure OpenAI** resource in your subscription.  
- Deploy the **gpt-4.1-mini** model with 20 K TPM capacity.  
- Record the endpoint and API key for later use.

## Steps to Complete
1. In the Azure Portal search for **Microsoft Foundry** and choose **Create a Foundry resource**.

2. Fill in the basics for the Foundry resource:
   - **Subscription:** Your active subscription.
   - **Resource Group:** ODL-demolab-<inject key="DeploymentID"></inject>.
   - **Region:** <inject key="Region"></inject>.
   - **Name:** openai-mfg-<inject key="DeploymentID"></inject>.
   - **Default Project Name:** `mfg-proj-<inject key="DeploymentID"></inject>`.
   
3. Click **Review + Create** → **Create** and wait for deployment to complete.

4. After deployment, open the Microsoft Foundry resource and navigate to the project `mfg-proj-<inject key="DeploymentID"></inject>`.

5. Deploy or enable the following model capabilities in the Foundry project (or equivalent model deployment area):
   - **gpt-4.1-mini** — *Global Standard* tier with **20,000 TPM** capacity.
   - **text-embedding-ada-002** — embedding model with **30,000 TPM** capacity (Requried for semantic search).

6. Note any endpoints, project identifiers, and keys provided by Foundry for later use.

## Success Criteria
- Azure OpenAI resource deployed successfully.  
- `gpt-4.1-mini` and `text-embedding-ada-002` model available for prompt testing.  
- Endpoint and API key ready for subsequent use.

## Additional Resources
- [Azure OpenAI Service Overview](https://learn.microsoft.com/azure/ai-services/openai/overview)
- [Deploy a model in Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource)

Now, click **Next** to continue to **Challenge 03: Analyze Data Using GenAI Prompts**.
