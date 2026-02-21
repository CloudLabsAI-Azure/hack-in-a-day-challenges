# Challenge 02: Build Specialized AI Agents (Using Semantic Kernel)

## Introduction

In this challenge, you will implement your **first set of AI agents** using **Semantic Kernel**.
Each agent will have **one clear responsibility** and will be implemented as a **self-contained skill**.
At this stage, agents will run **locally**.

## Challenge Objectives

- Create multiple AI agents using Semantic Kernel
- Assign one responsibility per agent
- Implement prompt-based skills for each agent
- Validate agent outputs independently
- Ensure agents return structured JSON

## Steps to Complete

### Task 1: Create Agent Folder Structure

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

### Task 2: Create the Extraction Agent

Extract structured data from raw text input.

1. Copy the below mentioned code and paste it in `extraction_agent.py`, and save the file.

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

### Task 3: Create the Validation Agent

Validate extracted data for completeness and correctness.

1. Create `validation_agent.py` and paste the following code, and save the file:

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

### Task 4: Create the Communication Agent

Generate email or notification content based on validated data.

1. Create `communication_agent.py` and paste the following code, and save the file:

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

### Task 5: Create the Reporting Agent

Generate a human-readable summary of the workflow.

1. Create `reporting_agent.py` and paste the following code, and save the file:

  ```python
  from semantic_kernel import Kernel
  from semantic_kernel.functions import KernelArguments

  async def run_reporting(kernel: Kernel, workflow_data):
      prompt = """
You are a reporting agent.

Summarize the workflow execution below.
Return ONLY valid JSON.

Workflow State:
{{$data}}
"""

      arguments = KernelArguments(
          data=str(workflow_data)
      )

      result = await kernel.invoke_prompt(
          prompt=prompt,
          arguments=arguments
      )

      return result
  ```

### Task 6: Test Agents Individually

Update `app/main.py` temporarily to test **only the Extraction Agent** and save the file.

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

### Task 7: Verify Agent Output

Expected output (example):

  ```json
  {
    "employeeName": "Jane Doe",
    "department": "Engineering",
    "startDate": "2026-02-01"
  }
  ```

Minor variations are acceptable.

## Success Criteria

- All four agent files are created (`extraction_agent.py`, `validation_agent.py`, `communication_agent.py`, `reporting_agent.py`)
- Each agent has one clear responsibility and uses `KernelArguments` for prompt variables
- Agents return structured JSON output
- The Extraction Agent runs successfully with the sample input and produces valid output
- Agent folder structure matches the expected layout

## Additional Resources

- [Semantic Kernel Overview](https://learn.microsoft.com/semantic-kernel/overview/)
- [Semantic Kernel Prompt Templates](https://learn.microsoft.com/semantic-kernel/prompts/)
- [Azure OpenAI Chat Completions](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt)
- [Multi-Agent Design Patterns](https://learn.microsoft.com/semantic-kernel/frameworks/agent/agent-architecture)

Now, click **Next** to continue to **Challenge 03**.