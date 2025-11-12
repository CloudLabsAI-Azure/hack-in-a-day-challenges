# Hands-on with Azure AI Foundry & Agent Frameworks

Welcome to the Copilot Hackathon! Today, you’ll level up from basic LLM calls to **goal-driven agentic AI** using **Azure AI Foundry**. You’ll wire up projects, connect models and tools, add RAG, experiment with multimodal inputs, and ship task-oriented **AI agents** with observability and governance in mind.

## Introduction

Your quest is to build an end-to-end AI application stack powered by Azure AI Foundry. You’ll authenticate and configure your workspace, explore chat completions and embeddings, ground your model with enterprise data using **RAG**, and orchestrate **agents** augmented with tools such as **Azure AI Search** and **Bing grounding**. You’ll also add **tracing/evaluation** for reliability and finish by integrating with event-driven services to automate real-world workflows.

## Learning Objectives

By participating in this hackathon, you will learn how to:

- **Set up the AI project and connections** in Azure AI Foundry (models, keys, identity) and validate access via SDK.
- Build **chat** and **embedding** flows; apply **Retrieval-Augmented Generation (RAG)** with vector stores and hybrid search.
- Design **agents** that use tools (code interpreter, web grounding, Azure AI Search) to plan, reason, and act.
- Explore **multimodal** capabilities for richer inputs/outputs where applicable.
- Implement **observability & evaluation** (tracing, telemetry, automated checks) for safe and reliable agents.
- Integrate with **event-driven automation** (e.g., Functions/queues) to trigger agent actions from real-world signals.

## Hackathon Format: Challenge-Based

This hackathon adopts a challenge-based format so you learn by building a working solution:

- Analyze the problem and required outcomes.
- Plan the agentic architecture (data grounding, tools, orchestration).
- Leverage the provided environment, Azure AI Foundry SDK, and supporting services.

## Challenge Overview

Begin by authenticating to Azure and initializing an **Azure AI Foundry** project in VS Code/Jupyter. Use the SDK to run **chat completions** and **embeddings**, then stand up a **RAG** pipeline that indexes health/fitness content and answers grounded queries. Next, create **task-specialized agents** (e.g., wellness coach, health calculator, file-search agent) and enrich them with **Bing grounding** and **Azure AI Search** for real-time, relevant responses. Add **observability and tracing** to capture prompts, tool calls, and results, and evaluate model behavior against simple quality gates. Finally, connect your agent to an **event-driven trigger** to demonstrate automated actions in response to live signals.

## Happy Hacking!!
