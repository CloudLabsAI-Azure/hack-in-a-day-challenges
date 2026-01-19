# Challenge 05: Integrate with Cosmos DB for Data Persistence

## Introduction

Azure Cosmos DB provides a scalable NoSQL database to store translation results, validation logs, and optimization recommendations. This challenge focuses on integrating your multi-agent system with Cosmos DB to persist all workflow data, enable audit trails, and support batch processing of large SQL file sets. You will create data models for each workflow stage and implement retry logic for reliable cloud operations.

## Challenge Objectives

- Connect to Azure Cosmos DB using Python SDK
- Create data models for translation, validation, and optimization results
- Implement CRUD operations for each Cosmos DB container
- Add retry logic for transient failures
- Store complete workflow results with metadata
- Query historical results for analysis and reporting

## Steps to Complete

### Part 1: Install Cosmos DB SDK

1. In **Azure AI Foundry Studio**, create a new notebook named `Cosmos_Integration`.

2. In the first cell, install the Cosmos DB SDK:

```python
%pip install azure-cosmos azure-identity --quiet

print("Azure Cosmos DB SDK installed")
```

3. Run the cell.

### Part 2: Configure Cosmos DB Connection

1. Add a new cell with Cosmos DB configuration:

```python
from azure.cosmos import CosmosClient, PartitionKey, exceptions
from azure.identity import DefaultAzureCredential
import json
from datetime import datetime
import time

# Cosmos DB configuration
COSMOS_ENDPOINT = "https://sql-modernization-cosmosdb-xxxxx.documents.azure.com:443/"  # Replace
COSMOS_KEY = "your-cosmos-primary-key-here"  # Replace
DATABASE_NAME = "SQLModernization"

# Container names
TRANSLATION_CONTAINER = "TranslationResults"
VALIDATION_CONTAINER = "ValidationLogs"
OPTIMIZATION_CONTAINER = "OptimizationResults"

# Initialize Cosmos client
cosmos_client = CosmosClient(COSMOS_ENDPOINT, credential=COSMOS_KEY)

# Get database
database = cosmos_client.get_database_client(DATABASE_NAME)

print(f"Connected to Cosmos DB: {DATABASE_NAME}")
```

2. Run the cell.

### Part 3: Create Data Models

1. Add a new cell to define data models:

```python
class TranslationResult:
    """Data model for translation results"""
    
    def __init__(self, source_sql: str, translated_sql: str, source_dialect: str = "Oracle"):
        self.id = self._generate_id()
        self.source_sql = source_sql
        self.translated_sql = translated_sql
        self.source_dialect = source_dialect
        self.target_dialect = "Azure SQL"
        self.timestamp = datetime.utcnow().isoformat()
        self.status = "completed"
        self.metadata = {}
    
    def _generate_id(self):
        """Generate unique ID"""
        import uuid
        return str(uuid.uuid4())
    
    def add_metadata(self, key: str, value):
        """Add metadata field"""
        self.metadata[key] = value
    
    def to_dict(self):
        """Convert to dictionary for Cosmos DB"""
        return {
            "id": self.id,
            "source_sql": self.source_sql,
            "translated_sql": self.translated_sql,
            "source_dialect": self.source_dialect,
            "target_dialect": self.target_dialect,
            "timestamp": self.timestamp,
            "status": self.status,
            "metadata": self.metadata
        }


class ValidationLog:
    """Data model for validation logs"""
    
    def __init__(self, translation_id: str, sql_code: str, validation_results: dict):
        self.id = self._generate_id()
        self.translation_id = translation_id
        self.sql_code = sql_code
        self.validation_results = validation_results
        self.timestamp = datetime.utcnow().isoformat()
        self.is_valid = validation_results.get('overall_valid', False)
        self.validation_methods = []
    
    def _generate_id(self):
        import uuid
        return str(uuid.uuid4())
    
    def add_validation_method(self, method: str, result: bool):
        """Add validation method result"""
        self.validation_methods.append({
            "method": method,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        })
    
    def to_dict(self):
        return {
            "id": self.id,
            "translation_id": self.translation_id,
            "sql_code": self.sql_code,
            "validation_results": self.validation_results,
            "timestamp": self.timestamp,
            "is_valid": self.is_valid,
            "validation_methods": self.validation_methods
        }


class OptimizationResult:
    """Data model for optimization results"""
    
    def __init__(self, translation_id: str, sql_code: str, optimization_data: dict):
        self.id = self._generate_id()
        self.translation_id = translation_id
        self.sql_code = sql_code
        self.optimization_score = optimization_data.get('overall_score', 0)
        self.priority_optimizations = optimization_data.get('priority_optimizations', [])
        self.index_recommendations = optimization_data.get('index_recommendations', [])
        self.azure_features = optimization_data.get('azure_features', [])
        self.timestamp = datetime.utcnow().isoformat()
    
    def _generate_id(self):
        import uuid
        return str(uuid.uuid4())
    
    def to_dict(self):
        return {
            "id": self.id,
            "translation_id": self.translation_id,
            "sql_code": self.sql_code,
            "optimization_score": self.optimization_score,
            "priority_optimizations": self.priority_optimizations,
            "index_recommendations": self.index_recommendations,
            "azure_features": self.azure_features,
            "timestamp": self.timestamp
        }

print("Data models created")
```

2. Run the cell.

### Part 4: Implement Save Functions with Retry Logic

1. Add a new cell to create save functions:

```python
def save_to_cosmos(container_name: str, item: dict, partition_key: str, max_retries: int = 3):
    """
    Save item to Cosmos DB with retry logic.
    
    Args:
        container_name (str): Container name
        item (dict): Item to save
        partition_key (str): Partition key value
        max_retries (int): Maximum retry attempts
    
    Returns:
        dict: Created item or error
    """
    container = database.get_container_client(container_name)
    
    for attempt in range(max_retries):
        try:
            # Ensure partition key is in item
            if 'translation_id' not in item and partition_key:
                item['partition_key'] = partition_key
            
            created_item = container.create_item(body=item)
            print(f"Item saved to {container_name}: {item['id']}")
            return created_item
            
        except exceptions.CosmosHttpResponseError as e:
            if e.status_code == 409:
                print(f"Item {item['id']} already exists in {container_name}")
                return item
            elif e.status_code == 429:
                # Rate limit exceeded, wait and retry
                wait_time = 2 ** attempt
                print(f"Rate limited. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Error saving to Cosmos DB: {e.message}")
                if attempt == max_retries - 1:
                    raise
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            if attempt == max_retries - 1:
                raise
    
    return None


def save_translation_result(translation_result: TranslationResult):
    """Save translation result to Cosmos DB"""
    return save_to_cosmos(
        container_name=TRANSLATION_CONTAINER,
        item=translation_result.to_dict(),
        partition_key=translation_result.id
    )


def save_validation_log(validation_log: ValidationLog):
    """Save validation log to Cosmos DB"""
    return save_to_cosmos(
        container_name=VALIDATION_CONTAINER,
        item=validation_log.to_dict(),
        partition_key=validation_log.translation_id
    )


def save_optimization_result(optimization_result: OptimizationResult):
    """Save optimization result to Cosmos DB"""
    return save_to_cosmos(
        container_name=OPTIMIZATION_CONTAINER,
        item=optimization_result.to_dict(),
        partition_key=optimization_result.translation_id
    )

print("Save functions with retry logic created")
```

2. Run the cell.

### Part 5: Test Translation Result Storage

1. Add a new cell to test saving translation results:

```python
# Sample translation to save
oracle_sql = """
SELECT emp_id, emp_name, salary
FROM employees
WHERE hire_date > SYSDATE - 30;
"""

azure_sql = """
SELECT emp_id, emp_name, salary
FROM employees
WHERE hire_date > DATEADD(day, -30, GETDATE());
"""

# Create translation result
translation = TranslationResult(
    source_sql=oracle_sql,
    translated_sql=azure_sql,
    source_dialect="Oracle PL/SQL"
)

# Add metadata
translation.add_metadata("tokens_used", 250)
translation.add_metadata("translation_time_ms", 1250)
translation.add_metadata("source_file", "employee_report.sql")

# Save to Cosmos DB
saved_translation = save_translation_result(translation)

print(f"Translation saved with ID: {translation.id}")
print(f"Timestamp: {translation.timestamp}")
```

2. Run the cell.

### Part 6: Test Validation Log Storage

1. Add a new cell to test saving validation logs:

```python
# Sample validation results
validation_results = {
    "overall_valid": True,
    "ai_validation": {
        "valid": True,
        "confidence": 0.95,
        "issues": []
    },
    "parser_validation": {
        "valid": True,
        "syntax_errors": []
    },
    "database_validation": {
        "executed": False,
        "reason": "Optional validation skipped"
    }
}

# Create validation log
validation = ValidationLog(
    translation_id=translation.id,
    sql_code=azure_sql,
    validation_results=validation_results
)

# Add validation methods
validation.add_validation_method("AI-based", True)
validation.add_validation_method("Parser-based", True)

# Save to Cosmos DB
saved_validation = save_validation_log(validation)

print(f"Validation log saved with ID: {validation.id}")
print(f"Linked to translation: {validation.translation_id}")
print(f"Overall valid: {validation.is_valid}")
```

2. Run the cell.

### Part 7: Test Optimization Result Storage

1. Add a new cell to test saving optimization results:

```python
# Sample optimization data
optimization_data = {
    "overall_score": 75,
    "priority_optimizations": [
        {
            "priority": "HIGH",
            "category": "Index",
            "recommendation": "Add index on employees(hire_date)",
            "reason": "Frequent date range filtering",
            "estimated_impact": "40-60% query time reduction"
        }
    ],
    "index_recommendations": [
        {
            "index_name": "IX_Employees_HireDate",
            "index_type": "Non-clustered",
            "columns": "hire_date",
            "reason": "WHERE clause filtering"
        }
    ],
    "azure_features": [
        {
            "feature_name": "Automatic Tuning",
            "benefit": "Auto-create missing indexes",
            "implementation_notes": "Enable via Azure Portal"
        }
    ]
}

# Create optimization result
optimization = OptimizationResult(
    translation_id=translation.id,
    sql_code=azure_sql,
    optimization_data=optimization_data
)

# Save to Cosmos DB
saved_optimization = save_optimization_result(optimization)

print(f"Optimization result saved with ID: {optimization.id}")
print(f"Optimization score: {optimization.optimization_score}/100")
print(f"Recommendations: {len(optimization.priority_optimizations)}")
```

2. Run the cell.

### Part 8: Query Historical Results

1. Add a new cell to query stored results:

```python
def query_translations(limit: int = 10, source_dialect: str = None):
    """
    Query translation results.
    
    Args:
        limit (int): Maximum results to return
        source_dialect (str): Filter by source dialect
    
    Returns:
        list: Translation results
    """
    container = database.get_container_client(TRANSLATION_CONTAINER)
    
    query = "SELECT * FROM c"
    parameters = []
    
    if source_dialect:
        query += " WHERE c.source_dialect = @dialect"
        parameters.append({"name": "@dialect", "value": source_dialect})
    
    query += " ORDER BY c.timestamp DESC"
    
    items = list(container.query_items(
        query=query,
        parameters=parameters,
        max_item_count=limit
    ))
    
    return items


def query_validations_by_translation(translation_id: str):
    """Query validation logs for a specific translation"""
    container = database.get_container_client(VALIDATION_CONTAINER)
    
    query = "SELECT * FROM c WHERE c.translation_id = @translation_id"
    parameters = [{"name": "@translation_id", "value": translation_id}]
    
    items = list(container.query_items(
        query=query,
        parameters=parameters
    ))
    
    return items


def query_optimizations_by_score(min_score: int = 0, max_score: int = 100):
    """Query optimizations by score range"""
    container = database.get_container_client(OPTIMIZATION_CONTAINER)
    
    query = """
    SELECT * FROM c 
    WHERE c.optimization_score >= @min_score 
      AND c.optimization_score <= @max_score
    ORDER BY c.optimization_score ASC
    """
    
    parameters = [
        {"name": "@min_score", "value": min_score},
        {"name": "@max_score", "value": max_score}
    ]
    
    items = list(container.query_items(
        query=query,
        parameters=parameters
    ))
    
    return items

print("Query functions created")
```

2. Run the cell.

### Part 9: Test Query Operations

1. Add a new cell to test queries:

```python
# Query recent translations
print("Recent Translations:")
recent_translations = query_translations(limit=5)
for trans in recent_translations:
    print(f"  - {trans['id'][:8]}... | {trans['source_dialect']} -> {trans['target_dialect']} | {trans['timestamp']}")

print(f"\nTotal translations found: {len(recent_translations)}")

# Query validations for our test translation
print(f"\nValidations for translation {translation.id[:8]}...:")
validations = query_validations_by_translation(translation.id)
for val in validations:
    print(f"  - Valid: {val['is_valid']} | Methods: {len(val['validation_methods'])} | {val['timestamp']}")

# Query low-score optimizations (need improvement)
print("\nQueries needing optimization (score < 70):")
low_score_opts = query_optimizations_by_score(min_score=0, max_score=69)
for opt in low_score_opts:
    print(f"  - Score: {opt['optimization_score']} | Recommendations: {len(opt['priority_optimizations'])}")
```

2. Run the cell.

### Part 10: Implement Batch Workflow Storage

1. Add a final cell to handle complete workflow results:

```python
def save_complete_workflow(oracle_sql: str, translated_sql: str, 
                          validation_results: dict, optimization_data: dict):
    """
    Saves complete workflow (translation -> validation -> optimization).
    
    Args:
        oracle_sql (str): Original Oracle SQL
        translated_sql (str): Translated Azure SQL
        validation_results (dict): Validation results
        optimization_data (dict): Optimization recommendations
    
    Returns:
        dict: Workflow IDs
    """
    workflow_ids = {}
    
    try:
        # Step 1: Save translation
        translation = TranslationResult(
            source_sql=oracle_sql,
            translated_sql=translated_sql
        )
        save_translation_result(translation)
        workflow_ids['translation_id'] = translation.id
        
        # Step 2: Save validation
        validation = ValidationLog(
            translation_id=translation.id,
            sql_code=translated_sql,
            validation_results=validation_results
        )
        save_validation_log(validation)
        workflow_ids['validation_id'] = validation.id
        
        # Step 3: Save optimization
        optimization = OptimizationResult(
            translation_id=translation.id,
            sql_code=translated_sql,
            optimization_data=optimization_data
        )
        save_optimization_result(optimization)
        workflow_ids['optimization_id'] = optimization.id
        
        print(f"Complete workflow saved:")
        print(f"  Translation ID: {translation.id}")
        print(f"  Validation ID: {validation.id}")
        print(f"  Optimization ID: {optimization.id}")
        
        return workflow_ids
        
    except Exception as e:
        print(f"Error saving workflow: {str(e)}")
        return workflow_ids


# Test complete workflow save
test_oracle = "SELECT * FROM employees WHERE ROWNUM <= 10;"
test_azure = "SELECT TOP 10 * FROM employees;"
test_validation = {"overall_valid": True, "ai_validation": {"valid": True}}
test_optimization = {"overall_score": 85, "priority_optimizations": []}

workflow_ids = save_complete_workflow(test_oracle, test_azure, test_validation, test_optimization)
```

2. Run the cell.

## Success Criteria

- Azure Cosmos DB Python SDK installed successfully
- Connected to Cosmos DB database and containers
- Data models created for TranslationResult, ValidationLog, and OptimizationResult
- Save functions implemented with retry logic for transient failures
- Translation results saved to TranslationResults container
- Validation logs saved with linkage to translation ID
- Optimization results saved with score and recommendations
- Query operations retrieve historical data successfully
- Batch workflow function saves complete translation pipeline
- All operations handle errors gracefully with appropriate logging

## Additional Resources

- [Azure Cosmos DB Python SDK](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-python)
- [Cosmos DB Query Language](https://learn.microsoft.com/azure/cosmos-db/nosql/query/getting-started)
- [Partitioning in Cosmos DB](https://learn.microsoft.com/azure/cosmos-db/partitioning-overview)
- [Retry Logic Best Practices](https://learn.microsoft.com/azure/architecture/best-practices/retry-service-specific)

Now, click **Next** to continue to **Challenge 06**.
