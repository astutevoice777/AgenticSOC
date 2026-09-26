# Development Milestones

## Milestone 1.0 — API Contract & Alert Ingestion Skeleton

- **Status**: Implemented
- **Verification**: Verified

### Goal
Establish the initial REST API boundary for receiving security alerts via HTTP `POST /api/v1/alerts`, validate incoming payloads strictly against a Pydantic schema, route alerts through an isolated `InvestigationService`, and return an immediate structured acknowledgement (`202 Accepted`).

### Pre-Implementation Plan
Presented on 2026-09-26 covering architecture, data flow, contracts, dependencies, and testing plan. Approved explicitly by user.

### Implementation Summary
- Created `Alert` and `AlertAcknowledgement` Pydantic models in `app/models/alert.py`.
- Created `InvestigationService` in `app/services/investigation_service.py` to decouple ingestion from the HTTP transport layer.
- Created `alerts` APIRouter in `app/api/alerts.py` mounting `POST /api/v1/alerts`.
- Initialized FastAPI application in `app/main.py` with `/health` and alerts router inclusion.

### Files Affected
- `app/models/alert.py`
- `app/services/investigation_service.py`
- `app/api/alerts.py`
- `app/main.py`

### Testing & Verification
The user executed manual verification tests against the local server (`uvicorn app.main:app --reload --port 8000`):
1. `GET /health` returned `200 OK` with `{"status": "healthy"}`.
2. `POST /api/v1/alerts` with valid alert payload returned `202 Accepted` with `AlertAcknowledgement` containing `alert_id: ALERT-001`.
3. `POST /api/v1/alerts` with missing fields returned `422 Unprocessable Content` with field-level validation errors.

### Known Limitations
- Ingested alerts are logged and acknowledged in-memory; persistent database storage and asynchronous queueing are not yet connected.
- Endpoint is unauthenticated (planned for a future security milestone).
- Agents and LLMs are not yet integrated into the investigation pipeline.

### Documentation Changes
- Created `documentation/api/alert-api.md`
- Created `documentation/architecture/system-overview.md`
- Created `documentation/decisions/ADR-001.md`
- Created `documentation/development/milestones.md`
- Created `documentation/development/current-status.md`
- Created `documentation/development/changelog.md`

### Next Iteration / Proposed Milestone
Milestone 2.0 — Investigation Agent Skeleton & Read-Only Tool Interface.
