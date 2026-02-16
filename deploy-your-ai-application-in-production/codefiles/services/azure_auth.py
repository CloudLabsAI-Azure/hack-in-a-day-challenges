"""
Azure Authentication Service using Managed Identity.

This module provides passwordless authentication to Azure services
using DefaultAzureCredential (Managed Identity when running on Azure VM).

Security: No API keys are used or stored anywhere!
"""
import logging
from typing import Optional

from azure.identity import DefaultAzureCredential, AzureCliCredential
from azure.core.credentials import TokenCredential

logger = logging.getLogger(__name__)


class AzureAuthService:
    """
    Azure Authentication Service using Managed Identity.
    
    When running on an Azure VM with Managed Identity enabled,
    this automatically authenticates without any credentials.
    
    For local development, falls back to Azure CLI credentials
    (requires `az login` to be completed).
    """
    
    _instance: Optional['AzureAuthService'] = None
    _credential: Optional[TokenCredential] = None
    
    def __new__(cls) -> 'AzureAuthService':
        """Singleton pattern to reuse credential across the application."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @property
    def credential(self) -> TokenCredential:
        """
        Get the Azure credential for authentication.
        
        Uses DefaultAzureCredential which tries multiple auth methods:
        1. Environment variables
        2. Managed Identity (when on Azure VM)
        3. Azure CLI (for local development)
        4. Visual Studio Code
        5. Azure PowerShell
        
        Returns:
            TokenCredential: Azure credential for authenticating to services
        """
        if self._credential is None:
            try:
                logger.info("Initializing Azure credential with Managed Identity...")
                self._credential = DefaultAzureCredential(
                    exclude_interactive_browser_credential=True,
                    exclude_shared_token_cache_credential=True
                )
                logger.info("Azure credential initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Azure credential: {e}")
                raise
        
        return self._credential
    
    def get_openai_token(self) -> str:
        """
        Get an access token for Azure OpenAI Cognitive Services.
        
        Returns:
            str: Bearer token for Azure OpenAI API calls
        """
        try:
            token = self.credential.get_token(
                "https://cognitiveservices.azure.com/.default"
            )
            return token.token
        except Exception as e:
            logger.error(f"Failed to get OpenAI token: {e}")
            raise
    
    def get_token_provider(self):
        """
        Get a token provider callable for Azure OpenAI client.
        
        Returns:
            Callable that returns a fresh token on each call
        """
        return lambda: self.get_openai_token()
    
    def validate_authentication(self) -> tuple[bool, str]:
        """
        Validate that authentication is working.
        
        Returns:
            Tuple of (success, message)
        """
        try:
            # Try to get a token to validate authentication works
            _ = self.credential.get_token(
                "https://management.azure.com/.default"
            )
            return True, "Authentication successful using Managed Identity"
        except Exception as e:
            error_msg = str(e)
            if "ManagedIdentityCredential" in error_msg:
                return False, "Managed Identity not available. Ensure you're running on an Azure VM with MI enabled."
            elif "AzureCliCredential" in error_msg:
                return False, "Azure CLI not authenticated. Run 'az login' first."
            else:
                return False, f"Authentication failed: {error_msg}"


# Singleton instance for easy import
auth_service = AzureAuthService()
