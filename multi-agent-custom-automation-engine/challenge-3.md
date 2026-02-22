# Challenge 03: Shared Memory & Agent Communication (Azure Cosmos DB)

## Introduction

In this challenge, you will enable **agent collaboration** by introducing a **shared memory layer**.
In a multi-agent system, agents must not operate in isolation - they need a **common source of truth** to store workflow state, intermediate results, and execution history.

You will use **Azure Cosmos DB** as a **shared memory and messaging layer** so that all agents can read from and write to the same workflow context.

## Challenge Objectives

- Use Cosmos DB as shared memory for agents
- Store workflow state centrally
- Persist agent outputs between steps
- Enable agents to read prior agent results
- Maintain auditability and traceability

## Steps to Complete

### Task 1: Verify Cosmos DB Setup

Ensure the following already exist (from Challenge 01):

- Cosmos DB account (NoSQL)
- Database: `agent-memory-db`
- Container: `agent-state`
- Partition key: `/workflowId`

### Task 2: Define Workflow State Schema

This is how the Agent Context schema will be stored in your Azure Cosmos DB.

This is a **logical schema** (no code yet):

```json
{
  "id": "wf-001",
  "workflowId": "wf-001",
  "currentStep": "extraction",
  "status": "IN_PROGRESS",
  "agentData": {},
  "history": [],
  "timestamp": "2026-01-26T10:30:00Z"
}
```

### What Each Field Means

| Field         | Purpose                |
| ------------- | ---------------------- |
| `workflowId`  | Partition key          |
| `currentStep` | Which agent is running |
| `status`      | Workflow status        |
| `agentData`   | Outputs from agents    |
| `history`     | Audit trail            |
| `timestamp`   | Execution tracking     |

### Task 3: Install Cosmos DB SDK

In your active virtual environment, install the SDK:

```powershell
pip install azure-cosmos
```

### Task 4: Configure Cosmos DB Connection

Add these values to your `.env` file and save the file:

   ```env
   COSMOS_DB_ENDPOINT=https://<your-cosmos-account>.documents.azure.com:443/
   COSMOS_DB_KEY=<your-cosmos-primary-key>
   COSMOS_DB_DATABASE=agent-memory-db
   COSMOS_DB_CONTAINER=agent-state
   ```

   > **Note:** Navigate to **Settings** and then select **Keys** from the Cosmos DB resource in the Azure Portal.


### Task 5: Create Cosmos DB Helper Module

1. Create a new file using the below format:

   ```
   app/storage/cosmos_client.py
   ```

1. Now, add the below code in the `cosmos_client.py` and save the file.

   ```python
   import os
   from azure.cosmos import CosmosClient
   from dotenv import load_dotenv

   load_dotenv()

   client = CosmosClient(
      os.environ["COSMOS_DB_ENDPOINT"],
      credential=os.environ["COSMOS_DB_KEY"]
   )

   database = client.get_database_client(os.environ["COSMOS_DB_DATABASE"])
   container = database.get_container_client(os.environ["COSMOS_DB_CONTAINER"])

   def save_workflow_state(workflow_state: dict):
      container.upsert_item(workflow_state)

   def get_workflow_state(workflow_id: str):
      query = f"SELECT * FROM c WHERE c.workflowId = '{workflow_id}'"
      items = list(container.query_items(query=query, enable_cross_partition_query=True))
      return items[0] if items else None
   ```

### Task 6: Store Extraction Agent Output in Cosmos DB

Update **`main.py`** temporarily to test shared memory.

   ```python
   import os
   import asyncio
   import uuid
   from dotenv import load_dotenv

   from semantic_kernel import Kernel
   from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

   from agents.extraction_agent import run_extraction
   from storage.cosmos_client import save_workflow_state

   # Load environment variables
   load_dotenv()

   async def main():
      # Initialize Semantic Kernel
      kernel = Kernel()

      kernel.add_service(
         AzureChatCompletion(
               service_id="chat",
               deployment_name=os.environ["AZURE_DEPLOYMENT_NAME"],
               endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
               api_key=os.environ["MICROSOFT_FOUNDRY_API_KEY"]
         )
      )

      # Sample input for testing
      sample_input = "Employee Jane Doe joins Engineering on Feb 1, 2026."

      # Generate workflow ID
      workflow_id = str(uuid.uuid4())

      # Run Extraction Agent
      extraction_result = await run_extraction(kernel, sample_input)

      # IMPORTANT: Convert FunctionResult to string (JSON-safe)
      extracted_data = str(extraction_result)

      # Create workflow state object
      workflow_state = {
         "id": workflow_id,
         "workflowId": workflow_id,
         "currentStep": "extraction",
         "status": "IN_PROGRESS",
         "agentData": {
               "extraction": extracted_data
         },
         "history": [
               {
                  "agent": "ExtractionAgent",
                  "output": extracted_data
               }
         ]
      }

      # Save workflow state to Cosmos DB
      save_workflow_state(workflow_state)

      print("Workflow state saved to Cosmos DB")
      print("Workflow ID:", workflow_id)

   if __name__ == "__main__":
      asyncio.run(main())
   ```

Run:

```powershell
py app/main.py
```

### Task 7: Verify Data in Azure Portal

1. Open **Cosmos DB** and navigate to **Data Explorer**.
2. Select:

   - Database: `agent-memory-db`
   - Container: `agent-state`
3. Confirm a new document exists with:

   - Workflow ID
   - Extraction output
   - History entry

## Success Criteria

- Cosmos DB stores workflow state with the correct schema (`workflowId`, `currentStep`, `status`, `agentData`, `history`)
- Agent output from the Extraction Agent is persisted in Cosmos DB
- Workflow state can be retrieved by workflow ID
- Data is visible in Azure Portal under **Data Explorer** in `agent-memory-db` / `agent-state`
- The `save_workflow_state` and `get_workflow_state` functions work correctly

## Additional Resources

- [Azure Cosmos DB for NoSQL Documentation](https://learn.microsoft.com/azure/cosmos-db/nosql/)
- [Azure Cosmos DB Python SDK](https://learn.microsoft.com/azure/cosmos-db/nosql/sdk-python)
- [Semantic Kernel Memory and State](https://learn.microsoft.com/semantic-kernel/overview/)
- [Multi-Agent Shared Memory Patterns](https://learn.microsoft.com/azure/architecture/patterns/event-sourcing)

Now, click **Next** to continue to **Challenge 04**.