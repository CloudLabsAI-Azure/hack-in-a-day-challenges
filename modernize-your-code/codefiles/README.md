# SQL Modernization Platform - Streamlit Application

Production-ready web application for Oracle to Azure SQL migration using Azure AI Foundry multi-agent system.

## ✨ Features

- **Beautiful UI** - Modern gradient design with responsive layout
- **3-Agent Pipeline** - Translation → Validation → Optimization
- **File Upload** - Support for .sql and .txt files
- **Real-time Progress** - Visual feedback during processing
- **Cosmos DB Integration** - Automatic history tracking
- **Sample Queries** - Pre-built Oracle SQL examples
- **Production Ready** - Error handling, validation, and logging

## 🚀 Quick Start

### 1. Configure Environment

Rename `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:
```env
# Azure AI Foundry Agent API - Use Foundry services endpoint
AGENT_API_ENDPOINT=https://ai-project-XXXX.services.ai.azure.com/api/projects/sql-modernization-XXXX
AGENT_ID=asst_YourAgentID
PROJECT_NAME=

# Cosmos DB Configuration
COSMOS_ENDPOINT=https://your-cosmos.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key-here
DATABASE_NAME=SQLModernizationDB
```

**Note:** Authentication uses Azure CLI (`az login`), not API keys.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Authenticate with Azure CLI

```bash
az login
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📖 Usage

1. **Select Input Method:**
   - Upload a .sql file
   - Paste SQL code directly
   - Load a sample query

2. **Click "Modernize SQL"**

3. **View Results in 3 columns:**
   - **Translation**: Azure SQL T-SQL code
   - **Validation**: Syntax errors and warnings
   - **Optimization**: Performance recommendations with score

4. **Review History:**
   - All translations saved to Cosmos DB
   - Reload previous queries

## 📁 File Structure

```
codefiles/
├── app.py              # Main Streamlit application (704 lines)
├── agents.py           # Agent helper classes (optional legacy file)
├── cosmos_helper.py    # Cosmos DB helper functions
├── streamlit_app.py    # Alternative app version (optional)
├── requirements.txt    # Python dependencies
├── .env.example       # Environment template
├── .gitignore         # Git ignore rules
├── Dockerfile         # Container configuration
├── README.md          # This file
└── sample_queries/    # Sample SQL files (optional reference)
```

## 🏗 Architecture

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

## 📦 Dependencies

- **streamlit 1.30.0** - Web framework
- **azure-ai-projects 1.0.0** - Azure AI Foundry SDK
- **azure-identity** - Azure CLI authentication
- **azure-cosmos 4.7+** - Cosmos DB SDK
- **python-dotenv 1.0.0** - Environment configuration
- **pandas** - Data processing

## 🔧 Key Components

### app.py Structure

- **Lines 1-50**: Imports and configuration
- **Lines 51-169**: Custom CSS styling
- **Lines 171-230**: Cosmos DB connection and history retrieval
- **Lines 232-350**: Agent API integration using azure-ai-projects SDK
- **Lines 352-704**: Streamlit UI (3 tabs: Modernize, Results, History)

### Agent API Flow

1. **Create thread** - Initialize conversation with agent
2. **Add message** - Send Oracle SQL to Translation Agent
3. **Run agent** - Execute with connected agents (Validation + Optimization)
4. **Poll status** - Wait for all agents to complete
5. **Get response** - Parse results from all 3 agents
6. **Save to Cosmos** - Store results for history

## 🎨 Customization

### Add Sample Queries

Edit `samples` dictionary in app.py (line 485):

```python
samples = {
    "Your Query": """SELECT * FROM your_table;"""
}
```

### Modify UI Colors

Edit CSS variables (lines 51-60):

```css
:root {
    --primary-color: #0078D4;
    --secondary-color: #50E6FF;
}
```

### Adjust Timeout

Change `max_attempts` (line 291):

```python
max_attempts = 120  # 120 × 2s = 4 minutes max
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| ModuleNotFoundError | Run `pip install -r requirements.txt` |
| DefaultAzureCredential failed | Run `az login` to authenticate |
| 404 Resource not found | Verify endpoint is Foundry services (`.services.ai.azure.com`) not OpenAI |
| Config missing | Ensure `.env` exists (not `.env.example`) |
| Timeout | Complex queries need 1-2 min for 3 agents |
| No validation/optimization | Check Connected agents in Azure AI Foundry Studio |
| Azure CLI not found | Install Azure CLI, restart terminal |

## 🚀 Portability

This codefiles folder is fully portable! To use on any VM:

1. **Copy entire `codefiles` folder**
2. **Update `.env` file** with your Azure credentials
3. **Run `pip install -r requirements.txt`**
4. **Run `az login`** for authentication
5. **Run `streamlit run app.py`**

**No hardcoded paths or credentials!** All configuration is in `.env` file.

## 📚 Learn More

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Cosmos DB Documentation](https://learn.microsoft.com/azure/cosmos-db/)
