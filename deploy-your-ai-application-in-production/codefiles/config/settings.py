"""
Application Settings and Configuration Management.

This module handles all configuration loading from environment variables.
Secrets are retrieved from Azure Key Vault at runtime - never stored locally.
"""
import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


@dataclass
class Settings:
    """
    Application settings loaded from environment variables.
    
    Note: Sensitive values (OpenAI endpoint, API keys, etc.) are NOT stored here.
    They are retrieved from Azure Key Vault at runtime using Managed Identity.
    """
    
    # Key Vault Configuration (the ONLY credential needed!)
    key_vault_name: str = field(default_factory=lambda: os.getenv("KEY_VAULT_NAME", ""))
    
    # Application Settings
    app_name: str = field(default_factory=lambda: os.getenv("APP_NAME", "Secure Enterprise Chat"))
    app_version: str = field(default_factory=lambda: os.getenv("APP_VERSION", "1.0.0"))
    debug: bool = field(default_factory=lambda: os.getenv("DEBUG", "false").lower() == "true")
    
    # Chat Configuration
    max_tokens: int = field(default_factory=lambda: int(os.getenv("MAX_TOKENS", "1000")))
    temperature: float = field(default_factory=lambda: float(os.getenv("TEMPERATURE", "0.7")))
    system_prompt: str = field(default_factory=lambda: os.getenv(
        "SYSTEM_PROMPT",
        "You are a helpful AI assistant specializing in cloud security, Azure, and enterprise architecture. "
        "Provide clear, accurate, and secure guidance."
    ))
    
    # Session Configuration
    session_container_name: str = field(default_factory=lambda: os.getenv("SESSION_CONTAINER", "chat-sessions"))
    enable_session_history: bool = field(default_factory=lambda: os.getenv("ENABLE_SESSION_HISTORY", "true").lower() == "true")
    
    # UI Configuration
    page_title: str = field(default_factory=lambda: os.getenv("PAGE_TITLE", "Secure Azure OpenAI Chat"))
    page_icon: str = field(default_factory=lambda: os.getenv("PAGE_ICON", "🔒"))
    
    # Logging
    log_level: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    
    @property
    def key_vault_url(self) -> str:
        """Get the full Key Vault URL."""
        if not self.key_vault_name:
            return ""
        return f"https://{self.key_vault_name}.vault.azure.net"
    
    def validate(self) -> tuple[bool, list[str]]:
        """
        Validate required settings are present.
        
        Returns:
            Tuple of (is_valid, list of error messages)
        """
        errors = []
        
        if not self.key_vault_name:
            errors.append("KEY_VAULT_NAME is required in .env file")
        
        return len(errors) == 0, errors


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached application settings.
    
    Uses lru_cache to ensure settings are only loaded once.
    """
    return Settings()
