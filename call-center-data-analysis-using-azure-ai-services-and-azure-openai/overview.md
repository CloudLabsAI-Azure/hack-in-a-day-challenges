# Call Center Data Analysis using Azure AI services and Azure OpenAI

Welcome to the Copilot Hackathon! Today, you’ll extract actionable insights from customer conversations using Azure AI services and Azure OpenAI. You’ll apply both real-time and post-call analytics—covering transcription, sentiment analysis, and visual reporting—to boost call center efficiency and customer satisfaction.

## Introduction
Your quest is to build an analytics workflow for call center data that turns raw audio and transcripts into insights. You’ll use Azure AI Speech for transcription, Azure OpenAI for summarization and intent/action-item extraction, and Azure AI Language for sentiment, key phrases, and PII redaction—then surface findings via dashboards for supervisors and QA teams.

![Architecture](images/archdiag.png)

## Learning Objectives
By participating in this hackathon, you will learn how to:
- Configure ingestion for live and recorded calls; generate high-accuracy transcripts with Azure AI Speech.
- Enrich conversations using Azure OpenAI (summaries, topics, intents, action items) and Azure AI Language (sentiment, key phrases, PII redaction).
- Orchestrate real-time vs. post-call pipelines and persist insights for analytics.
- Visualize KPIs (CSAT proxies, sentiment trends, agent coaching cues) in a lightweight dashboard.

## Hackathon Format: Challenge-Based
This hackathon adopts a challenge-based format to learn by solving a practical problem:
- Analyzing the problem statement.  
- Strategizing your approach to find the most effective solution.  
- Leveraging the provided lab environment and Azure AI services.

## Challenge Overview
Begin by setting up Azure AI Speech for transcription and storage for call artifacts. Build an enrichment pipeline that uses Azure OpenAI for conversation summaries and intent/action-item extraction, plus Azure AI Language for sentiment and key-phrase analysis with PII redaction. For real-time scenarios, emit interim insights (e.g., live sentiment) to a store/stream; for post-call, batch-process recordings to compute call-level metrics. Finally, wire a simple dashboard to visualize trends (sentiment over time, agent-level insights, topic hotspots) and iterate on prompts and thresholds to improve accuracy and usefulness.

**Happy Hacking!!**
