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
AGENT_API_ENDPOINT=https://ai-project-XXXX.openai.azure.com/
AGENT_API_KEY=your-api-key-here
AGENT_ID=asst_YourAgentID
COSMOS_ENDPOINT=https://your-cosmos.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key-here
DATABASE_NAME=SQLModernizationDB
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

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
├── app.py              # Main Streamlit application (711 lines)
├── requirements.txt    # Python dependencies
├── .env.example       # Environment template
├── Dockerfile         # Container configuration
└── README.md          # This file
```

## 🏗 Architecture

```
User Input (Oracle SQL)
    ↓
Streamlit UI (app.py)
    ↓
Azure AI Foundry Assistants API
    ↓
Translation Agent → Validation Agent + Optimization Agent
    ↓
Parse Results (Translation + Validation JSON + Optimization JSON)
    ↓
Save to Cosmos DB + Display in UI
```

## 📦 Dependencies

- **streamlit 1.30.0** - Web framework
- **requests 2.31.0** - HTTP client for Agent API
- **azure-cosmos 4.5.1** - Cosmos DB SDK
- **python-dotenv 1.0.0** - Environment configuration
- **pandas 2.1.4** - Data processing

## 🔧 Key Components

### app.py Structure

- **Lines 51-169**: Custom CSS styling
- **Lines 171-186**: Cosmos DB connection
- **Lines 188-228**: Response parsing
- **Lines 230-330**: Agent API integration
- **Lines 332-711**: Streamlit UI (3 tabs)

### Agent API Flow

1. **Create thread** - Initialize conversation
2. **Add message** - Send Oracle SQL
3. **Run agent** - Execute Translation Agent
4. **Poll status** - Wait for completion (includes connected agents)
5. **Get response** - Retrieve all 3 agent outputs

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
| 401 Unauthorized | Verify AGENT_API_KEY is correct Primary Key |
| Config missing | Ensure `.env` exists (not `.env.example`) |
| Timeout | Complex queries need 1-2 min, increase max_attempts |
| No validation/optimization | Check Connected agents in AI Foundry |

## 🚢 Production Deployment

See Challenge 6 documentation for Azure Container Apps deployment steps.

## 📚 Learn More

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Azure Cosmos DB Documentation](https://learn.microsoft.com/azure/cosmos-db/)
