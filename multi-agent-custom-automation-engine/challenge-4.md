# Challenge 04: Central Orchestrator & Workflow Execution

## Introduction

In this challenge, you will implement a **Central Orchestrator** that coordinates multiple AI agents.
Instead of running agents manually, the orchestrator will:

* Decide which agent runs next
* Pass data between agents using Cosmos DB
* Validate outputs
* Update workflow state

This is the **brain of the multi-agent system**.

## Challenge Objectives

* Create a central orchestration layer
* Execute agents in the correct order
* Read and update workflow state from Cosmos DB
* Route data between agents
* Maintain execution trace

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

## Step 1: Create Orchestrator Module

Create a new file:

```
app/orchestrator.py
```

## Step 2: Implement Orchestrator Logic

Paste the following code into `orchestrator.py`:

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

## Step 3: Update `main.py` to Use Orchestrator

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
            deployment_name=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
            endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"]
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

## Step 4: Delete Existing Agent Files

To avoid leftover or cached prompt issues, **delete** the following files completely:

```
app/agents/validation_agent.py
app/agents/communication_agent.py
app/agents/reporting_agent.py
```

> Do not edit these files — delete them first.

## Step 5: Recreate the Validation Agent

Create a new file:

```
app/agents/validation_agent.py
```

Paste the following code:

```python
from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments

async def run_validation(kernel: Kernel, extracted_text: str):
    prompt = """
You are a validation agent.

Validate the extracted data below.
Check for missing or inconsistent fields.
Return ONLY valid JSON.

Extracted Data:
{{$data}}
"""

    arguments = KernelArguments(
        data=extracted_text
    )

    result = await kernel.invoke_prompt(
        prompt=prompt,
        arguments=arguments
    )

    return result
```

Save the file.

## Step 6: Recreate the Communication Agent

Create a new file:

```
app/agents/communication_agent.py
```

Paste the following code:

```python
from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments

async def run_communication(kernel: Kernel, validated_text: str):
    prompt = """
You are a communication agent.

Draft a professional email based on the validated data below.
Return ONLY valid JSON with subject and body.

Validated Data:
{{$data}}
"""

    arguments = KernelArguments(
        data=validated_text
    )

    result = await kernel.invoke_prompt(
        prompt=prompt,
        arguments=arguments
    )

    return result
```

Save the file.

## Step 7: Recreate the Reporting Agent

Create a new file:

```
app/agents/reporting_agent.py
```

Paste the following code:

```python
from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments

async def run_reporting(kernel: Kernel, workflow_state: dict):
    prompt = """
You are a reporting agent.

Summarize the workflow execution below.
Return ONLY valid JSON.

Workflow State:
{{$data}}
"""

    arguments = KernelArguments(
        data=str(workflow_state)
    )

    result = await kernel.invoke_prompt(
        prompt=prompt,
        arguments=arguments
    )

    return result
```

Save the file.

## Step 8: Run the Full Workflow

Run:

```powershell
py app/main.py
```

## Step 9: Verify Workflow Execution

In **Azure Portal → Cosmos DB → Data Explorer**:

* Open `agent-state` container
* Locate the document with your workflow ID
* Confirm:

  * `status` = `COMPLETED`
  * `agentData` contains:

    * extraction
    * validation
    * communication
    * reporting
  * `history` contains all agent executions

## Completion Criteria

You have successfully completed Challenge 04:

* Orchestrator executes all agents sequentially
* Each agent writes output to Cosmos DB
* Workflow state transitions correctly
* Final status is `COMPLETED`
* Full execution history is visible

Now, click **Next** to continue to **Challenge 05**.