from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.octostar_event import OctostarEvent
from ...models.pull_events_from_stream_response_401 import PullEventsFromStreamResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    stream_id: str,
    *,
    client: Client = None,
    count: Union[Unset, None, int] = 10,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/streams/{stream_id}".format(client.base_url, stream_id=stream_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["count"] = count

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
) -> Optional[Union[Any, List["OctostarEvent"], PullEventsFromStreamResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OctostarEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = PullEventsFromStreamResponse401.from_dict(response.json())

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
) -> Response[Union[Any, List["OctostarEvent"], PullEventsFromStreamResponse401]]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stream_id: str,
    *,
    client: Client = None,
    count: Union[Unset, None, int] = 10,
) -> Response[Union[Any, List["OctostarEvent"], PullEventsFromStreamResponse401]]:
    """Pulls events from a stream

    Args:
        stream_id (str):
        count (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['OctostarEvent'], PullEventsFromStreamResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        stream_id=stream_id,
        client=client,
        count=count,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    if response.is_error:
        print(f"{str(response.status_code)} Error: {response.text} for request", str(kwargs))
    return _build_response(client=client, response=response)


def sync(
    stream_id: str,
    *,
    client: Client = None,
    count: Union[Unset, None, int] = 10,
) -> Optional[Union[Any, List["OctostarEvent"], PullEventsFromStreamResponse401]]:
    """Pulls events from a stream

    Args:
        stream_id (str):
        count (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['OctostarEvent'], PullEventsFromStreamResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        stream_id=stream_id,
        client=client,
        count=count,
    ).parsed


async def asyncio_detailed(
    stream_id: str,
    *,
    client: Client = None,
    count: Union[Unset, None, int] = 10,
) -> Response[Union[Any, List["OctostarEvent"], PullEventsFromStreamResponse401]]:
    """Pulls events from a stream

    Args:
        stream_id (str):
        count (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['OctostarEvent'], PullEventsFromStreamResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        stream_id=stream_id,
        client=client,
        count=count,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stream_id: str,
    *,
    client: Client = None,
    count: Union[Unset, None, int] = 10,
) -> Optional[Union[Any, List["OctostarEvent"], PullEventsFromStreamResponse401]]:
    """Pulls events from a stream

    Args:
        stream_id (str):
        count (Union[Unset, None, int]):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['OctostarEvent'], PullEventsFromStreamResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            stream_id=stream_id,
            client=client,
            count=count,
        )
    ).parsed
