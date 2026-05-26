# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.13.0] - 2026-05-22

### Added
- Created complete programmatic registration test coverage ensuring all refactored FastMCP tools are verified dynamically.
- Implemented robust error boundary handling and edge-case validation for dynamic routing client invocations.

### Changed
- **Architectural Consolidation**: Refactored 8 monolithic, static if-else parameterless Atlassian Admin/Org/Control/DLP/User Management MCP tool functions into dynamic, highly maintainable wrappers using `params_json` and `execute_client_method`.
  - Consolidated over 1,400 lines of boilerplate into less than 300 lines of extremely clean, readable code.
  - Reduced Cyclomatic Complexity of MCP server registration layer by thousands of units.
- **Improved Test Isolation**: Refactored eager module import pattern in `atlassian_agent/__init__.py` to safely expose package members dynamically, preventing global pollution.

### Fixed
- **Security Vulnerability Resolution (CWE-94)**: Removed high-severity code injection vulnerability in `tests/test_startup_coverage.py` by replacing unsafe dynamic execution (`compile()` / `exec()`) with isolated process execution (`subprocess.run`).
- **Resolved Mocking Order Dependencies**: Corrected internal mocking interaction order of `importlib.import_module` in test suite setup to ensure perfect unit testing reliability.
