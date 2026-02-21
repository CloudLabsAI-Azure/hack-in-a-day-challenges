# Challenge 04: Central Orchestrator & Workflow Execution

## Introduction

In this challenge, you will implement a **Central Orchestrator** that coordinates multiple AI agents.
Instead of running agents manually, the orchestrator will:

- Decide which agent runs next
- Pass data between agents using Cosmos DB
- Validate outputs
- Update workflow state

This is the **brain of the multi-agent system**.

## Challenge Objectives

- Create a central orchestration layer
- Execute agents in the correct order
- Read and update workflow state from Cosmos DB
- Route data between agents
- Maintain execution trace

## What the Orchestrator Will Do (Simple View)

```
User Input
   ↓
Orchestrator
   ↓
Extraction Agent
   ↓
Validation Agent
   ↓
Communication Agent
   ↓
Reporting Agent
```

All intermediate data is stored in **Cosmos DB**.

## Steps to Complete

### Task 1: Create Orchestrator Module

Create a new file:

```
app/orchestrator.py
```

### Task 2: Implement Orchestrator Logic

Paste the following code into `orchestrator.py`, and save the file:

```python
from agents.extraction_agent import run_extraction
from agents.validation_agent import run_validation
from agents.communication_agent import run_communication
from agents.reporting_agent import run_reporting
from storage.cosmos_client import save_workflow_state

async def run_workflow(kernel, workflow_id, input_text):
    workflow_state = {
        "id": workflow_id,
        "workflowId": workflow_id,
        "currentStep": "extraction",
        "status": "IN_PROGRESS",
        "agentData": {},
        "history": []
    }

    # Step 1: Extraction
    extraction_result = await run_extraction(kernel, input_text)
    extraction_output = str(extraction_result)

    workflow_state["agentData"]["extraction"] = extraction_output
    workflow_state["history"].append({
        "agent": "ExtractionAgent",
        "output": extraction_output
    })
    workflow_state["currentStep"] = "validation"
    save_workflow_state(workflow_state)

    # Step 2: Validation
    validation_result = await run_validation(kernel, extraction_output)
    validation_output = str(validation_result)

    workflow_state["agentData"]["validation"] = validation_output
    workflow_state["history"].append({
        "agent": "ValidationAgent",
        "output": validation_output
    })
    workflow_state["currentStep"] = "communication"
    save_workflow_state(workflow_state)

    # Step 3: Communication
    communication_result = await run_communication(kernel, validation_output)
    communication_output = str(communication_result)

    workflow_state["agentData"]["communication"] = communication_output
    workflow_state["history"].append({
        "agent": "CommunicationAgent",
        "output": communication_output
    })
    workflow_state["currentStep"] = "reporting"
    save_workflow_state(workflow_state)

    # Step 4: Reporting
    reporting_result = await run_reporting(kernel, workflow_state)
    reporting_output = str(reporting_result)

    workflow_state["agentData"]["reporting"] = reporting_output
    workflow_state["history"].append({
        "agent": "ReportingAgent",
        "output": reporting_output
    })

    workflow_state["currentStep"] = "completed"
    workflow_state["status"] = "COMPLETED"
    save_workflow_state(workflow_state)

    return workflow_state
```

### Task 3: Update `main.py` to Use Orchestrator

Replace the logic in `app/main.py` with the following:

```python
import os
import asyncio
import uuid
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from orchestrator import run_workflow

load_dotenv()

async def main():
    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            service_id="chat",
            deployment_name=os.environ["AZURE_DEPLOYMENT_NAME"],
            endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["MICROSOFT_FOUNDRY_API_KEY"]
        )
    )

    workflow_id = str(uuid.uuid4())
    input_text = "Employee Jane Doe joins Engineering on Feb 1, 2026."

    final_state = await run_workflow(kernel, workflow_id, input_text)

    print("Workflow completed")
    print("Workflow ID:", workflow_id)

if __name__ == "__main__":
    asyncio.run(main())
```

### Task 4: Verify Agent Compatibility

Before running the orchestrator, verify that your agents from Challenge 02 are compatible with the orchestrator.

The orchestrator expects the following function signatures:

| Agent | Function | Input |
|-------|----------|-------|
| Extraction Agent | `run_extraction(kernel, input_text)` | Raw text string |
| Validation Agent | `run_validation(kernel, extracted_text)` | Extracted JSON string |
| Communication Agent | `run_communication(kernel, validated_text)` | Validated JSON string |
| Reporting Agent | `run_reporting(kernel, workflow_data)` | Workflow state (dict or string) |

Open each agent file in `app/agents/` and confirm:

- Each function uses `KernelArguments` for prompt variables
- Each prompt uses `{{$data}}` or `{{$inputText}}` template syntax
- Each function returns the result from `kernel.invoke_prompt()`

> **Note:** If you completed Challenge 02 correctly, all agents should already be compatible. No changes are needed.

### Task 5: Run the Full Workflow

Run:

```powershell
py app/main.py
```

### Task 6: Verify Workflow Execution

In **Azure Portal**, navigate to **Cosmos DB** and then open **Data Explorer**:

- Open the `agent-state` container
- Locate the document with your workflow ID
- Confirm that `status` is set to `COMPLETED`
- Confirm that `agentData` contains extraction, validation, communication, and reporting
- Confirm that `history` contains all agent executions

## Success Criteria

- Orchestrator module (`orchestrator.py`) executes all four agents sequentially
- Each agent writes its output to the Cosmos DB workflow state
- Workflow state transitions correctly from `extraction` to `validation` to `communication` to `reporting` to `completed`
- Final `status` is `COMPLETED` in the Cosmos DB document
- `agentData` contains outputs from all four agents (extraction, validation, communication, reporting)
- `history` array contains all four agent execution entries
- Full execution history is visible in Azure Portal under **Data Explorer**

## Additional Resources

- [Semantic Kernel Orchestration](https://learn.microsoft.com/semantic-kernel/overview/)
- [Multi-Agent Orchestration Patterns](https://learn.microsoft.com/azure/architecture/patterns/choreography)
- [Azure Cosmos DB Data Explorer](https://learn.microsoft.com/azure/cosmos-db/data-explorer)
- [Building AI Agents with Semantic Kernel](https://learn.microsoft.com/semantic-kernel/frameworks/agent/)

Now, click **Next** to continue to **Challenge 05**.