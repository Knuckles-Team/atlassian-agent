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
        try:
            data = response.json()
        except Exception:
            data = {"content": response.text}

        return cls(
            status_code=response.status_code,
            data=data,
            message="Success" if response.ok else f"Error: {response.reason}",
        )
