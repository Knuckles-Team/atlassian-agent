"""Deployment-neutral Jira and Confluence operations.

Jira and Confluence each ship a Cloud client and a Server/Data Center client whose
methods are deployment-prefixed (``jira_cloud_add_comment``,
``jira_server_add_comment``). This module serves one tool per operation,
``jira_<operation>`` and ``confluence_<operation>``. Each tool reads the deployment
from configuration when it is called (``ATLASSIAN_JIRA_DEPLOYMENT``,
``ATLASSIAN_CONFLUENCE_DEPLOYMENT``: ``cloud`` or ``server``, default ``cloud``) and
calls that deployment's client.

The operations offered are the configured deployment's operations, typed from that
client's method signatures. Cloud (REST v3) and Server (REST v2) share few
operations, so the tool list follows the configuration.
"""

from __future__ import annotations

import functools
import importlib
import inspect
import re
from collections.abc import Callable
from typing import Any

from scion_sdk.config import setting

DEPLOYMENTS = ("cloud", "server")

#: product -> (setting name, {deployment: (module, class, factory)})
PRODUCTS: dict[str, tuple[str, dict[str, tuple[str, str, str]]]] = {
    "jira": (
        "ATLASSIAN_JIRA_DEPLOYMENT",
        {
            "cloud": ("api_client_jira_cloud", "JiraCloudAPI", "get_jira_cloud_client"),
            "server": (
                "api_client_jira_server",
                "JiraServerAPI",
                "get_jira_server_client",
            ),
        },
    ),
    "confluence": (
        "ATLASSIAN_CONFLUENCE_DEPLOYMENT",
        {
            "cloud": (
                "api_client_confluence_cloud",
                "ConfluenceCloudAPI",
                "get_confluence_cloud_client",
            ),
            "server": (
                "api_client_confluence_server",
                "ConfluenceServerAPI",
                "get_confluence_server_client",
            ),
        },
    ),
}

_METHOD_LINE = re.compile(r"^\s*Method:\s*([A-Z]+)\s*$", re.MULTILINE)


class DeploymentUnavailableError(RuntimeError):
    """The configured deployment does not offer the requested operation."""


def configured_deployment(product: str) -> str:
    """``cloud`` or ``server`` for ``product``, from configuration."""
    name, _ = PRODUCTS[product]
    raw = (
        setting("ATLASSIAN_JIRA_DEPLOYMENT", "cloud")
        if product == "jira"
        else setting("ATLASSIAN_CONFLUENCE_DEPLOYMENT", "cloud")
    )
    value = str(raw or "cloud").strip().lower()
    if value not in DEPLOYMENTS:
        raise ValueError(f"{name} must be 'cloud' or 'server', not {value!r}")
    return value


def _client_class(product: str, deployment: str) -> type:
    module, cls, _ = PRODUCTS[product][1][deployment]
    return getattr(importlib.import_module(f"atlassian_agent.api.{module}"), cls)


def operations(product: str, deployment: str) -> dict[str, Callable[..., Any]]:
    """Unprefixed operation name -> the deployment client's method."""
    prefix = f"{product}_{deployment}_"
    cls = _client_class(product, deployment)
    return {
        name[len(prefix) :]: member
        for name, member in vars(cls).items()
        if name.startswith(prefix) and callable(member)
    }


class DeploymentClient:
    """Holds a product's clients; built per call by :func:`client_factory`."""

    def __init__(self, product: str) -> None:
        self._product = product
        self._clients: dict[str, Any] = {}

    def _client(self, deployment: str) -> Any:
        if deployment not in self._clients:
            from atlassian_agent import auth

            factory = PRODUCTS[self._product][1][deployment][2]
            self._clients[deployment] = getattr(auth, factory)()
        return self._clients[deployment]

    def _call(self, operation: str, kwargs: dict[str, Any]) -> Any:
        deployment = configured_deployment(self._product)
        method = getattr(
            self._client(deployment), f"{self._product}_{deployment}_{operation}", None
        )
        if method is None:
            raise DeploymentUnavailableError(
                f"{self._product} {deployment} has no operation {operation!r}"
            )
        return method(**kwargs)


def _operation(product: str, name: str, source: Callable[..., Any]) -> Any:
    @functools.wraps(source)
    def method(self: DeploymentClient, **kwargs: Any) -> Any:
        return self._call(name, kwargs)

    method.__name__ = name
    method.__qualname__ = f"{product.capitalize()}API.{name}"
    verb = _METHOD_LINE.search(source.__doc__ or "")
    if verb:
        method.__http_method__ = verb.group(1)  # type: ignore[attr-defined]
    # The SDK types the tool from the signature; drop __wrapped__ so it does not
    # read the prefixed source method's name.
    method.__signature__ = inspect.signature(source)  # type: ignore[attr-defined]
    del method.__wrapped__  # type: ignore[attr-defined]
    return method


def facade_class(product: str, deployment: str | None = None) -> type:
    """A client class with one method per operation of the configured deployment."""
    chosen = deployment or configured_deployment(product)
    members = {
        name: _operation(product, name, source)
        for name, source in sorted(operations(product, chosen).items())
    }
    members["__init__"] = lambda self: DeploymentClient.__init__(self, product)
    members["__doc__"] = (
        f"{product.capitalize()} operations; Cloud or Server is chosen per call "
        f"from {PRODUCTS[product][0]}."
    )
    return type(f"{product.capitalize()}API", (DeploymentClient,), members)


def client_factory(product: str) -> Callable[[], DeploymentClient]:
    cls = facade_class(product)
    return lambda: cls()
