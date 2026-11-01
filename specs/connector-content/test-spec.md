# CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Proving test | Expected observation |
|---|---|---|---|
| T-001 | `CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R001` | `tests/test_default_content_surfaces.py` | The listings include the packaged skills, ontology and prompts. |

## Rows awaiting bound tests
- `CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R002`: planned proof `tests/test_access_contracts.py::test_competency_contracts_certified`. Expected: Certification passes and the issue recording validates against key and the status, assignee, blockedBy and pullRequestUrl columns.. Refusal: A contract naming a missing tool or a recording missing a declared column fails certification..
