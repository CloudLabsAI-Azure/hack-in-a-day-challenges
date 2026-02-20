# Multi-Agent Custom Automation Engine

## Overview

Welcome to the **Multi-Agent Custom Automation Engine – Hack in a Day**.
In this hands-on lab, you will design and build an **AI-driven automation engine** where multiple specialized agents collaborate to execute complex enterprise workflows autonomously.

Modern enterprises rely on multi-step processes across HR, finance, marketing, and operations. These workflows often involve manual coordination, email handoffs, spreadsheets, and disconnected tools—leading to delays, inconsistent outcomes, and limited auditability. Traditional automation systems struggle with contextual decision-making and dynamic task routing.

This lab demonstrates how **AI agents**, powered by large language models and orchestrated through a central control layer, can collaborate intelligently, share context, validate outcomes, and produce reliable, traceable automation results.

## Scenario

Contoso Enterprises operates across multiple departments and manages workflows such as employee onboarding, compliance reporting, internal communications, and operational updates. These workflows require extracting information, validating data, drafting communications, and producing summaries—often across different systems and teams.

Manual execution of these steps introduces delays and errors, while rule-based automation tools lack the flexibility to adapt to changing inputs and context.

To modernize its operations, Contoso decides to build a **Multi-Agent Automation Engine** where:

* Each AI agent specializes in a specific task
* Agents collaborate using shared context and memory
* A central orchestrator coordinates execution and decision-making
* Workflow state and audit history are persisted for transparency

Your mission is to build this automation engine end-to-end.

## Introduction

In this lab, you will build a **Multi-Agent Custom Automation Engine** using AI orchestration patterns commonly adopted in modern enterprise systems. Instead of relying on a single monolithic AI model, you will design **multiple specialized agents**, each responsible for a distinct role:

* Extracting structured information
* Validating data quality and correctness
* Generating communications
* Producing summaries and reports

A **central orchestrator** coordinates these agents, routes tasks, manages workflow state, and ensures outputs are traceable and reliable. Shared memory is implemented using a cloud database, enabling agents to collaborate across steps and maintain execution context.

The lab focuses on **core AI orchestration principles**, not infrastructure complexity, ensuring that all participants can complete the solution within the allocated time.

## Architecture

```
┌─────────────────┐     ┌─────────────────────────┐
│  User Input     │     │  Central Orchestrator   │
│  (Text / File   │────▶│  (Semantic Kernel)       │
│   / Sample Data)│     │                         │
└─────────────────┘     └────────────┬────────────┘
                                  │
                    ┌────────────▼────────────┐
                    │  Extraction Agent       │
                    │  (Structured Data)      │
                    └────────────┬────────────┘
                                  │
                    ┌────────────▼────────────┐
                    │  Validation Agent       │
                    │  (Quality Check)        │
                    └────────────┬────────────┘
                                  │
                    ┌────────────▼────────────┐
                    │  Communication Agent    │
                    │  (Email / Notification) │
                    └────────────┬────────────┘
                                  │
                    ┌────────────▼────────────┐
                    │  Reporting Agent        │
                    │  (Summary / Report)     │
                    └────────────┬────────────┘
                                  │
                    ┌────────────▼────────────┐
                    │  Azure Cosmos DB        │
                    │  (Shared Memory &       │
                    │   Audit Trail)          │
                    └─────────────────────────┘
                                  │
                    ┌────────────▼────────────┐
                    │  Streamlit Dashboard    │
                    │  (Process, Results,     │
                    │   History)              │
                    └─────────────────────────┘
```

## Key Azure Services

| Service | Purpose |
|---------|---------|
| **Microsoft Foundry (Azure AI Foundry)** | AI model hosting — GPT-4o-mini for agent intelligence |
| **Azure Cosmos DB (NoSQL)** | Shared memory — workflow state, agent outputs, audit history |
| **Azure Container Registry** | (Bonus) Container image storage for deployment |
| **Semantic Kernel** | Multi-agent orchestration framework |
| **Streamlit** | Production dashboard for workflow processing and history |

## Learning Objectives

By completing this hackathon, you will learn how to:

* Design multi-agent AI systems using orchestration patterns
* Create specialized AI agents for extraction, validation, communication, and reporting
* Coordinate agents using a central orchestrator
* Share context and state across agents using a persistent memory layer
* Execute autonomous, multi-step workflows driven by natural language input
* Build explainable and auditable AI-driven automation solutions

## Hack in a Day Format: Challenge-Based

This lab is structured into **five progressive challenges**, each building on the previous one to model a real-world enterprise automation lifecycle:

| Challenge | Title | Duration | Description |
|-----------|-------|----------|-------------|
| **1** | Environment & AI Foundation Setup | ~45 min | Provision Microsoft Foundry, Cosmos DB, and ACR. Initialize Semantic Kernel project and define agent roles. |
| **2** | Build Specialized AI Agents | ~40 min | Create four AI agents (Extraction, Validation, Communication, Reporting) using Semantic Kernel with proper prompt templates. |
| **3** | Shared Memory with Cosmos DB | ~40 min | Persist workflow state and agent outputs using a shared data store. Enable agents to read prior results. |
| **4** | Central Orchestrator & Agent Collaboration | ~45 min | Implement the orchestrator that coordinates all agents, manages workflow execution, and maintains audit trails. |
| **5** | Production Dashboard & End-to-End Validation | ~50 min | Configure and run the pre-built Streamlit dashboard. Test multi-agent pipeline with sample enterprise scenarios. Verify in Cosmos DB. |

Each challenge is designed to be **independently verifiable**, ensuring steady progress and clear milestones throughout the hackathon.

## Challenge Outcome

By the end of this lab, you will have built:

* A fully functional **multi-agent automation engine** with four specialized AI agents
* A centralized **orchestration layer** managing execution flow using Semantic Kernel
* A **shared memory system** (Cosmos DB) enabling transparency and auditability
* A **production-grade Streamlit dashboard** for workflow processing, results visualization, and history
* A containerizable solution pattern suitable for enterprise deployment

## Prerequisites

- Basic familiarity with the Azure portal
- Understanding of AI/ML concepts (no deep expertise required)
- Basic Python knowledge (helpful but not mandatory — code is pre-built)
- Curiosity and willingness to experiment!

**Duration:** ~4–6 hours (depending on experience level)

## Final Note

> In production environments, this automation engine can be deployed using container-based platforms or managed app services.
> For this hackathon, execution is intentionally simplified to focus on **AI orchestration, agent collaboration, and workflow correctness**.

## Support Contact

The CloudLabs support team is available 24/7 to assist you throughout the lab.

* Email: [cloudlabs-support@spektrasystems.com](mailto:cloudlabs-support@spektrasystems.com)
* Live Chat: [https://cloudlabs.ai/labs-support](https://cloudlabs.ai/labs-support)

> Click **Next** to begin **Challenge 01: Environment & AI Foundation Setup**.
