"""
Azure Blob Storage Service for Session History.

This module handles session persistence to Azure Blob Storage.
Sessions are saved as JSON files for easy retrieval and analysis.

Security: Uses Managed Identity - no connection strings or keys!
"""
import json
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional

from azure.storage.blob import BlobServiceClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError, ResourceExistsError

from .azure_auth import auth_service
from .keyvault_service import KeyVaultService

logger = logging.getLogger(__name__)


class StorageService:
    """
    Azure Blob Storage Service for chat session persistence.
    
    Saves and retrieves chat sessions using Managed Identity authentication.
    Sessions are stored as JSON blobs in a configurable container.
    """
    
    def __init__(
        self,
        keyvault_service: KeyVaultService,
        container_name: str = "chat-sessions"
    ):
        """
        Initialize Storage Service.
        
        Args:
            keyvault_service: Initialized KeyVaultService with storage config
            container_name: Name of blob container for sessions
        """
        self.kv_service = keyvault_service
        self.container_name = container_name
        self._client: Optional[BlobServiceClient] = None
        self._container_client: Optional[ContainerClient] = None
        self._initialized = False
        self._enabled = False
        self._error_message: Optional[str] = None
    
    @property
    def storage_url(self) -> str:
        """Get the storage account URL."""
        account_name = self.kv_service.storage_account_name
        if not account_name:
            return ""
        return f"https://{account_name}.blob.core.windows.net"
    
    @property
    def client(self) -> BlobServiceClient:
        """Get or create the Blob Service client."""
        if self._client is None:
            self._client = BlobServiceClient(
                account_url=self.storage_url,
                credential=auth_service.credential
            )
        return self._client
    
    @property
    def container_client(self) -> ContainerClient:
        """Get or create the container client."""
        if self._container_client is None:
            self._container_client = self.client.get_container_client(self.container_name)
        return self._container_client
    
    def initialize(self) -> tuple[bool, str]:
        """
        Initialize the storage service and ensure container exists.
        
        Returns:
            Tuple of (success, message)
        """
        # Check if storage is configured
        if not self.kv_service.storage_enabled:
            self._enabled = False
            self._initialized = True
            logger.info("Storage service disabled (no StorageAccountName in Key Vault)")
            return True, "Session history disabled (storage not configured)"
        
        try:
            logger.info(f"Initializing storage service: {self.storage_url}")
            
            # Ensure container exists
            try:
                self.container_client.create_container()
                logger.info(f"Created container: {self.container_name}")
            except ResourceExistsError:
                logger.info(f"Container already exists: {self.container_name}")
            
            self._enabled = True
            self._initialized = True
            logger.info("Storage service initialized successfully")
            return True, "Session history enabled"
            
        except Exception as e:
            error_msg = str(e)
            if "AuthorizationFailure" in error_msg:
                self._error_message = "Storage access denied. Ensure 'Storage Blob Data Contributor' role assigned."
            else:
                self._error_message = f"Storage initialization failed: {error_msg}"
            
            logger.warning(f"Storage service not available: {self._error_message}")
            # Don't fail the app - storage is optional
            self._enabled = False
            self._initialized = True
            return True, f"Session history disabled: {self._error_message}"
    
    @property
    def is_enabled(self) -> bool:
        """Check if storage service is enabled and working."""
        return self._enabled
    
    @property
    def is_initialized(self) -> bool:
        """Check if service has been initialized."""
        return self._initialized
    
    def save_session(
        self,
        session_id: str,
        messages: List[Dict[str, str]],
        metadata: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, str]:
        """
        Save a chat session to blob storage.
        
        Args:
            session_id: Unique session identifier
            messages: List of chat messages
            metadata: Optional additional metadata
            
        Returns:
            Tuple of (success, message)
        """
        if not self._enabled:
            return True, "Session history disabled"
        
        try:
            session_data = {
                "session_id": session_id,
                "timestamp": datetime.utcnow().isoformat(),
                "message_count": len(messages),
                "messages": messages,
                "metadata": metadata or {}
            }
            
            blob_name = f"{session_id}.json"
            blob_client = self.client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            
            blob_client.upload_blob(
                json.dumps(session_data, indent=2, default=str),
                overwrite=True
            )
            
            logger.debug(f"Session saved: {blob_name}")
            return True, "Session saved"
            
        except Exception as e:
            logger.warning(f"Failed to save session: {e}")
            return False, f"Failed to save session: {str(e)}"
    
    def load_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Load a chat session from blob storage.
        
        Args:
            session_id: Session identifier to load
            
        Returns:
            Session data dict or None if not found
        """
        if not self._enabled:
            return None
        
        try:
            blob_name = f"{session_id}.json"
            blob_client = self.client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            
            download = blob_client.download_blob()
            content = download.readall()
            return json.loads(content)
            
        except ResourceNotFoundError:
            logger.debug(f"Session not found: {session_id}")
            return None
        except Exception as e:
            logger.warning(f"Failed to load session: {e}")
            return None
    
    def list_sessions(self, limit: int = 50) -> List[Dict[str, Any]]:
        """
        List recent chat sessions.
        
        Args:
            limit: Maximum number of sessions to return
            
        Returns:
            List of session metadata dicts
        """
        if not self._enabled:
            return []
        
        try:
            sessions = []
            blobs = self.container_client.list_blobs()
            
            for blob in blobs:
                if len(sessions) >= limit:
                    break
                    
                sessions.append({
                    "session_id": blob.name.replace(".json", ""),
                    "last_modified": blob.last_modified,
                    "size": blob.size
                })
            
            # Sort by most recent first
            sessions.sort(key=lambda x: x["last_modified"], reverse=True)
            return sessions
            
        except Exception as e:
            logger.warning(f"Failed to list sessions: {e}")
            return []
    
    def delete_session(self, session_id: str) -> tuple[bool, str]:
        """
        Delete a chat session from storage.
        
        Args:
            session_id: Session identifier to delete
            
        Returns:
            Tuple of (success, message)
        """
        if not self._enabled:
            return True, "Storage not enabled"
        
        try:
            blob_name = f"{session_id}.json"
            blob_client = self.client.get_blob_client(
                container=self.container_name,
                blob=blob_name
            )
            blob_client.delete_blob()
            
            logger.info(f"Session deleted: {session_id}")
            return True, "Session deleted"
            
        except ResourceNotFoundError:
            return True, "Session not found"
        except Exception as e:
            logger.warning(f"Failed to delete session: {e}")
            return False, f"Failed to delete: {str(e)}"
