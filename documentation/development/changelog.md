# Changelog

All notable changes to the Agentic SOC project will be documented in this file.

## [2026-09-27]

### Milestone 2.1 — Multi-Source Telemetry & Network Tool Integration
- **Added**: `NetworkEvent` model in `app/models/investigation.py`.
- **Added**: Read-only `get_network_logs` tool in `app/tools/network_tools.py` with mock network telemetry.
- **Updated**: `app/tools/__init__.py` exporting `get_network_logs`.
- **Updated**: `InvestigationAgent` in `app/agents/investigator.py` to pivot from suspicious process IDs to network telemetry, extracting `network_c2_connection` evidence.
- **Updated**: `tests/test_investigation.py` with unit tests for `get_network_logs` and multi-source cross-telemetry correlation.
- **Tested & Verified**: 7 automated tests passed.

### Milestone 2.0 — Investigation Agent & Read-Only Tool Architecture
- **Added**: `ProcessEvent`, `Evidence`, and `InvestigationResult` models in `app/models/investigation.py`.
- **Added**: Read-only `get_process_logs` tool in `app/tools/process_tools.py` with mock process telemetry.
- **Added**: `InvestigationAgent` in `app/agents/investigator.py` to query telemetry, evaluate suspicious process execution, and correlate findings.
- **Updated**: `InvestigationService` in `app/services/investigation_service.py` to trigger investigation workflow upon alert ingestion.
- **Added**: Automated unit and integration test suite in `tests/test_investigation.py`.
- **Tested & Verified**: 5 automated tests passed verifying tool queries, evidence correlation, inconclusive handling, and end-to-end API integration.

### Documentation
- **Added**: `documentation/decisions/ADR-002.md` (Read-only tool pattern for SOC agents).
- **Added**: `documentation/agents/investigator.md` (Investigation agent specification).
- **Added**: `documentation/tools/tool-architecture.md` (Tool architecture specification).
- **Updated**: `documentation/development/milestones.md`.
- **Updated**: `documentation/development/current-status.md`.
- **Updated**: `documentation/development/changelog.md`.

---

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
