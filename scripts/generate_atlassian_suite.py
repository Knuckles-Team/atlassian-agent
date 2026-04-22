import json
from typing import Any
import os
import re
from pathlib import Path
from jinja2 import Template

# --- Templates ---

API_TEMPLATE = """# Generated API Client for {{ product_name }}
from typing import Any, Dict, List, Optional, Union
from .base import BaseAtlassianClient
from ..models import Response

class {{ product_name }}API:
    def __init__(self, base_api: BaseAtlassianClient):
        self.base_api = base_api

    {% for m in methods %}
    def {{ m.name }}(self,
        {% for p in m.params %}{% if p.required %}{{ p.py_name }}: {{ p.type }}, {% endif %}{% endfor %}
        {% for p in m.params %}{% if not p.required %}{{ p.py_name }}: Optional[{{ p.type }}] = None, {% endif %}{% endfor %}
        {% if m.body %}payload: Optional[Dict[str, Any]] = None, {% endif %}
        max_pages: Optional[int] | None = None
    ) -> Response:
        \"\"\"{{ m.summary }}

        Path: {{ m.path }}
        Method: {{ m.method }}
        \"\"\"
        path = f\"{{ m.path_formatted }}\"
        params = {
            {% for p in m.params %}{% if p.in == 'query' or p.in == 'header' %}
            \"{{ p.name }}\": {{ p.py_name }},
            {% endif %}{% endfor %}
        }
        # Filter None values from params
        params = {k: v for k, v in params.items() if v is not None}

        return self.base_api.request(\"{{ m.method }}\", path, params=params, json=payload if payload else None)

    {% endfor %}
"""

TOOLS_TEMPLATE = """# Generated MCP Tools for {{ product_name }}
import os
from typing import Any, Dict, List, Optional, Union
from pydantic import Field
from fastmcp import FastMCP, Context
from ..api.{{ module_name }}_api import {{ product_name }}API
from ..auth import get_base_client

def get_api() -> {{ product_name }}API:
    return {{ product_name }}API(get_base_client())

def register_{{ module_name }}_tools(mcp: FastMCP):
    tags = {{ tags|safe }}

    {% for m in methods %}
    @mcp.tool(name=\"{{ m.name }}\", tags={"atlassian"})
    def {{ m.name }}(
        {% for p in m.params %}{% if p.required %}{{ p.py_name }}: {{ p.type }} = Field(..., description=\"{{ p.description }}\"),
        {% endif %}{% endfor %}
        {% for p in m.params %}{% if not p.required %}{{ p.py_name }}: Optional[{{ p.type }}] = Field(None, description=\"{{ p.description }}\"),
        {% endif %}{% endfor %}
        {% if m.body %}payload: Optional[Dict[str, Any]] = Field(None, description=\"JSON payload for the request\"),
        {% endif %}
        ctx: Optional[Context] | None = None
    ) -> Dict[str, Any]:
        \"\"\"{{ m.summary }}\"\"\"
        api = get_api()
        response = api.{{ m.name }}(
            {% for p in m.params %}{{ p.py_name }}={{ p.py_name }}, {% endfor %}
            {% if m.body %}payload=payload, {% endif %}
        )
        return response.model_dump()

    {% endfor %}
"""

# --- Helper logic ---


def clean_identifier(name):
    # Strictly allow only alphanumeric and underscore
    name = re.sub(r"[^\w]", "_", name)
    # Handle the cases like "GetIssue" -> "get_issue"
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Handle the cases like "APIKey" -> "api_key"
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()
    # Normalize other characters
    res = (
        s2.strip("_")
        .replace("-", "_")
        .replace(".", "_")
        .replace(" ", "_")
        .replace("__", "_")
        .strip("_")
    )
    if res in [
        "from",
        "class",
        "def",
        "return",
        "import",
        "global",
        "with",
        "as",
        "if",
        "else",
        "elif",
        "for",
        "while",
        "try",
        "except",
        "finally",
        "raise",
        "yield",
        "lambda",
        "async",
        "await",
        "pass",
        "break",
        "switch",
        "case",
        "and",
        "or",
        "not",
        "is",
        "in",
        "del",
        "assert",
        "None",
        "True",
        "False",
        "type",
        "id",
    ]:
        res = f"{res}_"
    return res


def map_type(openapi_type):
    mapping = {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "number": "float",
        "array": "List[Any]",
        "object": "Dict[str, Any]",
    }
    return mapping.get(openapi_type, "Any")


def clean_desc(desc):
    if not desc:
        return ""
    # Remove newlines and escape quotes
    desc = desc.replace("\n", " ").replace('"', "'").replace("\\", "\\\\").strip()
    return desc


def clean_path(path):
    # Remove any stray quotes from path
    return path.replace('"', "").replace("'", "")


def generate_suite(
    openapi_path, api_output, tools_output, product_name, module_name, tags
):
    with open(openapi_path, "r") as f:
        spec = json.load(f)

    paths = spec.get("paths", {})
    methods = []

    product_prefix = module_name

    operation_ids: dict[str, Any] = {}

    for path, path_item in paths.items():
        path_params_global = path_item.get("parameters", [])

        for method_type, op_spec in path_item.items():
            if method_type not in ["get", "post", "put", "delete", "patch"]:
                continue

            op_id = op_spec.get("operationId")
            if not op_id:
                clean_p = (
                    path.replace("{", "").replace("}", "").strip("/").replace("/", "_")
                )
                op_id = f"{method_type}_{clean_p}"

            if op_id in operation_ids:
                operation_ids[op_id] += 1
                op_id = f"{op_id}_{operation_ids[op_id]}"
            else:
                operation_ids[op_id] = 1

            clean_op_id = clean_identifier(op_id)
            if clean_op_id.startswith(product_prefix):
                op_name = clean_op_id
            else:
                op_name = f"{product_prefix}_{clean_op_id}"

            op_name = op_name.replace("__", "_").strip("_")

            summary = op_spec.get(
                "summary", op_spec.get("description", "No description provided.")
            )
            summary = clean_desc(summary)

            all_params_raw = path_params_global + op_spec.get("parameters", [])
            seen_param_names = set()
            params = []

            path_fmt = clean_path(path)

            for p in all_params_raw:
                if "$ref" in p:
                    continue

                p_name = p.get("name", "param")
                p_py_name = clean_identifier(p_name)

                if p_py_name in seen_param_names:
                    continue
                seen_param_names.add(p_py_name)

                p_type = map_type(p.get("schema", {}).get("type", "string"))
                p_in = p.get("in", "query")
                p_required = p.get("required", False) or p_in == "path"
                p_description = clean_desc(p.get("description", f"Parameter {p_name}"))

                params.append(
                    {
                        "name": p_name,
                        "py_name": p_py_name,
                        "type": p_type,
                        "in": p_in,
                        "required": p_required,
                        "description": p_description,
                    }
                )
                if p_in == "path":
                    path_fmt = path_fmt.replace(f"{{{p_name}}}", f"{{{p_py_name}}}")

            body = "requestBody" in op_spec or any(
                p.get("in") == "body" for p in all_params_raw
            )

            methods.append(
                {
                    "name": op_name,
                    "path": path,
                    "path_formatted": path_fmt,
                    "method": method_type.upper(),
                    "summary": summary,
                    "params": params,
                    "body": body,
                }
            )

    api_template = Template(API_TEMPLATE)
    api_content = api_template.render(product_name=product_name, methods=methods)
    with open(api_output, "w") as f:
        f.write(api_content)

    tools_template = Template(TOOLS_TEMPLATE)
    tools_content = tools_template.render(
        product_name=product_name,
        module_name=module_name,
        methods=methods,
        tags={"atlassian"},
    )
    with open(tools_output, "w") as f:
        f.write(tools_content)


if __name__ == "__main__":
    base_dir = Path(__file__).parent.parent
    openapi_dir = base_dir / "openapi"
    api_dir = base_dir / "atlassian_agent" / "api"
    tools_dir = base_dir / "atlassian_agent" / "tools"

    os.makedirs(api_dir, exist_ok=True)
    os.makedirs(tools_dir, exist_ok=True)
    (api_dir / "__init__.py").touch()
    (tools_dir / "__init__.py").touch()

    suite_configs = [
        (
            "jira-swagger-v3.v3.json",
            "JiraCloud",
            "jira_cloud",
            ["atlassian", "jira", "cloud"],
        ),
        (
            "jira-server-openapi.json",
            "JiraServer",
            "jira_server",
            ["atlassian", "jira", "server"],
        ),
        (
            "confluence-cloud-openapi-v2.v3.json",
            "ConfluenceCloud",
            "confluence_cloud",
            ["atlassian", "confluence", "cloud"],
        ),
        (
            "confluence-server-openapi.json",
            "ConfluenceServer",
            "confluence_server",
            ["atlassian", "confluence", "server"],
        ),
        (
            "admin-cloud-openapi.json",
            "AdminCloud",
            "admin_cloud",
            ["atlassian", "admin", "cloud"],
        ),
        (
            "api-access-cloud-openapi.json",
            "APIAccessCloud",
            "api_access_cloud",
            ["atlassian", "api-access", "cloud"],
        ),
        (
            "atlassian-cloud-organizations.json",
            "OrgCloud",
            "org_cloud",
            ["atlassian", "org", "cloud"],
        ),
        (
            "cloud-user-managementjson.json",
            "UserMgmtCloud",
            "user_mgmt_cloud",
            ["atlassian", "user-mgmt", "cloud"],
        ),
        (
            "control-cloud-openapi.json",
            "ControlCloud",
            "control_cloud",
            ["atlassian", "control", "cloud"],
        ),
        (
            "dataloss-prevention-openapi.json",
            "DLPCloud",
            "dlp_cloud",
            ["atlassian", "dlp", "cloud"],
        ),
        (
            "user-provisioning-openapi.json",
            "UserProvisioningCloud",
            "user_provisioning_cloud",
            ["atlassian", "user-provisioning", "cloud"],
        ),
    ]

    for filename, product, module, tags in suite_configs:
        openapi_path = openapi_dir / filename
        if openapi_path.exists():
            print(f"Generating {product} suite (API & Tools)...")
            generate_suite(
                openapi_path,
                api_dir / f"{module}_api.py",
                tools_dir / f"{module}_tools.py",
                product,
                module,
                tags,
            )
        else:
            print(f"Warning: {filename} not found in {openapi_dir}")
