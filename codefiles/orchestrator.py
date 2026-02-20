"""
Multi-Agent Orchestrator Module
Coordinates Extraction, Validation, Communication, and Reporting agents
using Semantic Kernel for enterprise workflow automation.
"""

import os
import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions import KernelArguments


class MultiAgentOrchestrator:
    """Orchestrates multiple AI agents for enterprise workflow processing."""

    def __init__(self, endpoint: str, api_key: str, deployment: str):
        """
        Initialize the orchestrator with Azure OpenAI credentials.

        Args:
            endpoint: Azure OpenAI endpoint URL
            api_key: Azure OpenAI API key
            deployment: Model deployment name (e.g., 'agent-gpt-4o-mini')
        """
        self.endpoint = endpoint
        self.api_key = api_key
        self.deployment = deployment
        self.kernel = Kernel()
        self.kernel.add_service(
            AzureChatCompletion(
                service_id="chat",
                deployment_name=deployment,
                endpoint=endpoint,
                api_key=api_key,
            )
        )

    # ─── Agent Definitions ───────────────────────────────────────────

    async def run_extraction(self, input_text: str) -> str:
        """
        Extraction Agent: Extracts structured data from raw text input.

        Args:
            input_text: Raw unstructured text to extract data from

        Returns:
            JSON string with extracted structured data
        """
        prompt = """
You are an extraction agent in an enterprise automation engine.

Extract ALL structured data from the text below. Identify and organize:
- People (names, roles, titles, contact info)
- Dates (start dates, deadlines, periods)
- Financial amounts (costs, salaries, totals)
- Organizations (companies, departments, teams)
- Action items (tasks, requirements, deliverables)
- Reference IDs (employee IDs, contract numbers, claim numbers)
- Locations (offices, addresses)

Return ONLY valid JSON with clearly labeled fields.
Do NOT include any explanation or commentary.

Text:
{{$inputText}}
"""
        arguments = KernelArguments(inputText=input_text)
        result = await self.kernel.invoke_prompt(prompt, arguments=arguments)
        return str(result)

    async def run_validation(self, extracted_text: str) -> str:
        """
        Validation Agent: Validates extracted data for completeness and correctness.

        Args:
            extracted_text: JSON string of extracted data

        Returns:
            JSON string with validation results
        """
        prompt = """
You are a validation agent in an enterprise automation engine.

Validate the extracted data below for:
1. Completeness - Are all expected fields present?
2. Consistency - Do dates, amounts, and references make sense?
3. Format correctness - Are dates in proper format, amounts numeric, IDs valid?
4. Logical validation - Do relationships between fields make sense?

Return ONLY valid JSON with this structure:
{
    "isValid": true/false,
    "confidence": 0.0-1.0,
    "validatedData": { ... the validated/corrected data ... },
    "issues": [
        {"field": "fieldName", "severity": "error|warning|info", "message": "description"}
    ],
    "summary": "Brief validation summary"
}

Extracted Data:
{{$data}}
"""
        arguments = KernelArguments(data=extracted_text)
        result = await self.kernel.invoke_prompt(prompt, arguments=arguments)
        return str(result)

    async def run_communication(self, validated_text: str) -> str:
        """
        Communication Agent: Generates professional email/notification content.

        Args:
            validated_text: JSON string of validated data

        Returns:
            JSON string with email subject and body
        """
        prompt = """
You are a communication agent in an enterprise automation engine.

Based on the validated data below, draft a professional email notification.
The email should:
- Have a clear, actionable subject line
- Summarize the key information concisely
- Include relevant dates, amounts, and action items
- Use a professional, friendly tone
- Include next steps or required actions

Return ONLY valid JSON with this structure:
{
    "subject": "Email subject line",
    "body": "Full email body text",
    "priority": "high|normal|low",
    "recipients": "Suggested recipient roles",
    "actionRequired": true/false
}

Validated Data:
{{$data}}
"""
        arguments = KernelArguments(data=validated_text)
        result = await self.kernel.invoke_prompt(prompt, arguments=arguments)
        return str(result)

    async def run_reporting(self, workflow_data) -> str:
        """
        Reporting Agent: Generates workflow execution summary report.

        Args:
            workflow_data: Workflow state dict or string

        Returns:
            JSON string with workflow summary report
        """
        prompt = """
You are a reporting agent in an enterprise automation engine.

Summarize the complete workflow execution below into a concise report.
Include:
- What was processed (input summary)
- Key data points extracted
- Validation status and confidence
- Communication generated
- Overall workflow outcome
- Any recommendations or follow-ups

Return ONLY valid JSON with this structure:
{
    "workflowSummary": "One-line summary",
    "dataPointsExtracted": number,
    "validationStatus": "passed|failed|partial",
    "confidence": 0.0-1.0,
    "keyFindings": ["finding1", "finding2"],
    "recommendations": ["rec1", "rec2"],
    "overallStatus": "success|partial|failed"
}

Workflow State:
{{$data}}
"""
        arguments = KernelArguments(data=str(workflow_data))
        result = await self.kernel.invoke_prompt(prompt, arguments=arguments)
        return str(result)

    # ─── Single Agent Runner ─────────────────────────────────────────

    async def run_single_agent(self, agent_key: str, input_data: str, workflow_state: dict) -> str:
        """
        Run a single agent by key.

        Args:
            agent_key: One of 'extraction', 'validation', 'communication', 'reporting'
            input_data: Input text for the agent
            workflow_state: Current workflow state dict

        Returns:
            Agent output as string
        """
        agent_map = {
            "extraction": self.run_extraction,
            "validation": self.run_validation,
            "communication": self.run_communication,
            "reporting": self.run_reporting,
        }

        agent_func = agent_map.get(agent_key)
        if not agent_func:
            raise ValueError(f"Unknown agent: {agent_key}")

        if agent_key == "reporting":
            return await agent_func(workflow_state)
        else:
            return await agent_func(input_data)

    # ─── Full Pipeline Runner ────────────────────────────────────────

    async def run_full_pipeline(self, input_text: str, workflow_id: str) -> dict:
        """
        Run the complete 4-agent pipeline.

        Args:
            input_text: Raw input text
            workflow_id: Unique workflow identifier

        Returns:
            Complete workflow state dict
        """
        from datetime import datetime

        workflow_state = {
            "id": workflow_id,
            "workflowId": workflow_id,
            "currentStep": "extraction",
            "status": "IN_PROGRESS",
            "agentData": {},
            "history": [],
            "input": input_text[:500],
            "timestamp": datetime.utcnow().isoformat(),
        }

        # Step 1: Extraction
        extraction_result = await self.run_extraction(input_text)
        workflow_state["agentData"]["extraction"] = extraction_result
        workflow_state["history"].append({
            "agent": "ExtractionAgent",
            "output": extraction_result,
            "timestamp": datetime.utcnow().isoformat(),
        })
        workflow_state["currentStep"] = "validation"

        # Step 2: Validation
        validation_result = await self.run_validation(extraction_result)
        workflow_state["agentData"]["validation"] = validation_result
        workflow_state["history"].append({
            "agent": "ValidationAgent",
            "output": validation_result,
            "timestamp": datetime.utcnow().isoformat(),
        })
        workflow_state["currentStep"] = "communication"

        # Step 3: Communication
        communication_result = await self.run_communication(validation_result)
        workflow_state["agentData"]["communication"] = communication_result
        workflow_state["history"].append({
            "agent": "CommunicationAgent",
            "output": communication_result,
            "timestamp": datetime.utcnow().isoformat(),
        })
        workflow_state["currentStep"] = "reporting"

        # Step 4: Reporting
        reporting_result = await self.run_reporting(workflow_state)
        workflow_state["agentData"]["reporting"] = reporting_result
        workflow_state["history"].append({
            "agent": "ReportingAgent",
            "output": reporting_result,
            "timestamp": datetime.utcnow().isoformat(),
        })

        workflow_state["currentStep"] = "completed"
        workflow_state["status"] = "COMPLETED"

        return workflow_state
