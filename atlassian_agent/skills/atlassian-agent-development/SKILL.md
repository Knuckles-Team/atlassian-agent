---
name: atlassian-agent-development
skill_type: skill
domain: development
description: >-
  Develop, test, gate, and release the atlassian-agent connector. Use this
  skill when changing Jira or Confluence mappings, MCP tools, packaging,
  documentation, or repository gates.
license: MIT
tags: [atlassian-agent, development, connector, jira, confluence, gates]
tier: repository
metadata:
  author: Genius
  version: '0.1.0'
---

# atlassian-agent development

This repository owns Jira and Confluence calls, mappings, MCP tools, and agent
entry points. Shared connector contracts and transports belong to
`agent-connector-sdk`; admission, serving, and durable graph state belong to
their owning repositories. Read `AGENTS.md` before changing code and keep
Atlassian credentials and raw customer data out of source, logs, and skill
content.

## Rapid delivery: the 5-minute contract

Specs are already designed. Deliver small, reviewable slices and cite the
owning spec row in the commit trailer.

- Find the owning row first with `git grep -n "<term>" -- specs` and extend
  that spec before adding new requirement text.
- Reuse existing SDK clients, auth policy, pagination helpers, and tool
  factories. Do not create a second implementation of a connector capability.
- Keep changes scoped to this connector. A change owned by the SDK, Arbora,
  or the knowledge graph belongs in that repository instead.
- Every delivered requirement needs a bound test. Generated `status.json`
  files are produced by `pipelines-hook spec-status`; never hand-edit them.
- One logical change per commit, with `Spec: <ID>` and the assisting agent
  trailer adjacent in the final paragraph.

## Setup and gates

Use the pinned environment from `uv sync --locked`. Run the repository
gate from the checkout root:

```bash
uvx pre-commit run --all-files
```

For focused feedback, run the repository's bounded tests with the pinned
environment, for example:

```bash
uv run --all-extras pytest tests/test_models.py -q
uv run --all-extras pytest tests/test_connector_tool_parity.py -q
```

The canonical `.pre-commit-config.yaml` delegates connector-standard,
secrets, spec, tests-fast, and dependency-readiness checks to
`Knuckles-Team/pipelines` at `rev: main`. Do not replace those shared hooks
with local copies or bypass a failing check.

## Connector-specific checks

- Preserve Jira and Confluence tool parity and the existing auth boundaries.
- Validate environment variables and credential presence before provider
  calls; handle missing credentials without leaking secrets.
- Mock external Atlassian calls in tests; never use live credentials in a
  local gate.
- Keep `atlassian_agent/skills/` package data intact when adding skills.
- Documentation lives under `docs/` and is published by the shared Pages
  workflow; source status records live under `specs/`.

## Delivery discipline

Work in a real Git worktree based on `origin/main`. Inspect the complete diff,
stage only reviewed paths, and verify `git status --short` after every gate.
Do not use `git stash`, `git add -A`, or `git add .`; do not claim Pages
publication until a successful exact-source workflow run and the public page
are both observed.
