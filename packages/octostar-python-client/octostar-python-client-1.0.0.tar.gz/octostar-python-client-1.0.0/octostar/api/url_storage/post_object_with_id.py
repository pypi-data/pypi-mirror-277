from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.acknowledgement import Acknowledgement
from ...models.post_object_with_id_json_body import PostObjectWithIdJsonBody
from ...models.post_object_with_id_response_401 import PostObjectWithIdResponse401
from ...types import Response


def _get_kwargs(
    object_id: str,
    *,
    client: Client = None,
    json_body: PostObjectWithIdJsonBody,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/url_storage/{object_id}".format(client.base_url, object_id=object_id)

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
) -> Optional[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = Acknowledgement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PostObjectWithIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: str,
    *,
    client: Client = None,
    json_body: PostObjectWithIdJsonBody,
) -> Response[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]:
    """Store an object in the URL storage with a specific ID

    Args:
        object_id (str):
        json_body (PostObjectWithIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        object_id=object_id,
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
    object_id: str,
    *,
    client: Client = None,
    json_body: PostObjectWithIdJsonBody,
) -> Optional[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]:
    """Store an object in the URL storage with a specific ID

    Args:
        object_id (str):
        json_body (PostObjectWithIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, PostObjectWithIdResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        object_id=object_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    object_id: str,
    *,
    client: Client = None,
    json_body: PostObjectWithIdJsonBody,
) -> Response[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]:
    """Store an object in the URL storage with a specific ID

    Args:
        object_id (str):
        json_body (PostObjectWithIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        object_id=object_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: str,
    *,
    client: Client = None,
    json_body: PostObjectWithIdJsonBody,
) -> Optional[Union[Acknowledgement, Any, PostObjectWithIdResponse401]]:
    """Store an object in the URL storage with a specific ID

    Args:
        object_id (str):
        json_body (PostObjectWithIdJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, PostObjectWithIdResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
