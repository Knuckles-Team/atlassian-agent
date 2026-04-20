# Generated MCP Tools for UserProvisioningCloud
from typing import Any, Dict, Optional
from pydantic import Field
from fastmcp import FastMCP, Context
from ..api.user_provisioning_cloud_api import UserProvisioningCloudAPI
from ..auth import get_base_client


def get_api() -> UserProvisioningCloudAPI:
    return UserProvisioningCloudAPI(get_base_client())


def register_user_provisioning_cloud_tools(mcp: FastMCP):
    @mcp.tool(name="user_provisioning_cloud_get", tags={"atlassian-user-provisioning"})
    def user_provisioning_cloud_get(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        id_: str = Field(
            ...,
            description="Unique SCIM id that serves as reference to the group. Use the [Get groups API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-groups/#api-scim-directory-directoryid-groups-get) to get the SCIM id.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get a group by ID"""
        api = get_api()
        response = api.user_provisioning_cloud_get(
            directory_id=directory_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(name="user_provisioning_cloud_put", tags={"atlassian-user-provisioning"})
    def user_provisioning_cloud_put(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        id_: str = Field(
            ...,
            description="Unique SCIM id that serves as reference to the group. Use the [Get groups API] (https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-groups/#api-scim-directory-directoryid-groups-get) to get the SCIM id.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update a group by ID"""
        api = get_api()
        response = api.user_provisioning_cloud_put(
            directory_id=directory_id,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_delete_a_group",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_delete_a_group(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        id_: str = Field(
            ...,
            description="Unique SCIM id that serves as reference to the group. Use the [Get groups API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-groups/#api-scim-directory-directoryid-groups-get) to get the SCIM id.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete a group by ID"""
        api = get_api()
        response = api.user_provisioning_cloud_delete_a_group(
            directory_id=directory_id,
            id_=id_,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_patch", tags={"atlassian-user-provisioning"}
    )
    def user_provisioning_cloud_patch(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        id_: str = Field(
            ...,
            description="Unique SCIM id that serves as reference to the group. Use the [Get groups API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-groups/#api-scim-directory-directoryid-groups-get) to get the SCIM id.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update a group by ID (PATCH)"""
        api = get_api()
        response = api.user_provisioning_cloud_patch(
            directory_id=directory_id,
            id_=id_,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_all_groups_from_an_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_all_groups_from_an_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        filter: Optional[str] = Field(
            None,
            description="Filter for `displayName`. Example: `displayName eq 'SCIM_GROUP'`",
        ),
        start_index: Optional[int] = Field(
            None, description="A 1-based index of the first query result."
        ),
        count: Optional[int] = Field(
            None,
            description="Desired maximum number of query results in the list response page.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get groups"""
        api = get_api()
        response = api.user_provisioning_cloud_get_all_groups_from_an_active_directory(
            directory_id=directory_id,
            filter=filter,
            start_index=start_index,
            count=count,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_create_a_group_in_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_create_a_group_in_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create a group"""
        api = get_api()
        response = api.user_provisioning_cloud_create_a_group_in_active_directory(
            directory_id=directory_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_schemas", tags={"atlassian-user-provisioning"}
    )
    def user_provisioning_cloud_get_schemas(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get all schemas"""
        api = get_api()
        response = api.user_provisioning_cloud_get_schemas(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_resource_types",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_resource_types(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get resource types"""
        api = get_api()
        response = api.user_provisioning_cloud_get_resource_types(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_user_resource_type",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_user_resource_type(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get user resource types"""
        api = get_api()
        response = api.user_provisioning_cloud_get_user_resource_type(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_group_resource_type",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_group_resource_type(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get group resource types"""
        api = get_api()
        response = api.user_provisioning_cloud_get_group_resource_type(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_user_schemas",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_user_schemas(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get user schemas"""
        api = get_api()
        response = api.user_provisioning_cloud_get_user_schemas(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_group_schemas",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_group_schemas(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get group schemas"""
        api = get_api()
        response = api.user_provisioning_cloud_get_group_schemas(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_extension_user_schemas",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_extension_user_schemas(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get user enterprise extension schemas"""
        api = get_api()
        response = api.user_provisioning_cloud_get_extension_user_schemas(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_config", tags={"atlassian-user-provisioning"}
    )
    def user_provisioning_cloud_get_config(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get feature metadata"""
        api = get_api()
        response = api.user_provisioning_cloud_get_config(
            directory_id=directory_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_a_user_from_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_a_user_from_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        user_id: str = Field(
            ...,
            description="Unique ID to identify the users. Use the [Get users API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-get) to get the userId.",
        ),
        attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be included in response. Mutually exclusive with `excludedAttributes`.  Example: `userName,emails.value`",
        ),
        excluded_attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be excluded from response. Mutually exclusive with `attributes`.  Example: `timezone,emails.type,department`",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get a user by ID"""
        api = get_api()
        response = api.user_provisioning_cloud_get_a_user_from_active_directory(
            directory_id=directory_id,
            user_id=user_id,
            attributes=attributes,
            excluded_attributes=excluded_attributes,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_update_user_information_in_an_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_update_user_information_in_an_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        user_id: str = Field(
            ...,
            description="Unique ID to identify the users. Use the [Get users API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-get) to get the userId.",
        ),
        attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be included in the response. Mutually exclusive from  `excludedAttributes`. Example: `userName,emails.value`",
        ),
        excluded_attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be excluded in the response. Mutually exclusive from `attributes`.  Example: `timezone,emails.type,department`",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update user via user attributes"""
        api = get_api()
        response = (
            api.user_provisioning_cloud_update_user_information_in_an_active_directory(
                directory_id=directory_id,
                user_id=user_id,
                attributes=attributes,
                excluded_attributes=excluded_attributes,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_delete_a_user_from_an_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_delete_a_user_from_an_active_directory(
        directory_id: str = Field(
            ...,
            description="The ID assigned to your identity provider when linked to your Atlassian organization.",
        ),
        user_id: str = Field(
            ...,
            description="Unique ID to identify the SCIM users. Use the [Get users API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-get) to get the userId.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete a user"""
        api = get_api()
        response = api.user_provisioning_cloud_delete_a_user_from_an_active_directory(
            directory_id=directory_id,
            user_id=user_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_patch_user_information_in_an_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_patch_user_information_in_an_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        user_id: str = Field(
            ...,
            description="Unique ID to identify the users. Use the [Get users API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-get) to get the userId.",
        ),
        attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be included in the response. Mutually exclusive from  `excludedAttributes`. Example: `userName,emails.value`",
        ),
        excluded_attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be included in the response. Mutually exclusive from `attributes`.  Example: `timezone,emails.type,department`",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Update user by ID (PATCH)"""
        api = get_api()
        response = (
            api.user_provisioning_cloud_patch_user_information_in_an_active_directory(
                directory_id=directory_id,
                user_id=user_id,
                attributes=attributes,
                excluded_attributes=excluded_attributes,
                payload=payload,
            )
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_users_from_an_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_users_from_an_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be included in response. Mutually exclusive from `excludedAttributes`.  Example: `userName,emails.value`",
        ),
        excluded_attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be excluded from response. Mutually exclusive from `attributes`.  Example: `timezone,emails.type,department`",
        ),
        filter: Optional[str] = Field(
            None,
            description="Filter for `userName` or `externalId`. Example: `userName eq 'Atlassian'`",
        ),
        start_index: Optional[int] = Field(
            None, description="A 1-based index of the first query result."
        ),
        count: Optional[int] = Field(
            None,
            description="Desired maximum number of query results in the list response page.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get users"""
        api = get_api()
        response = api.user_provisioning_cloud_get_users_from_an_active_directory(
            directory_id=directory_id,
            attributes=attributes,
            excluded_attributes=excluded_attributes,
            filter=filter,
            start_index=start_index,
            count=count,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_create_a_user_in_an_active_directory",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_create_a_user_in_an_active_directory(
        directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be included in response. Mutually exclusive from `excludedAttributes`.  Example: `userName,emails.value`",
        ),
        excluded_attributes: Optional[str] = Field(
            None,
            description="Resource attributes to be excluded from response. Mutually exclusive from  `attributes`. Example: `timezone,emails.type,department`",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Create a user"""
        api = get_api()
        response = api.user_provisioning_cloud_create_a_user_in_an_active_directory(
            directory_id=directory_id,
            attributes=attributes,
            excluded_attributes=excluded_attributes,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        aaid: str = Field(
            ...,
            description="Unique ID of the user's account. The AAID can either be found in the URL of a user's profile, when browsing in the 'Users' tab or the 'Managed Users' tab or use the [Get Users API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-get) to get the AAID.  The URL could look like:  ```https://admin.atlassian.com/o/{org_id}/users/{aaId}```  ```https://admin.atlassian.com/o/{org_id}/members/{aaId}```  ```https://admin.atlassian.com/s/{siteId}/users/{aaId}```",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Delete user in SCIM DB"""
        api = get_api()
        response = api.user_provisioning_cloud_delete_admin_user_provisioning_v1_org_org_id_user_aaid_only_delete_user_in_db(
            org_id=org_id,
            aaid=aaid,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_scim_links",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_scim_links(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        aa_id: str = Field(
            ...,
            description="Unique ID of the user's account. The AAID can either be found in the URL of a user's profile, when browsing in the 'Users' tab or the 'Managed Users' tab or use the [Get Users API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-users/#api-scim-directory-directoryid-users-get) to get the AAID.  The URL could look like:  ```https://admin.atlassian.com/o/{org_id}/users/{aaId}```  ```https://admin.atlassian.com/o/{org_id}/members/{aaId}```  ```https://admin.atlassian.com/s/{siteId}/users/{aaId}```",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get SCIM links for an account"""
        api = get_api()
        response = api.user_provisioning_cloud_get_scim_links(
            org_id=org_id,
            aa_id=aa_id,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_get_scim_links_by_email",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_get_scim_links_by_email(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        payload: Optional[Dict[str, Any]] = Field(
            None, description="JSON payload for the request"
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Get SCIM Links for an email"""
        api = get_api()
        response = api.user_provisioning_cloud_get_scim_links_by_email(
            org_id=org_id,
            payload=payload,
        )
        return response.model_dump()

    @mcp.tool(
        name="user_provisioning_cloud_unlink_scim_user",
        tags={"atlassian-user-provisioning"},
    )
    def user_provisioning_cloud_unlink_scim_user(
        org_id: str = Field(
            ...,
            description="Your organization is identified by a Unique ID. You get your organization ID and Organization API key simultaneously.",
        ),
        scim_directory_id: str = Field(
            ...,
            description="The SCIM base URL that is generated when [connecting an identity provider with SCIM provisioning](https://support.atlassian.com/provisioning-users/docs/configure-user-provisioning-with-an-identity-provider/#Connect-an-identity-provider-with-SCIM-provisioning).",
        ),
        scim_user_id: str = Field(
            ...,
            description="The SCIM user ID to unlink. Use the [Get SCIM Links for an email API](https://developer.atlassian.com/cloud/admin/user-provisioning/rest/api-group-admin-apis/#api-admin-user-provisioning-v1-org-orgid-get-scim-links-for-email-post) to get the SCIM User ID.",
        ),
        _ctx: Optional[Context] = None,
    ) -> Dict[str, Any]:
        """Unlink a SCIM user from their Atlassian account"""
        api = get_api()
        response = api.user_provisioning_cloud_unlink_scim_user(
            org_id=org_id,
            scim_directory_id=scim_directory_id,
            scim_user_id=scim_user_id,
        )
        return response.model_dump()
