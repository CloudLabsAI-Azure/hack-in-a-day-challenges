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

1. Create the Foundry resource with the following details:

   - Subscription: Select the **defualt Subscription**.
   - Resource group: Select **challenge-rg-<inject key="DeploymentID"></inject>**.
   - Name: **openai-mfg-<inject key="DeploymentID"></inject>**.
   - Region: **<inject key="Region"></inject>**.
   - Default Project Name: **mfg-proj-<inject key="DeploymentID"></inject>**.

   > **Note:** Keep clicking **Next** until you reach **Review + Create**, then select **Create**.

1. After deployment, open the Microsoft Foundry resource and navigate to the project **mfg-proj-<inject key="DeploymentID"></inject>**.

1. From the Foundry resource **Overview** page click **Go to Foundry portal** 

1. Deploy the following models in the **Models + Endpoints** section by selecting **Deploy base model**:

   - **gpt-4.1-mini**: **Global Standard** tierx` with **20,000 TPM** capacity.
   - **text-embedding-ada-002**: *Global Standard* with **30,000 TPM** capacity (Requried for semantic search).

   > **Hint:** If a model doesn’t appear when you search for it, click **Go to model catalog** in the model selection screen and deploy it from there.

<validation step="0e3316a0-8749-494b-b375-e696faea24f2" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Microsoft Foundry resource deployed successfully.  
- `gpt-4.1-mini` and `text-embedding-ada-002` model available for prompt testing.  
- Endpoint and API key ready for subsequent use.

## Additional Resources

- [Azure OpenAI Service Overview](https://learn.microsoft.com/azure/ai-services/openai/overview)
- [Deploy a model in Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource)

Now, click **Next** to continue to **Challenge 03: Analyze Data Using GenAI Prompts**.
