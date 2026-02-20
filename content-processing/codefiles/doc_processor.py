"""
Intelligent Content Processing - Document Processor Module
Azure AI Document Intelligence integration for OCR extraction
"""

import os
import io
from dotenv import load_dotenv

load_dotenv()


class DocumentProcessor:
    """Handles document analysis using Azure AI Document Intelligence."""

    def __init__(self):
        self.endpoint = os.getenv("DOC_INTELLIGENCE_ENDPOINT")
        self.key = os.getenv("DOC_INTELLIGENCE_KEY")
        self._client = None

    @property
    def client(self):
        """Lazy-initialize the Document Intelligence client."""
        if self._client is None:
            from azure.ai.documentintelligence import DocumentIntelligenceClient
            from azure.core.credentials import AzureKeyCredential

            self._client = DocumentIntelligenceClient(
                endpoint=self.endpoint,
                credential=AzureKeyCredential(self.key),
            )
        return self._client

    def is_configured(self) -> bool:
        """Check if Document Intelligence is properly configured."""
        return bool(self.endpoint and self.key)

    def analyze_document(self, file_content: bytes, filename: str) -> dict:
        """
        Analyze a document using Document Intelligence Layout model.

        Args:
            file_content: Raw bytes of the document file
            filename: Original filename (used to determine content type)

        Returns:
            dict with extracted_text, tables, key_value_pairs, and metadata
        """
        try:
            from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

            # Determine content type
            ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else "txt"
            content_type_map = {
                "pdf": "application/pdf",
                "jpg": "image/jpeg",
                "jpeg": "image/jpeg",
                "png": "image/png",
                "tiff": "image/tiff",
                "tif": "image/tiff",
                "bmp": "image/bmp",
            }
            content_type = content_type_map.get(ext, "application/octet-stream")

            # Analyze with OCR/Read model
            poller = self.client.begin_analyze_document(
                model_id="prebuilt-read",
                analyze_request=file_content,
                content_type=content_type,
            )
            result = poller.result()

            # Extract text content
            extracted_text = ""
            if result.content:
                extracted_text = result.content

            # Extract tables
            tables = []
            if result.tables:
                for table_idx, table in enumerate(result.tables):
                    table_data = {
                        "table_index": table_idx,
                        "row_count": table.row_count,
                        "column_count": table.column_count,
                        "cells": [],
                    }
                    if table.cells:
                        for cell in table.cells:
                            table_data["cells"].append(
                                {
                                    "row": cell.row_index,
                                    "column": cell.column_index,
                                    "content": cell.content,
                                    "kind": getattr(cell, "kind", "content"),
                                }
                            )
                    tables.append(table_data)

            # Extract key-value pairs
            key_value_pairs = []
            if result.key_value_pairs:
                for kv in result.key_value_pairs:
                    key_text = kv.key.content if kv.key else ""
                    value_text = kv.value.content if kv.value else ""
                    confidence = getattr(kv, "confidence", None)
                    key_value_pairs.append(
                        {
                            "key": key_text,
                            "value": value_text,
                            "confidence": confidence,
                        }
                    )

            # Build summary
            page_count = len(result.pages) if result.pages else 0

            return {
                "success": True,
                "extracted_text": extracted_text,
                "tables": tables,
                "key_value_pairs": key_value_pairs,
                "metadata": {
                    "page_count": page_count,
                    "table_count": len(tables),
                    "kv_pair_count": len(key_value_pairs),
                    "text_length": len(extracted_text),
                    "content_type": content_type,
                    "filename": filename,
                },
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "extracted_text": "",
                "tables": [],
                "key_value_pairs": [],
                "metadata": {"filename": filename},
            }

    def analyze_from_text(self, text: str, filename: str = "text_input.txt") -> dict:
        """
        Create a result dict from raw text (for sample data or pre-extracted OCR).

        Args:
            text: Pre-extracted OCR text
            filename: Source filename

        Returns:
            dict matching the analyze_document output format
        """
        return {
            "success": True,
            "extracted_text": text,
            "tables": [],
            "key_value_pairs": [],
            "metadata": {
                "page_count": 1,
                "table_count": 0,
                "kv_pair_count": 0,
                "text_length": len(text),
                "content_type": "text/plain",
                "filename": filename,
            },
        }
