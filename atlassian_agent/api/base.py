import logging
from typing import Any

import requests

from ..models import Response

logger = logging.getLogger(__name__)


class BaseAtlassianClient:
    def __init__(self, base_url: str, username: str, token: str, verify: bool = True):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.token = token
        self.verify = verify
        self.session = requests.Session()
        self.session.auth = (self.username, self.token)
        self.session.verify = self.verify

    def request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            response = self.session.request(method, url, params=params, json=json)
            # We don't call raise_for_status() immediately to handle error responses gracefully in the Response model
            return Response.from_requests_response(response)
        except Exception as e:
            logger.error(f"Request failed: {str(e)}")
            return Response(status_code=500, data=None, message=str(e))
