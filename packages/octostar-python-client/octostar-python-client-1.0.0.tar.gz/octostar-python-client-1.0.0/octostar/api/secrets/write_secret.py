from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.write_secret_json_body import WriteSecretJsonBody
from ...models.write_secret_response_200 import WriteSecretResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client = None,
    json_body: WriteSecretJsonBody,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/secret/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client = None, response: httpx.Response) -> Optional[Union[Any, WriteSecretResponse200]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = WriteSecretResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client = None, response: httpx.Response) -> Response[Union[Any, WriteSecretResponse200]]:
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
    json_body: WriteSecretJsonBody,
) -> Response[Union[Any, WriteSecretResponse200]]:
    """Write or update a secret key-value for a job

     Write or update a secret key and value for a job. Users can't override OS_* prefixed keys.

    Args:
        json_body (WriteSecretJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WriteSecretResponse200]]
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
    json_body: WriteSecretJsonBody,
) -> Optional[Union[Any, WriteSecretResponse200]]:
    """Write or update a secret key-value for a job

     Write or update a secret key and value for a job. Users can't override OS_* prefixed keys.

    Args:
        json_body (WriteSecretJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WriteSecretResponse200]
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
    json_body: WriteSecretJsonBody,
) -> Response[Union[Any, WriteSecretResponse200]]:
    """Write or update a secret key-value for a job

     Write or update a secret key and value for a job. Users can't override OS_* prefixed keys.

    Args:
        json_body (WriteSecretJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, WriteSecretResponse200]]
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
    json_body: WriteSecretJsonBody,
) -> Optional[Union[Any, WriteSecretResponse200]]:
    """Write or update a secret key-value for a job

     Write or update a secret key and value for a job. Users can't override OS_* prefixed keys.

    Args:
        json_body (WriteSecretJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, WriteSecretResponse200]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
