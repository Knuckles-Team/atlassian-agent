import re
from typing import Any, Generic, TypeVar

import requests
from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    """
    A wrapper class to hold the original requests.Response along with the data.
    """

    model_config = ConfigDict(extra="allow", arbitrary_types_allowed=True)

    status_code: int = Field(..., description="HTTP status code")
    data: T | list[T] | dict[str, Any] | None = Field(
        default=None, description="The parsed data from the response"
    )
    message: str | None = Field(None, description="Optional message or error details")

    @classmethod
    def from_requests_response(cls, response: requests.Response) -> "Response":
        detail = ""
        try:
            data = response.json()
            if not response.ok and isinstance(data, dict):
                detail = str(data.get("errorMessage") or data.get("message") or "")
        except Exception:
            text = response.text
            if text.lstrip().startswith("<"):
                # An HTML page (site removed, login redirect, outage) is not data.
                text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).strip()[:300]
                detail = text
            data = {"content": text}

        message = "Success"
        if not response.ok:
            message = f"Error: {response.reason}"
            if detail:
                message = f"{message}: {detail}"
        return cls(status_code=response.status_code, data=data, message=message)
