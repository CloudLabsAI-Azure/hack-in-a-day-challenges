# Challenge 01: Environment Setup & Agent Foundations

## Introduction

In this challenge, you will prepare the **core infrastructure** required to build a multi-agent automation engine. You will provision Azure services, set up the development environment, and define the responsibilities of each AI agent. This foundation will be used throughout the hackathon to enable agent collaboration and orchestration.

## Challenge Objectives

* Create the Azure resources required for a multi-agent system
* Set up Azure OpenAI for agent intelligence
* Create shared state storage using Azure Cosmos DB
* Create Azure Container Registry (ACR) for agent containers
* Initialize a Semantic Kernel project
* Define agent roles and responsibilities

## Steps to Complete

### Step 1: Create a Resource Group

1. In the **Azure Portal**, search for **Resource groups**.
2. Click **Create**.
3. Provide:

   * **Subscription:** Use the available subscription
   * **Resource group name:** `agent-hack-rg-<yourname>`
   * **Region:** Choose a region that supports Azure OpenAI
4. Click **Review + Create** → **Create**.

### Step 2: Create Azure OpenAI Resource

1. In the **Azure Portal**, search for **Azure OpenAI** and click **Create**.
2. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** `agent-hack-rg-<yourname>`
   * **Region:** Supported Azure OpenAI region
   * **Name:** `agent-openai-<unique>`
   * **Pricing Tier:** Standard
3. Click **Review + Create** → **Create**.
4. After deployment succeeds, open the **Azure OpenAI** resource.

### Step 3: Deploy the Model

1. In the Azure OpenAI resource, click **Go to Azure OpenAI Studio**.
2. Navigate to **Deployments** → **Create deployment**.
3. Provide:

   * **Model:** `gpt-4o-mini`
   * **Deployment name:** `agent-gpt-4o-mini`
   * **Version:** Latest
4. Click **Create** and wait for deployment.

### Step 4: Create Azure Cosmos DB (Shared Agent Memory)

1. In the **Azure Portal**, search for **Azure Cosmos DB** and click **Create**.
2. Select **Azure Cosmos DB for NoSQL**.
3. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** `agent-hack-rg-<yourname>`
   * **Account Name:** `agent-cosmos-<unique>`
   * **Location:** Same region as other resources
   * **Capacity mode:** Provisioned throughput
4. Click **Review + Create** → **Create**.

### Step 5: Create Database and Container

1. Open the Cosmos DB account.
2. Go to **Data Explorer**.
3. Click **New Database**:

   * **Database ID:** `agent-memory-db`
4. Click **New Container**:

   * **Container ID:** `agent-state`
   * **Partition key:** `/workflowId`
5. Click **OK**.

### Step 6: Create Azure Container Registry (ACR)

1. In the **Azure Portal**, search for **Container Registries** and click **Create**.
2. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** `agent-hack-rg-<yourname>`
   * **Registry name:** `agentacr<unique>`
   * **Location:** Same region
   * **SKU:** Basic
3. Click **Review + Create** → **Create**.

### Step 7: Initialize Local Project (Agent Codebase)

1. Create a new local project folder.
2. Initialize a Python or Node.js project.
3. Install **Semantic Kernel**.
4. Verify you can run a simple Semantic Kernel script.

*(No agent logic yet — just setup)*

### Step 8: Define Agent Roles (Conceptual)

Document the following agent roles (no code required yet):

* **Extraction Agent**
  Extracts structured data from raw input.

* **Validation Agent**
  Validates extracted data for correctness and completeness.

* **Communication Agent**
  Drafts emails or messages based on processed data.

* **Reporting Agent**
  Generates summaries or reports.

* **Orchestrator Agent**
  Coordinates task execution across agents.

## Completion Criteria

You have successfully completed Challenge 01 if:

* All Azure resources are created
* Azure OpenAI model deployment is ready
* Cosmos DB database and container exist
* ACR is created
* Semantic Kernel project is initialized
* Agent roles are clearly defined
