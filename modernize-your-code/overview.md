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

Using Azure OpenAI, Azure AI Foundry, Cosmos DB, and Azure Container Apps, you will build a complete SQL modernization solution that demonstrates how AI can accelerate enterprise cloud migration at scale.

## Introduction

Your mission is to build a Multi-Agent SQL Modernization Pipeline that automates the translation, validation, and optimization of legacy SQL code. The system consists of three specialized AI agents:

1. **Translation Agent**: Converts Oracle PL/SQL syntax to Azure SQL T-SQL syntax using GPT-4
2. **Validation Agent**: Verifies syntax correctness, checks for semantic errors, and optionally executes queries against a test database
3. **Optimization Agent**: Analyzes translated SQL and suggests performance improvements for Azure SQL

The pipeline processes SQL files uploaded to Azure Storage, orchestrates agent execution, stores results in Cosmos DB, and provides an interactive Streamlit web interface for monitoring and managing translations.

## Learning Objectives

By participating in this Hack in a Day, you will learn how to:

- Create and configure Azure OpenAI Service for SQL translation tasks
- Build an Azure AI Foundry project for orchestrating AI agents
- Design multi-agent systems with specialized roles (translation, validation, optimization)
- Implement prompt engineering techniques for accurate SQL dialect conversion
- Use Azure Cosmos DB to store translation results, logs, and error tracking
- Validate SQL syntax and semantics using hybrid AI and database execution
- Deploy AI applications to Azure Container Apps for production use
- Build interactive web interfaces with Streamlit for AI-powered tools
- Handle retries, error logging, and audit trails for enterprise workflows
- Optimize SQL queries for cloud database performance

## Hack in a Day Format: Challenge-Based

This hands-on lab is structured into six progressive challenges:

**Challenge 1: Set Up Azure Infrastructure**  
Create Azure OpenAI Service, AI Foundry project, Cosmos DB, Storage Account, and Azure SQL Database for validation testing.

**Challenge 2: Build the Translation Agent**  
Design a GPT-4 powered agent that converts Oracle PL/SQL to Azure SQL T-SQL, handling syntax differences, deprecated functions, and dialect-specific features.

**Challenge 3: Build the Validation Agent**  
Create a hybrid validation system that performs AI-based syntax checking, semantic error detection, and optional real database execution for verification.

**Challenge 4: Build the Optimization Agent**  
Implement an agent that analyzes translated SQL and provides Azure SQL specific optimization recommendations for indexes, query hints, and performance tuning.

**Challenge 5: Integrate Cosmos DB for Storage and Logging**  
Store translation results, validation logs, optimization suggestions, and error details in Cosmos DB with proper data models and retry logic.

**Challenge 6: Deploy Streamlit App and Container Apps**  
Package the solution as a containerized Streamlit application and deploy to Azure Container Apps for production-ready access.

Throughout each challenge, you will iteratively build, test, and enhance your SQL modernization pipeline using real Oracle SQL samples.

## Challenge Overview

You will begin by provisioning Azure resources including OpenAI, AI Foundry, Cosmos DB, and Azure SQL Database. Next, you will build three specialized AI agents using Python and Azure OpenAI API. Then, you will integrate Cosmos DB to persist all translation artifacts and enable audit trails. Finally, you will deploy a complete Streamlit web application to Azure Container Apps, creating a production-ready SQL modernization platform.

By the end of this Hack in a Day, you will have a fully functional Multi-Agent SQL Modernization System capable of translating thousands of Oracle queries to Azure SQL with validation, optimization, and enterprise-grade logging.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year via email and live chat to ensure seamless assistance throughout the lab.

**Learner Support Contacts**  
- Email: cloudlabs-support@spektrasystems.com  
- Live Chat: https://cloudlabs.ai/labs-support

Click **Next** from the bottom-right corner to continue.
