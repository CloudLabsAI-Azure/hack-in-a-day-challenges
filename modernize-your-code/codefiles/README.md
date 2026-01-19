# SQL Modernization Platform

Complete Streamlit application for Oracle to Azure SQL migration with AI-powered translation, validation, and optimization.

## Features

- **Translation Agent**: Converts Oracle PL/SQL to Azure SQL T-SQL using GPT-4
- **Validation Agent**: Validates translated SQL using AI and parser-based methods
- **Optimization Agent**: Provides performance recommendations and index suggestions
- **Cosmos DB Integration**: Persists all workflow data for audit and history
- **Batch Processing**: Handle multiple SQL files at once
- **History View**: Browse and download past translations

## Prerequisites

- Python 3.11 or higher
- Azure subscription with:
  - Azure AI Foundry (with GPT-4 deployment)
  - Azure Cosmos DB for NoSQL
  - (Optional) Azure SQL Database for validation

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
# AI Foundry Configuration
AZURE_OPENAI_ENDPOINT=https://your-ai-foundry-endpoint.openai.azure.com/
AZURE_OPENAI_KEY=your-ai-foundry-key-here
AZURE_OPENAI_DEPLOYMENT=gpt-4-sql-translator
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Cosmos DB Configuration
COSMOS_ENDPOINT=https://your-cosmos-account.documents.azure.com:443/
COSMOS_KEY=your-cosmos-key-here
DATABASE_NAME=SQLModernizationDB

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
