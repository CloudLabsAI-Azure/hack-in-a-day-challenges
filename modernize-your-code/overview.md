# Modernize Your Code with AI-Powered SQL Translation

Welcome to the Modernize Your Code Hack in a Day! In this hands-on challenge, you will build an enterprise-grade SQL modernization pipeline powered by Azure AI and multi-agent orchestration. You will learn to automatically translate legacy SQL dialects (Oracle PL/SQL) to modern cloud-native SQL (Azure SQL), validate the translations, optimize performance, and deploy the solution as a containerized application.

## Scenario

A large financial services company operates thousands of Oracle databases containing critical business logic embedded in PL/SQL stored procedures, functions, and complex queries. The organization wants to migrate to Azure SQL Database to reduce licensing costs, improve scalability, and adopt cloud-native features. However, manual translation of 5,000+ SQL objects is:

- Time-consuming (estimated 18-24 months)
- Error-prone (syntax differences, deprecated functions, semantic mismatches)
- Expensive (requires specialized Oracle and T-SQL expertise)
- Risky (breaks production pipelines if done incorrectly)

The data engineering team needs an automated, AI-powered system that can:

- Translate Oracle PL/SQL to Azure SQL T-SQL accurately
- Validate translations for syntax and semantic correctness
- Optimize queries for Azure SQL performance
- Log all transformations and errors for audit trails
- Provide a retry mechanism for failed translations
- Scale to process thousands of queries efficiently

Using Microsoft Foundry (with models such as GPT-4.1, for example), Cosmos DB, and Azure Container Apps, you will build a complete SQL modernization solution that demonstrates how AI can accelerate enterprise cloud migration at scale.

## Introduction

Your mission is to build a Multi-Agent SQL Modernization Pipeline using Microsoft Foundry Agents that automates the translation, validation, and optimization of legacy SQL code. The system consists of three specialized AI agents built using the Visual Agent Builder:

1. **SQL-Translation-Agent**: Converts Oracle PL/SQL syntax to Azure SQL T-SQL syntax using advanced AI models (for example, GPT-4.1)
2. **SQL-Validation-Agent**: Verifies syntax correctness, checks for semantic errors, and validates translated SQL
3. **SQL-Optimization-Agent**: Analyses translated SQL and suggests performance improvements for Azure SQL

The agents are connected in a pipeline using AI Foundry's "Connected agents" feature, enabling automatic hand-off from Translation to Validation to Optimization. Results are stored in Cosmos DB using built-in Actions, and a Streamlit web interface provides an intuitive front-end for users.

## Learning Objectives

By participating in this Hack in a Day, you will learn how to:

- Create a Microsoft Foundry project and deploy an advanced AI model (such as GPT-4.1)
- Build AI agents using the visual Agent builder in Microsoft Foundry
- Design multi-agent systems with connected pipeline orchestration
- Implement prompt engineering techniques for accurate SQL dialect conversion
- Configure agent hand-off for automated multi-phase processing
- Use Cosmos DB for persisting agent results automatically
- Authenticate with Azure CLI using DefaultAzureCredential
- Consume Microsoft Foundry Agent APIs from web applications
- Build interactive web interfaces with Streamlit
- Work with Cosmos DB for storing agent results and history

## Hack in a Day Format: Challenge-Based

This hands-on lab is structured into five progressive challenges:

**Challenge 1: Set Up Azure Infrastructure**  
Create a Microsoft Foundry project with GPT-4.1 deployment and Cosmos DB for storing translation history.

**Challenge 2: Build the Translation Agent**  
Create your first AI agent using the visual Agent builder in Microsoft Foundry. Configure comprehensive Oracle-to-T-SQL translation rules and test in the playground.

**Challenge 3: Build the Validation Agent and Connect Pipeline**  
Create a second agent for validation and use the "Connected agents" feature to link it to the Translation Agent, enabling automatic hand-off.

**Challenge 4: Build the Optimization Agent and Complete Pipeline**  
Create the final agent for SQL optimization and connect it to the Validation Agent, completing the three-agent pipeline with automatic orchestration.

**Challenge 5: Run the Production Streamlit Application**  
Authenticate with Azure CLI and run a pre-built Streamlit web application that calls the Translation Agent, receives results from all three connected agents, and displays them in a premium user interface with history from Cosmos DB.

Throughout each challenge, you will iteratively build, test, and enhance your SQL modernization pipeline using real Oracle SQL samples.

## Challenge Overview

You will begin by provisioning Azure resources, including Microsoft Foundry with GPT-4.1 deployment and Cosmos DB. Next, you will build three specialized AI agents using the visual Agent builder in Microsoft Foundry and connect them in a pipeline. Finally, you will authenticate with Azure CLI and run a pre-built Streamlit web application that integrates with the agent pipeline, creating a production-ready SQL modernization platform with a premium user interface.

By the end of this Hack in a Day, you will have a fully functional Multi-Agent SQL Modernization System with connected agents, automatic persistence via Cosmos DB, and an intuitive web interface.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year via email and live chat to ensure seamless assistance throughout the lab.

**Learner Support Contacts**  
- Email: cloudlabs-support@spektrasystems.com  
- Live Chat: https://cloudlabs.ai/labs-support

Click **Next** from the bottom-right corner to continue.