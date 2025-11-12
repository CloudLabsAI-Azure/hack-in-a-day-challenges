# Challenge: Call Center Data Analysis using Azure AI Services and Azure OpenAI

**Estimated Time:** 4 Hours  

**Industry Focus:** Customer Service / BPO Operations

## Problem Statement
Thousands of calls contain sentiment, intents, and action items but stay locked in raw audio/transcripts. Manual review is slow, inconsistent, and not privacy-safe; there's no unified pipeline for transcription, enrichment (summaries/PII), and near-real-time reporting.

In this challenge, you will build an **end-to-end analytics workflow** using Azure AI Speech for transcription; enrich with Azure OpenAI (summaries, intents, action items) and Azure AI Language (sentiment, key phrases, PII redaction); orchestrate via Azure Functions + Storage; persist to Azure SQL Database; visualize KPIs and trends in Power BI dashboards (with refresh when new calls arrive).

## Goals
By the end of this challenge, you will deliver a **working pipeline that transcribes sample calls, writes enriched outputs to SQL, and surfaces sentiment trends, topics, and summaries in a published Power BI report/dashboard; new uploads auto-flow through to refreshed visuals** including:

- Configure ingestion for live/recorded calls and generate accurate transcripts
- Enrich conversations with summaries/intents/action items and sentiment/key phrases/PII
- Design real-time vs post-call pipelines
- Persist insights to SQL
- Build a Power BI dashboard with CSAT proxies, sentiment trends, agent coaching cues
- Iterate prompts/thresholds

## Prerequisites
- **Skill Level:** Basic familiarity with Azure Functions/Storage/SQL
- **Audience:** Contact center ops & QA leads, BI/analytics teams, data engineers
- **Technology Stack:** Azure AI Speech, Azure OpenAI Service, Azure AI Language, Azure Functions, Azure Storage, Azure SQL Database, Power BI Desktop/Service, Azure Monitor & Event Grid

## Datasets
Use the following sample datasets provided in lab files:

- **Sample Call Recordings:** Real-world customer service scenarios including complaints, inquiries, and positive feedback
- **Power BI Template:** Pre-configured dashboard with models and visualizations for call center analytics
- **ARM Templates:** Infrastructure-as-code for rapid Azure resource deployment

Ensure all datasets are stored in your local directory: `C:\LabFiles\CallCenter`

| File Path | Description |
|-----------|-------------|
| `C:\LabFiles\Recordings\bad_review.wav` | Customer complaint scenario |
| `C:\LabFiles\Recordings\Call_pharmacy_call.wav` | Pharmacy inquiry call |
| `C:\LabFiles\Recordings\Call_apply_loan.wav` | Loan application process |
| `C:\LabFiles\Recordings\Call_health_insurance.wav` | Health insurance consultation |
| `C:\LabFiles\Recordings\good_review.wav` | Positive customer feedback |
| `C:\LabFiles\callcenter-dataanalysis.pbix` | Pre-built Power BI report template |

## Challenge Objectives

### **Challenge 1: Foundation - Deploy Azure AI Infrastructure**
**Estimated Duration:** 60 Minutes

#### Objective
Establish the foundational Azure AI services and data infrastructure for call center analytics pipeline.

#### Tasks
1. **Deploy Azure AI Services Infrastructure:**
   - Use ARM template (`azuredeploy-01.json`) to provision integrated AI services
   - Configure Azure AI Speech for real-time transcription capabilities
   - Set up Azure OpenAI Service with GPT models for conversation analysis
   - Deploy Azure AI Language for sentiment analysis and PII detection

2. **Configure Data Pipeline Architecture:**
   - Deploy Azure Functions for serverless orchestration and event processing
   - Set up Azure Storage for audio file ingestion and JSON transcript output
   - Provision Azure SQL Database for structured insights storage
   - Configure Azure Monitor and Event Grid for pipeline monitoring

3. **Initialize Database Schema:**
   - Create `dbo.Output` table with proper schema for call analytics
   - Set up indexes for optimal query performance
   - Configure connection strings and security settings
   - Verify database connectivity and permissions

4. **Validate Infrastructure Readiness:**
   - Test ARM deployment completion and resource provisioning
   - Verify Azure Functions are operational and properly configured
   - Confirm database schema creation and connectivity
   - Check Azure AI service endpoints and API key configuration

#### Validation Check
- ARM deployment completed successfully with all Azure AI services operational
- Azure SQL Database contains properly structured `dbo.Output` table with required schema
- Azure Functions are running and ready for event-driven processing
- Storage containers are configured for audio input and JSON transcript output
- All service connections and permissions are properly established

### **Challenge 2: Data Ingestion - Process Call Recordings with AI Pipeline**
**Estimated Duration:** 75 Minutes

#### Objective
Implement end-to-end call processing pipeline with Azure AI Speech transcription, Azure OpenAI enrichment, and Azure AI Language analysis.

#### Tasks
1. **Configure Serverless Processing Pipeline:**
   - Restart and validate Azure Functions: `StartTranscriptionFunction`, `FetchTranscriptionFunction`, `AnalyzeTranscriptionFunction`
   - Test event-driven architecture with storage blob triggers
   - Configure function app settings and environment variables
   - Verify Azure AI service integrations and API connections

2. **Process Sample Call Recordings:**
   - Upload audio files to `audio-input` container to trigger processing pipeline
   - Process customer complaint scenario (`bad_review.wav`)
   - Handle pharmacy inquiry consultation (`Call_pharmacy_call.wav`) 
   - Analyze loan application conversation (`Call_apply_loan.wav`)
   - Monitor real-time processing through Azure Functions logs

3. **Implement AI-Powered Call Analysis:**
   - **Transcription:** Convert audio to accurate text using Azure AI Speech
   - **Summarization:** Generate concise call summaries using Azure OpenAI GPT models
   - **Intent Recognition:** Extract customer intents and action items with GPT analysis
   - **Sentiment Analysis:** Analyze emotional tone using Azure AI Language
   - **PII Detection:** Identify and redact sensitive information for privacy compliance
   - **Key Phrase Extraction:** Surface important topics and themes from conversations

4. **Validate Processing Pipeline:**
   - Monitor JSON transcript generation in `json-result-output` container
   - Verify enriched data contains summaries, sentiment scores, and extracted insights
   - Check Azure SQL Database for populated analysis results
   - Test error handling and retry mechanisms for failed processing

#### Validation Check
- All Azure Functions are operational and processing audio files successfully
- JSON transcripts with enriched AI analysis appear in output storage container
- Azure SQL Database contains structured call insights with sentiment, summaries, and metadata
- Processing pipeline handles various call types and scenarios accurately
- PII redaction and privacy controls are functioning correctly

### **Challenge 3: Analytics & Visualization - Build Call Center Intelligence Dashboard**
**Estimated Duration:** 105 Minutes

#### Objective
Create comprehensive Power BI dashboards with real-time call center KPIs, sentiment trends, and agent coaching insights that automatically refresh with new call data.

#### Tasks
1. **Configure Power BI Data Integration:**
   - Connect Power BI Desktop to Azure SQL Database with call analytics data
   - Configure secure authentication using SQL credentials and gateway settings
   - Set up automatic data refresh schedules for near-real-time dashboard updates
   - Optimize data model relationships and performance for large call volumes

2. **Build Call Center KPI Dashboard:**
   - **Customer Satisfaction Metrics:** CSAT proxy scores derived from sentiment analysis
   - **Sentiment Distribution:** Visual breakdown of positive, negative, and neutral calls
   - **Topic Analysis:** Word clouds and trend charts of key phrases and call themes  
   - **Agent Performance:** Individual agent coaching cues based on call outcomes
   - **Volume Metrics:** Call volume trends by hour, day, and call type
   - **Response Time Analysis:** Average handling time and resolution metrics

3. **Implement Advanced Analytics Features:**
   - **Sentiment Trend Analysis:** Time-series visualization of sentiment patterns
   - **Intent Classification Dashboard:** Visual breakdown of customer intent categories
   - **Action Item Tracking:** Summary of follow-up actions identified by AI analysis
   - **PII Compliance Monitoring:** Dashboard showing redaction effectiveness and privacy metrics
   - **Call Quality Scoring:** Automated quality assessments based on AI analysis

4. **Deploy and Test Real-Time Updates:**
   - Publish dashboard to Power BI Service with appropriate sharing permissions
   - Configure automatic refresh triggers when new calls are processed
   - Test end-to-end pipeline: upload new audio → process with AI → refresh dashboard
   - Validate dashboard responsiveness and data accuracy with new call samples
   - Set up alerts for significant sentiment changes or quality issues

5. **Optimize for Operational Use:**
   - Configure role-based access control for different user types (managers, agents, QA)
   - Set up scheduled email reports for key stakeholders
   - Implement drill-down capabilities for detailed call analysis
   - Create mobile-optimized views for on-the-go monitoring

#### Validation Check
- Power BI report successfully connects to Azure SQL Database with proper authentication
- Dashboard displays accurate call center KPIs including sentiment trends and agent metrics
- Real-time refresh functionality works when new audio files are uploaded and processed
- All visualizations respond correctly to filters and show meaningful business insights
- Published dashboard is accessible to stakeholders with appropriate permissions and security

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

A **working pipeline that transcribes sample calls, writes enriched outputs to SQL, and surfaces sentiment trends, topics, and summaries in a published Power BI report/dashboard; new uploads auto-flow through to refreshed visuals**.

### **Technical Deliverables:**
- **Infrastructure:** Azure AI services properly deployed and configured for call center analytics
- **Data Processing:** Audio transcription pipeline operational with consistent quality and accuracy
- **AI Enrichment:** Conversation analysis producing summaries, sentiment scores, intents, and PII redaction
- **Data Persistence:** Structured insights stored in Azure SQL Database with proper schema and indexing
- **Visualization:** Interactive Power BI dashboard with real-time call center KPIs and trends
- **Automation:** End-to-end pipeline with automatic processing and dashboard refresh capabilities
- **Compliance:** PII detection and redaction working correctly for privacy protection

### **Business Outcomes:**
- **Instant Insights:** Real-time visibility into customer sentiment and call quality metrics
- **Agent Coaching:** Data-driven coaching cues and performance metrics for continuous improvement
- **Quality Assurance:** Automated call quality scoring and compliance monitoring
- **Operational Efficiency:** Reduced manual review time with AI-powered call analysis and summarization

## Additional Resources
- [Azure AI Speech Service Documentation](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Language Documentation](https://learn.microsoft.com/azure/ai-services/language-service/)
- [Azure Functions Documentation](https://learn.microsoft.com/azure/azure-functions/)
- [Azure SQL Database Documentation](https://learn.microsoft.com/azure/azure-sql/)
- [Power BI Documentation](https://learn.microsoft.com/power-bi/)

## Conclusion
By completing this challenge, you will have built an **end-to-end AI-powered call center analytics pipeline** using Azure AI services.

You learned how to:
- Deploy and configure Azure AI Speech, OpenAI, and Language services for call analysis
- Build serverless processing pipelines using Azure Functions and Storage
- Implement privacy-safe AI analysis with PII detection and redaction
- Create real-time Power BI dashboards with automated refresh capabilities

This solution demonstrates how Azure AI services enable **intelligent call center operations** through automated transcription, sentiment analysis, and actionable business insights.