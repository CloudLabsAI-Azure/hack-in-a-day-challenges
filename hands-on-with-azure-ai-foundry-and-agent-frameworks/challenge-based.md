# Fitness-Fun Lab: Azure AI Foundry Hands-On Workshop

## Lab Overview

This hands-on lab will guide you through building AI-driven health and fitness solutions using Azure AI Foundry, Azure AI Search, Semantic Kernel, and multi-agent orchestration frameworks like Autogen. You will learn how to:

* Authenticate and configure Azure AI environments.
* Perform chat completions, embeddings, and RAG workflows.
* Develop intelligent AI agents for fitness, nutrition, and health guidance.
* Integrate observability and monitoring with OpenTelemetry and Azure Monitor.
* Build multi-agent AI pipelines for complex reasoning and task orchestration.

By completing this lab, you will gain practical experience in designing, deploying, and monitoring AI solutions using Azure AI Foundry and related technologies.

---

# Exercise 1: Introduction to Azure AI Foundry

**Estimated Duration:** 40 Minutes

### Overview

In this exercise, you will set up your Azure AI environment and explore the Azure AI Foundry interface. You will get familiar with the platform, resources, and basic operations.

### Lab Objectives

* Explore Azure AI Foundry workspace.
* Understand available models and endpoints.
* Learn navigation and initial setup for AI projects.

### Steps

1. Navigate to your Azure AI Foundry workspace.
2. Explore the UI, highlighting:

   * Models
   * Endpoints
   * Projects
   * Data and embeddings
3. Observe and note the sample outputs from the Azure AI Foundry demo.

### Summary

You have familiarized yourself with the Azure AI Foundry environment and basic functionality, preparing for hands-on AI development in subsequent exercises.

---

# Exercise 2: Build & Connect: AI Project Initialization with Azure Tools

**Estimated Duration:** 40 Minutes

### Overview

Authenticate credentials using Azure CLI, configure the AI Project Client, and validate model and search connections. Initialize AI projects, list available models, and make a chat completion request.

### Lab Objectives

* Authenticate Azure credentials in VS Code Jupyter notebooks.
* Configure the AI Project Client.
* Validate Azure AI Search and OpenAI connections.
* Initialize an AI project and make a chat completion request.

### Tasks

#### Task 1: Authenticate your Credentials

1. Open `1-introduction/1-authentication.ipynb`.
2. Select kernel `ai-foundry-workshop (Python 3.12.1)`.
3. Execute cells to:

   * Log in to Azure portal.
   * Acquire authentication tokens.
4. Save changes.

#### Task 2: Configuring the Environment

1. Open `1-introduction/2-environment_setup.ipynb`.
2. Execute cells to:

   * Install dependencies.
   * Initialize project and validate Azure service connections.

#### Task 3: Quick Start to the Workshop

1. Open `1-introduction/3-quick_start.ipynb`.
2. Execute cells to:

   * Test model completion.
   * Create an AI agent and conversation thread.
   * Generate visual output.

### Summary

* Authenticated Azure credentials.
* Configured AI Project Client.
* Validated essential service connections.
* Explored available models and executed basic chat completion.

---

# Exercise 3: Chat Completion & Retrieval-Augmented Generation (RAG)

**Estimated Duration:** 40 Minutes

### Overview

Use Azure AI Foundry SDK to create health and fitness applications with chat completions, embeddings, and RAG.

### Lab Objectives

* Perform chat completions using AI models.
* Generate text and image embeddings.
* Build RAG pipelines to answer health-related queries.
* Configure and test Phi-4 and DeepSeek-R1 models.

### Tasks

#### Task 1: Chat Completions

* Open `2-notebooks/1-chat_completion/1-basic-chat-completion.ipynb`.
* Select kernel `ai-foundry-workshop (Python 3.12.1)`.
* Execute cells to configure chat completion client, define prompts, and generate assistant responses.

#### Task 2: Health & Fitness Embeddings

* Open `2-embeddings.ipynb`.
* Generate text embeddings, apply prompt templates, and embed health-related images.

#### Task 3: RAG with AI Project Client

* Open `3-basic-rag.ipynb`.
* Embed health tips, index them, and query using LLM for context-aware responses.

#### Task 4: Phi-4 Model

* Open `4-phi-4.ipynb`.
* Edit `.env` to use Phi-4 model.
* Execute cells to chat with Phi-4 and simulate RAG flow.

#### Task 5: DeepSeek-R1 Model

* Open `5-deep-seek-r1.ipynb`.
* Configure `.env` with model endpoint and key.
* Run queries to evaluate technical and general responses.

### Summary

* Performed chat completions and embedding generation.
* Built RAG pipelines for health tips.
* Configured Phi-4 and DeepSeek-R1 models for contextual and technical queries.

---

# Exercise 4: Agent Development

**Estimated Duration:** 40 Minutes

### Overview

Develop AI agents for health and fitness, including a wellness assistant, health calculator, file search agent, and Bing Grounding agent. Integrate with Azure AI Search and Azure Functions.

### Lab Objectives

* Create playful health & fitness assistant agent.
* Develop health calculator and file search agents.
* Integrate Bing grounding for real-time web data.
* Build AI Search + Agent service for fitness applications.

### Tasks

#### Task 1: Health & Fitness Assistant Agent

* Open `2-notebooks/2-agent_service/1-basics.ipynb`.
* Execute cells to create, query, and delete agent.

#### Task 2: Health Calculator Agent

* Open `2-code_interpreter.ipynb`.
* Create CSV, enable Code Interpreter, perform BMI and nutrition analysis.

#### Task 3: Health Resource Search Agent

* Open `3-file-search.ipynb`.
* Create markdown files, store in vector store, and query agent.

#### Task 4: Health & Fitness Agent with Bing Grounding

* Open `4-bing_grounding.ipynb`.
* Configure agent, create multiple conversation threads, and query Bing-grounded agent.

#### Task 5: AI Search + Agent Service

* Open `5-agents-aisearch.ipynb`.
* Build search index, add documents, create agent, and query Azure AI Search.

### Summary

* Built multiple AI agents for health and fitness tasks.
* Integrated tools like code interpreters, vector search, and Bing grounding.
* Created dynamic AI agents capable of multi-turn conversation and data retrieval.

---

# Exercise 5: Enhance the Agent

**Estimated Duration:** 40 Minutes

### Overview

Integrate observability, tracing, and model evaluation into AI agents using OpenTelemetry and Azure Monitor.

### Lab Objectives

* Enable observability and tracing for AI agents.
* Monitor LLM interactions for reliability and compliance.
* Execute step-by-step tracing workflows in VS Code notebooks.

### Task: Observability & Tracing Demo

1. Open `2-notebooks/3-quality_attributes/1-Observability.ipynb`.
2. Select kernel `ai-foundry-workshop (Python 3.12.1)`.
3. Execute cells sequentially to:

   * Initialize client.
   * Configure OpenTelemetry tracing.
   * Monitor execution of AI models.
4. Create a tracing session in Azure AI Foundry portal:

   * Tracing → Create new → Name: `insights-` → Create.
5. Save changes.

### Summary

* Integrated observability and tracing.
* Monitored agent interactions and verified performance via Azure Monitor.

---

# Exercise 6: Fitness-Fun Workshop

**Estimated Duration:** 40 Minutes

### Overview

Build a multi-agent AI-driven fitness assistant integrating Azure AI Search with Semantic Kernel and Autogen for RAG-based reasoning.

### Lab Objectives

* Integrate Azure AI Search with Semantic Kernel.
* Enable multi-agent RAG pipelines.
* Index fitness data and create context-aware agents.
* Configure GitHub authentication for secure orchestration.

### Task 1: Azure AI Search + Semantic Kernel + AI Agents

1. Update Semantic Kernel package:

   ```bash
   uv pip install semantic-kernel[azure]==1.28.0 --prerelease=allow
   ```
2. Open `2-notebooks/4-frameworks/1-rag-sk-agents-aisearch.ipynb`.
3. Select kernel `ai-foundry-workshop (Python 3.12.1)`.
4. Execute cells sequentially to initialize client and create agents.

### Task 2: Multi-Agent RAG

1. Sign in to GitHub and Outlook to verify login.
2. Generate Personal Access Token (PAT) in GitHub → Add to `.env` as `GITHUB_TOKEN`.
3. Open `2-notebooks/4-frameworks/2-autogen-multi-agent-rag.ipynb`.
4. Execute cells to run multi-agent RAG workflow.

### Summary

* Created AI-driven fitness assistant with Azure AI Search + Semantic Kernel.
* Enabled multi-turn, context-aware, asynchronous AI conversations.
* Implemented multi-agent RAG pipeline for advanced reasoning.

---

# Conclusion

Congratulations! You have completed the **Fitness-Fun Lab**. Through these exercises, you:

* Set up Azure AI Foundry and authenticated services.
* Explored chat completions, embeddings, and RAG pipelines.
* Developed intelligent AI agents with multi-tool integration.
* Implemented observability and tracing for reliable AI operations.
* Built advanced multi-agent pipelines for reasoning and collaboration.

You are now equipped to design, deploy, and monitor intelligent AI-driven health and fitness applications using Azure AI Foundry.
 
