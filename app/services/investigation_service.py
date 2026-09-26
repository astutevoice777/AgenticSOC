import logging
from datetime import datetime, timezone
from app.models.alert import Alert, AlertAcknowledgement

logger = logging.getLogger(__name__)


class InvestigationService:
    """Service layer responsible for ingesting alerts and orchestrating investigations."""

    async def ingest_alert(self, alert: Alert) -> AlertAcknowledgement:
        """
        Receives and validates a security alert, queuing it for investigation.
        In Milestone 1.0, this confirms ingestion boundary contract.
        """
        logger.info(f"Ingested alert {alert.alert_id} for host {alert.host} with severity {alert.severity}")
        
        return AlertAcknowledgement(
            status="accepted",
            alert_id=alert.alert_id,
            message="Alert received and queued for investigation",
            received_at=datetime.now(timezone.utc),
        )
