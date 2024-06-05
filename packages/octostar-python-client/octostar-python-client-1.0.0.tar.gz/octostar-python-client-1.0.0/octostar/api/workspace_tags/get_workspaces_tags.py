from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.acknowledgement import Acknowledgement
from ...models.get_workspaces_tags_response_401 import GetWorkspacesTagsResponse401
from ...models.successful_get_tags import SuccessfulGetTags
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client = None,
    os_workspace: Union[Unset, None, str] = UNSET,
    os_workspaces: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/v1/octostar/workspace-tags/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["os_workspace"] = os_workspace

    params["os_workspaces"] = os_workspaces

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessfulGetTags.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Acknowledgement.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetWorkspacesTagsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Acknowledgement.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]:
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
    os_workspace: Union[Unset, None, str] = UNSET,
    os_workspaces: Union[Unset, None, str] = UNSET,
) -> Response[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]:
    """Get tags for the workspace

    Args:
        os_workspace (Union[Unset, None, str]):
        os_workspaces (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        os_workspace=os_workspace,
        os_workspaces=os_workspaces,
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
    os_workspace: Union[Unset, None, str] = UNSET,
    os_workspaces: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]:
    """Get tags for the workspace

    Args:
        os_workspace (Union[Unset, None, str]):
        os_workspaces (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        os_workspace=os_workspace,
        os_workspaces=os_workspaces,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    os_workspace: Union[Unset, None, str] = UNSET,
    os_workspaces: Union[Unset, None, str] = UNSET,
) -> Response[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]:
    """Get tags for the workspace

    Args:
        os_workspace (Union[Unset, None, str]):
        os_workspaces (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        os_workspace=os_workspace,
        os_workspaces=os_workspaces,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    os_workspace: Union[Unset, None, str] = UNSET,
    os_workspaces: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]]:
    """Get tags for the workspace

    Args:
        os_workspace (Union[Unset, None, str]):
        os_workspaces (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, GetWorkspacesTagsResponse401, SuccessfulGetTags]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            os_workspace=os_workspace,
            os_workspaces=os_workspaces,
        )
    ).parsed
