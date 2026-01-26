# Challenge 02: Build Specialized AI Agents (Using Semantic Kernel)

## Introduction

In this challenge, you will implement your **first set of AI agents** using **Semantic Kernel**.
Each agent will have **one clear responsibility** and will be implemented as a **self-contained skill**.
At this stage, agents will run **locally** (not containerized yet).

## Challenge Objectives

* Create multiple AI agents using Semantic Kernel
* Assign one responsibility per agent
* Implement prompt-based skills for each agent
* Validate agent outputs independently
* Ensure agents return structured JSON

## Steps to Complete

## Step 1: Create Agent Folder Structure

Inside your existing project, update the structure as follows:

  ```
  multi-agent-engine/
  │
  ├── app/
  │   ├── main.py
  │   ├── agents/
  │   │   ├── extraction_agent.py
  │   │   ├── validation_agent.py
  │   │   ├── communication_agent.py
  │   │   └── reporting_agent.py
  │
  ├── .env
  ├── requirements.txt
  └── README.md
  ```

## Step 2: Create the Extraction Agent

### Purpose

Extract structured data from raw text input.

### Step 2.1: Create `extraction_agent.py`

Paste the following code:

  ```python
  from semantic_kernel import Kernel
  from semantic_kernel.functions import KernelArguments

  async def run_extraction(kernel: Kernel, input_text: str):
    prompt = """
  You are an extraction agent.

  Extract structured data from the text below.
  Return ONLY valid JSON.

  Text:
  {{$inputText}}
  """

    arguments = KernelArguments(
        inputText=input_text
    )

    result = await kernel.invoke_prompt(
        prompt,
        arguments=arguments
    )

    return result

  ```

## Step 3: Create the Validation Agent

### Purpose

Validate extracted data for completeness and correctness.

### Step 3.1: Create `validation_agent.py`

  ```python
  from semantic_kernel import Kernel

  async def run_validation(kernel: Kernel, extracted_json: str):
      prompt = """
      You are a validation agent.

      Validate the extracted data.
      Check for missing or inconsistent fields.
      Return valid JSON only.

      INPUT:
      {{input}}
      """

      result = await kernel.invoke_prompt(
          prompt,
          input=extracted_json
      )

      return result
  ```

## Step 4: Create the Communication Agent

### Purpose

Generate email or notification content based on validated data.

### Step 4.1: Create `communication_agent.py`

  ```python
  from semantic_kernel import Kernel

  async def run_communication(kernel: Kernel, validated_json: str):
      prompt = """
      You are a communication agent.

      Draft a professional email message based on the validated data.
      Return valid JSON only with subject and body.

      INPUT:
      {{input}}
      """

      result = await kernel.invoke_prompt(
          prompt,
          input=validated_json
      )

      return result
  ```

## Step 5: Create the Reporting Agent

### Purpose

Generate a human-readable summary of the workflow.

### Step 5.1: Create `reporting_agent.py`

  ```python
  from semantic_kernel import Kernel

  async def run_reporting(kernel: Kernel, workflow_data: str):
      prompt = """
      You are a reporting agent.

      Summarize the workflow outcome in a concise manner.
      Return valid JSON only.

      INPUT:
      {{input}}
      """

      result = await kernel.invoke_prompt(
          prompt,
          input=workflow_data
      )

      return result
  ```

## Step 6: Test Agents Individually

Update `app/main.py` temporarily to test **only the Extraction Agent**.

  ```python
  import os
  import asyncio
  from dotenv import load_dotenv
  from semantic_kernel import Kernel
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from agents.extraction_agent import run_extraction

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

      sample_input = "Employee Jane Doe joins Engineering on Feb 1, 2026."

      result = await run_extraction(kernel, sample_input)
      print(result)

  if __name__ == "__main__":
      asyncio.run(main())
  ```

- Run:

  ```powershell
  py app/main.py
  ```

## Step 7: Verify Agent Output

Expected output (example):

  ```json
  {
    "employeeName": "Jane Doe",
    "department": "Engineering",
    "startDate": "2026-02-01"
  }
  ```

Minor variations are acceptable.

## Completion Criteria

You have successfully completed Challenge 02:

* All four agents are created
* Each agent has one clear responsibility
* Agents return structured JSON
* At least one agent runs successfully

Now, click **Next** to continue to **Challenge 03**.