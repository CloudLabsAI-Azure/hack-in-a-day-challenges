# Challenge 01: Environment Setup & Agent Foundations

## Introduction

In this challenge, you will prepare the **core infrastructure** required to build a multi-agent automation engine. You will provision Azure services, set up the development environment, and define the responsibilities of each AI agent. This foundation will be used throughout the hackathon to enable agent collaboration and orchestration.

## Challenge Objectives

* Set up Microsoft Foundry for agent intelligence
* Create shared state storage using Azure Cosmos DB
* Create Azure Container Registry (ACR) for agent containers
* Initialize a Semantic Kernel project
* Define agent roles and responsibilities

## Steps to Complete

### Step 1: Create Microsoft Foundry Resource

1. In the **Azure Portal**, search for **Microsoft Foundry** under **Use with Foundry**, select **Foundry** and click **+ Create**.

2. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   * **Region:** Supported Microsoft Foundry region
   * **Name:** **agent-foundry-<inject key="DeploymentID" enableCopy="false"/>**

3. Click **Review + Create** → **Create**.
4. After deployment succeeds, open the **Microsoft Foundry** resource.

### Step 2: Deploy the Model

1. In the Microsoft Foundry resource, click **Go to Microsoft Foundry portal**.
2. Navigate to **Models + endpoints** → **+ Deploy model > Deploy base model**.
3. Provide:

   * **Model:** `gpt-4o-mini`
   * **Deployment name:** `agent-gpt-4o-mini`
   * **Deployment type:** Standard

4. Click **Deploy** and wait for deployment.

### Step 3: Create Azure Cosmos DB (Shared Agent Memory)

1. In the **Azure Portal**, search for **Azure Cosmos DB** and click **Create**.
2. Select **Azure Cosmos DB for NoSQL**.
3. Under **Basics**, provide:

   * **Workload Type:** Development/ Testing
   * **Subscription:** Use the available subscription
   * **Resource Group:** **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   * **Account Name:** **agent-cosmos-<inject key="DeploymentID" enableCopy="false"/>**
   * **Location:** Same region as other resources
   * **Capacity mode:** Provisioned throughput
4. Click **Review + Create** → **Create**.

### Step 4: Create Database and Container

1. Open the Cosmos DB account.
2. Go to **Data Explorer**.
3. Click **+ New Container > + New Database**:

   * **Database ID:** `agent-memory-db`
   * Select **OK**

4. Click **New Container** >:

   * Select **Use existing**
   * **Container ID:** `agent-state`
   * **Partition key:** `/workflowId`

5. Click **OK**.

### Step 5: Create Azure Container Registry (ACR)

1. In the **Azure Portal**, search for **Container Registries** and click **Create**.

2. Under **Basics**, provide:

   * **Subscription:** Use the available subscription
   * **Resource Group:** **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
   * **Registry name:** **agentacr<inject key="DeploymentID" enableCopy="false"/>**
   * **Location:** Same region
   * **Pricing plan:** Basic

3. Click **Review + Create** → **Create**.

### Step 6: Initialize Local Project (Agent Codebase)

#### Step 6.1: Create Project Folder Structure

1. Create a new folder named:

   ```
   multi-agent-engine
   ```

2. Inside the folder, create the following structure:

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

#### Step 6.2: Create and Activate Virtual Environment (Windows)

1. Open **VS Code** and open the `multi-agent-engine` folder.

2. Open the **Terminal** in VS Code.

3. Create a virtual environment using the Python launcher:

   ```powershell
   py -m venv .venv
   ```

4. Activate the virtual environment:

   ```powershell
   .venv\Scripts\activate
   ```

You should see `(.venv)` in the terminal prompt.

#### Step 6.3: Install Required Packages

1. Add the following to `requirements.txt`:

   ```txt
   semantic-kernel
   python-dotenv
   ```

2. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

#### Step 6.4: Configure Environment Variables

1. Open the `.env` file in the project root.

2. Add the following values (replace placeholders):

   ```env
   AZURE_OPENAI_ENDPOINT=https://<your-openai-resource-name>.openai.azure.com/
   MICROSOFT_FOUNDRY_API_KEY=<your-foundry-key>
   AZURE_DEPLOYMENT_NAME=agent-gpt-4o-mini
   ```

> **Note:** The deployment name must exactly match the deployment created in Microsoft Foundry Portal.

#### Step 6.5: Verify Semantic Kernel Setup

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

2. Run the script:

   ```powershell
   py app/main.py
   ```

3. Verify you see a greeting message from the model.


### Step 7: Define Agent Roles (Conceptual)

#### Step 7.1: Why Agent Roles Matter

Multi-agent systems work best when:

* Each agent has a **single responsibility**
* Agents do not overlap tasks
* Coordination is handled centrally

#### Step 7.2: Define Agent Responsibilities

Document the following agent roles in `README.md`:

#### Extraction Agent

**Purpose:**
Extract structured data from raw or unstructured input.

**Example Output:**

   ```json
   {
   "keyData": "value"
   }
   ```

#### Validation Agent

**Purpose:**
Validate extracted data for completeness, accuracy, and consistency.

**Example Output:**

```json
{
  "isValid": true,
  "errors": []
}
```

#### Communication Agent

**Purpose:**
Generate emails, notifications, or messages based on validated data.

**Example Output:**

   ```json
   {
   "subject": "Action Required",
   "message": "The workflow has been completed successfully."
   }
   ```

#### Reporting Agent

**Purpose:**
Generate summaries or reports describing the workflow outcome.

**Example Output:**

   ```json
   {
   "summary": "All workflow steps executed successfully."
   }
   ```

#### Orchestrator Agent

**Purpose:**
Coordinate execution across all agents, manage task order, handle retries, and maintain workflow state.

**Example Flow:**

   ```
   Extraction → Validation → Communication → Reporting
   ```
<validation step="57edd22d-51dc-4216-b7b4-ea8170d67205" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Completion Criteria

You have successfully completed Challenge 01:

* Microsoft Foundry model deployment is ready
* Cosmos DB database and container exist
* ACR is created
* Semantic Kernel project is initialized
* Agent roles are clearly defined

Now, click **Next** to continue to **Challenge 02**.
