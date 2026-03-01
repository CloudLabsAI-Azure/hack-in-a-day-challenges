# AI-Powered Data Security & Compliance Agent

Welcome to the AI-Powered Data Security & Compliance Agent Hack in a Day! In this hands-on challenge, you will build an autonomous Data Security Agent that identifies sensitive data across multiple databases, detects risky access patterns, and recommends security controls. You will work with sample datasets and metadata to classify sensitive information, analyze permissions, and generate actionable compliance insights using Azure AI agents.

## Scenario

A large healthcare and financial services company manages multiple databases containing customer records, medical data, financial transactions, and employee information across its cloud environment. The security and compliance team is responsible for:

- Knowing where sensitive data (PII, PHI, PCI) exists across all databases
- Ensuring only authorized users access sensitive data
- Detecting suspicious access patterns and over-privileged roles
- Staying compliant with GDPR, HIPAA, and PCI-DSS regulations
- Generating remediation plans when violations are found

Currently, the team relies on manual audits that take weeks to complete and are outdated the moment they finish. They need an automated, AI-powered system that can continuously scan data assets, detect risks, and recommend fixes — with human approval for critical actions.

## Introduction

Your mission is to build a Multi-Agent Data Security Pipeline using Microsoft Foundry Agents that automates the classification, risk detection, and compliance reporting for sensitive data. The system consists of three specialized AI agents:

1. **Data-Classification-Agent**: Scans data schemas and sample rows to classify columns as PII, PHI, PCI, Confidential, or Public
2. **Risk-Detection-Agent**: Cross-references classifications with access policies and activity logs to detect over-privilege, anomalies, and compliance gaps
3. **Compliance-Advisor-Agent**: Maps risks to regulations (GDPR, HIPAA, PCI-DSS) and generates remediation playbooks with approval requirements

The agents are connected in a pipeline using AI Foundry's "Connected agents" feature, enabling automatic hand-off from Classification to Risk Detection to Compliance Advisory. Results are stored in Cosmos DB, critical alerts are published to Azure Event Grid and processed by a Logic App, and a Streamlit web dashboard provides the user interface.

## Learning Objectives

By participating in this Hack in a Day, you will learn how to:

- Create a Microsoft Foundry project and deploy an AI model
- Build AI agents using the visual Agent builder in Microsoft Foundry
- Design multi-agent systems with connected pipeline orchestration
- Work with Azure Blob Storage to store and retrieve data assets
- Configure Azure Event Grid topics for event-driven alerting
- Build Logic App workflows that process events and trigger notifications
- Use Azure Cosmos DB for persisting scan results and security alerts
- Authenticate with Azure CLI using DefaultAzureCredential
- Consume Microsoft Foundry Agent APIs from web applications
- Build interactive web interfaces with Streamlit

## Hack in a Day Format: Challenge-Based

This hands-on lab is structured into five progressive challenges:

**Challenge 1: Set Up Azure Infrastructure**  
Create a Microsoft Foundry project with GPT model deployment, Cosmos DB for storing scan results and alerts, a Storage Account for data assets, and an Event Grid Topic for alerting.

**Challenge 2: Build the Data Classification Agent**  
Create your first AI agent using the visual Agent builder in Microsoft Foundry. Configure it with instructions to classify data columns as PII, PHI, PCI, Confidential, or Public.

**Challenge 3: Build the Risk Detection Agent and Connect Pipeline**  
Create a second agent for risk detection and use the "Connected agents" feature to link it to the Classification Agent, enabling automatic hand-off.

**Challenge 4: Build the Compliance Advisor Agent and Complete Pipeline**  
Create the third agent for compliance mapping and remediation, and connect it to complete the three-agent pipeline with automatic orchestration.

**Challenge 5: Configure Event Grid, Logic App, and Run the Dashboard**  
Set up the Logic App to process Event Grid alerts, configure the Streamlit application with your Azure credentials, and run the complete end-to-end security scanning pipeline.

Throughout each challenge, you will iteratively build, test, and enhance your Data Security Agent using real sample datasets.

## Challenge Overview

You will begin by provisioning Azure resources, including Microsoft Foundry with GPT model deployment, Cosmos DB, a Storage Account, and an Event Grid Topic. Next, you will build three specialized AI agents using the visual Agent builder in Microsoft Foundry and connect them in a pipeline. Finally, you will configure a Logic App for alert processing, set up the Streamlit application, and run the complete security scanning system.

By the end of this Hack in a Day, you will have a fully functional AI-Powered Data Security & Compliance Agent with connected agents, event-driven alerting, and an interactive web dashboard.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year via email and live chat to ensure seamless assistance throughout the lab.

**Learner Support Contacts**  
- Email: cloudlabs-support@spektrasystems.com  
- Live Chat: https://cloudlabs.ai/labs-support

Click **Next** from the bottom-right corner to continue.
