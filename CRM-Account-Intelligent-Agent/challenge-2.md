# Challenge 02: Deploy Foundry Models for Account Intelligence

## Introduction

To generate contextual account briefings and actionable sales insights, the B2B Account Intelligence Assistant relies on Generative AI models for language understanding and semantic retrieval.

In this challenge, you will deploy the required models using **Microsoft Foundry**, enabling the AI agent to summarize account data and support Retrieval-Augmented Generation (RAG).

## Challenge Objectives

- Create a Microsoft Foundry resource  
- Deploy an LLM for sales and account analysis  
- Deploy an embedding model for semantic search  

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Microsoft Foundry** and select **Create a Foundry resource**.

1. Create the Foundry resource with the following details:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - Name: **foundry-crm-<inject key="DeploymentID" enableCopy="false"/>**
   - Region: **<inject key="Region"></inject>**
   - Default project name: **crm-proj-<inject key="DeploymentID" enableCopy="false"/>**

1. Click **Review + Create**, then select **Create**.

1. After deployment, open the Foundry resource and navigate to **crm-proj-<inject key="DeploymentID" enableCopy="false"/>**.

1. Click **Go to Foundry portal** from the Overview page.

1. In **Models + Endpoints**, deploy the following base models:

   - **gpt-4.1-mini**
     - Tier: **Global Standard**
     - Capacity: **20K TPM**

   - **text-embedding-ada-002**
     - Tier: **Global Standard**
     - Capacity: **30K TPM**

1. Once done, from the portal, please copy the **OpenAI Endpoint** and **API Key**. Note this in a notepad, as you will be using this in further challenges.

<validation step="691592e7-201b-458e-b8a2-b494eb7bf30f" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Foundry resource deployed successfully  
- LLM available for account intelligence generation  
- Embedding model available for semantic search and RAG  

## Additional Resources

- [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Retrieval-Augmented Generation Overview](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 03**.
