from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.copy_json_body import CopyJsonBody
from ...models.copy_response_200 import CopyResponse200
from ...models.copy_response_400 import CopyResponse400
from ...models.copy_response_401 import CopyResponse401
from ...models.copy_response_500 import CopyResponse500
from ...types import Response


def _get_kwargs(
    *,
    client: Client = None,
    json_body: CopyJsonBody,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/copy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = CopyResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = CopyResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = CopyResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CopyResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]:
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
    json_body: CopyJsonBody,
) -> Response[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]:
    """Copy a file or folder to a folder.

    Args:
        json_body (CopyJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: CopyJsonBody,
) -> Optional[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]:
    """Copy a file or folder to a folder.

    Args:
        json_body (CopyJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    json_body: CopyJsonBody,
) -> Response[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]:
    """Copy a file or folder to a folder.

    Args:
        json_body (CopyJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    json_body: CopyJsonBody,
) -> Optional[Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]]:
    """Copy a file or folder to a folder.

    Args:
        json_body (CopyJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CopyResponse200, CopyResponse400, CopyResponse401, CopyResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
