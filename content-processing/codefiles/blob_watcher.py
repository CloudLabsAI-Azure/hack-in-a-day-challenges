"""
Intelligent Content Processing - Blob Storage Watcher Module
Monitors Azure Blob Storage container for newly uploaded documents
and triggers the AI processing pipeline automatically.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Supported document file extensions for auto-processing
SUPPORTED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".tiff", ".tif", ".bmp", ".txt"}


class BlobWatcher:
    """Monitors Azure Blob Storage for new document uploads."""

    def __init__(self):
        self.connection_string = os.getenv("STORAGE_CONNECTION_STRING")
        self.container_name = os.getenv("BLOB_CONTAINER_NAME", "documents")
        self._client = None
        self._container = None

    def is_configured(self) -> bool:
        """Check if Blob Storage is properly configured for watching."""
        return bool(self.connection_string)

    @property
    def client(self):
        """Lazy-initialize the BlobServiceClient."""
        if self._client is None:
            from azure.storage.blob import BlobServiceClient

            self._client = BlobServiceClient.from_connection_string(
                self.connection_string
            )
        return self._client

    @property
    def container(self):
        """Get the container client for the monitored container."""
        if self._container is None:
            self._container = self.client.get_container_client(self.container_name)
        return self._container

    def list_blob_names(self) -> set:
        """List all blob names in the monitored container."""
        try:
            return {blob.name for blob in self.container.list_blobs()}
        except Exception:
            return set()

    def list_supported_blobs(self) -> set:
        """List only blobs with supported document file extensions."""
        all_blobs = self.list_blob_names()
        return {
            name
            for name in all_blobs
            if any(name.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS)
        }

    def download_blob(self, blob_name: str):
        """Download blob content as bytes. Returns None on failure."""
        try:
            blob_client = self.container.get_blob_client(blob_name)
            return blob_client.download_blob().readall()
        except Exception:
            return None

    def get_blob_url(self, blob_name: str) -> str:
        """Construct the full URL for a blob."""
        try:
            base = self.client.url
            # Ensure no double slash
            if base.endswith("/"):
                return f"{base}{self.container_name}/{blob_name}"
            return f"{base}/{self.container_name}/{blob_name}"
        except Exception:
            return ""
