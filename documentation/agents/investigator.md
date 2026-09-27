# Investigation Agent Specification

**Status**: Implemented  
**Verification**: Verified  
**Component**: `app/agents/investigator.py`  

---

## 1. Purpose

The Investigation Agent is responsible for answering the core operational question:

> **"What actually happened on the host surrounding this security alert?"**

It gathers telemetry through read-only tools, correlates multi-source events (processes and network connections), inspects command execution sequences and parent-child process relationships, and synthesizes a structured `InvestigationResult`.

---

## 2. Responsibilities

- Receive a structured `Alert` schema.
- Formulate targeted queries for host telemetry.
- Invoke read-only tools:
  - `get_process_logs`
  - `get_network_logs`
- Perform cross-telemetry correlation: pivot from suspicious process IDs to network socket logs.
- Detect indicators of compromise (e.g., encoded command lines, anomalous child reconnaissance binaries, outbound C2 traffic).
- Structure discrete findings into `Evidence` objects with confidence scores.
- Formulate an overall investigation verdict (`suspicious`, `benign`, or `inconclusive`).

---

## 3. Explicit Non-Responsibilities

- **The Investigation Agent does NOT execute direct database or raw log queries**: All access is mediated by read-only tools.
- **The Investigation Agent does NOT take containment or response actions**: It produces analysis only; remediation is deferred to human-in-the-loop workflows.
- **The Investigation Agent does NOT manage high-level triage routing**: Orchestration across multiple specialized agents is handled by the Orchestrator service.

---

## 4. Interfaces & Schemas

### Input
- `Alert` ([`app/models/alert.py`](file:///home/astute/Projects/AgenticSOC/app/models/alert.py))

### Tools Available
- `get_process_logs(host, timestamp, window_minutes, process_name)` ([`app/tools/process_tools.py`](file:///home/astute/Projects/AgenticSOC/app/tools/process_tools.py))
- `get_network_logs(host, timestamp, window_minutes, process_id, destination_ip)` ([`app/tools/network_tools.py`](file:///home/astute/Projects/AgenticSOC/app/tools/network_tools.py))

### Output
- `InvestigationResult` ([`app/models/investigation.py`](file:///home/astute/Projects/AgenticSOC/app/models/investigation.py)) containing:
  - `alert_id`: ID of the investigated alert.
  - `host`: Hostname where events occurred.
  - `verdict`: `"suspicious" | "benign" | "inconclusive"`.
  - `summary`: Narrative synthesis of findings.
  - `evidence`: List of `Evidence` objects (`artifact_type`, `description`, `data`, `confidence`).
  - `investigated_at`: UTC timestamp of investigation completion.

---

## 5. Failure Modes & Edge Cases

- **No Logs Found**: If telemetry is missing, the agent returns an `inconclusive` verdict safely without crashing.
- **Process Found Without Network Traffic**: The agent correlates available process evidence even if network telemetry yields no matching sockets.
- **Timezone Normalization**: Timezone-aware UTC comparisons prevent window filtering discrepancies.
