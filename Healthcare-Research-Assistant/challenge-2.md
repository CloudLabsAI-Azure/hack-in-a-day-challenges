# Challenge 02: Deploy Foundry Models for Clinical Research Analysis

## Introduction

To analyze complex medical literature and generate evidence-based insights, the Clinical Research Intelligence Assistant requires access to Large Language Models (LLMs) and embedding models.

In this challenge, you will deploy the required models using **Microsoft Foundry**, enabling natural-language understanding, semantic search, and Retrieval-Augmented Generation (RAG) for healthcare research scenarios.

## Challenge Objectives

- Create a Microsoft Foundry resource  
- Deploy an LLM for clinical research analysis  
- Deploy an embedding model for semantic search and retrieval  

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Microsoft Foundry** and select **Create a Foundry resource**.

1. Create the Foundry resource with the following details:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID" enableCopy="false"/>**
   - Name: **health-foundry-<inject key="DeploymentID" enableCopy="false"/>**
   - Region: **<inject key="Region"></inject>**
   - Default project name: **health-proj-<inject key="DeploymentID" enableCopy="false"/>**

   > Click **Next** through the configuration pages, then select **Review + Create** → **Create**.

1. Once deployment completes, open the Foundry resource.

1. Navigate to the project **health-proj-<inject key="DeploymentID"></inject>**.

1. From the Foundry Overview page, click **Go to Foundry portal**.

1. In the **Models + Endpoints** section, select **Deploy base model** and deploy the following models:

   - **gpt-4.1-mini**
     - Deployment type: **Global Standard**
     - Capacity: **20K TPM**

   - **text-embedding-ada-002**
     - Deployment type: **Global Standard**
     - Capacity: **30K TPM**

1. Once done, from the portal, please copy the **OpenAI Endpoint** and **API Key**. Note this in a notepad, as you will be using this in further challenges.

   > If a model does not appear in search, select **Go to model catalog** and deploy it from there.

## Success Criteria

- Microsoft Foundry resource created successfully  
- `gpt-4.1-mini` deployed and available  
- `text-embedding-ada-002` deployed for semantic search  
- Models ready for clinical research analysis  

## Additional Resources

- [Azure AI Foundry Overview](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Models](https://learn.microsoft.com/azure/ai-services/openai/concepts/models)

Now, click **Next** to continue to **Challenge 03**.
