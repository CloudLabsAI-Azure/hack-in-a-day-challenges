# SQL Modernization Platform

Streamlit web application for Oracle to Azure SQL migration using Azure AI Foundry Agents.

## Features

- **3-Agent Pipeline**: Translation → Validation → Optimization using AI Foundry visual agents
- **Real-time Processing**: Call agent API and get results from all connected agents
- **Cosmos DB Integration**: Automatic persistence of translation history
- **Sample Queries**: Pre-loaded Oracle SQL examples for testing
- **Clean UI**: Three-column results display with validation and optimization insights

## Prerequisites

- Python 3.11 or higher
- Azure subscription with:
  - Azure AI Foundry with deployed agents (SQL-Translation-Agent, SQL-Validation-Agent, SQL-Optimization-Agent)
  - Azure Cosmos DB for NoSQL

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and update with your Azure credentials:

```bash
cp .env.example .env
```

Edit `.env` file:

```env
# Azure AI Foundry Agent API Configuration
AGENT_API_ENDPOINT=https://your-agent-endpoint.azure.com/agents/...
AGENT_API_KEY=your-agent-api-key-here

# Cosmos DB Configuration
COSMOS_ENDPOINT=https://your-cosmos-account.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key-here
DATABASE_NAME=SQLModernizationDB
```

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## Usage

1. **Enter SQL**: Paste Oracle SQL or load a sample query
2. **Click Modernize**: The Translation Agent processes your query
3. **View Results**: See translation, validation, and optimization in 3 columns
4. **Check History**: View past translations from Cosmos DB

## Deployment

See Challenge 6 in the hackathon guide for deploying to Azure Container Apps.

## Architecture

```
User Input (Oracle SQL)
    ↓
Translation Agent (GPT-4.1)
    ↓
Validation Agent (Connected)
    ↓
Optimization Agent (Connected)
    ↓
Streamlit UI + Cosmos DB
```

# Azure SQL Configuration (Optional)
AZURE_SQL_SERVER=your-server.database.windows.net
AZURE_SQL_DATABASE=ValidationTestDB
AZURE_SQL_USERNAME=sqladmin
AZURE_SQL_PASSWORD=your-password-here
```

### 3. Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open in your default browser at `http://localhost:8501`.

## Using the Application

### Translate SQL

1. Navigate to "Translate SQL" page
2. Enter Oracle SQL code or load a sample query
3. Click "Translate" to convert to Azure SQL
4. Click "Validate" to check the translated code
5. Click "Optimize" to get performance recommendations
6. Download the translated SQL file

### Batch Processing

1. Navigate to "Batch Processing" page
2. Upload multiple `.sql` files
3. Click "Process All Files"
4. View results summary table
5. Individual results are saved to Cosmos DB

### View History

1. Navigate to "History" page
2. Browse recent translations
3. Download any previous translation
4. View metadata and timestamps

## Docker Deployment

### Build Docker Image

```bash
docker build -t sql-modernization-app .
```

### Run with Docker

```bash
docker run -p 8501:8501 --env-file .env sql-modernization-app
```

### Deploy to Azure Container Apps

```bash
# Login to Azure
az login

# Create Container Registry
az acr create --resource-group SQL-Modernization-RG --name sqlmodernizationacr --sku Basic

# Build and push to ACR
az acr build --registry sqlmodernizationacr --image sql-modernization-app:v1 .

# Create Container App environment
az containerapp env create --name sql-modernization-env --resource-group SQL-Modernization-RG --location eastus

# Deploy Container App
az containerapp create \
  --name sql-modernization-app \
  --resource-group SQL-Modernization-RG \
  --environment sql-modernization-env \
  --image sqlmodernizationacr.azurecr.io/sql-modernization-app:v1 \
  --target-port 8501 \
  --ingress external \
  --registry-server sqlmodernizationacr.azurecr.io

# Get app URL
az containerapp show --name sql-modernization-app --resource-group SQL-Modernization-RG --query properties.configuration.ingress.fqdn
```

## Project Structure

```
codefiles/
├── streamlit_app.py          # Main Streamlit application
├── agents.py                  # Translation, Validation, and Optimization agents
├── cosmos_helper.py           # Cosmos DB data persistence
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
├── .gitignore                # Git ignore rules
├── Dockerfile                # Docker container configuration
├── README.md                 # This file
└── sample_queries/           # Sample Oracle SQL files
    ├── simple_select.sql
    ├── nvl_decode.sql
    ├── cursor_loop.sql
    ├── hierarchical.sql
    └── complex_procedure.sql
```

## Module Documentation

### agents.py

**SQLModernizationAgent** class provides:
- `translate_oracle_to_azure_sql(oracle_sql)`: Translates Oracle SQL to Azure SQL
- `validate_sql(sql_code)`: Validates SQL using AI and parser
- `optimize_sql(sql_code)`: Provides optimization recommendations

### cosmos_helper.py

**CosmosDBHelper** class provides:
- `save_translation(source_sql, translated_sql, metadata)`: Saves translation to Cosmos DB
- `save_validation(translation_id, validation_results)`: Saves validation log
- `save_optimization(translation_id, optimization_results)`: Saves optimization results
- `get_recent_translations(limit)`: Retrieves recent translations

### streamlit_app.py

Main Streamlit application with three pages:
- **Translate SQL**: Single query translation workflow
- **Batch Processing**: Multiple file processing
- **History**: Browse and download past translations

## Troubleshooting

### Connection Errors

If you see connection errors, verify:
- `.env` file exists and has correct values
- AI Foundry endpoint and key are valid (from your deployment)
- Cosmos DB endpoint and key are correct
- Firewall rules allow your IP address

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Cosmos DB Errors

Ensure your Cosmos DB has:
- Database: `SQLModernizationDB`
- Containers:
  - `TranslationResults` (partition key: `/sourceDialect`)
  - `ValidationLogs` (partition key: `/translationId`)
  - `OptimizationResults` (partition key: `/translationId`)

## Support

For issues or questions:
1. Check the challenge documentation
2. Review Azure service quotas and limits
3. Verify all environment variables are set correctly
4. Check Azure Portal for service health

## License

This project is provided as-is for educational and training purposes.
