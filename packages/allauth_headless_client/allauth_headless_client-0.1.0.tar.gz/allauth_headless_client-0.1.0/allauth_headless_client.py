
from operator import methodcaller

import httpx


class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session_token: str = None
        self.client = httpx.Client(base_url=self.base_url)

    def _transform_url(self, url: str) -> str:
        base = self.base_url.strip("/")
        url = url.strip("/")
        return f"{base}/_allauth/app/v1/{url}"

    def _handle_request(self, method, url, **kwargs) -> httpx.Response:
        
        headers = kwargs.pop("headers", {})
        headers.setdefault("Content-Type", "application/json")

        if self.session_token:
            headers.setdefault("X-Session-Token", self.session_token)

        response = methodcaller(
            method,
            url=self._transform_url(url),
            headers=headers,
            **kwargs,
        )(self.client)

        response.raise_for_status()

        if "session_token" in (meta := response.json().get("meta", {})):
            self.session_token = meta["session_token"]

        return response

    def post(self, url, **kwargs):
        return self._handle_request("post", url, **kwargs)

    def get(self, url, **kwargs):
        return self._handle_request("get", url, **kwargs)

    def put(self, url, **kwargs):
        return self._handle_request("put", url, **kwargs)

    def patch(self, url, **kwargs):
        return self._handle_request("patch", url, **kwargs)

    def login(
        self,
        password: str,
        email: str = None,
        username: str = None,
    ):
        assert (email or username) and not (
            email and username
        ), "Either email or username must be provided"

        payload = {"password": password}

        if email:
            payload["email"] = email
        elif username:
            payload["username"] = username

        return self.post("/auth/login", json=payload)

    def signup(
        self,
        password: str,
        email: str = None,
        username: str = None,
    ):
        payload = {"password": password}

        if email:
            payload["email"] = email
        if username:
            payload["username"] = username

        return self.post("/auth/signup", json=payload)
