# Multi-Agent Custom Automation Engine

**Duration:** 6 hours

## Overview

Welcome to the **Multi-Agent Custom Automation Engine - Hack in a Day**. In this hands-on lab, you will design and build an **AI-driven automation engine** where multiple specialized agents collaborate to execute complex enterprise workflows autonomously.

Modern enterprises rely on multi-step processes across HR, finance, marketing, and operations. These workflows often involve manual coordination, email handoffs, spreadsheets, and disconnected tools, leading to delays, inconsistent outcomes, and limited auditability. Traditional automation systems struggle with contextual decision-making and dynamic task routing.

At **Contoso Enterprises**, workflows such as employee onboarding, compliance reporting, internal communications, and operational updates require extracting information, validating data, drafting communications, and producing summaries, often across different systems and teams. Your mission is to build a **Multi-Agent Automation Engine** where each AI agent specializes in a specific task, agents collaborate using shared context and memory, a central orchestrator coordinates execution and decision-making, and workflow state and audit history are persisted for transparency.

## Key Azure Services

- **Microsoft Foundry** - AI model hosting with GPT-models for agent intelligence
- **Azure Cosmos DB (NoSQL)** - Shared memory for workflow state, agent outputs, and audit history
- **Azure Container Registry** - (Bonus) Container image storage for deployment
- **Semantic Kernel** - Multi-agent orchestration framework
- **Streamlit** - Production dashboard for workflow processing and history

## Challenges

- **Challenge 01: Environment & AI Foundation Setup** - Provision Microsoft Foundry, Cosmos DB, and ACR. Initialize Semantic Kernel project and define agent roles.
- **Challenge 02: Build Specialized AI Agents** - Create four AI agents (Extraction, Validation, Communication, Reporting) using Semantic Kernel with proper prompt templates.
- **Challenge 03: Shared Memory with Cosmos DB** - Persist workflow state and agent outputs using a shared data store. Enable agents to read prior results.
- **Challenge 04: Central Orchestrator & Agent Collaboration** - Implement the orchestrator that coordinates all agents, manages workflow execution, and maintains audit trails.
- **Challenge 05: Production Dashboard & End-to-End Validation** - Configure and run the pre-built Streamlit dashboard. Test multi-agent pipeline with sample enterprise scenarios. Verify in Cosmos DB.

## Learning Objectives

By completing this hackathon, you will:

- Design multi-agent AI systems using orchestration patterns
- Create specialized AI agents for extraction, validation, communication, and reporting
- Coordinate agents using a central orchestrator
- Share context and state across agents using a persistent memory layer
- Execute autonomous, multi-step workflows driven by natural language input
- Build explainable and auditable AI-driven automation solutions

## Prerequisites

- Basic familiarity with the Azure portal
- Understanding of AI/ML concepts (no deep expertise required)
- Basic Python knowledge (helpful but not mandatory - code is pre-built)
- Curiosity and willingness to experiment!

## Hackathon Format

This is a **challenge-based hackathon** - each challenge gives you objectives and guided steps to help you along the way. You will build progressively, starting from infrastructure setup and ending with a fully functional, demo-able multi-agent automation pipeline.

Click **Next** to set up your lab environment.
