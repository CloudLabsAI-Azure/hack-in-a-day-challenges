"""
Services package for Azure integrations.

All services use Managed Identity for authentication - no API keys!
"""
from .azure_auth import AzureAuthService
from .keyvault_service import KeyVaultService
from .openai_service import OpenAIService
from .storage_service import StorageService

__all__ = [
    "AzureAuthService",
    "KeyVaultService", 
    "OpenAIService",
    "StorageService"
]
