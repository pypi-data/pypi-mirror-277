import os
import ssl
from pathlib import Path
from typing import Dict, List, Union

import attr


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
        follow_redirects: Whether or not to follow redirects. Default value is False.
    """

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)
    raise_on_unexpected_status: bool = attr.ib(False, kw_only=True)
    follow_redirects: bool = attr.ib(False, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    fixed_token: str = None
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    @property
    def token(self) -> str:
        if self.fixed_token:
            return self.fixed_token
        token_file = Path("/TOKEN.txt")
        if token_file.is_file():
            token = token_file.read_text().strip()
            if token:
                os.environ["OS_JWT"] = token
        return os.environ.get("OS_JWT")

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}


def check_required_env_vars(required_vars: List[str]):
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}. Please set these variables and try again."
        )


def mk_os_client():
    ancestor = os.environ.get("OS_ANCESTOR")
    current_pod_name = os.environ.get("OS_CURRENT_POD_NAME")
    if not ancestor and current_pod_name:
        ancestor = current_pod_name[:-6]
    if not ancestor:
        ancestor = "local-dev"

    check_required_env_vars(["OS_API_ENDPOINT", "OS_ONTOLOGY"])

    return AuthenticatedClient(
        timeout=90,
        base_url=os.environ.get("OS_API_ENDPOINT"),
        headers={
            "x-ontology": os.environ.get("OS_ONTOLOGY"),
            "x-app-name": os.environ.get("OS_APP_NAME", "unknown-local-app"),
            "x-ancestor": ancestor,
        },
        follow_redirects=True,
        verify_ssl=True,
        raise_on_unexpected_status=False,
    )


def set_default_client(client):
    global custom_default_client
    custom_default_client = client


def get_default_client():
    return custom_default_client or os_client


os_client = mk_os_client()
custom_default_client = None
