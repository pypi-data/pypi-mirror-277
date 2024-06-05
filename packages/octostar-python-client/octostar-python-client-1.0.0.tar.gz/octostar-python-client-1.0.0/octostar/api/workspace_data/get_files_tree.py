from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.get_files_tree_response_200 import GetFilesTreeResponse200
from ...models.get_files_tree_response_400 import GetFilesTreeResponse400
from ...models.get_files_tree_response_401 import GetFilesTreeResponse401
from ...models.get_files_tree_response_500 import GetFilesTreeResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client = None,
    os_workspace: Union[Unset, None, str] = UNSET,
    root: Union[Unset, None, str] = UNSET,
    recurse: Union[Unset, None, bool] = UNSET,
    exclude_root: Union[Unset, None, bool] = UNSET,
    flat: Union[Unset, None, bool] = UNSET,
    minimal: Union[Unset, None, bool] = UNSET,
    structure: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/get_files_tree".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["os_workspace"] = os_workspace

    params["root"] = root

    params["recurse"] = recurse

    params["exclude_root"] = exclude_root

    params["flat"] = flat

    params["minimal"] = minimal

    params["structure"] = structure

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
) -> Optional[
    Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFilesTreeResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetFilesTreeResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetFilesTreeResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetFilesTreeResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[
    Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
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
    os_workspace: Union[Unset, None, str] = UNSET,
    root: Union[Unset, None, str] = UNSET,
    recurse: Union[Unset, None, bool] = UNSET,
    exclude_root: Union[Unset, None, bool] = UNSET,
    flat: Union[Unset, None, bool] = UNSET,
    minimal: Union[Unset, None, bool] = UNSET,
    structure: Union[Unset, None, bool] = UNSET,
) -> Response[
    Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
]:
    """Get a view (subtree) of a workspace filesystem.

    Args:
        os_workspace (Union[Unset, None, str]):
        root (Union[Unset, None, str]):
        recurse (Union[Unset, None, bool]):
        exclude_root (Union[Unset, None, bool]):
        flat (Union[Unset, None, bool]):
        minimal (Union[Unset, None, bool]):
        structure (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        os_workspace=os_workspace,
        root=root,
        recurse=recurse,
        exclude_root=exclude_root,
        flat=flat,
        minimal=minimal,
        structure=structure,
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
    root: Union[Unset, None, str] = UNSET,
    recurse: Union[Unset, None, bool] = UNSET,
    exclude_root: Union[Unset, None, bool] = UNSET,
    flat: Union[Unset, None, bool] = UNSET,
    minimal: Union[Unset, None, bool] = UNSET,
    structure: Union[Unset, None, bool] = UNSET,
) -> Optional[
    Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
]:
    """Get a view (subtree) of a workspace filesystem.

    Args:
        os_workspace (Union[Unset, None, str]):
        root (Union[Unset, None, str]):
        recurse (Union[Unset, None, bool]):
        exclude_root (Union[Unset, None, bool]):
        flat (Union[Unset, None, bool]):
        minimal (Union[Unset, None, bool]):
        structure (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        os_workspace=os_workspace,
        root=root,
        recurse=recurse,
        exclude_root=exclude_root,
        flat=flat,
        minimal=minimal,
        structure=structure,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    os_workspace: Union[Unset, None, str] = UNSET,
    root: Union[Unset, None, str] = UNSET,
    recurse: Union[Unset, None, bool] = UNSET,
    exclude_root: Union[Unset, None, bool] = UNSET,
    flat: Union[Unset, None, bool] = UNSET,
    minimal: Union[Unset, None, bool] = UNSET,
    structure: Union[Unset, None, bool] = UNSET,
) -> Response[
    Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
]:
    """Get a view (subtree) of a workspace filesystem.

    Args:
        os_workspace (Union[Unset, None, str]):
        root (Union[Unset, None, str]):
        recurse (Union[Unset, None, bool]):
        exclude_root (Union[Unset, None, bool]):
        flat (Union[Unset, None, bool]):
        minimal (Union[Unset, None, bool]):
        structure (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        os_workspace=os_workspace,
        root=root,
        recurse=recurse,
        exclude_root=exclude_root,
        flat=flat,
        minimal=minimal,
        structure=structure,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    os_workspace: Union[Unset, None, str] = UNSET,
    root: Union[Unset, None, str] = UNSET,
    recurse: Union[Unset, None, bool] = UNSET,
    exclude_root: Union[Unset, None, bool] = UNSET,
    flat: Union[Unset, None, bool] = UNSET,
    minimal: Union[Unset, None, bool] = UNSET,
    structure: Union[Unset, None, bool] = UNSET,
) -> Optional[
    Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
]:
    """Get a view (subtree) of a workspace filesystem.

    Args:
        os_workspace (Union[Unset, None, str]):
        root (Union[Unset, None, str]):
        recurse (Union[Unset, None, bool]):
        exclude_root (Union[Unset, None, bool]):
        flat (Union[Unset, None, bool]):
        minimal (Union[Unset, None, bool]):
        structure (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetFilesTreeResponse200, GetFilesTreeResponse400, GetFilesTreeResponse401, GetFilesTreeResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            os_workspace=os_workspace,
            root=root,
            recurse=recurse,
            exclude_root=exclude_root,
            flat=flat,
            minimal=minimal,
            structure=structure,
        )
    ).parsed
