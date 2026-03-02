"""
Event Grid Helper Module
Provides functions to publish security risk events to Azure Event Grid.
"""

from azure.eventgrid import EventGridPublisherClient, EventGridEvent
from azure.core.credentials import AzureKeyCredential
from datetime import datetime
import uuid


class EventGridHelper:
    """Helper class for publishing security events to Azure Event Grid."""

    def __init__(self, endpoint: str, key: str):
        self.client = EventGridPublisherClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )

    def publish_risk_alert(self, risk_data: dict) -> bool:
        """
        Publish a security risk alert to Event Grid.
        Only publishes CRITICAL and HIGH severity risks.
        """
        severity = risk_data.get("severity", "LOW")
        if severity not in ["CRITICAL", "HIGH"]:
            return False

        try:
            event = EventGridEvent(
                id=str(uuid.uuid4()),
                event_type="DataSecurity.RiskDetected",
                subject=f"/security/risks/{risk_data.get('risk_id', 'unknown')}",
                data={
                    "risk_id": risk_data.get("risk_id", ""),
                    "severity": severity,
                    "category": risk_data.get("category", ""),
                    "description": risk_data.get("description", ""),
                    "affected_resource": risk_data.get("affected_resource", ""),
                    "affected_data_classification": risk_data.get("affected_data_classification", ""),
                    "regulation_violated": risk_data.get("regulation_violated", []),
                    "recommended_action": risk_data.get("recommended_action", ""),
                    "requires_human_approval": risk_data.get("requires_human_approval", True),
                    "detected_at": datetime.utcnow().isoformat(),
                    "source": "AI-Data-Security-Agent"
                },
                data_version="1.0"
            )

            self.client.send([event])
            return True

        except Exception as e:
            print(f"Error publishing event: {str(e)}")
            return False

    def publish_batch_alerts(self, risks: list) -> dict:
        """
        Publish multiple risk alerts to Event Grid.
        Filters to only CRITICAL and HIGH severity.
        Returns counts of published and skipped events.
        """
        published = 0
        skipped = 0

        for risk in risks:
            severity = risk.get("severity", "LOW")
            if severity in ["CRITICAL", "HIGH"]:
                if self.publish_risk_alert(risk):
                    published += 1
                else:
                    skipped += 1
            else:
                skipped += 1

        return {"published": published, "skipped": skipped}
