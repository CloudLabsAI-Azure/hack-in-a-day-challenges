"""
Azure Key Vault Service for Secret Management.

This module retrieves all configuration secrets from Azure Key Vault.
No secrets are stored in code, environment variables, or config files!

Security: All sensitive data is centralized in Key Vault with RBAC access control.
"""
import logging
from dataclasses import dataclass
from typing import Optional, Dict, Any
from functools import lru_cache

from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError

from .azure_auth import auth_service

logger = logging.getLogger(__name__)


@dataclass
class SecretCache:
    """Cache for retrieved secrets to minimize Key Vault calls."""
    openai_endpoint: Optional[str] = None
    chat_deployment: Optional[str] = None
    api_version: Optional[str] = None
    storage_account_name: Optional[str] = None


class KeyVaultService:
    """
    Azure Key Vault Service for secure secret retrieval.
    
    Retrieves configuration from Key Vault using Managed Identity.
    Implements caching to minimize API calls.
    """
    
    # Secret names as defined in the challenge
    SECRET_OPENAI_ENDPOINT = "OpenAIEndpoint"
    SECRET_CHAT_DEPLOYMENT = "ChatModelDeployment"
    SECRET_API_VERSION = "OpenAIApiVersion"
    SECRET_STORAGE_ACCOUNT = "StorageAccountName"
    
    def __init__(self, vault_url: str):
        """
        Initialize Key Vault Service.
        
        Args:
            vault_url: Full URL to Key Vault (e.g., https://kv-name.vault.azure.net)
        """
        self.vault_url = vault_url
        self._client: Optional[SecretClient] = None
        self._cache = SecretCache()
        self._initialized = False
        self._error_message: Optional[str] = None
    
    @property
    def client(self) -> SecretClient:
        """Get or create the Key Vault client."""
        if self._client is None:
            self._client = SecretClient(
                vault_url=self.vault_url,
                credential=auth_service.credential
            )
        return self._client
    
    def _get_secret_safe(self, secret_name: str) -> Optional[str]:
        """
        Safely retrieve a secret from Key Vault.
        
        Args:
            secret_name: Name of the secret to retrieve
            
        Returns:
            Secret value or None if not found
        """
        try:
            secret = self.client.get_secret(secret_name)
            return secret.value
        except ResourceNotFoundError:
            logger.warning(f"Secret '{secret_name}' not found in Key Vault")
            return None
        except HttpResponseError as e:
            logger.error(f"Error accessing Key Vault: {e}")
            raise
    
    def initialize(self) -> tuple[bool, str]:
        """
        Initialize the service by loading all required secrets.
        
        Returns:
            Tuple of (success, message)
        """
        try:
            logger.info(f"Connecting to Key Vault: {self.vault_url}")
            
            # Load required secrets
            self._cache.openai_endpoint = self._get_secret_safe(self.SECRET_OPENAI_ENDPOINT)
            self._cache.chat_deployment = self._get_secret_safe(self.SECRET_CHAT_DEPLOYMENT)
            self._cache.api_version = self._get_secret_safe(self.SECRET_API_VERSION)
            
            # Load optional secrets
            self._cache.storage_account_name = self._get_secret_safe(self.SECRET_STORAGE_ACCOUNT)
            
            # Validate required secrets
            missing = []
            if not self._cache.openai_endpoint:
                missing.append(self.SECRET_OPENAI_ENDPOINT)
            if not self._cache.chat_deployment:
                missing.append(self.SECRET_CHAT_DEPLOYMENT)
            if not self._cache.api_version:
                missing.append(self.SECRET_API_VERSION)
            
            if missing:
                self._error_message = f"Missing required secrets: {', '.join(missing)}"
                logger.error(self._error_message)
                return False, self._error_message
            
            self._initialized = True
            logger.info("Key Vault secrets loaded successfully")
            return True, "Key Vault connected successfully"
            
        except HttpResponseError as e:
            if "Forbidden" in str(e):
                self._error_message = "Access denied. Ensure Managed Identity has 'Key Vault Secrets User' role."
            elif "public network access" in str(e).lower():
                self._error_message = "Public network access disabled. Connect via private endpoint."
            else:
                self._error_message = f"Key Vault error: {str(e)}"
            logger.error(self._error_message)
            return False, self._error_message
        except Exception as e:
            self._error_message = f"Unexpected error: {str(e)}"
            logger.error(self._error_message)
            return False, self._error_message
    
    @property
    def is_initialized(self) -> bool:
        """Check if service is initialized with all required secrets."""
        return self._initialized
    
    @property
    def openai_endpoint(self) -> str:
        """Get OpenAI endpoint URL."""
        if not self._initialized:
            raise RuntimeError("KeyVaultService not initialized. Call initialize() first.")
        return self._cache.openai_endpoint or ""
    
    @property
    def chat_deployment(self) -> str:
        """Get chat model deployment name."""
        if not self._initialized:
            raise RuntimeError("KeyVaultService not initialized. Call initialize() first.")
        return self._cache.chat_deployment or ""
    
    @property
    def api_version(self) -> str:
        """Get OpenAI API version."""
        if not self._initialized:
            raise RuntimeError("KeyVaultService not initialized. Call initialize() first.")
        return self._cache.api_version or ""
    
    @property
    def storage_account_name(self) -> Optional[str]:
        """Get storage account name (optional)."""
        return self._cache.storage_account_name
    
    @property
    def storage_enabled(self) -> bool:
        """Check if storage account is configured."""
        return bool(self._cache.storage_account_name)
    
    def get_config_summary(self) -> Dict[str, Any]:
        """
        Get a summary of loaded configuration (safe to display).
        
        Returns:
            Dictionary with config info (no sensitive values exposed)
        """
        return {
            "key_vault_url": self.vault_url,
            "openai_endpoint_configured": bool(self._cache.openai_endpoint),
            "chat_deployment": self._cache.chat_deployment,
            "api_version": self._cache.api_version,
            "storage_enabled": self.storage_enabled,
            "initialized": self._initialized
        }
