# AI-Powered Data Security & Compliance Agent

Streamlit dashboard for autonomous data security scanning, risk detection, and compliance reporting.

## Features

- **Sensitive Data Classification** — Scans schemas and sample data to identify PII, PHI, PCI, and confidential information
- **Risk Detection** — Cross-references access policies and activity logs to find over-privilege, anomalies, and compliance gaps
- **Compliance Remediation** — Generates fix plans mapped to GDPR, HIPAA, PCI-DSS with approval workflows
- **Event-Driven Alerts** — Publishes critical risks to Azure Event Grid, processed by Logic App
- **Scan History** — Stores all results in Cosmos DB for audit trail
- **Fast / Full Scan** — Choose between quick sample scan or comprehensive analysis

## Quick Start

### Prerequisites

- Python 3.11+
- Azure CLI installed and authenticated
- Azure AI Foundry project with agents configured
- Azure Cosmos DB, Storage Account, Event Grid Topic, Logic App

### Setup

```bash
# Copy and edit environment config
copy .env.example .env

# Authenticate with Azure
az login

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

### Environment Variables

| Variable | Source | Required |
|---|---|---|
| `AGENT_API_ENDPOINT` | AI Foundry Portal > Project > Overview | Yes |
| `AGENT_ID` | AI Foundry Portal > Agents > Setup panel | Yes |
| `COSMOS_ENDPOINT` | Azure Portal > Cosmos DB > Keys | Yes |
| `COSMOS_KEY` | Azure Portal > Cosmos DB > Keys | Yes |
| `STORAGE_ACCOUNT_NAME` | Azure Portal > Storage Account | Yes |
| `STORAGE_ACCOUNT_KEY` | Azure Portal > Storage Account > Access Keys | Yes |
| `EVENT_GRID_ENDPOINT` | Azure Portal > Event Grid Topic > Overview | Yes |
| `EVENT_GRID_KEY` | Azure Portal > Event Grid Topic > Access Keys | Yes |

## Architecture

```
User → Streamlit App → Classification Agent → Risk Agent → Compliance Agent
                                                                    ↓
                                        Event Grid Topic ← CRITICAL/HIGH risks
                                              ↓
                                          Logic App
                                         ↓         ↓
                                    Cosmos DB    Email/Teams
```

## File Structure

```
codefiles/
├── app.py                 # Streamlit dashboard
├── cosmos_helper.py       # Cosmos DB operations
├── storage_helper.py      # Azure Blob Storage operations
├── event_grid_helper.py   # Event Grid publishing
├── requirements.txt
├── .env / .env.example
├── Dockerfile
└── datasets/
    ├── customer_data.json
    ├── medical_records.json
    ├── financial_transactions.json
    ├── employee_data.json
    ├── access_policies.json
    └── access_logs.csv
```
