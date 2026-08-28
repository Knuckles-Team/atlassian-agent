"""Fleet-wide test-harness self-healing: `.uv-workspace-siblings/agent-utilities`.

`pyproject.toml`'s `[tool.uv.sources]` resolves the `agent-utilities`
dependency through the gitignored `.uv-workspace-siblings/agent-utilities`
symlink (it must be gitignored — it's a machine-local absolute path). Only
the canonical checkout has it hand-created; a freshly created `git worktree`
never gets one, so the FIRST `uv sync` in a new worktree fails outright:

    error: Distribution not found at:
    file://.../.uv-workspace-siblings/agent-utilities

Three lanes hit this independently on 2026-08-27/28 and each fixed it by
hand. This mirrors the self-healing pattern agent-webui's `pnpm-build`
pre-commit hook already uses for its own missing `node_modules`
(`test -d node_modules || pnpm install`): provision the missing, gitignored,
worktree-local artifact idempotently instead of requiring every lane to
remember to hand-create it.

LIMITATION: this only self-heals a venv that has ALREADY been synced at
least once (e.g. the symlink was later deleted by `git clean`) — once
synced, uv's editable-install finder points at the resolved absolute path,
not the symlink, so pytest runs fine without it from then on. It CANNOT fix
the very first `uv sync` in a brand-new worktree, because pytest itself is
not installed until that sync succeeds. For that case, run this file
directly, once, before your first sync:

    python tests/conftest.py && uv sync --extra test --extra mcp
"""

import pathlib
import subprocess
import sys

import pytest


def _ensure_agent_utilities_sibling() -> "pathlib.Path | None":
    here = pathlib.Path(__file__).resolve().parent  # .../tests
    repo_root = here.parent
    link = repo_root / ".uv-workspace-siblings" / "agent-utilities"
    if link.is_symlink() or link.exists():
        return link

    # Derive the canonical (non-worktree) checkout root from git's common
    # dir — a worktree's own directory name/location tells us nothing about
    # where its sibling `agent-utilities` repo lives (this program's other
    # fleet-wide defect: deriving anything from the worktree basename).
    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(repo_root),
                "rev-parse",
                "--path-format=absolute",
                "--git-common-dir",
            ],
            capture_output=True,
            text=True,
            timeout=10,
            check=True,
        )
    except Exception:
        return None
    common_dir = pathlib.Path(result.stdout.strip())
    canonical_root = common_dir.parent  # .../agent-packages/agents/<this-repo>
    packages_root = canonical_root.parent.parent  # .../agent-packages
    target = packages_root / "agent-utilities"
    if not (target / "pyproject.toml").exists():
        return None

    link.parent.mkdir(parents=True, exist_ok=True)
    try:
        link.symlink_to(target)
    except FileExistsError:
        pass
    return link


_ensure_agent_utilities_sibling()

if __name__ == "__main__":
    # Allows `python tests/conftest.py` to bootstrap a fresh worktree BEFORE
    # `uv sync`, without importing anything from this repo's own package or
    # its third-party deps — none of which exist yet in a pre-sync venv.
    raise SystemExit(0)


@pytest.fixture(autouse=True)
def _clean_argv(monkeypatch):
    """Fleet-wide test-harness defect: reset sys.argv to a single clean
    element before every test.

    Several tests in this suite exercise this package's own argparse-based
    CLI entrypoint — directly via `get_mcp_instance()`/`agent_server()`, or
    indirectly via `runpy.run_module(..., run_name="__main__")` — and that
    argparse call reads the LIVE `sys.argv`. Left alone, pytest's own
    invocation flags (`-p no:randomly`, `-n auto`, `--randomly-seed=...`, ...)
    end up in that argv and are rejected by the module's CLI parser:

        error: argument -p/--port: invalid int value: 'no:randomly'

    which makes `pytest tests/ -q -p no:randomly` disagree with a plain
    `pytest tests/ -q` run -- not a real regression, just this trap. A
    handful of call sites already pin their own argv locally (e.g. via
    `patch("sys.argv", [...])` around a `runpy.run_module` call); those
    still work unchanged, since that local patch simply overrides this
    fixture's baseline for the duration of its own `with` block, and
    monkeypatch restores this baseline afterward. This fixture is the
    fleet-wide backstop for every OTHER call site (most of them direct
    `get_mcp_instance()` calls with no local patch at all) that the
    per-call-site fix in WD4-FIX-01 could not enumerate exhaustively. See
    plans/complex/waves/wD4/WD4-FIX-01.md defect (a).
    """
    monkeypatch.setattr(sys, "argv", ["pytest"])


from unittest.mock import MagicMock

# 1. Mock fastmcp.Context methods to avoid RuntimeError in test environments
import fastmcp


async def dummy_async(*args, **kwargs):
    return None


fastmcp.Context.info = dummy_async  # type: ignore[method-assign]
fastmcp.Context.warning = dummy_async  # type: ignore[method-assign]
fastmcp.Context.error = dummy_async  # type: ignore[method-assign]
fastmcp.Context.debug = dummy_async  # type: ignore[method-assign]


# 2. Create a generic mock client that returns dummy data for any method call
class MockClient:
    def __getattr__(self, name):
        return lambda *args, **kwargs: {
            "id": "1",
            "key": "TEST",
            "values": [{"id": "1"}],
            "body": "test-body",
            "results": [{"id": "1"}],
        }


# 3. Patch all atlassian_agent.auth getters before other modules import them
import atlassian_agent.auth

for name in list(dir(atlassian_agent.auth)):
    if name.startswith("get_") and name.endswith("_client"):
        setattr(atlassian_agent.auth, name, MagicMock(return_value=MockClient()))
