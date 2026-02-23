# Challenge 01: Environment Setup & Agent Foundations

## Introduction

In this challenge, you will prepare the **core infrastructure** required to build a multi-agent automation engine. You will provision Azure services, set up the development environment, and define the responsibilities of each AI agent. This foundation will be used throughout the hackathon to enable agent collaboration and orchestration.

## Challenge Objectives

- Set up Microsoft Foundry for agent intelligence
- Create shared state storage using Azure Cosmos DB
- Initialize a Semantic Kernel project
- Define agent roles and responsibilities

## Steps to Complete

### Task 1: Create Microsoft Foundry Resource

1. In the **Azure Portal**, search for **Microsoft Foundry** under **Use with Foundry**, select **Foundry** and click **+ Create**.

1. Under **Basics**, provide:

   - **Subscription:** Use the available subscription
   - **Resource Group:** **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Region:** Supported Microsoft Foundry region
   - **Name:** **agent-foundry-<inject key="DeploymentID" enableCopy="false"/>**

1. Click on **Review + Create** and then click **Create**.

1. After deployment succeeds, open the **Microsoft Foundry** resource.

### Task 2: Deploy the Model

1. In the Microsoft Foundry resource, click **Go to Microsoft Foundry portal**.

1. Navigate to **Models + endpoints**, click on **+ Deploy model**, and then select **Deploy base model**.

1. Provide:

   - **Model:** `gpt-4o-mini`
   - **Deployment name:** `agent-gpt-4o-mini`
   - **Deployment type:** Standard

1. Click **Deploy** and wait for deployment.

### Task 3: Create Azure Cosmos DB (Shared Agent Memory)

1. In the **Azure Portal**, search for **Azure Cosmos DB** and click **Create**.

1. Select **Azure Cosmos DB for NoSQL**.

1. Under **Basics**, provide:

   - **Workload Type:** Development/Testing
   - **Subscription:** Use the available subscription
   - **Resource Group:** **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Account Name:** **agent-cosmos-<inject key="DeploymentID" enableCopy="false"/>**
   - **Location:** Same region as other resources
   - **Capacity mode:** Provisioned throughput
1. Click on **Review + Create** and then click **Create**.

### Task 4: Create Database and Container

1. Open the Cosmos DB account.

1. Go to **Data Explorer**.

1. Click on **+ New Container** and then select **+ New Database**:

   - **Database ID:** `agent-memory-db`
   - Select on **OK**

1. Right-click on the *agent-memory-db* and select **New Container**:

   - Select **Use existing**
   - **Container ID:** `agent-state`
   - **Partition key:** `/workflowId`

1. Click on **OK**.

### Task 5: Create Azure Container Registry (ACR)

1. In the **Azure Portal**, search for **Container registries** and click **+ Create**.

1. Under **Basics**, provide:

   - **Subscription:** Use the available subscription
   - **Resource Group:** **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   - **Registry name:** **agentacr<inject key="DeploymentID" enableCopy="false"/>**
   - **Location:** Same region
   - **Pricing plan:** Basic

1. Click on **Review + Create** and then click **Create**.

### Task 6: Initialize Local Project (Agent Codebase)

#### 6.1: Create Project Folder Structure

1. In the `C: drive` create a new folder named:

   ```
   multi-agent-engine
   ```

1. From the Desktop, open a **Visual Studio Code**. Open the new folder `multi-agent-engine` that you created.


1. Inside the folder, create the following structure:

   ```
   multi-agent-engine/
   │
   ├── app/
   │   └── main.py
   │
   ├── .env
   ├── requirements.txt
   └── README.md
   ```

#### 6.2: Create and Activate Virtual Environment (Windows)

1. Open the **Terminal** in VS Code, by pressing `CTRL+J` in keyboard.

1. Create a virtual environment using the Python launcher:

   ```powershell
   py -m venv .venv
   ```

1. Activate the virtual environment:

   ```powershell
   .venv\Scripts\activate
   ```

You should see `(.venv)` in the terminal prompt.

#### 6.3: Install Required Packages

1. Add the following to `requirements.txt`, and save the txt file:

   ```txt
   semantic-kernel
   python-dotenv
   ```

1. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

   >**Note:** It will take 5-10 minutes to deploy.

#### 6.4: Configure Environment Variables

1. Open the `.env` file in the project root.

1. Add the following values (replace placeholders) and save the file:

   ```env
   AZURE_OPENAI_ENDPOINT=https://<your-openai-resource-name>.openai.azure.com/
   MICROSOFT_FOUNDRY_API_KEY=<your-foundry-key>
   AZURE_DEPLOYMENT_NAME=agent-gpt-4o-mini
   ```

   > **Note:** You can get the values from the **Microsoft Foundry** resource by navigating to **Keys and Endpoint**.

#### 6.5: Verify Semantic Kernel Setup

1. Open `app/main.py` and add the following code:

   ```python
   import os
   import asyncio
   from dotenv import load_dotenv
   from semantic_kernel import Kernel
   from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

   load_dotenv()

   async def main():
      kernel = Kernel()

      kernel.add_service(
         AzureChatCompletion(
               service_id="chat",
               deployment_name=os.environ.get("AZURE_DEPLOYMENT_NAME"),
               endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
               api_key=os.environ.get("MICROSOFT_FOUNDRY_API_KEY")
         )
      )

      result = await kernel.invoke_prompt(
         "Say hello from a multi-agent automation engine."
      )

      print(result)

   if __name__ == "__main__":
      asyncio.run(main())
   ```

1. Run the script:

   ```powershell
   py app/main.py
   ```

1. Verify you see a greeting message from the model.

## Success Criteria

- Microsoft Foundry model deployment (`agent-gpt-4o-mini`) is ready and responding
- Cosmos DB database (`agent-memory-db`) and container (`agent-state`) exist
- Azure Container Registry is created
- Semantic Kernel project is initialized and returns a greeting from the model
- Agent roles are clearly documented in `README.md`

## Additional Resources

- [Microsoft Foundry Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/)
- [Azure Container Registry](https://learn.microsoft.com/azure/container-registry/)
- [Semantic Kernel Getting Started](https://learn.microsoft.com/semantic-kernel/get-started/)

Now, click **Next** to continue to **Challenge 02**.
