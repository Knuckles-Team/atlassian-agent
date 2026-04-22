# Generated MCP Tools for ControlCloud
from typing import Any

from fastmcp import Context, FastMCP
from pydantic import Field

from ..api.control_cloud_api import ControlCloudAPI
from ..auth import get_base_client


def get_api() -> ControlCloudAPI:
    return ControlCloudAPI(get_base_client())


def register_control_cloud_tools(mcp: FastMCP):
    @mcp.tool(name="control_cloud_ap_is_get_policies", tags={"atlassian-control"})
    def control_cloud_ap_is_get_policies(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return.",
        ),
        type_: str | None = Field(
            None, description="Sets the type for the page of policies to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of policies"""
        api = get_api()
        response = api.control_cloud_ap_is_get_policies(
            org_id=org_id,
            cursor=cursor,
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_create_policy", tags={"atlassian-control"})
    def control_cloud_ap_is_create_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new policy"""
        api = get_api()
        response = api.control_cloud_ap_is_create_policy(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_get_policy", tags={"atlassian-control"})
    def control_cloud_ap_is_get_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get single policy"""
        api = get_api()
        response = api.control_cloud_ap_is_get_policy(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_update_policy", tags={"atlassian-control"})
    def control_cloud_ap_is_update_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update single policy"""
        api = get_api()
        response = api.control_cloud_ap_is_update_policy(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_delete_policy", tags={"atlassian-control"})
    def control_cloud_ap_is_delete_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete single policy"""
        api = get_api()
        response = api.control_cloud_ap_is_delete_policy(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_get_policies_v2", tags={"atlassian-control"})
    def control_cloud_ap_is_get_policies_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        cursor: str | None = Field(
            None,
            description="Sets the starting point for the page of results to return.",
        ),
        type_: str | None = Field(
            None, description="Sets the type for the page of policies to return."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of policies V2"""
        api = get_api()
        response = api.control_cloud_ap_is_get_policies_v2(
            org_id=org_id,
            cursor=cursor,
            type_=type_,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_create_policy_v2", tags={"atlassian-control"})
    def control_cloud_ap_is_create_policy_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new policy V2"""
        api = get_api()
        response = api.control_cloud_ap_is_create_policy_v2(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_get_policy_v2", tags={"atlassian-control"})
    def control_cloud_ap_is_get_policy_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get single policy V2"""
        api = get_api()
        response = api.control_cloud_ap_is_get_policy_v2(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_update_policy_v2", tags={"atlassian-control"})
    def control_cloud_ap_is_update_policy_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update single policy V2"""
        api = get_api()
        response = api.control_cloud_ap_is_update_policy_v2(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="control_cloud_ap_is_publish_draft_policies", tags={"atlassian-control"}
    )
    def control_cloud_ap_is_publish_draft_policies(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Publish data security policies"""
        api = get_api()
        response = api.control_cloud_ap_is_publish_draft_policies(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_get_resources", tags={"atlassian-control"})
    def control_cloud_ap_is_get_resources(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of resources associated with a policy"""
        api = get_api()
        response = api.control_cloud_ap_is_get_resources(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_create_resource", tags={"atlassian-control"})
    def control_cloud_ap_is_create_resource(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Create a new policy resource"""
        api = get_api()
        response = api.control_cloud_ap_is_create_resource(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_delete_resources", tags={"atlassian-control"})
    def control_cloud_ap_is_delete_resources(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete all policy resources"""
        api = get_api()
        response = api.control_cloud_ap_is_delete_resources(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_update_resource", tags={"atlassian-control"})
    def control_cloud_ap_is_update_resource(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        resource_id: str = Field(
            ..., description="Unique Id associated with a resource."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Update single policy resource"""
        api = get_api()
        response = api.control_cloud_ap_is_update_resource(
            org_id=org_id,
            policy_id=policy_id,
            resource_id=resource_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_delete_resource", tags={"atlassian-control"})
    def control_cloud_ap_is_delete_resource(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        resource_id: str = Field(
            ..., description="Unique Id associated with a resource."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete single policy resource"""
        api = get_api()
        response = api.control_cloud_ap_is_delete_resource(
            org_id=org_id,
            policy_id=policy_id,
            resource_id=resource_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_get_resources_v2", tags={"atlassian-control"})
    def control_cloud_ap_is_get_resources_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get list of resources associated with a policy V2"""
        api = get_api()
        response = api.control_cloud_ap_is_get_resources_v2(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="control_cloud_ap_is_attach_detach_resources_v2",
        tags={"atlassian-control"},
    )
    def control_cloud_ap_is_attach_detach_resources_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add or remove policy resources V2"""
        api = get_api()
        response = api.control_cloud_ap_is_attach_detach_resources_v2(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="control_cloud_ap_is_delete_resources_v2", tags={"atlassian-control"}
    )
    def control_cloud_ap_is_delete_resources_v2(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Delete all policy resources V2"""
        api = get_api()
        response = api.control_cloud_ap_is_delete_resources_v2(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_validate_policy", tags={"atlassian-control"})
    def control_cloud_ap_is_validate_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Validate a policy"""
        api = get_api()
        response = api.control_cloud_ap_is_validate_policy(
            org_id=org_id,
            policy_id=policy_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="control_cloud_ap_is_add_users_to_policy", tags={"atlassian-control"}
    )
    def control_cloud_ap_is_add_users_to_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        policy_id: str = Field(
            ..., description="Unique Id associated with each policy."
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Add users to a policy"""
        api = get_api()
        response = api.control_cloud_ap_is_add_users_to_policy(
            org_id=org_id,
            policy_id=policy_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(name="control_cloud_ap_is_get_task_status", tags={"atlassian-control"})
    def control_cloud_ap_is_get_task_status(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        task_id: str = Field(
            ...,
            description="Unique Id obtained after adding users to an authentication policy.",
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get the status of a task"""
        api = get_api()
        response = api.control_cloud_ap_is_get_task_status(
            org_id=org_id,
            task_id=task_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="control_cloud_ap_is_bulk_fetch_auth_policy", tags={"atlassian-control"}
    )
    def control_cloud_ap_is_bulk_fetch_auth_policy(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: dict[str, Any] | None = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Get policy information for managed users"""
        api = get_api()
        response = api.control_cloud_ap_is_bulk_fetch_auth_policy(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()
