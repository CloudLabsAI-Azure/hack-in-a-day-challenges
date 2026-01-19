"""
Cosmos DB Helper Module
Provides functions to save and retrieve SQL modernization workflow data.
"""

from azure.cosmos import CosmosClient, exceptions
import uuid
from datetime import datetime
import time


class CosmosDBHelper:
    """Helper class for Cosmos DB operations"""
    
    def __init__(self, endpoint: str, key: str, database_name: str):
        """
        Initialize Cosmos DB helper.
        
        Args:
            endpoint: Cosmos DB endpoint URL
            key: Cosmos DB primary key
            database_name: Database name
        """
        self.client = CosmosClient(endpoint, credential=key)
        self.database = self.client.get_database_client(database_name)
        self.translation_container = self.database.get_container_client("TranslationResults")
        self.validation_container = self.database.get_container_client("ValidationLogs")
        self.optimization_container = self.database.get_container_client("OptimizationResults")
    
    def _retry_operation(self, operation, max_retries=3):
        """
        Retry an operation with exponential backoff.
        
        Args:
            operation: Function to retry
            max_retries: Maximum number of retry attempts
            
        Returns:
            Result of the operation
        """
        for attempt in range(max_retries):
            try:
                return operation()
            except exceptions.CosmosHttpResponseError as e:
                if e.status_code == 429 and attempt < max_retries - 1:
                    # Rate limit exceeded, wait and retry
                    wait_time = 2 ** attempt
                    print(f"Rate limited. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    raise
        return None
    
    def save_translation(self, source_sql: str, translated_sql: str, metadata: dict = None) -> str:
        """
        Save translation result to Cosmos DB.
        
        Args:
            source_sql: Original Oracle SQL
            translated_sql: Translated Azure SQL
            metadata: Optional metadata dict
            
        Returns:
            str: ID of created item
        """
        item = {
            "id": str(uuid.uuid4()),
            "sourceDialect": "Oracle",
            "source_sql": source_sql,
            "translated_sql": translated_sql,
            "target_dialect": "Azure SQL",
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": metadata or {}
        }
        
        def create_item():
            created = self.translation_container.create_item(body=item)
            return created["id"]
        
        try:
            return self._retry_operation(create_item)
        except exceptions.CosmosHttpResponseError as e:
            if e.status_code == 409:
                print(f"Item {item['id']} already exists")
                return item["id"]
            else:
                print(f"Error saving translation: {e.message}")
                return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None
    
    def save_validation(self, translation_id: str, validation_results: dict) -> str:
        """
        Save validation log to Cosmos DB.
        
        Args:
            translation_id: ID of the translation being validated
            validation_results: Validation results dict
            
        Returns:
            str: ID of created item
        """
        item = {
            "id": str(uuid.uuid4()),
            "translationId": translation_id,
            "validation_results": validation_results,
            "is_valid": validation_results.get("overall_valid", False),
            "timestamp": datetime.utcnow().isoformat()
        }
        
        def create_item():
            created = self.validation_container.create_item(body=item)
            return created["id"]
        
        try:
            return self._retry_operation(create_item)
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error saving validation: {e.message}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None
    
    def save_optimization(self, translation_id: str, optimization_results: dict) -> str:
        """
        Save optimization result to Cosmos DB.
        
        Args:
            translation_id: ID of the translation being optimized
            optimization_results: Optimization results dict
            
        Returns:
            str: ID of created item
        """
        item = {
            "id": str(uuid.uuid4()),
            "translationId": translation_id,
            "optimization_score": optimization_results.get("overall_score", 0),
            "optimization_results": optimization_results,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        def create_item():
            created = self.optimization_container.create_item(body=item)
            return created["id"]
        
        try:
            return self._retry_operation(create_item)
        except exceptions.CosmosHttpResponseError as e:
            print(f"Error saving optimization: {e.message}")
            return None
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return None
    
    def get_recent_translations(self, limit: int = 10) -> list:
        """
        Get recent translations from Cosmos DB.
        
        Args:
            limit: Maximum number of results
            
        Returns:
            list: List of translation items
        """
        try:
            query = "SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT @limit"
            items = list(self.translation_container.query_items(
                query=query,
                parameters=[{"name": "@limit", "value": limit}],
                enable_cross_partition_query=True
            ))
            return items
        except Exception as e:
            print(f"Error retrieving translations: {str(e)}")
            return []
    
    def get_validation_by_translation(self, translation_id: str) -> list:
        """
        Get validation logs for a specific translation.
        
        Args:
            translation_id: Translation ID to lookup
            
        Returns:
            list: List of validation items
        """
        try:
            query = "SELECT * FROM c WHERE c.translationId = @translation_id"
            items = list(self.validation_container.query_items(
                query=query,
                parameters=[{"name": "@translation_id", "value": translation_id}],
                enable_cross_partition_query=True
            ))
            return items
        except Exception as e:
            print(f"Error retrieving validations: {str(e)}")
            return []
    
    def get_optimization_by_translation(self, translation_id: str) -> list:
        """
        Get optimization results for a specific translation.
        
        Args:
            translation_id: Translation ID to lookup
            
        Returns:
            list: List of optimization items
        """
        try:
            query = "SELECT * FROM c WHERE c.translationId = @translation_id"
            items = list(self.optimization_container.query_items(
                query=query,
                parameters=[{"name": "@translation_id", "value": translation_id}],
                enable_cross_partition_query=True
            ))
            return items
        except Exception as e:
            print(f"Error retrieving optimizations: {str(e)}")
            return []


if __name__ == "__main__":
    print("Cosmos DB Helper module loaded successfully.")
    print("This module provides data persistence for SQL modernization workflows.")
