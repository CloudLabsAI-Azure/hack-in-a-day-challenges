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
   - Resource group: **agentic-ai-<inject key="DeploymentID"></inject>**
   - Name: **foundry-crm-<inject key="DeploymentID"></inject>**
   - Region: **<inject key="Region"></inject>**
   - Default project name: **crm-proj-<inject key="DeploymentID"></inject>**

1. Click **Review + Create**, then select **Create**.

1. After deployment, open the Foundry resource and navigate to **crm-proj-<inject key="DeploymentID"></inject>**.

1. Click **Go to Foundry portal** from the Overview page.

1. In **Models + Endpoints**, deploy the following base models:

   - **gpt-4.1-mini**
     - Tier: **Global Standard**
     - Capacity: **20K TPM**

   - **text-embedding-ada-002**
     - Tier: **Global Standard**
     - Capacity: **30K TPM**

## Success Criteria

- Foundry resource deployed successfully  
- LLM available for account intelligence generation  
- Embedding model available for semantic search and RAG  

## Additional Resources

- [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Retrieval-Augmented Generation Overview](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

Now, click **Next** to continue to **Challenge 03**.
