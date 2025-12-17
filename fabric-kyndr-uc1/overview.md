# Data Analysis with Generative AI (GenAI)

Welcome to the Data Analysis with Generative AI Hack in a Day! Today, you'll explore how AI can transform manufacturing data analysis by building an intelligent assistant that analyzes machine logs, detects patterns, and generates natural-language insights from operational data. Through this hands-on lab, you will create a Manufacturing Data Analysis Assistant capable of querying production data conversationally, identifying trends, and producing actionable recommendations, powered by Microsoft Foundry (Azure OpenAI), Azure AI Search, and Streamlit.

## Scenario

Contoso Manufacturing operates a network of machines across multiple plants. Each machine logs temperature, vibration, status, and downtime events continuously. Operations engineers need to analyze this data to identify performance trends, detect anomalies, and troubleshoot issues, but high data volume and complexity make manual analysis time-consuming and error-prone. To improve efficiency and insight generation, Contoso decides to build a Data Analysis Assistant that can analyze machine logs using Generative AI, answer natural-language queries, and generate automated insights. This allows engineers to ask questions like "Which machine had the most downtime?" or "Temperature of MACHINE_001" and receive instant AI-generated answers based on actual production data.

## Introduction

Your mission is to build an AI-powered **Manufacturing Data Analysis Assistant** that supports operations teams by analyzing machine data and generating conversational insights. Using Microsoft Foundry (Azure OpenAI), Azure AI Search, Azure Blob Storage, and Streamlit, you will design an end-to-end solution that can:

- Ingest and store manufacturing data (machine logs, temperature, vibration, status) in Azure Blob Storage
- Index data using Azure AI Search with vectorization for semantic search capabilities
- Deploy gpt-4.1-mini and text-embedding-ada-002 models for natural-language analysis
- Implement Retrieval-Augmented Generation (RAG) to ground AI responses in actual production data
- Build a Streamlit chat interface for querying data conversationally

This solution reduces manual data analysis time, enables conversational data exploration, and allows operations engineers to focus on decision-making rather than repetitive data queries.

## Learning Objectives

By participating in this Hack in a Day, you will learn how to:

- Upload and prepare manufacturing datasets in Azure Blob Storage for AI analysis
- Deploy Microsoft Foundry with gpt-4.1-mini and text-embedding-ada-002 models
- Create Azure AI Search indexes with vectorization for semantic search
- Implement Retrieval-Augmented Generation (RAG) to connect LLMs with manufacturing data
- Use Microsoft Foundry Studio playground to test AI-driven data queries
- Configure and run a Streamlit application for conversational data analysis

## Hack in a Day Format: Challenge-Based

This hands-on lab is structured into five progressive challenges that model the lifecycle of building a real-world AI-powered data analysis application:

- **Challenge 01: Create and Review the Sample Manufacturing Dataset**  
  Create an Azure Storage Account, upload synthetic manufacturing data to a blob container, and explore the dataset structure.

- **Challenge 02: Deploy Azure OpenAI Service**
  Create a Microsoft Foundry resource, deploy the gpt-4.1-mini model (20K TPM), and deploy the text-embedding-ada-002 model (30K TPM) for semantic search.

- **Challenge 03: Create Azure AI Search Resource and Import Manufacturing Data**  
  Create an Azure AI Search service, import data from Blob Storage, configure RAG, vectorize data using embeddings, and test search queries.

- **Challenge 04: Analyze Data Using GenAI Prompts**  
  Use Microsoft Foundry Studio playground to connect Azure AI Search as a data source and test prompts like "Temperature of MACHINE_001" to generate AI-driven insights.

- **Challenge 05: Configure the Application and Run the Manufacturing Data Analysis Assistant**  
  Configure environment variables, install Python dependencies, and run the Streamlit application to query manufacturing data conversationally.

Throughout each challenge, you will iteratively design, build, and test your Data Analysis Assistant, from data preparation to model deployment and application integration.

## Challenge Overview

You will begin by provisioning Azure Storage and uploading manufacturing machine logs with temperature, vibration, and status data. Next, you will deploy Microsoft Foundry with gpt-4.1-mini and text-embedding-ada-002 models for natural-language analysis and semantic search. You will then create an Azure AI Search index with vectorization to enable Retrieval-Augmented Generation. After that, you will test AI prompts in Foundry Studio to query data and generate insights. Finally, you will configure and run a Streamlit chat application to interact with your manufacturing data conversationally, asking questions and receiving AI-generated answers.

By the end of this Hack in a Day, you will have a fully functional **Manufacturing Data Analysis Assistant** that can answer natural-language queries about production data, detect patterns, and support faster operational decision-making on the factory floor.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year via email and live chat to ensure seamless assistance throughout the lab. Dedicated support channels are available for both learners and instructors.

**Learner Support Contacts**  
- Email: cloudlabs-support@spektrasystems.com  
- Live Chat: https://cloudlabs.ai/labs-support

Click **Next** from the bottom-right corner to continue.