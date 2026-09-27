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

### Follow-up
Progressed to Milestone 2.0.

---

## Milestone 2.0 — Investigation Agent & Read-Only Tool Architecture

- **Status**: Implemented
- **Verification**: Verified

### Goal
Implement the Investigation Agent skeleton and the foundational Read-Only Tool abstraction for querying host process logs, correlating suspicious process creation chains, and synthesizing structured investigation evidence.

### Pre-Implementation Plan
Presented on 2026-09-27 covering goal, architecture, data flow, contracts, tool boundaries, dependencies, and testing plan. Approved explicitly by user.

### Implementation Summary
- Created `ProcessEvent`, `Evidence`, and `InvestigationResult` models in `app/models/investigation.py`.
- Created `get_process_logs` read-only tool in `app/tools/process_tools.py` with mock process telemetry.
- Created `InvestigationAgent` in `app/agents/investigator.py` to query telemetry, detect obfuscated commands and recon tools, and assemble `InvestigationResult`.
- Updated `InvestigationService` in `app/services/investigation_service.py` to trigger the investigation workflow during alert ingestion.
- Created automated test suite in `tests/test_investigation.py`.

### Files Affected
- `app/models/investigation.py`
- `app/tools/process_tools.py`
- `app/tools/__init__.py`
- `app/agents/investigator.py`
- `app/services/investigation_service.py`
- `tests/test_investigation.py`

### Testing & Verification
The user ran `python -m pytest tests/test_investigation.py -v`:
- 5 automated unit and integration tests passed.

### Follow-up
Progressed to Milestone 2.1 to add network telemetry.

---

## Milestone 2.1 — Multi-Source Telemetry & Network Tool Integration

- **Status**: Implemented
- **Verification**: Verified

### Goal
Expand the Investigation Agent with multi-source telemetry correlation by introducing the read-only `get_network_logs` tool and pivoting from suspicious process IDs to network socket connections and C2 communications.

### Pre-Implementation Plan
Presented on 2026-09-27 covering cross-telemetry correlation, `NetworkEvent` schemas, tool contracts, and testing strategy. Approved explicitly by user.

### Implementation Summary
- Created `NetworkEvent` model in `app/models/investigation.py`.
- Created `get_network_logs` read-only tool in `app/tools/network_tools.py` with mock network connection telemetry.
- Exported `get_network_logs` in `app/tools/__init__.py`.
- Enhanced `InvestigationAgent` in `app/agents/investigator.py` to pivot from suspicious PIDs to network telemetry, extracting `network_c2_connection` evidence.
- Expanded `tests/test_investigation.py` with 2 new test cases covering network tool queries and cross-source correlation.

### Files Affected
- `app/models/investigation.py`
- `app/tools/network_tools.py`
- `app/tools/__init__.py`
- `app/agents/investigator.py`
- `tests/test_investigation.py`

### Testing & Verification
The user ran `python -m pytest tests/test_investigation.py -v`:
- `test_get_process_logs_tool_matches`: PASSED
- `test_get_process_logs_tool_no_match`: PASSED
- `test_get_network_logs_tool_matches`: PASSED (network tool retrieves socket connections)
- `test_get_network_logs_tool_pid_filter`: PASSED (network tool accurately filters by PID)
- `test_investigator_correlates_process_and_network_evidence`: PASSED (produces correlated process and network C2 evidence)
- `test_investigator_handles_missing_logs`: PASSED
- `test_api_alert_ingest_with_investigation`: PASSED

### Known Limitations
- Telemetry datasets remain in-memory mock fixtures.
- User identity/authentication telemetry tools are not yet implemented.
- Agent uses rule-based correlation; LLM-powered multi-turn function calling is scheduled next.

### Documentation Changes
- Updated `documentation/tools/tool-architecture.md`
- Updated `documentation/agents/investigator.md`
- Updated `documentation/development/milestones.md`
- Updated `documentation/development/current-status.md`
- Updated `documentation/development/changelog.md`

### Next Iteration / Proposed Milestone
Milestone 2.2 — LLM Brain Integration (Function/Tool Calling with Google Gemini).
