# Intelligent Content Processing: AI-Powered Document Pipeline

## Overview

Every day, enterprises process thousands of documents — invoices from vendors, insurance claims, medical forms, receipts, and identity documents. At **Contoso Enterprises**, a diversified conglomerate spanning finance, healthcare, and insurance, this manual document processing bottleneck costs **$2.4 million annually** in labor and delays critical business decisions by an average of 72 hours.

Your mission: **Build an AI-powered document processing pipeline** that automatically ingests documents, extracts text using Azure AI Document Intelligence, classifies and extracts structured data using a multi-agent AI pipeline, and intelligently routes results based on confidence scoring — high-confidence documents are auto-approved, while low-confidence documents are flagged for human review.

## Architecture

```
┌──────────────┐     ┌─────────────────────┐     ┌──────────────────────────────────┐
│  Document     │     │  Azure AI Document  │     │  Azure AI Foundry Agent Pipeline │
│  Upload       │────▶│  Intelligence       │────▶│                                  │
│  (Blob Store) │     │  (OCR + Layout)     │     │  Classification Agent            │
└──────────────┘     └─────────────────────┘     │       ↓ (connected)              │
                                                  │  Extraction Agent                │
                                                  │       ↓ (connected)              │
                                                  │  Validation Agent                │
                                                  └──────────┬───────────────────────┘
                                                             │
                                                    ┌────────┴────────┐
                                                    │  Smart Router   │
                                                    └───┬─────────┬───┘
                                                        │         │
                                            ┌───────────▼──┐  ┌──▼──────────────┐
                                            │ Auto-Approved │  │  Review Queue   │
                                            │ (Cosmos DB)   │  │  (Cosmos DB)    │
                                            │ confidence    │  │  confidence     │
                                            │ ≥ 0.85       │  │  < 0.85        │
                                            └──────────────┘  └─────────────────┘
                                                        │         │
                                                    ┌───▼─────────▼───┐
                                                    │   Streamlit     │
                                                    │   Dashboard     │
                                                    │   (Upload,      │
                                                    │    Review,      │
                                                    │    Analytics)   │
                                                    └─────────────────┘
```

## Key Azure Services

| Service | Purpose |
|---------|---------|
| **Azure Blob Storage** | Document ingestion and storage |
| **Azure AI Document Intelligence** | OCR extraction — text, tables, key-value pairs from PDFs, images, scans |
| **Microsoft Foundry (Azure AI Foundry)** | Multi-agent AI pipeline — classification, extraction, validation |
| **Azure Cosmos DB (NoSQL)** | Dual-container persistence — auto-approved results + human review queue |
| **Streamlit** | Interactive dashboard for upload, review, and analytics |

## Challenges

| Challenge | Title | Duration | Description |
|-----------|-------|----------|-------------|
| **1** | Set Up Azure Infrastructure | ~40 min | Provision Storage Account, Document Intelligence, AI Foundry project (GPT-4.1), and Cosmos DB with dual containers. Upload sample documents and test OCR extraction. |
| **2** | Build the Document Classification Agent | ~40 min | Create a classification agent in Azure AI Foundry that identifies document types (invoice, receipt, medical form, insurance claim, ID) from OCR text and returns structured JSON. |
| **3** | Build Extraction & Validation Agents + Connect Pipeline | ~60 min | Create extraction and validation agents. Connect all three agents using Foundry's connected agents feature for automatic hand-off. Test the full pipeline. |
| **4** | Run the Content Processing Application | ~50 min | Configure and run the pre-built Streamlit application. Upload documents, watch the pipeline process them, and verify smart routing to the correct Cosmos DB container. |
| **5** | Review Queue & End-to-End Validation | ~30 min | Use the dashboard's Review tab to approve or reject low-confidence documents. Process all sample documents end-to-end. Explore the analytics dashboard. Tackle bonus challenges. |

## Learning Objectives

By completing this hackathon, you will:

- **Provision and configure** Azure AI services for enterprise document processing
- **Use Azure AI Document Intelligence** to extract text, tables, and key-value pairs from diverse document types
- **Design and build AI agents** in Microsoft Foundry with domain-specific prompt engineering
- **Orchestrate multi-agent pipelines** using Foundry's connected agents for automatic hand-off
- **Implement confidence-based routing** to separate auto-approved results from documents requiring human review
- **Build a production-grade dashboard** with document upload, real-time processing, review queues, and analytics
- **Integrate Azure Cosmos DB** for dual-container persistence with partition strategies

## Prerequisites

- Basic familiarity with the Azure portal
- Understanding of AI/ML concepts (no deep expertise required)
- Basic Python knowledge (helpful but not mandatory — code is pre-built)
- Curiosity and willingness to experiment!

## Hackathon Format

This is a **challenge-based hackathon** — each challenge gives you objectives and success criteria, with guided steps to help you along the way. You'll build progressively, starting from infrastructure setup and ending with a fully functional, demo-able document processing pipeline.

**Duration:** ~4–6 hours (depending on experience level)

Click **Next** to set up your lab environment.
