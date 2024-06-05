from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.get_attachment_response_200 import GetAttachmentResponse200
from ...models.get_attachment_response_401 import GetAttachmentResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    file_path: str,
    *,
    client: Client = None,
    no_redirect: Union[Unset, None, str] = UNSET,
    content_disposition: Union[Unset, None, str] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/attachments/{workspace}/{file_path}".format(
        client.base_url, workspace=workspace, file_path=file_path
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["no_redirect"] = no_redirect

    params["content_disposition"] = content_disposition

    params["content_type"] = content_type

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
) -> Optional[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = GetAttachmentResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.MOVED_PERMANENTLY:
        response_301 = cast(Any, None)
        return response_301
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetAttachmentResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    file_path: str,
    *,
    client: Client = None,
    no_redirect: Union[Unset, None, str] = UNSET,
    content_disposition: Union[Unset, None, str] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]:
    """Get S3 attachments operation

     This operation will get attachments given a workspace and file_path

    Args:
        workspace (str):
        file_path (str):
        no_redirect (Union[Unset, None, str]):
        content_disposition (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace=workspace,
        file_path=file_path,
        client=client,
        no_redirect=no_redirect,
        content_disposition=content_disposition,
        content_type=content_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    if response.is_error:
        print(f"{str(response.status_code)} Error: {response.text} for request", str(kwargs))
    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    file_path: str,
    *,
    client: Client = None,
    no_redirect: Union[Unset, None, str] = UNSET,
    content_disposition: Union[Unset, None, str] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]:
    """Get S3 attachments operation

     This operation will get attachments given a workspace and file_path

    Args:
        workspace (str):
        file_path (str):
        no_redirect (Union[Unset, None, str]):
        content_disposition (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        workspace=workspace,
        file_path=file_path,
        client=client,
        no_redirect=no_redirect,
        content_disposition=content_disposition,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    file_path: str,
    *,
    client: Client = None,
    no_redirect: Union[Unset, None, str] = UNSET,
    content_disposition: Union[Unset, None, str] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]:
    """Get S3 attachments operation

     This operation will get attachments given a workspace and file_path

    Args:
        workspace (str):
        file_path (str):
        no_redirect (Union[Unset, None, str]):
        content_disposition (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace=workspace,
        file_path=file_path,
        client=client,
        no_redirect=no_redirect,
        content_disposition=content_disposition,
        content_type=content_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    file_path: str,
    *,
    client: Client = None,
    no_redirect: Union[Unset, None, str] = UNSET,
    content_disposition: Union[Unset, None, str] = UNSET,
    content_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]]:
    """Get S3 attachments operation

     This operation will get attachments given a workspace and file_path

    Args:
        workspace (str):
        file_path (str):
        no_redirect (Union[Unset, None, str]):
        content_disposition (Union[Unset, None, str]):
        content_type (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetAttachmentResponse200, GetAttachmentResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            workspace=workspace,
            file_path=file_path,
            client=client,
            no_redirect=no_redirect,
            content_disposition=content_disposition,
            content_type=content_type,
        )
    ).parsed
