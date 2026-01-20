# Challenge 05: Add Cosmos DB Persistence (Optional)

## Introduction

> **Note**: This challenge is **optional**. Your three-agent pipeline is fully functional without it. You can skip directly to **Challenge 06** where the Streamlit app will handle Cosmos DB persistence directly (simpler approach).

If you want to learn about Azure Functions and Agent Actions, this challenge shows how to create HTTP-triggered functions that agents can call to save results to Cosmos DB. Otherwise, proceed to Challenge 6.

## Challenge Objectives

- Understand Azure AI Foundry Agent Actions
- Create Cosmos DB connection configuration
- Add Actions to Translation Agent for saving translations
- Add Actions to Validation Agent for saving validation logs
- Add Actions to Optimization Agent for saving optimization results
- Test that data is being saved to Cosmos DB containers
- Verify complete workflow saves results at each stage

## Steps to Complete

### Part 1: Understand Agent Actions

**What are Actions?**
Actions let agents execute code or call APIs as part of their workflow. Instead of just returning text, agents can:
- Save data to databases
- Call external APIs
- Execute custom functions
- Trigger workflows

For this challenge, we'll use Actions to save each agent's output to Cosmos DB.

### Part 2: Prepare Cosmos DB Information

1. From Challenge 1, gather your Cosmos DB details:
   - **Cosmos DB Endpoint**: `https://your-cosmos-account.documents.azure.com:443/`
   - **Cosmos DB Key**: Your primary key
   - **Database Name**: `SQLModernizationDB`
   - **Containers**:
     - `TranslationResults` (for Agent 1)
     - `ValidationLogs` (for Agent 2)
     - `OptimizationResults` (for Agent 3)

2. Keep these handy for the next steps.

### Part 3: Create Azure Function for Cosmos DB Actions

Since AI Foundry Actions work best with HTTP endpoints, we'll create a simple Azure Function to handle Cosmos DB writes.

1. In the **Azure Portal**, search for **Function App**.

2. Click **+ Create**.

3. Configure:
   - **Resource Group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Function App name**: **sql-mod-actions-<inject key="DeploymentID"></inject>**
   - **Runtime**: **Python**
   - **Version**: **3.11**
   - **Region**: **<inject key="Region"></inject>**
   - **Operating System**: **Linux**
   - **Plan type**: **Consumption (Serverless)**

4. Click **Review + Create**, then **Create**.

5. Wait for deployment (2-3 minutes).

### Part 4: Create HTTP Function for Translation Results

1. Go to your **Function App**.

2. Click **Functions** in the left menu.

3. Click **+ Create**.

4. Select **HTTP trigger**.

5. Configure:
   - **Name**: `SaveTranslation`
   - **Authorization level**: **Function**

6. Click **Create**.

7. Click on the function, then **Code + Test**.

8. Replace the code with:

```python
import azure.functions as func
import json
import logging
from azure.cosmos import CosmosClient
import os
import uuid
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('SaveTranslation function triggered')
    
    try:
        req_body = req.get_json()
        
        # Cosmos DB configuration
        endpoint = os.environ["COSMOS_ENDPOINT"]
        key = os.environ["COSMOS_KEY"]
        database_name = os.environ["DATABASE_NAME"]
        
        client = CosmosClient(endpoint, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client("TranslationResults")
        
        # Prepare item
        item = {
            "id": str(uuid.uuid4()),
            "sourceDialect": "Oracle",
            "source_sql": req_body.get("source_sql"),
            "translated_sql": req_body.get("translated_sql"),
            "target_dialect": "Azure SQL",
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": req_body.get("metadata", {})
        }
        
        # Save to Cosmos DB
        created = container.create_item(body=item)
        
        return func.HttpResponse(
            json.dumps({"status": "success", "id": created["id"]}),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"status": "error", "message": str(e)}),
            mimetype="application/json",
            status_code=500
        )
```

9. Click **Save**.

### Part 5: Add Environment Variables to Function App

1. Go back to your Function App overview.

2. Click **Configuration** in the left menu.

3. Click **+ New application setting** and add:
   - **Name**: `COSMOS_ENDPOINT`
   - **Value**: Your Cosmos DB endpoint

4. Add another:
   - **Name**: `COSMOS_KEY`
   - **Value**: Your Cosmos DB primary key

5. Add another:
   - **Name**: `DATABASE_NAME`
   - **Value**: `SQLModernizationDB`

6. Click **Save**, then **Continue**.

### Part 6: Create Functions for Validation and Optimization

1. Create another function: **SaveValidation**

Code:
```python
import azure.functions as func
import json
import logging
from azure.cosmos import CosmosClient
import os
import uuid
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        
        endpoint = os.environ["COSMOS_ENDPOINT"]
        key = os.environ["COSMOS_KEY"]
        database_name = os.environ["DATABASE_NAME"]
        
        client = CosmosClient(endpoint, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client("ValidationLogs")
        
        item = {
            "id": str(uuid.uuid4()),
            "translationId": req_body.get("translation_id"),
            "sql_code": req_body.get("sql_code"),
            "validation_results": req_body.get("validation_results"),
            "is_valid": req_body.get("validation_results", {}).get("valid", False),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        created = container.create_item(body=item)
        
        return func.HttpResponse(
            json.dumps({"status": "success", "id": created["id"]}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"status": "error", "message": str(e)}),
            mimetype="application/json",
            status_code=500
        )
```

2. Create another function: **SaveOptimization**

Code:
```python
import azure.functions as func
import json
import logging
from azure.cosmos import CosmosClient
import os
import uuid
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        
        endpoint = os.environ["COSMOS_ENDPOINT"]
        key = os.environ["COSMOS_KEY"]
        database_name = os.environ["DATABASE_NAME"]
        
        client = CosmosClient(endpoint, credential=key)
        database = client.get_database_client(database_name)
        container = database.get_container_client("OptimizationResults")
        
        item = {
            "id": str(uuid.uuid4()),
            "translationId": req_body.get("translation_id"),
            "sql_code": req_body.get("sql_code"),
            "optimization_score": req_body.get("optimization_results", {}).get("optimization_score", 0),
            "optimization_results": req_body.get("optimization_results"),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        created = container.create_item(body=item)
        
        return func.HttpResponse(
            json.dumps({"status": "success", "id": created["id"]}),
            mimetype="application/json",
            status_code=200
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"status": "error", "message": str(e)}),
            mimetype="application/json",
            status_code=500
        )
```

### Part 7: Get Function URLs

1. Go to each function (SaveTranslation, SaveValidation, SaveOptimization).

2. Click **Get Function URL**.

3. Copy the URL (includes the function key).

4. Save all three URLs.

### Part 8: Add Actions to Translation Agent

1. Go to **Azure AI Foundry Studio** → **Agents**.

2. Click on **SQL-Translation-Agent**.

3. Scroll to **Actions** section.

4. Click **+ Add**.

5. Configure the action:
   - **Action Type**: **Function**
   - **Name**: `save_translation`
   - **Description**: `Saves the translation result to Cosmos DB`
   - **Function URL**: Paste your SaveTranslation function URL
   - **Method**: **POST**

6. Add **Parameters** schema:
```json
{
  "type": "object",
  "properties": {
    "source_sql": {
      "type": "string",
      "description": "Original Oracle SQL code"
    },
    "translated_sql": {
      "type": "string",
      "description": "Translated Azure SQL T-SQL code"
    }
  },
  "required": ["source_sql", "translated_sql"]
}
```

7. Click **Add**.

8. Update Translation Agent **Instructions** to include:
```
After translating the SQL, call the save_translation action with the source_sql and translated_sql to persist the result.
```

### Part 9: Add Actions to Validation Agent

1. Go to **SQL-Validation-Agent**.

2. Add Action:
   - **Name**: `save_validation`
   - **Description**: `Saves validation results to Cosmos DB`
   - **Function URL**: SaveValidation URL
   - **Method**: **POST**

Parameters schema:
```json
{
  "type": "object",
  "properties": {
    "translation_id": {"type": "string"},
    "sql_code": {"type": "string"},
    "validation_results": {"type": "object"}
  },
  "required": ["sql_code", "validation_results"]
}
```

3. Update instructions:
```
After validating the SQL, call save_validation with the validation results to persist the log.
```

### Part 10: Add Actions to Optimization Agent

1. Go to **SQL-Optimization-Agent**.

2. Add Action:
   - **Name**: `save_optimization`
   - **Function URL**: SaveOptimization URL
   - **Method**: **POST**

Parameters:
```json
{
  "type": "object",
  "properties": {
    "translation_id": {"type": "string"},
    "sql_code": {"type": "string"},
    "optimization_results": {"type": "object"}
  },
  "required": ["sql_code", "optimization_results"]
}
```

3. Update instructions:
```
After analyzing the SQL, call save_optimization with the optimization results to persist the recommendations.
```

### Part 11: Test the Complete Workflow

1. Go to **SQL-Translation-Agent** playground.

2. Send Oracle SQL:
```sql
SELECT emp_id, emp_name, NVL(salary, 0) as salary
FROM employees
WHERE hire_date > SYSDATE - 30
AND ROWNUM <= 10;
```

3. Wait for all three agents to process.

4. Go to **Azure Portal** → **Cosmos DB** → **Data Explorer**.

5. Check **TranslationResults** container - you should see a new item.

6. Check **ValidationLogs** container - should have validation entry.

7. Check **OptimizationResults** container - should have optimization entry.

8. All three containers should have data!

## Success Criteria

- Azure Function App created successfully
- Three HTTP functions created (SaveTranslation, SaveValidation, SaveOptimization)
- Cosmos DB environment variables configured
- Function URLs obtained and saved
- Actions added to all three agents
- Agent instructions updated to call actions
- Complete pipeline tested: Translation → Validation → Optimization
- Data saved to TranslationResults container
- Data saved to ValidationLogs container
- Data saved to OptimizationResults container
- All records have proper timestamps and structure

## Additional Resources

- [Azure Functions Python Developer Guide](https://learn.microsoft.com/azure/azure-functions/functions-reference-python)
- [Azure AI Foundry Agent Actions](https://learn.microsoft.com/azure/ai-studio/how-to/develop/agents#actions)
- [Cosmos DB Python SDK](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-python)

Now, click **Next** to continue to **Challenge 06**.
