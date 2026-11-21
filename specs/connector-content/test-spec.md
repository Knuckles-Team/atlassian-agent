# CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT — Test specification

Governing spec: [spec.md](spec.md).

| Test ID | Requirement | Proving test | Expected observation |
|---|---|---|---|
| T-001 | `CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R001` | `tests/test_default_content_surfaces.py` | The listings include the packaged skills, ontology and prompts. |
| T-002 | `CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R004` | `tests/test_ontology_extends_core.py::test_pack_declares_no_core_term` | The served Turtle declares none of the listed core terms. |

## Rows awaiting bound tests
- `CONN-ATLASSIAN-AGENT-CONNECTOR-CONTENT-R002`: planned proof `tests/test_access_contracts.py::test_competency_contracts_certified`. Expected: Certification passes and the issue recording validates against key and the status, assignee, blockedBy and pullRequestUrl columns.. Refusal: A contract naming a missing tool or a recording missing a declared column fails certification..
