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
