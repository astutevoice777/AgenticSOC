# Changelog

All notable changes to the Agentic SOC project will be documented in this file.

## [2026-09-26]

### Milestone 1.0 — Alert Ingestion API Skeleton
- **Added**: `Alert` and `AlertAcknowledgement` Pydantic models in `app/models/alert.py`.
- **Added**: `InvestigationService` in `app/services/investigation_service.py` for decoupled domain logic.
- **Added**: `POST /api/v1/alerts` endpoint in `app/api/alerts.py` returning HTTP 202 Accepted.
- **Added**: `GET /health` endpoint and FastAPI app initialization in `app/main.py`.
- **Tested & Verified**: Health check, valid alert payload ingestion, and invalid schema rejection with HTTP 422.

### Documentation
- **Added**: `documentation/api/alert-api.md` (API specification).
- **Added**: `documentation/architecture/system-overview.md` (System overview).
- **Added**: `documentation/decisions/ADR-001.md` (ADR for REST API boundary).
- **Added**: `documentation/development/milestones.md` (Milestone history).
- **Added**: `documentation/development/current-status.md` (Current system state).
- **Added**: `documentation/development/changelog.md` (Project changelog).
