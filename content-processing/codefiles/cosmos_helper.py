"""
Intelligent Content Processing - Cosmos DB Helper Module
Dual-container operations for ProcessedDocuments and ReviewQueue
"""

import os
import uuid
from datetime import datetime, timezone
from dotenv import load_dotenv
from azure.cosmos import CosmosClient, exceptions

load_dotenv()


class CosmosHelper:
    """Manages Cosmos DB operations for the dual-container routing architecture."""

    def __init__(self):
        self.endpoint = os.getenv("COSMOS_ENDPOINT")
        self.key = os.getenv("COSMOS_KEY")
        self.database_name = os.getenv("DATABASE_NAME", "ContentProcessingDB")
        self._client = None
        self._database = None
        self._processed_container = None
        self._review_container = None

    def is_configured(self) -> bool:
        """Check if Cosmos DB is properly configured."""
        return bool(self.endpoint and self.key)

    @property
    def client(self):
        if self._client is None:
            self._client = CosmosClient(self.endpoint, credential=self.key)
        return self._client

    @property
    def database(self):
        if self._database is None:
            self._database = self.client.get_database_client(self.database_name)
        return self._database

    @property
    def processed_container(self):
        if self._processed_container is None:
            self._processed_container = self.database.get_container_client(
                "ProcessedDocuments"
            )
        return self._processed_container

    @property
    def review_container(self):
        if self._review_container is None:
            self._review_container = self.database.get_container_client("ReviewQueue")
        return self._review_container

    # ── Save Operations ─────────────────────────────────────────────

    def save_processed_document(self, document_data: dict) -> str:
        """Save an auto-approved document to ProcessedDocuments."""
        doc_id = str(uuid.uuid4())
        item = {
            "id": doc_id,
            "documentId": doc_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "docType": document_data.get("doc_type", "UNKNOWN"),
            "filename": document_data.get("filename", "unknown"),
            "classification": document_data.get("classification", {}),
            "extraction": document_data.get("extraction", {}),
            "validation": document_data.get("validation", {}),
            "routing_decision": "AUTO_APPROVE",
            "confidence_score": document_data.get("confidence_score", 0.0),
            "review_status": "AUTO_APPROVED",
            "ocr_metadata": document_data.get("ocr_metadata", {}),
            "blob_url": document_data.get("blob_url", ""),
        }
        try:
            self.processed_container.create_item(body=item)
            return doc_id
        except exceptions.CosmosHttpResponseError as e:
            raise Exception(f"Failed to save to ProcessedDocuments: {str(e)}")

    def save_to_review_queue(self, document_data: dict) -> str:
        """Save a low-confidence document to ReviewQueue."""
        doc_id = str(uuid.uuid4())
        item = {
            "id": doc_id,
            "documentId": doc_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "docType": document_data.get("doc_type", "UNKNOWN"),
            "filename": document_data.get("filename", "unknown"),
            "classification": document_data.get("classification", {}),
            "extraction": document_data.get("extraction", {}),
            "validation": document_data.get("validation", {}),
            "routing_decision": "MANUAL_REVIEW",
            "confidence_score": document_data.get("confidence_score", 0.0),
            "review_status": "PENDING",
            "review_reasons": document_data.get("review_reasons", []),
            "ocr_text": document_data.get("ocr_text", ""),
            "ocr_metadata": document_data.get("ocr_metadata", {}),
            "blob_url": document_data.get("blob_url", ""),
        }
        try:
            self.review_container.create_item(body=item)
            return doc_id
        except exceptions.CosmosHttpResponseError as e:
            raise Exception(f"Failed to save to ReviewQueue: {str(e)}")

    # ── Read Operations ─────────────────────────────────────────────

    def get_processed_documents(self, limit: int = 50) -> list:
        """Get recent auto-approved / human-approved documents."""
        try:
            query = f"SELECT * FROM c ORDER BY c.timestamp DESC OFFSET 0 LIMIT {limit}"
            return list(
                self.processed_container.query_items(
                    query=query, enable_cross_partition_query=True
                )
            )
        except Exception:
            return []

    def get_review_queue(self, status: str = "PENDING") -> list:
        """Get documents pending human review."""
        try:
            if status == "ALL":
                query = "SELECT * FROM c ORDER BY c.timestamp DESC"
            else:
                query = f"SELECT * FROM c WHERE c.review_status = '{status}' ORDER BY c.timestamp DESC"
            return list(
                self.review_container.query_items(
                    query=query, enable_cross_partition_query=True
                )
            )
        except Exception:
            return []

    def get_all_documents(self) -> list:
        """Get all documents from both containers for analytics."""
        processed = self.get_processed_documents(limit=200)
        review = self.get_review_queue(status="ALL")
        return processed + review

    # ── Review Actions ──────────────────────────────────────────────

    def approve_document(self, document_id: str) -> bool:
        """Approve a document from ReviewQueue → move to ProcessedDocuments."""
        try:
            # Find in review queue
            items = list(
                self.review_container.query_items(
                    query=f"SELECT * FROM c WHERE c.id = '{document_id}'",
                    enable_cross_partition_query=True,
                )
            )
            if not items:
                return False

            item = items[0]

            # Update status and move to processed
            item["review_status"] = "HUMAN_APPROVED"
            item["reviewed_at"] = datetime.now(timezone.utc).isoformat()
            item["routing_decision"] = "HUMAN_APPROVED"

            # Save to ProcessedDocuments
            self.processed_container.create_item(body={**item, "id": str(uuid.uuid4())})

            # Delete from ReviewQueue
            self.review_container.delete_item(
                item=document_id, partition_key=item["documentId"]
            )
            return True

        except Exception:
            return False

    def reject_document(self, document_id: str, reason: str = "") -> bool:
        """Reject a document in the ReviewQueue."""
        try:
            items = list(
                self.review_container.query_items(
                    query=f"SELECT * FROM c WHERE c.id = '{document_id}'",
                    enable_cross_partition_query=True,
                )
            )
            if not items:
                return False

            item = items[0]
            item["review_status"] = "REJECTED"
            item["rejection_reason"] = reason
            item["reviewed_at"] = datetime.now(timezone.utc).isoformat()

            self.review_container.replace_item(item=document_id, body=item)
            return True

        except Exception:
            return False

    # ── Analytics Queries ───────────────────────────────────────────

    def get_analytics(self) -> dict:
        """Get processing analytics across both containers."""
        try:
            processed = self.get_processed_documents(limit=500)
            review_all = self.get_review_queue(status="ALL")

            auto_approved = [d for d in processed if d.get("review_status") == "AUTO_APPROVED"]
            human_approved = [d for d in processed if d.get("review_status") == "HUMAN_APPROVED"]
            pending = [d for d in review_all if d.get("review_status") == "PENDING"]
            rejected = [d for d in review_all if d.get("review_status") == "REJECTED"]

            all_docs = processed + review_all
            confidence_scores = [
                d.get("confidence_score", 0) for d in all_docs if d.get("confidence_score")
            ]
            avg_confidence = (
                sum(confidence_scores) / len(confidence_scores)
                if confidence_scores
                else 0
            )

            # Document type distribution
            doc_types = {}
            for d in all_docs:
                dt = d.get("docType", "UNKNOWN")
                doc_types[dt] = doc_types.get(dt, 0) + 1

            return {
                "total_processed": len(all_docs),
                "auto_approved": len(auto_approved),
                "human_approved": len(human_approved),
                "pending_review": len(pending),
                "rejected": len(rejected),
                "avg_confidence": round(avg_confidence, 3),
                "confidence_scores": confidence_scores,
                "doc_type_distribution": doc_types,
            }
        except Exception:
            return {
                "total_processed": 0,
                "auto_approved": 0,
                "human_approved": 0,
                "pending_review": 0,
                "rejected": 0,
                "avg_confidence": 0,
                "confidence_scores": [],
                "doc_type_distribution": {},
            }
