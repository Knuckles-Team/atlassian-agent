# Atlassian Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/atlassian-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/atlassian-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/atlassian-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/atlassian-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/atlassian-agent)
![PyPI - License](https://img.shields.io/pypi/l/atlassian-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/atlassian-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/atlassian-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/atlassian-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/atlassian-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/atlassian-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/atlassian-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/atlassian-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/atlassian-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/atlassian-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/atlassian-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/atlassian-agent)

*Version: 2.1.0*

> **Documentation** — Installation, deployment, and usage across the MCP, Python API,
> and CLI interfaces, along with guidance for connecting to Atlassian Cloud and
> Server instances, are maintained in the [official documentation](https://knuckles-team.github.io/atlassian-agent/).

---

## Overview

**Atlassian Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Comprehensive AI agent for Jira and Confluence management..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Comprehensive AI agent for Jira and Confluence management. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools

The table below is auto-generated from the live server — do not edit by hand.

<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (`MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `atlassian_atlassian` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian_admin` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_api_access` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_control` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_dlp` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_org` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_user_mgmt` | `ATLASSIAN_USER_MGMTTOOL` | Manage atlassian user mgmt operations. |
| `atlassian_atlassian_user_provisioning` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_confluence_other` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_page` | `CONFLUENCE_PAGETOOL` | Manage Confluence page operations. |
| `atlassian_confluence_space` | `CONFLUENCE_SPACETOOL` | Manage Confluence space operations. |
| `atlassian_confluence_user` | `CONFLUENCE_USERTOOL` | Manage Confluence user operations. |
| `atlassian_ingest_confluence` | `KGTOOL` | Natively ingest Confluence pages into epistemic-graph as :Document nodes. |
| `atlassian_ingest_issues` | `KGTOOL` | Natively ingest Jira issues into epistemic-graph as typed :Issue/:Epic/:Person nodes. |
| `atlassian_jira_comment` | `JIRA_COMMENTTOOL` | Manage Jira comment operations. |
| `atlassian_jira_field` | `JIRA_FIELDTOOL` | Manage Jira field operations. |
| `atlassian_jira_issue` | `JIRA_ISSUETOOL` | Manage Jira issue operations. |
| `atlassian_jira_other` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_project` | `JIRA_PROJECTTOOL` | Manage Jira project operations. |
| `atlassian_jira_screen` | `JIRA_SCREENTOOL` | Manage Jira screen operations. |
| `atlassian_jira_user` | `JIRA_USERTOOL` | Manage Jira user operations. |
| `atlassian_jira_workflow` | `JIRA_WORKFLOWTOOL` | Manage Jira workflow operations. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>1022 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `atlassian_atlassian__user_mgmt_cloud_delete_users_account_id_manage_api_tokens_token_id` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_get_users_account_id_manage` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_get_users_account_id_manage_api_tokens` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_get_users_account_id_manage_profile` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_patch_users_account_id_manage_profile` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_post_users_account_id_manage_lifecycle_cancel_delete` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_post_users_account_id_manage_lifecycle_delete` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_post_users_account_id_manage_lifecycle_disable` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_post_users_account_id_manage_lifecycle_enable` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian__user_mgmt_cloud_put_users_account_id_manage_email` | `ATLASSIANTOOL` | Manage atlassian operations. |
| `atlassian_atlassian_admin__admin_cloud_add_resource_to_policy` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_assign_role` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_assign_role_to_group` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_create_policy` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_policy` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_policy_resource` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_v1_orgs_org_id_directory_users_account_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_directories_for_org` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_directory_user_details` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_directory_users` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_directory_users_count` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_domain_by_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_domains` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_event_actions` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_event_by_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_events` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_group` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_group_role_assignments` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_groups` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_groups_count` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_groups_stats` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_org_by_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_orgs` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_policies` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_policy_by_id` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_user_role_assignments` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_user_stats` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_users` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_poll_events` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_directory_groups` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_users_invite` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_post_v2_orgs_org_id_users_invite` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_query_workspaces_v2` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_revoke_role` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_revoke_role_to_group` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_search_groups` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_search_users` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_update_policy` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_update_policy_resource` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_admin__admin_cloud_validate_policy` | `ATLASSIAN_ADMINTOOL` | Manage atlassian admin operations. |
| `atlassian_atlassian_api_access__api_access_cloud_bulk_revoke_api_tokens` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_count_service_account_api_tokens` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_get_all_api_keys_by_org_id` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_get_all_api_tokens_by_org_id` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_get_api_key_count_by_org_id` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_get_api_token_count_by_org_id` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_get_service_account_api_token` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_revoke_api_key` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_api_access__api_access_cloud_revoke_api_tokens` | `ATLASSIAN_API_ACCESSTOOL` | Manage atlassian api access operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_add_users_to_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_attach_detach_resources_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_bulk_fetch_auth_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_create_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_create_policy_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_create_resource` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_delete_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_delete_resource` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_delete_resources` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_delete_resources_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_policies` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_policies_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_policy_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_resources` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_resources_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_get_task_status` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_publish_draft_policies` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_update_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_update_policy_v2` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_update_resource` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_control__control_cloud_ap_is_validate_policy` | `ATLASSIAN_CONTROLTOOL` | Manage atlassian control operations. |
| `atlassian_atlassian_dlp__dlp_cloud_archive_level` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_create_level` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_edit_level` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_get_level` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_get_level_list` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_publish_level` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_reorder` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_dlp__dlp_cloud_restore_level` | `ATLASSIAN_DLPTOOL` | Manage atlassian dlp operations. |
| `atlassian_atlassian_org__org_cloud_add_resource_to_policy` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_assign_role` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_assign_role_to_group` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_create_policy` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_policy` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_policy_resource` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_v1_orgs_org_id_directory_groups_group_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_v1_orgs_org_id_directory_groups_group_id_memberships_account_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_v1_orgs_org_id_directory_users_account_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships_account_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_delete_v2_orgs_org_id_directories_directory_id_users_account_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_directories_for_org` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_directory_user_details` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_directory_users` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_directory_users_count` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_domain_by_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_domains` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_event_actions` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_event_by_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_events` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_group` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_group_role_assignments` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_groups` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_groups_count` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_groups_stats` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_org_by_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_orgs` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_policies` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_policy_by_id` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_user_role_assignments` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_user_stats` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_users` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_get_v1_orgs_org_id_directory_users_account_id_last_active_dates` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_poll_events` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_directory_groups` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_directory_groups_group_id_memberships` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_directory_users_account_id_restore_access` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_directory_users_account_id_suspend_access` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_users_invite` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_assign` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v1_orgs_org_id_users_user_id_role_assignments_revoke` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_directories_directory_id_groups` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_memberships` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_assign` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_directories_directory_id_groups_group_id_role_assignments_revoke` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_restore` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_directories_directory_id_users_account_id_suspend` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_post_v2_orgs_org_id_users_invite` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_query_workspaces_v2` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_revoke_role` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_revoke_role_to_group` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_search_groups` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_search_users` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_update_policy` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_update_policy_resource` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_org__org_cloud_validate_policy` | `ATLASSIAN_ORGTOOL` | Manage atlassian org operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_create_a_group_in_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_create_a_user_in_an_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_delete_a_group` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_delete_a_user_from_an_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_a_user_from_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_all_groups_from_an_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_config` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_extension_user_schemas` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_group_resource_type` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_group_schemas` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_resource_types` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_schemas` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_scim_links` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_scim_links_by_email` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_user_resource_type` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_user_schemas` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_get_users_from_an_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_patch` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_patch_user_information_in_an_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_put` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_unlink_scim_user` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_atlassian_user_provisioning__user_provisioning_cloud_update_user_information_in_an_active_directory` | `ATLASSIAN_USER_PROVISIONINGTOOL` | Manage atlassian user provisioning operations. |
| `atlassian_confluence_other__confluence_cloud_add_calendar_event` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_check_access_by_email` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_convert_content_ids_to_content_types` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_attachment_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_blog_post` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_blogpost_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_bulk_user_lookup` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_comment_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_custom_content` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_custom_content_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_database` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_database_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_folder` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_folder_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_footer_comment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_inline_comment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_page` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_page_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_smart_link` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_smart_link_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_space` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_space_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_space_role` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_whiteboard` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_create_whiteboard_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_attachment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_attachment_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_blog_post` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_blogpost_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_comment_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_custom_content` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_custom_content_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_database` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_database_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_folder` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_folder_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_footer_comment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_forge_app_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_inline_comment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_page` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_page_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_smart_link` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_smart_link_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_space_default_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_space_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_space_role` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_whiteboard` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_delete_whiteboard_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_disable_admin_key` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_enable_admin_key` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_admin_key` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_version_details` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachment_versions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_attachments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_available_space_permissions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_available_space_roles` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_footer_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_inline_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_like_count` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_like_users` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_version_details` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_post_versions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_posts` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blog_posts_in_space` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blogpost_attachments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blogpost_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_blogpost_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_calendars` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_child_custom_content` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_child_pages` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_classification_levels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_comment_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_comment_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_attachments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_by_type` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_by_type_in_blog_post` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_by_type_in_page` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_by_type_in_space` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_version_details` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_custom_content_versions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_data_policy_metadata` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_data_policy_spaces` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_ancestors` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_descendants` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_direct_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_database_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_ancestors` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_descendants` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_direct_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_folder_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_comment_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_comment_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_comment_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_comment_version_details` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_comment_versions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_like_count` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_footer_like_users` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_forge_app_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_forge_app_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_comment_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_comment_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_comment_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_comment_version_details` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_comment_versions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_like_count` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_inline_like_users` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_label_attachments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_label_blog_posts` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_label_pages` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_ancestors` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_attachments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_descendants` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_direct_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_footer_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_inline_comments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_like_count` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_like_users` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_version_details` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_page_versions` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_pages` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_pages_in_space` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_ancestors` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_descendants` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_direct_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_smart_link_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_content_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_default_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_labels` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_permissions_assignments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_role_assignments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_role_mode` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_space_roles_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_spaces` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_task_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_tasks` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_ancestors` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_content_properties` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_content_properties_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_descendants` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_direct_children` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_get_whiteboard_operations` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_invite_by_email` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_post_blog_post_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_post_database_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_post_page_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_post_redact_blog` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_post_redact_page` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_post_whiteboard_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_put_blog_post_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_put_database_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_put_forge_app_property` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_put_page_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_put_space_default_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_put_whiteboard_classification_level` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_set_space_role_assignments` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_attachment_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_blog_post` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_blogpost_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_comment_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_custom_content` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_custom_content_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_database_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_folder_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_footer_comment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_inline_comment` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_page` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_page_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_page_title` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_smart_link_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_space_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_space_role` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_task` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_confluence_other__confluence_cloud_update_whiteboard_property_by_id` | `CONFLUENCE_OTHERTOOL` | Manage Confluence other operations. |
| `atlassian_jira_other__jira_cloud_add_actor_users` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_atlassian_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_attachment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_comment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_field_to_default_screen` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_gadget` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_issue_types_to_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_issue_types_to_issue_type_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_notifications` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_project_role_actors_to_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_screen_tab` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_screen_tab_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_security_level` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_security_level_members` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_share_permission` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_user_to_group` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_vote` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_watcher` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_add_worklog` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_addon_properties_resource_delete_addon_property_delete` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_addon_properties_resource_get_addon_properties_get` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_addon_properties_resource_get_addon_property_get` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_addon_properties_resource_put_addon_property_put` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_analyse_expression` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_app_issue_field_value_update_resource_update_issue_fields_put` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_append_mappings_for_issue_type_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_archive_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_archive_issues_async` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_archive_plan` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_archive_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_field_configuration_scheme_to_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_issue` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_issue_type_scheme_to_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_issue_type_screen_scheme_to_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_permission_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_projects_to_custom_field_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_assign_scheme_to_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_associate_projects_to_field_association_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_associate_schemes_to_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_delete_issue_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_delete_worklogs` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_edit_dashboards` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_fetch_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_get_groups` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_get_users` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_get_users_migration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_move_worklogs` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_pin_unpin_projects_async` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_set_issue_properties_by_issue` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_set_issue_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_bulk_set_issues_properties_list` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_cancel_task` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_change_filter_owner` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_clone_field_association_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_connect_to_forge_migration_fetch_task_resource_fetch_migration_task_get` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_connect_to_forge_migration_task_submission_resource_submit_task_post` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_copy_dashboard` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_count_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_associations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_component` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_custom_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_custom_field_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_custom_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_dashboard` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_field_association_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_field_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_field_configuration_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_filter` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_group` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_link_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_security_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_type_avatar` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_type_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issue_type_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_notification_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_or_update_remote_issue_link` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_permission_grant` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_permission_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_plan` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_plan_only_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_priority` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_priority_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_project_avatar` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_project_category` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_project_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_project_with_custom_template` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_related_work` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_resolution` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_screen` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_statuses` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_ui_modification` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_user` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_version` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_workflow_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_workflow_scheme_draft_from_parent` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_workflow_transition_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_create_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_actor` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_and_replace_version` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_avatar` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_comment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_comment_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_component` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_custom_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_custom_field_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_custom_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_dashboard` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_dashboard_item_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_default_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_draft_default_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_draft_workflow_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_favourite_for_filter` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_field_association_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_field_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_field_configuration_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_filter` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_forge_app_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_inactive_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_link` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_link_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_type_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_type_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_issue_type_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_notification_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_permission_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_permission_scheme_entity` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_plan_only_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_priority` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_priority_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_project_asynchronously` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_project_avatar` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_project_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_project_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_project_role_actors_from_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_related_work` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_remote_issue_link_by_global_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_remote_issue_link_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_resolution` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_screen` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_screen_tab` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_security_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_share_permission` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_statuses_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_ui_modification` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_user_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_version` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_webhook_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_scheme_draft` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_scheme_draft_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_scheme_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_transition_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_workflow_transition_rule_configurations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_worklog` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_delete_worklog_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_do_transition` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_duplicate_plan` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_dynamic_modules_resource_get_modules_get` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_dynamic_modules_resource_register_modules_post` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_dynamic_modules_resource_remove_modules_delete` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_edit_issue` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_edit_template` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_evaluate_jira_expression` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_evaluate_jsis_jira_expression` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_expand_attachment_for_humans` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_expand_attachment_for_machines` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_export_archived_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_assignable_users` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_bulk_assignable_users` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_components_for_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_groups` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_user_keys_by_query` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_users` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_users_and_groups` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_users_by_query` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_users_for_picker` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_users_with_all_permissions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_find_users_with_browse_permission` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_fully_update_project_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_accessible_project_type_by_key` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_advanced_settings` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_accessible_project_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_application_roles` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_available_dashboard_gadgets` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_dashboards` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_field_configuration_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_field_configurations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_gadgets` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_issue_field_options` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_issue_type_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_labels` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_permission_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_permissions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_project_avatars` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_project_categories` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_project_roles` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_project_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_screen_tab_fields` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_screen_tabs` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_statuses` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_system_avatars` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_user_data_classification_levels` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_users` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_users_default` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_workflow_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_all_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_alternative_issue_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_application_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_application_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_approximate_application_license_count` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_approximate_license_count` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_assigned_permission_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_atlassian_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_attachment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_attachment_content` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_attachment_meta` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_attachment_thumbnail` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_audit_records` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_auto_complete` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_auto_complete_post` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_available_priorities_by_priority_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_available_screen_fields` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_available_time_tracking_implementations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_available_transitions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_avatar_image_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_avatar_image_by_owner` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_avatar_image_by_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_avatars` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_banner` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_bulk_changelogs` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_bulk_editable_fields` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_bulk_operation_progress` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_bulk_permissions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_bulk_screen_tabs` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_change_logs` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_change_logs_by_ids` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_comment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_comment_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_comment_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_comments` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_comments_by_ids` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_component` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_component_related_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_contexts_for_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_contexts_for_field_deprecated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_create_issue_meta` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_create_issue_meta_issue_type_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_create_issue_meta_issue_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_current_user` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_custom_field_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_custom_field_contexts_for_projects_and_issue_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_custom_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_custom_fields_configurations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_dashboard` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_dashboard_item_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_dashboard_item_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_dashboards_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_default_editor` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_default_project_classification` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_default_share_scope` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_default_values` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_default_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_draft_default_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_draft_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_dynamic_webhooks_for_app` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_edit_issue_meta` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_events` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_failed_webhooks` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_favourite_filters` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_features_for_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_association_scheme_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_association_scheme_item_parameters` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_association_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_auto_complete_for_query_string` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_configuration_items` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_configuration_scheme_mappings` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_configuration_scheme_project_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_field_project_associations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_fields` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_fields_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_filter` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_filters_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_forge_app_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_forge_app_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_group` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_hierarchy` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_ids_of_worklogs_deleted_since` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_ids_of_worklogs_modified_since` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_is_watching_issue_bulk` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_all_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_limit_report` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_link` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_link_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_link_types` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_navigator_default_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_picker_resource` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_security_level` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_security_level_members` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_security_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_security_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_mappings_for_contexts` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_scheme_for_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_schemes_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_screen_scheme_mappings` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_screen_scheme_project_associations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_type_screen_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_types_for_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_watchers` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_issue_worklog` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_license` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_locale` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_my_filters` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_my_permissions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_notification_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_notification_scheme_for_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_notification_scheme_to_project_mappings` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_notification_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_options_for_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_permission_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_permission_scheme_grant` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_permission_scheme_grants` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_permitted_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_plan` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_plan_only_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_plans` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_policies` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_policy` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_precomputations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_precomputations_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_preference` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_priorities` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_priorities_by_priority_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_priority` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_priority_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_category_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_classification_config` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_components` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_components_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_context_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_email` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_fields` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_issue_security_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_issue_type_usages_for_status` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_role_actors_for_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_role_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_role_details` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_roles` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_type_by_key` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_usages_for_status` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_usages_for_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_usages_for_workflow_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_versions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_project_versions_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_projects_by_priority_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_projects_for_issue_type_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_projects_with_field_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_recent` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_redaction_status` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_related_work` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_remote_issue_link_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_remote_issue_links` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_required_workflow_scheme_mappings` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_resolution` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_resolutions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_screen_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_screens` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_screens_for_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_security_level_members` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_security_levels` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_security_levels_for_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_selectable_issue_field_options` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_selected_time_tracking_implementation` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_server_info` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_share_permission` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_share_permissions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_shared_time_tracking_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_status` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_status_categories` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_status_category` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_statuses` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_statuses_by_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_statuses_by_name` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_task` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_teams` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_transitions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_trashed_fields_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_ui_modifications` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user_default_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user_email` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user_email_bulk` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user_groups` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_user_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_users_from_group` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_valid_project_key` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_valid_project_name` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_version` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_version_related_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_version_unresolved_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_visible_issue_field_options` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_votes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_project_issue_type_usages` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_scheme_draft` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_scheme_draft_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_scheme_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_scheme_project_associations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_scheme_usages_for_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_transition_properties` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_transition_rule_configurations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflow_usages_for_status` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_workflows_paginated` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_worklog` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_worklog_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_worklog_property_keys` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_worklogs_by_issue_id_and_worklog_id` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_get_worklogs_for_ids` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_link_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_list_workflow_history` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_live_template` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_match_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_merge_versions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_migrate_queries` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_migration_resource_update_entity_properties_value_put` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_migration_resource_workflow_rule_search_post` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_move_priorities` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_move_resolutions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_move_screen_tab` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_move_screen_tab_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_move_version` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_notify` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_parse_jql_queries` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_partial_update_project_role` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_publish_draft_workflow_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_put_forge_app_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_read_workflow_from_history` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_read_workflow_previews` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_read_workflow_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_read_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_redact` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_refresh_webhooks` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_register_dynamic_webhooks` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_associations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_atlassian_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_attachment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_custom_field_context_from_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_default_project_classification` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_field_association_scheme_item_parameters` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_fields_associated_with_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_gadget` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_group` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_issue_type_from_issue_type_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_issue_types_from_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_issue_types_from_global_field_configuration_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_level` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_mappings_from_issue_type_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_member_from_security_level` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_notification_from_notification_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_preference` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_project_category` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_screen_tab_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_template` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_user` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_user_from_group` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_vote` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_remove_watcher` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_rename_screen_tab` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_reorder_custom_field_options` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_reorder_issue_types_in_issue_type_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_replace_custom_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_replace_issue_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_reset_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_reset_user_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_restore` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_restore_custom_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_sanitise_jql_queries` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_save_template` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_and_reconsile_issues_using_jql` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_and_reconsile_issues_using_jql_post` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_field_association_scheme_fields` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_field_association_scheme_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_for_issues_using_jql` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_for_issues_using_jql_post` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_priorities` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_projects` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_projects_using_security_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_resolutions` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_security_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_search_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_select_time_tracking_implementation` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_service_registry_resource_services_get` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_actors` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_application_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_banner` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_comment_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_dashboard_item_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_default_levels` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_default_priority` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_default_resolution` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_default_share_scope` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_default_values` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_favourite_for_filter` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_field_configuration_scheme_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_issue_navigator_default_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_issue_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_issue_type_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_locale` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_preference` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_project_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_shared_time_tracking_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_user_columns` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_user_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_workflow_scheme_draft_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_workflow_scheme_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_set_worklog_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_store_avatar` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_submit_bulk_delete` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_submit_bulk_edit` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_submit_bulk_move` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_submit_bulk_transition` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_submit_bulk_unwatch` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_submit_bulk_watch` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_suggested_priorities_for_mappings` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_switch_workflow_scheme_for_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_toggle_feature_for_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_trash_custom_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_trash_plan` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_unarchive_issues` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_atlassian_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_comment` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_component` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_custom_field` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_custom_field_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_custom_field_context` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_custom_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_custom_field_value` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_dashboard` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_default_project_classification` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_default_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_default_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_draft_default_workflow` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_draft_workflow_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_field_association_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_field_association_scheme_item_parameters` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_field_configuration` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_field_configuration_items` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_field_configuration_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_fields_associated_with_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_filter` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_gadget` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_issue_field_option` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_issue_link_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_issue_security_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_issue_type` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_issue_type_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_issue_type_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_multiple_custom_field_values` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_notification_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_permission_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_plan` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_plan_only_team` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_precomputations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_priority` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_priority_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_project` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_project_avatar` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_project_category` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_project_email` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_related_work` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_remote_issue_link` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_resolution` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_schemes` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_screen` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_screen_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_security_level` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_statuses` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_ui_modification` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_version` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_workflow_mapping` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_workflow_scheme` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_workflow_scheme_draft` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_workflow_transition_property` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_workflow_transition_rule_configurations` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_update_worklog` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_validate_create_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_validate_project_key` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_validate_update_workflows` | `JIRA_OTHERTOOL` | Manage Jira other operations. |
| `atlassian_jira_other__jira_cloud_workflow_capabilities` | `JIRA_OTHERTOOL` | Manage Jira other operations. |

</details>

_22 action-routed tool(s) · 1022 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (**`intent` default** — the six verb-tools, granular set loaded on demand · `condensed` action-routed · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/usage.md](docs/usage.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

<!-- MCP-CONFIG-EXAMPLES:START -->

> **Install the connector-focused `[mcp]` extra.** Examples use `atlassian-agent[mcp]` to add
> FastMCP / FastAPI through `agent-utilities[mcp]`; the required Agent Utilities core
> still carries `epistemic-graph[full]`. The `[agent-runtime]` extra additionally
> enables model orchestration.

#### stdio Transport (local IDEs — Cursor, Claude Desktop, VS Code)

```json
{
  "mcpServers": {
    "atlassian-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "atlassian-agent[mcp]",
        "atlassian-mcp"
      ],
      "env": {
        "MCP_TOOL_MODE": "intent",
        "ATLASSIANTOOL": "True",
        "ATLASSIAN_ADMINTOOL": "True",
        "ATLASSIAN_AGENT_TOKEN": "your_token_here",
        "ATLASSIAN_AGENT_URL": "http://localhost:8080",
        "ATLASSIAN_AGENT_USER": "your-email@example.com",
        "ATLASSIAN_API_ACCESSTOOL": "True",
        "ATLASSIAN_BEARER_TOKEN": "your_personal_access_token",
        "ATLASSIAN_CONTROLTOOL": "True",
        "ATLASSIAN_DLPTOOL": "True",
        "ATLASSIAN_OAUTH_TOKEN": "your_3lo_access_token",
        "ATLASSIAN_ORGTOOL": "True",
        "ATLASSIAN_USER_MGMTTOOL": "True",
        "ATLASSIAN_USER_PROVISIONINGTOOL": "True",
        "AUDIENCE": "https://your-instance.atlassian.net",
        "CONFLUENCE_OTHERTOOL": "True",
        "CONFLUENCE_PAGETOOL": "True",
        "CONFLUENCE_SPACETOOL": "True",
        "CONFLUENCE_USERTOOL": "True",
        "DELEGATED_SCOPES": "read:jira-work write:jira-work",
        "JIRA_COMMENTTOOL": "True",
        "JIRA_FIELDTOOL": "True",
        "JIRA_ISSUETOOL": "True",
        "JIRA_OTHERTOOL": "True",
        "JIRA_PROJECTTOOL": "True",
        "JIRA_SCREENTOOL": "True",
        "JIRA_USERTOOL": "True",
        "JIRA_WORKFLOWTOOL": "True",
        "KGTOOL": "True"
      }
    }
  }
}
```

Runtime references require an alias-aware launcher such as GraphOS. Other
launchers must omit those entries and inject the resolved values through their
own runtime secret boundary.

#### Streamable-HTTP Transport (networked / production)

```json
{
  "mcpServers": {
    "atlassian-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "atlassian-agent[mcp]",
        "atlassian-mcp",
        "--transport",
        "streamable-http",
        "--port",
        "8000"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "MCP_TOOL_MODE": "intent",
        "ATLASSIANTOOL": "True",
        "ATLASSIAN_ADMINTOOL": "True",
        "ATLASSIAN_AGENT_TOKEN": "your_token_here",
        "ATLASSIAN_AGENT_URL": "http://localhost:8080",
        "ATLASSIAN_AGENT_USER": "your-email@example.com",
        "ATLASSIAN_API_ACCESSTOOL": "True",
        "ATLASSIAN_BEARER_TOKEN": "your_personal_access_token",
        "ATLASSIAN_CONTROLTOOL": "True",
        "ATLASSIAN_DLPTOOL": "True",
        "ATLASSIAN_OAUTH_TOKEN": "your_3lo_access_token",
        "ATLASSIAN_ORGTOOL": "True",
        "ATLASSIAN_USER_MGMTTOOL": "True",
        "ATLASSIAN_USER_PROVISIONINGTOOL": "True",
        "AUDIENCE": "https://your-instance.atlassian.net",
        "CONFLUENCE_OTHERTOOL": "True",
        "CONFLUENCE_PAGETOOL": "True",
        "CONFLUENCE_SPACETOOL": "True",
        "CONFLUENCE_USERTOOL": "True",
        "DELEGATED_SCOPES": "read:jira-work write:jira-work",
        "JIRA_COMMENTTOOL": "True",
        "JIRA_FIELDTOOL": "True",
        "JIRA_ISSUETOOL": "True",
        "JIRA_OTHERTOOL": "True",
        "JIRA_PROJECTTOOL": "True",
        "JIRA_SCREENTOOL": "True",
        "JIRA_USERTOOL": "True",
        "JIRA_WORKFLOWTOOL": "True",
        "KGTOOL": "True"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed Streamable-HTTP instance by `url`:

```json
{
  "mcpServers": {
    "atlassian-mcp": {
      "url": "http://localhost:8000/atlassian-mcp/mcp"
    }
  }
}
```

Run a reviewed container image as a least-privilege stdio child (no
listener or published port):

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  -e MCP_TOOL_MODE=intent \
  -e ATLASSIANTOOL=True \
  -e ATLASSIAN_ADMINTOOL=True \
  -e ATLASSIAN_AGENT_TOKEN=your_token_here \
  -e ATLASSIAN_AGENT_URL=http://localhost:8080 \
  -e ATLASSIAN_AGENT_USER=your-email@example.com \
  -e ATLASSIAN_API_ACCESSTOOL=True \
  -e ATLASSIAN_BEARER_TOKEN=your_personal_access_token \
  -e ATLASSIAN_CONTROLTOOL=True \
  -e ATLASSIAN_DLPTOOL=True \
  -e ATLASSIAN_OAUTH_TOKEN=your_3lo_access_token \
  -e ATLASSIAN_ORGTOOL=True \
  -e ATLASSIAN_USER_MGMTTOOL=True \
  -e ATLASSIAN_USER_PROVISIONINGTOOL=True \
  -e AUDIENCE=https://your-instance.atlassian.net \
  -e CONFLUENCE_OTHERTOOL=True \
  -e CONFLUENCE_PAGETOOL=True \
  -e CONFLUENCE_SPACETOOL=True \
  -e CONFLUENCE_USERTOOL=True \
  -e DELEGATED_SCOPES="read:jira-work write:jira-work" \
  -e JIRA_COMMENTTOOL=True \
  -e JIRA_FIELDTOOL=True \
  -e JIRA_ISSUETOOL=True \
  -e JIRA_OTHERTOOL=True \
  -e JIRA_PROJECTTOOL=True \
  -e JIRA_SCREENTOOL=True \
  -e JIRA_USERTOOL=True \
  -e JIRA_WORKFLOWTOOL=True \
  -e KGTOOL=True \
  registry.example.invalid/atlassian-agent@sha256:<digest> atlassian-mcp
```

For containerized network HTTP, supply an authenticated TLS ingress (or
direct server TLS), exact `MCP_ALLOWED_HOSTS`, and an exact trusted-proxy
CIDR policy through the operator-owned deployment profile. The generator
does not emit an unauthenticated non-loopback listener.

_Auto-generated from the code-read env surface (`MCP_TOOL_MODE` + package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`atlassian-agent` can run as a local stdio process or container, or behind a remote
network boundary. The
[Deployment guide](https://knuckles-team.github.io/atlassian-agent/deployment/) carries
the detailed transport contract.

- **Local container** — launch a reviewed immutable image as a least-privilege
  stdio child with no listener or published port.
- **Remote URL** — connect through an operator-supplied authenticated HTTPS
  ingress. Keep its URL, outbound identity references, trust profile, and exact
  `MCP_ALLOWED_HOSTS` in `AgentConfig`.
<!-- END GENERATED: additional-deployment-options -->

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | secret-injected |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | secret-injected |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `ATLASSIAN_AGENT_URL` | `http://localhost:8080` | These are the shared fallback used by every suite when no suite-specific (ATLASSIAN_{SUITE}_*) override is set. |
| `ATLASSIAN_AGENT_USER` | `your-email@example.com` |  |
| `ATLASSIAN_AGENT_TOKEN` | secret-injected |  |
| `ATLASSIAN_TLS_PROFILE` | — | named AgentConfig TLS profile shared by every suite |
| `ATLASSIAN_JIRA_TLS_PROFILE` | — | optional suite-specific profile override |
| `DEBUG` | `False` |  |
| `PYTHONUNBUFFERED` | `1` |  |
| `ENABLE_DELEGATION` | `True` | 1. OIDC delegation (RFC 8693) — flow the caller's IdP token to Atlassian |
| `OIDC_CONFIG_URL` | `https://idp.example.com/.well-known/openid-configuration` |  |
| `OIDC_CLIENT_ID` | `your_client_id` |  |
| `OIDC_CLIENT_SECRET` | secret-injected |  |
| `AUDIENCE` | `https://your-instance.atlassian.net` |  |
| `DELEGATED_SCOPES` | `read:jira-work write:jira-work` |  |
| `ATLASSIAN_OAUTH_TOKEN` | secret-injected | 2. 3-Legged OAuth (3LO) bearer token |
| `ATLASSIAN_BEARER_TOKEN` | secret-injected | 3. Bearer token / Personal Access Token (Server / Data Center) — global |
| `ATLASSIANTOOL` | `True` | These names match the authoritative "Toggle Env Var" column in the README MCP tools table (condensed action-routed surface). |
| `ATLASSIAN_ADMINTOOL` | `True` |  |
| `ATLASSIAN_API_ACCESSTOOL` | `True` |  |
| `ATLASSIAN_CONTROLTOOL` | `True` |  |
| `ATLASSIAN_DLPTOOL` | `True` |  |
| `ATLASSIAN_ORGTOOL` | `True` |  |
| `ATLASSIAN_USER_MGMTTOOL` | `True` |  |
| `ATLASSIAN_USER_PROVISIONINGTOOL` | `True` |  |
| `JIRA_PROJECTTOOL` | `True` |  |
| `JIRA_USERTOOL` | `True` |  |
| `JIRA_ISSUETOOL` | `True` |  |
| `JIRA_COMMENTTOOL` | `True` |  |
| `JIRA_FIELDTOOL` | `True` |  |
| `JIRA_SCREENTOOL` | `True` |  |
| `JIRA_WORKFLOWTOOL` | `True` |  |
| `JIRA_OTHERTOOL` | `True` |  |
| `CONFLUENCE_PAGETOOL` | `True` |  |
| `CONFLUENCE_SPACETOOL` | `True` |  |
| `CONFLUENCE_USERTOOL` | `True` |  |
| `CONFLUENCE_OTHERTOOL` | `True` |  |
| `KGTOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `intent` | Tool surface: `intent` \| `condensed` \| `verbose` \| `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_47 package + 13 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads. Suite-specific credential variables follow the pattern
`ATLASSIAN_{SUITE}_{URL|USER|TOKEN|VERIFY|BEARER_TOKEN}` and **fall back** to the shared
`ATLASSIAN_AGENT_*` values when unset — so you can run everything off one credential, or split
Jira vs Confluence (and Cloud vs Server/DC) by setting the prefixed variables.

### Connection & Credentials — shared fallback
| Variable | Description | Default |
|----------|-------------|---------|
| `ATLASSIAN_AGENT_URL` | Base Atlassian URL (shared fallback for all suites) | `http://localhost:8080` |
| `ATLASSIAN_AGENT_USER` | Account email / username (basic auth) | — |
| `ATLASSIAN_AGENT_TOKEN` | API token (basic auth) | — |
| `ATLASSIAN_TLS_PROFILE` | Optional shared runtime TLS profile selector | _(unset)_ |

### Connection & Credentials — Jira (per-suite overrides)
| Variable | Description |
|----------|-------------|
| `ATLASSIAN_JIRA_CLOUD_URL` / `_USER` / `_TOKEN` / `_TLS_PROFILE` | Jira **Cloud** connection, credentials, and optional TLS profile selector |
| `ATLASSIAN_JIRA_CLOUD_BEARER_TOKEN` | Jira Cloud bearer token (OAuth/PAT) |
| `ATLASSIAN_JIRA_SERVER_URL` / `_USER` / `_TOKEN` / `_TLS_PROFILE` | Jira **Server / Data Center** connection, credentials, and optional TLS profile selector |
| `ATLASSIAN_JIRA_SERVER_BEARER_TOKEN` | Jira Server/DC Personal Access Token (PAT) |

### Connection & Credentials — Confluence (per-suite overrides)
| Variable | Description |
|----------|-------------|
| `ATLASSIAN_CONFLUENCE_CLOUD_URL` / `_USER` / `_TOKEN` / `_TLS_PROFILE` | Confluence **Cloud** connection, credentials, and optional TLS profile selector |
| `ATLASSIAN_CONFLUENCE_CLOUD_BEARER_TOKEN` | Confluence Cloud bearer token (OAuth/PAT) |
| `ATLASSIAN_CONFLUENCE_SERVER_URL` / `_USER` / `_TOKEN` / `_TLS_PROFILE` | Confluence **Server / Data Center** connection, credentials, and optional TLS profile selector |
| `ATLASSIAN_CONFLUENCE_SERVER_BEARER_TOKEN` | Confluence Server/DC Personal Access Token (PAT) |

### Connection & Credentials — Admin suites (per-suite overrides)
Each admin suite accepts the same `_URL` / `_USER` / `_TOKEN` / `_TLS_PROFILE` / `_BEARER_TOKEN` set,
falling back to the shared `ATLASSIAN_AGENT_*` values:
`ATLASSIAN_ADMIN_CLOUD_*`, `ATLASSIAN_API_ACCESS_CLOUD_*`, `ATLASSIAN_CONTROL_CLOUD_*`,
`ATLASSIAN_DLP_CLOUD_*`, `ATLASSIAN_ORG_CLOUD_*`, `ATLASSIAN_USER_MGMT_CLOUD_*`,
`ATLASSIAN_USER_PROVISIONING_CLOUD_*`.

### Authentication mode
Resolved in priority order (first match wins). The bearer token is sent as
`Authorization: Bearer <token>`; basic auth uses email + API token.

| Variable | Auth mode | Notes |
|----------|-----------|-------|
| `ENABLE_DELEGATION` | **1. OIDC delegation** (RFC 8693 token exchange) | Set `true` to flow the caller's IdP token through to Atlassian |
| `OIDC_CONFIG_URL` / `OIDC_CLIENT_ID` / `OIDC_CLIENT_SECRET` | OIDC delegation IdP config | Required when delegation is enabled |
| `AUDIENCE` | OIDC delegation token audience | Defaults to the resolved URL |
| `DELEGATED_SCOPES` | OIDC delegation scopes | `read:jira-work write:jira-work` |
| `ATLASSIAN_OAUTH_TOKEN` | **2. 3-Legged OAuth (3LO)** bearer token | From the 3LO consent flow |
| `ATLASSIAN_BEARER_TOKEN` | **3. Bearer token / PAT** (global) | Server/DC Personal Access Token; per-suite `ATLASSIAN_{SUITE}_BEARER_TOKEN` overrides this |
| `ATLASSIAN_AGENT_TOKEN` (+ `_USER`) | **4. Basic auth** (fallback) | Email + API token |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list | — |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Tool toggles
Each action-routed tool can be disabled individually via its toggle env var (set to `false`).
The full list is in the [Available MCP Tools](#available-mcp-tools) table above
(e.g. `JIRA_ISSUETOOL`, `CONFLUENCE_PAGETOOL`, `ATLASSIAN_ADMINTOOL`).

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface | `True` |

See [`.env.example`](.env.example) for a copy-paste starting point.

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export ATLASSIAN_AGENT_URL="your_value"
export ATLASSIAN_AGENT_USER="your_value"
export ATLASSIAN_AGENT_TOKEN="your_value"
export ATLASSIAN_TLS_PROFILE="private-pki"
export DEBUG="your_value"
export PYTHONUNBUFFERED="your_value"

# Run the agent server
atlassian-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  atlassian-agent-mcp:
    image: example/atlassian-agent:mcp
    container_name: atlassian-agent-mcp
    hostname: atlassian-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  atlassian-agent-agent:
    image: example/atlassian-agent@sha256:<digest>
    container_name: atlassian-agent-agent
    hostname: atlassian-agent-agent
    restart: always
    depends_on:
      - atlassian-agent-mcp
    env_file:
      - ../.env
    command: [ "atlassian-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://atlassian-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/deployment.md](docs/deployment.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `atlassian-agent[mcp]` | Connector-focused MCP server (`agent-utilities[mcp]` — FastMCP/FastAPI + `epistemic-graph[full]`) | You only run the **MCP server** (smallest install / image) |
| `atlassian-agent[agent]` | Agent runtime (`agent-utilities[agent-runtime,logfire]` — model orchestration + `epistemic-graph[full]`) | You run the **integrated agent** |
| `atlassian-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# Connector-focused MCP server (includes the shared graph engine)
uv pip install "atlassian-agent[mcp]"

# Agent runtime (adds model orchestration to the shared graph engine)
uv pip install "atlassian-agent[agent]"

# Everything (development)
uv pip install "atlassian-agent[all]"      # or: python -m pip install "atlassian-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `example/atlassian-agent:mcp` | `--target mcp` | `atlassian-agent[mcp]` — **connector-focused**, includes `epistemic-graph[full]`; no model-orchestration stack | `atlassian-mcp` |
| `example/atlassian-agent@sha256:<digest>` | `--target agent` (default) | `atlassian-agent[agent]` — **agent runtime**, model orchestration + `epistemic-graph[full]` | `atlassian-agent` |

```bash
docker build --target mcp   -t example/atlassian-agent:mcp    docker/   # connector-focused MCP server
docker build --target agent -t example/atlassian-agent:agent-local docker/   # agent runtime
```

`docker/mcp.compose.yml` runs the connector-focused `:mcp` server; `docker/agent.compose.yml` runs the
agent (`immutable agent digest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

Both `[mcp]` and `[agent]` carry the **epistemic-graph** engine through the required
Agent Utilities core dependency (`epistemic-graph[full]`). The `[mcp]` extra keeps
the server connector-focused; `[agent]` additionally enables model orchestration. Local
deployments can use the bundled engine. For production or shared state, run
**epistemic-graph as a dedicated database service** and configure the runtime to use it.
Deployment recipes (single-node + Raft HA), connection configuration, and architecture
diagrams are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/atlassian-agent/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/atlassian-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/atlassian-agent/deployment/) | run the MCP server, the agent server, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/atlassian-agent/usage/) | the MCP tools, the Atlassian Python clients, the CLI |
| [Overview](https://knuckles-team.github.io/atlassian-agent/overview/) | architecture, enterprise readiness, MCP configuration |
| [Concepts](https://knuckles-team.github.io/atlassian-agent/concepts/) | concept registry (`CONCEPT:ATL-*`) |

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=example&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/example)
![GitHub User's stars](https://img.shields.io/github/stars/example)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-utilities-deployment (generated; do not edit between markers) -->

## Deploy with `agent-utilities-deployment`

Provision this package with the consolidated **`agent-utilities-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `atlassian-agent` with agent-utilities-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "atlassian-agent[mcp]"`, then run `atlassian-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `atlassian-mcp` |
| Immutable container | deploy `registry.example.invalid/atlassian-agent@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-utilities-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, GraphOS delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
