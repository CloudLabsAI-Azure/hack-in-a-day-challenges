# Challenge 02: Deploy Foundry Models for Network Diagnostics

## Introduction

To interpret telemetry data, explain network issues, and recommend optimizations, the Network Diagnostics Assistant requires Generative AI models capable of reasoning over technical data.

In this challenge, you will deploy the required models using **Microsoft Foundry**, enabling AI-powered diagnostics and Retrieval-Augmented Generation (RAG).

## Challenge Objectives

- Create a Microsoft Foundry resource  
- Deploy an LLM for network diagnostics and explanations  
- Deploy an embedding model for semantic search  

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Microsoft Foundry** and select **Create a Foundry resource**.

1. Create the Foundry resource with the following configuration:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID"></inject>**
   - Name: **foundry-telecom-<inject key="DeploymentID"></inject>**
   - Region: **<inject key="Region"></inject>**
   - Default project name: **telecom-proj-<inject key="DeploymentID"></inject>**

1. Click **Review + Create**, then select **Create**.

1. Once deployed, open the Foundry resource and navigate to **telecom-proj-<inject key="DeploymentID"></inject>**.

1. Click **Go to Foundry portal**.

1. In **Models + Endpoints**, deploy:

   - **gpt-4.1-mini**
     - Deployment type: **Global Standard**
     - Capacity: **20K TPM**

   - **text-embedding-ada-002**
     - Deployment type: **Global Standard**
     - Capacity: **30K TPM**

1. Once done, from the portal, please copy the **OpenAI Endpoint** and **API Key**. Note this in a notepad, as you will be using this in further challenges.

## Success Criteria

- Foundry resource deployed successfully  
- LLM available for network diagnostics reasoning  
- Embedding model available for semantic indexing  

## Additional Resources

- [Azure AI Foundry Overview](https://learn.microsoft.com/azure/ai-foundry/)
- [Generative AI for Telecom](https://learn.microsoft.com/azure/architecture/industries/telecommunications/)

Now, click **Next** to continue to **Challenge 03**.
