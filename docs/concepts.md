# Concept Registry — atlassian-agent

> **Prefix**: `CONCEPT:ATL-*`
> **Version**: 0.13.0
> **Bridge**: [`CONCEPT:ECO-4.0`](https://github.com/Knuckles-Team/agent-utilities/blob/main/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:ATL-001` | Atlassian Operations | MCP tool domain `atlassian` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-002` | Atlassian Admin Operations | MCP tool domain `atlassian_admin` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-003` | Atlassian Api Access Operations | MCP tool domain `atlassian_api_access` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-004` | Atlassian Control Operations | MCP tool domain `atlassian_control` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-005` | Atlassian Dlp Operations | MCP tool domain `atlassian_dlp` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-006` | Atlassian Org Operations | MCP tool domain `atlassian_org` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-007` | Atlassian User Mgmt Operations | MCP tool domain `atlassian_user_mgmt` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-008` | Atlassian User Provisioning Operations | MCP tool domain `atlassian_user_provisioning` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-009` | Confluence Other Operations | MCP tool domain `confluence_other` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-010` | Confluence Page Operations | MCP tool domain `confluence_page` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-011` | Confluence Space Operations | MCP tool domain `confluence_space` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-012` | Confluence User Operations | MCP tool domain `confluence_user` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-013` | Jira Comment Operations | MCP tool domain `jira_comment` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-014` | Jira Field Operations | MCP tool domain `jira_field` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-015` | Jira Issue Operations | MCP tool domain `jira_issue` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-016` | Jira Other Operations | MCP tool domain `jira_other` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-017` | Jira Project Operations | MCP tool domain `jira_project` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-018` | Jira Screen Operations | MCP tool domain `jira_screen` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-019` | Jira User Operations | MCP tool domain `jira_user` — Action-routed dynamic tool registration |
| `CONCEPT:ATL-020` | Jira Workflow Operations | MCP tool domain `jira_workflow` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:ECO-4.0` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:ORCH-1.2` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:OS-5.1` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:OS-5.2` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:OS-5.3` | Guardrail Engine | agent-utilities |
| `CONCEPT:OS-5.4` | Audit Logging | agent-utilities |
| `CONCEPT:KG-2.0` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:ECO-4.0` (Unified Toolkit Ingestion). The `atlassian_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all ATL-* concepts.
