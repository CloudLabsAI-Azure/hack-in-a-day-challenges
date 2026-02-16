"""
Azure OpenAI Service for Chat Completions.

This module provides a clean interface to Azure OpenAI using Managed Identity.
All authentication is handled via Azure tokens - no API keys used!

Security: Uses token-based authentication via Managed Identity.
"""
import logging
from typing import List, Dict, Any, Generator, Optional

from openai import AzureOpenAI
from openai.types.chat import ChatCompletion, ChatCompletionChunk

from .azure_auth import auth_service
from .keyvault_service import KeyVaultService

logger = logging.getLogger(__name__)


class OpenAIService:
    """
    Azure OpenAI Service for chat completions.
    
    Uses Managed Identity for authentication through private endpoints.
    Supports both streaming and non-streaming responses.
    """
    
    def __init__(self, keyvault_service: KeyVaultService):
        """
        Initialize OpenAI Service.
        
        Args:
            keyvault_service: Initialized KeyVaultService with OpenAI config
        """
        self.kv_service = keyvault_service
        self._client: Optional[AzureOpenAI] = None
        self._initialized = False
        self._error_message: Optional[str] = None
    
    @property
    def client(self) -> AzureOpenAI:
        """Get or create the Azure OpenAI client."""
        if self._client is None:
            self._client = AzureOpenAI(
                azure_endpoint=self.kv_service.openai_endpoint,
                api_version=self.kv_service.api_version,
                azure_ad_token_provider=auth_service.get_token_provider()
            )
        return self._client
    
    def initialize(self) -> tuple[bool, str]:
        """
        Initialize the OpenAI service and validate connection.
        
        Returns:
            Tuple of (success, message)
        """
        try:
            if not self.kv_service.is_initialized:
                return False, "KeyVaultService not initialized"
            
            logger.info(f"Initializing OpenAI client for endpoint: {self.kv_service.openai_endpoint}")
            
            # Create the client (this doesn't make a network call yet)
            _ = self.client
            
            self._initialized = True
            logger.info("OpenAI client initialized successfully")
            return True, f"OpenAI connected (Model: {self.kv_service.chat_deployment})"
            
        except Exception as e:
            self._error_message = f"Failed to initialize OpenAI client: {str(e)}"
            logger.error(self._error_message)
            return False, self._error_message
    
    @property
    def is_initialized(self) -> bool:
        """Check if service is initialized."""
        return self._initialized
    
    @property
    def model_name(self) -> str:
        """Get the deployment/model name."""
        return self.kv_service.chat_deployment
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        system_prompt: str,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        stream: bool = True
    ) -> Generator[str, None, None] | str:
        """
        Send a chat completion request to Azure OpenAI.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            system_prompt: System message to guide AI behavior
            max_tokens: Maximum tokens in response
            temperature: Creativity level (0.0-2.0)
            stream: Whether to stream the response
            
        Yields/Returns:
            If stream=True: Yields response chunks as they arrive
            If stream=False: Returns complete response string
        """
        if not self._initialized:
            raise RuntimeError("OpenAIService not initialized. Call initialize() first.")
        
        # Prepare messages with system prompt
        api_messages = [{"role": "system", "content": system_prompt}]
        api_messages.extend(messages)
        
        try:
            if stream:
                return self._stream_response(api_messages, max_tokens, temperature)
            else:
                return self._complete_response(api_messages, max_tokens, temperature)
                
        except Exception as e:
            logger.error(f"Chat completion error: {e}")
            raise
    
    def _stream_response(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float
    ) -> Generator[str, None, None]:
        """
        Stream response chunks from Azure OpenAI.
        
        Yields:
            Response text chunks as they arrive
        """
        response = self.client.chat.completions.create(
            model=self.kv_service.chat_deployment,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True
        )
        
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
    
    def _complete_response(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int,
        temperature: float
    ) -> str:
        """
        Get complete response from Azure OpenAI.
        
        Returns:
            Complete response text
        """
        response = self.client.chat.completions.create(
            model=self.kv_service.chat_deployment,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=False
        )
        
        return response.choices[0].message.content or ""
    
    def test_connection(self) -> tuple[bool, str]:
        """
        Test the OpenAI connection with a simple request.
        
        Returns:
            Tuple of (success, message)
        """
        try:
            response = self.client.chat.completions.create(
                model=self.kv_service.chat_deployment,
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5,
                temperature=0
            )
            
            if response.choices:
                return True, "OpenAI connection test successful"
            else:
                return False, "No response received from OpenAI"
                
        except Exception as e:
            error_msg = str(e)
            if "custom subdomain" in error_msg.lower():
                return False, "Custom subdomain required for token auth. Configure in Azure Portal."
            elif "404" in error_msg:
                return False, f"Model deployment '{self.kv_service.chat_deployment}' not found."
            elif "Unauthorized" in error_msg or "401" in error_msg:
                return False, "Authentication failed. Check Managed Identity roles."
            else:
                return False, f"Connection test failed: {error_msg}"
