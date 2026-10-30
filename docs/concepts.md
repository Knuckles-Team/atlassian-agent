# Concept Registry — atlassian-agent

> **Prefix**: `CONCEPT:ATL-*`
> **Version**: 0.13.0
> **Bridge**: [`CONCEPT:AU-ECO.messaging.native-backend-abstraction`](https://github.com/Knuckles-Team/scion-sdk/blob/main/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:AL-OS.governance.atl` | Atlassian Operations | MCP tool domain `atlassian` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-2` | Atlassian Admin Operations | MCP tool domain `atlassian_admin` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-3` | Atlassian Api Access Operations | MCP tool domain `atlassian_api_access` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-4` | Atlassian Control Operations | MCP tool domain `atlassian_control` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-5` | Atlassian Dlp Operations | MCP tool domain `atlassian_dlp` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-6` | Atlassian Org Operations | MCP tool domain `atlassian_org` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-7` | Atlassian User Mgmt Operations | MCP tool domain `atlassian_user_mgmt` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-8` | Atlassian User Provisioning Operations | MCP tool domain `atlassian_user_provisioning` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-9` | Confluence Other Operations | MCP tool domain `confluence_other` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-10` | Confluence Page Operations | MCP tool domain `confluence_page` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-11` | Confluence Space Operations | MCP tool domain `confluence_space` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-12` | Confluence User Operations | MCP tool domain `confluence_user` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-13` | Jira Comment Operations | MCP tool domain `jira_comment` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-14` | Jira Field Operations | MCP tool domain `jira_field` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-15` | Jira Issue Operations | MCP tool domain `jira_issue` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-16` | Jira Other Operations | MCP tool domain `jira_other` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-17` | Jira Project Operations | MCP tool domain `jira_project` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-18` | Jira Screen Operations | MCP tool domain `jira_screen` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-19` | Jira User Operations | MCP tool domain `jira_user` — Action-routed dynamic tool registration |
| `CONCEPT:AL-OS.governance.atl-20` | Jira Workflow Operations | MCP tool domain `jira_workflow` — Action-routed dynamic tool registration |

## Cross-Project References (from scion-sdk)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:AU-ECO.messaging.native-backend-abstraction` | Unified Toolkit Ingestion | scion-sdk |
| `CONCEPT:AU-ORCH.adapter.hot-cache-invalidation` | Confidence-Gated Router | scion-sdk |
| `CONCEPT:AU-OS.config.secrets-authentication` | Prompt Injection Defense | scion-sdk |
| `CONCEPT:AU-OS.state.cognitive-scheduler-preemption` | Cognitive Scheduler | scion-sdk |
| `CONCEPT:AU-OS.governance.reactive-multi-axis-budget` | Guardrail Engine | scion-sdk |
| `CONCEPT:AU-OS.governance.wasm-micro-agent-sandbox` | Audit Logging | scion-sdk |
| `CONCEPT:AU-KG.query.object-graph-mapper` | Knowledge Graph Core | scion-sdk |

## Synergy with scion-sdk

This project integrates with `scion-sdk` via `CONCEPT:AU-ECO.messaging.native-backend-abstraction` (Unified Toolkit Ingestion). The `atlassian_agent` MCP server registers its tools with the scion-sdk FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all ATL-* concepts.
