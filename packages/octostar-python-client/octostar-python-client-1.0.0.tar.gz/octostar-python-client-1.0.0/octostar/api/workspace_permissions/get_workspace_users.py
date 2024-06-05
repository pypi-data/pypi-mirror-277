from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.get_workspace_users_response_200 import GetWorkspaceUsersResponse200
from ...models.get_workspace_users_response_400 import GetWorkspaceUsersResponse400
from ...models.get_workspace_users_response_401 import GetWorkspaceUsersResponse401
from ...models.get_workspace_users_response_500 import GetWorkspaceUsersResponse500
from ...types import Response


def _get_kwargs(
    *,
    client: Client = None,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/v1/octostar/workspace-permissions/users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[
    Union[
        GetWorkspaceUsersResponse200,
        GetWorkspaceUsersResponse400,
        GetWorkspaceUsersResponse401,
        GetWorkspaceUsersResponse500,
    ]
]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = GetWorkspaceUsersResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetWorkspaceUsersResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetWorkspaceUsersResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetWorkspaceUsersResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[
    Union[
        GetWorkspaceUsersResponse200,
        GetWorkspaceUsersResponse400,
        GetWorkspaceUsersResponse401,
        GetWorkspaceUsersResponse500,
    ]
]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client = None,
) -> Response[
    Union[
        GetWorkspaceUsersResponse200,
        GetWorkspaceUsersResponse400,
        GetWorkspaceUsersResponse401,
        GetWorkspaceUsersResponse500,
    ]
]:
    """List of workspace users

     Get the list of users that can be assigned permissions for a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWorkspaceUsersResponse200, GetWorkspaceUsersResponse400, GetWorkspaceUsersResponse401, GetWorkspaceUsersResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    if response.is_error:
        print(f"{str(response.status_code)} Error: {response.text} for request", str(kwargs))
    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client = None,
) -> Optional[
    Union[
        GetWorkspaceUsersResponse200,
        GetWorkspaceUsersResponse400,
        GetWorkspaceUsersResponse401,
        GetWorkspaceUsersResponse500,
    ]
]:
    """List of workspace users

     Get the list of users that can be assigned permissions for a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWorkspaceUsersResponse200, GetWorkspaceUsersResponse400, GetWorkspaceUsersResponse401, GetWorkspaceUsersResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
) -> Response[
    Union[
        GetWorkspaceUsersResponse200,
        GetWorkspaceUsersResponse400,
        GetWorkspaceUsersResponse401,
        GetWorkspaceUsersResponse500,
    ]
]:
    """List of workspace users

     Get the list of users that can be assigned permissions for a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWorkspaceUsersResponse200, GetWorkspaceUsersResponse400, GetWorkspaceUsersResponse401, GetWorkspaceUsersResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
) -> Optional[
    Union[
        GetWorkspaceUsersResponse200,
        GetWorkspaceUsersResponse400,
        GetWorkspaceUsersResponse401,
        GetWorkspaceUsersResponse500,
    ]
]:
    """List of workspace users

     Get the list of users that can be assigned permissions for a workspace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWorkspaceUsersResponse200, GetWorkspaceUsersResponse400, GetWorkspaceUsersResponse401, GetWorkspaceUsersResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
