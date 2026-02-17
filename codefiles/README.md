# SQL Modernization Platform

Production-ready web application for Oracle to Azure SQL migration using Azure AI Foundry multi-agent system.

## Features

- **AI-Powered Translation** - Convert Oracle SQL to Azure SQL T-SQL automatically
- **Multi-Agent Pipeline** - Translation → Validation → Optimization
- **File Upload Support** - Process `.sql` and `.txt` files
- **Real-time Progress** - Visual feedback during processing
- **History Tracking** - Save and review past translations (requires Cosmos DB)
- **Sample Queries** - Pre-built Oracle SQL examples to get started
- **Modern UI** - Clean, responsive design with gradient styling
- **Setup Wizard** - Guided configuration if env vars are missing

## Quick Start

### Prerequisites

- Python 3.11 or higher
- Azure CLI installed and authenticated
- Azure AI Foundry project with agents configured
- (Optional) Azure Cosmos DB for history persistence

### Step 1: Configure Environment

Copy the example environment file and edit with your credentials:

```bash
cp .env.example .env
```

Edit `.env`:
```env
# Required - Azure AI Foundry
AGENT_API_ENDPOINT=https://your-resource.services.ai.azure.com/api/projects/proj-default
AGENT_ID=asst_your_agent_id

# Optional - Cosmos DB (for history feature)
COSMOS_ENDPOINT=https://your-cosmos.documents.azure.com:443/
COSMOS_KEY=your-cosmos-primary-key
DATABASE_NAME=SQLModernizationDB
```

> **Note:** Authentication uses Azure CLI (`az login`), not API keys.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Authenticate with Azure

```bash
az login
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`

## Usage

### Translating SQL

1. **Upload a file**: Click the file upload area and select a `.sql` file
2. **Or paste directly**: Enter Oracle SQL in the text area
3. **Or use samples**: Select a sample query from the dropdown
4. Click **"Modernize SQL"**

### Viewing Results

After processing, you'll see three columns:

| Column | Description |
|--------|-------------|
| **Translation** | The converted Azure SQL T-SQL code |
| **Validation** | Syntax check results and warnings |
| **Optimization** | Performance score and recommendations |

### History

Previous translations are saved to Cosmos DB (if configured) and viewable in the History tab.

## Project Structure

```
codefiles/
├── app.py              # Main Streamlit application
├── agents.py           # Agent helper classes (legacy/optional)
├── cosmos_helper.py    # Cosmos DB helper functions
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template (copy to .env)
├── .gitignore          # Git ignore rules
├── Dockerfile          # Container configuration
├── README.md           # This file
└── sample_queries/     # Sample Oracle SQL files
    ├── simple_select.sql
    ├── nvl_decode.sql
    ├── hierarchical.sql
    ├── cursor_loop.sql
    └── complex_procedure.sql
```

## Configuration Reference

| Variable | Required | Description |
|----------|----------|-------------|
| `AGENT_API_ENDPOINT` | Yes | Azure AI Foundry project endpoint |
| `AGENT_ID` | Yes | Your Translation Agent ID (starts with `asst_`) |
| `COSMOS_ENDPOINT` | No | Cosmos DB URI for history feature |
| `COSMOS_KEY` | No | Cosmos DB primary key |
| `DATABASE_NAME` | No | Cosmos DB database name (default: `SQLModernizationDB`) |

## Architecture

```
User Input (Oracle SQL)
    ↓
Streamlit UI (app.py)
    ↓
Azure AI Foundry Agent API (via azure-ai-projects SDK)
    ↓
Translation Agent → Validation Agent → Optimization Agent
    ↓
Parse Results (Translation + Validation JSON + Optimization JSON)
    ↓
Save to Cosmos DB + Display in UI
```

## Docker Deployment

Build and run with Docker:

```bash
# Build the image
docker build -t sql-modernization-app .

# Run the container (with Azure CLI mounted for auth)
docker run -p 8501:8501 \
  -v ~/.azure:/root/.azure \
  -e AGENT_API_ENDPOINT="your-endpoint" \
  -e AGENT_ID="your-agent-id" \
  sql-modernization-app
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Configuration Required" | Edit `.env` file with valid credentials |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `DefaultAzureCredential failed` | Run `az login` to authenticate |
| `404 Resource not found` | Verify endpoint ends with `/api/projects/proj-default` |
| Config missing | Ensure `.env` exists (not `.env.example`) |
| Timeout errors | Complex queries need 1-2 min for 3 agents |
| No validation/optimization | Check Connected agents in Azure AI Foundry |
| Azure CLI not found | Install Azure CLI, restart terminal |

## Portability

This folder is fully portable! To use on any machine:

1. Copy entire `codefiles` folder
2. Edit `.env` file with your Azure credentials
3. Run `pip install -r requirements.txt`
4. Run `az login` for authentication  
5. Run `streamlit run app.py`

**No hardcoded paths or credentials!** All configuration is in `.env` file.

## Dependencies

- **streamlit** - Web framework
- **azure-ai-projects** - Azure AI Foundry SDK
- **azure-identity** - Azure CLI authentication
- **azure-cosmos** - Cosmos DB SDK
- **python-dotenv** - Environment configuration
- **pandas** - Data processing

## Learn More

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Cosmos DB Documentation](https://learn.microsoft.com/azure/cosmos-db/)
