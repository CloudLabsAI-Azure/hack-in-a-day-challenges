# Challenge: Financial Insight & Risk Advisor Agent

**Estimated Time:** 4 Hours  

**Industry Focus:** Financial Services, Corporate Finance, FP&A, Risk Management  

## Problem Statement

Financial analysts spend days reviewing reports and identifying potential anomalies or risks manually. This process is slow and often subjective, increasing the chance of missed early-warning indicators in areas such as revenue trends, expense spikes, or liquidity risks.

In this challenge, you will build an **autonomous financial risk advisor agent** that ingests financial reports (PDF/Excel) via Azure Document Intelligence, summarizes key trends, and flags anomalies using reasoning prompts in Azure AI Foundry. The agent will decide when to trigger alerts or generate summaries for CFO or finance leadership review.

## Goals

By the end of this challenge, you will deliver an **AI-driven finance insight agent** capable of:

- Ingesting financial reports and extracting structured data.  
- Summarizing financial performance and identifying unusual patterns.  
- Automatically generating risk-focused narratives and recommendations.  
- Triggering alerts or distributing summaries to finance stakeholders.  

## Expected Outcomes

You will have:

- AI-generated finance summaries and anomaly detection reports.  
- Automated insight generation using AI reasoning.  
- Reduced manual analysis time for recurring financial cycles.  
- Validated explainability and traceability of AI predictions and flags.

## Prerequisites

- **Skill Level:** Familiarity with finance data (P&L, balance sheet, cash flow) and Power BI basics.  
- **Audience:** Financial analysts, FP&A teams, data analysts, and solution architects.  
- **Technology Stack:**  
  - Azure AI Foundry / Azure OpenAI  
  - Azure Document Intelligence  
  - Power Automate  
  - Power BI  
  - Azure Storage / data services (for input and processed data)

## Learning Objectives

By completing this challenge, you will:

- Use Azure AI Foundry to chain document ingestion → reasoning → alerting.  
- Build agents that evaluate confidence scores and act autonomously.  
- Create natural-language summaries and recommendations for finance leaders.  
- Implement explainability and traceability in AI outputs.

## Datasets

Use the following sample assets provided in the lab files:

- **Financial Reports:** A set of quarterly or monthly financial statements in PDF/Excel format (e.g., revenue, expenses, profit/loss, balance sheet, cash flow).  
- **Reference Data:** Mapping tables or metadata (such as account hierarchies, cost center mappings) in CSV or Excel for better grouping and analysis.  
- **Risk Rules / Thresholds:** A simple configuration file (JSON/CSV) defining thresholds and rules (e.g., “Expense growth > 20% quarter-on-quarter” or “Gross margin drop > 5%”).

Ensure all datasets are stored under your local lab path (for example):  
`C:\LabFiles\FinancialRiskAdvisor`

## Challenge Objectives

### **Challenge 1: Foundation – Set Up Environment and Financial Data**

**Estimated Duration:** 45 Minutes  

#### Objective

Establish the foundational components for the Financial Insight & Risk Advisor Agent, including AI resources, data storage, and sample financial documents.

#### Tasks

1. Create or validate access to:
   - Azure AI Foundry / Azure OpenAI resource.
   - Azure Storage (or equivalent) for uploading financial reports.
2. Upload sample financial reports (PDF/Excel) to your chosen storage location.
3. Prepare or review reference data (account mapping, cost centers) and risk rule configuration files.
4. Define a basic schema for:
   - **ExtractedFinancials**: Period, Account, CostCenter, Amount, Currency.
   - **RiskRules**: RuleName, Metric, Condition, Threshold, Severity.
5. Confirm that your environment can read these inputs from storage.

#### Validation Check

- Azure AI and storage resources are accessible.  
- Sample financial reports and reference data are available in storage.  
- Basic schemas for extracted financials and risk rules are defined and understood.

---

### **Challenge 2: Document Intelligence – Ingest and Extract Financial Data**

**Estimated Duration:** 60 Minutes  

#### Objective

Ingest financial reports using Azure Document Intelligence and transform them into structured, analysis-ready data.

#### Tasks

1. Create a **Document Intelligence** resource or confirm access to an existing one.
2. Build or configure a model/workflow to:
   - Ingest PDFs/Excel financial reports.
   - Extract key fields such as revenue, expenses, profit, balance sheet line items, and dates.
3. Map extracted entities into your **ExtractedFinancials** schema.
4. Store the extracted data in a structured format (e.g., table, CSV, or a database) that Power BI and the agent can consume.
5. Test on multiple sample reports to ensure consistent extraction quality.

#### Validation Check

- Document Intelligence successfully processes PDFs/Excel reports.  
- Extracted data is mapped into the ExtractedFinancials structure.  
- Sample records show correct period, account, and amount values.

---

### **Challenge 3: Reasoning & Risk Analysis – Build the AI Advisor**

**Estimated Duration:** 60 Minutes  

#### Objective

Use Azure AI Foundry and Azure OpenAI to summarize financial performance, detect anomalies, and generate risk-aware narratives.

#### Tasks

1. In Azure AI Foundry, define a **Finance Insight Agent** with:
   - A system prompt describing its role as a financial risk and insight advisor.
   - Instructions to use extracted financial data and risk rules rather than guessing.
2. Implement a reasoning flow that:
   - Reads the latest ExtractedFinancials and RiskRules.
   - Calculates key metrics (growth rates, margins, variance vs prior period/plan).
   - Identifies anomalies using the risk rules and basic statistical checks.
3. Configure the agent to:
   - Generate structured outputs (e.g., JSON) listing detected anomalies with severity and evidence.
   - Produce natural-language **executive summaries** highlighting trends, risks, and recommendations.
4. Introduce **confidence and explainability**:
   - Include brief explanations of why each anomaly was flagged.
   - Identify data points and rules that triggered each risk.
5. Test the agent with at least two different reporting periods and compare outputs.

#### Validation Check

- Agent can successfully summarize financial performance for a given period.  
- Anomalies are detected according to the defined rules and metrics.  
- Outputs include clear explanations and evidence for flagged risks.

---

### **Challenge 4: Visualization & Alerting – Power BI and Automated Notifications**

**Estimated Duration:** 45 Minutes  

#### Objective

Visualize financial trends and risks in Power BI, and configure automated alerts and summary delivery through Power Automate.

#### Tasks

1. Create a **Power BI report** that:
   - Connects to the ExtractedFinancials dataset.
   - Shows key visuals such as revenue and expense trends, margin analysis, and variance charts.
   - Highlights risk flags or anomaly counts per period.
2. Integrate the AI agent outputs:
   - Surface anomaly summaries and risk scores in Power BI (e.g., via a table or card visual).
   - Optionally add a narrative visual or text box for CFO-ready summaries.
3. Build a **Power Automate flow** that:
   - Triggers when a new period’s analysis completes or when high-severity anomalies are detected.
   - Sends an email or Teams notification to finance stakeholders with:
     - Key metrics.
     - A link to the Power BI report.
     - The AI-generated executive summary.
4. Validate **traceability**:
   - Ensure that from any alert or summary, users can trace back to the underlying data and rules.
5. Run an end-to-end scenario:
   - Upload a new financial report.
   - Run extraction and AI reasoning.
   - Refresh Power BI.
   - Verify alerts and summary delivery.

#### Validation Check

- Power BI report accurately reflects financial trends and risk indicators.  
- AI-generated summaries and anomaly details appear in the report or in notifications.  
- Alerts fire correctly when thresholds are exceeded.  
- Users can trace from high-level alerts down to detailed data and rules.

---

## Success Criteria

**You will have successfully completed this challenge when you deliver:**

A **Financial Insight & Risk Advisor Agent** that can:

- Ingest and extract financial report data via Document Intelligence.  
- Analyze metrics, apply risk rules, and detect anomalies.  
- Generate executive-ready summaries and recommendations.  
- Trigger alerts and share insights through Power BI and Power Automate.

### Technical Deliverables

- **Foundation:** Azure AI Foundry/OpenAI, Document Intelligence, storage, and sample financial data configured.  
- **Extraction:** Robust extraction of key financial fields into structured datasets.  
- **Reasoning:** An AI agent that performs reasoning, anomaly detection, and summary generation.  
- **Visualization:** Power BI report with financial trends, risk indicators, and AI outputs.  
- **Automation:** Power Automate flow delivering alerts and summaries to stakeholders.  
- **Explainability:** Clear traceability from AI insights back to underlying data and rules.

### Business Outcomes

- **Faster Analysis:** Reduced manual review time for recurring financial reporting cycles.  
- **Earlier Detection:** Improved ability to catch anomalies and risks earlier.  
- **Consistent Insights:** Standardized narratives and risk assessments across periods.  
- **Decision Support:** CFOs and finance leaders receive timely, data-backed summaries.

## Additional Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)  
- [Azure Document Intelligence Documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/)  
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)  
- [Power BI Documentation](https://learn.microsoft.com/power-bi/)  
- [Power Automate Documentation](https://learn.microsoft.com/power-automate/)  

## Conclusion

By completing this challenge, you have built an **end-to-end Financial Insight & Risk Advisor Agent** on the Microsoft cloud.

You learned how to:

- Ingest and extract financial data from documents using Azure Document Intelligence.  
- Use Azure AI Foundry and Azure OpenAI to reason over financial metrics and detect anomalies.  
- Present insights and risks to stakeholders through Power BI.  
- Automate notifications and summary delivery with Power Automate while maintaining explainability.

This lab demonstrates how AI can enhance financial analysis by enabling **faster, more consistent, and more transparent insight generation and risk detection**.