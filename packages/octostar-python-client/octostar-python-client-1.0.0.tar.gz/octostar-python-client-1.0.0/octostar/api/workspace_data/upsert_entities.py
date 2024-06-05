from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.entity_response import EntityResponse
from ...models.upsert_entities_response_401 import UpsertEntitiesResponse401
from ...models.upsert_entity import UpsertEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client = None,
    json_body: List["UpsertEntity"],
    asis: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/entity".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["asis"] = asis

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[Union[EntityResponse, UpsertEntitiesResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = EntityResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = UpsertEntitiesResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[EntityResponse, UpsertEntitiesResponse401]]:
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
    json_body: List["UpsertEntity"],
    asis: Union[Unset, None, bool] = UNSET,
) -> Response[Union[EntityResponse, UpsertEntitiesResponse401]]:
    """Insert / Update entities operation

     This operation will upsert local entities

    Args:
        asis (Union[Unset, None, bool]):
        json_body (List['UpsertEntity']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityResponse, UpsertEntitiesResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        asis=asis,
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
    json_body: List["UpsertEntity"],
    asis: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[EntityResponse, UpsertEntitiesResponse401]]:
    """Insert / Update entities operation

     This operation will upsert local entities

    Args:
        asis (Union[Unset, None, bool]):
        json_body (List['UpsertEntity']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityResponse, UpsertEntitiesResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        json_body=json_body,
        asis=asis,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    json_body: List["UpsertEntity"],
    asis: Union[Unset, None, bool] = UNSET,
) -> Response[Union[EntityResponse, UpsertEntitiesResponse401]]:
    """Insert / Update entities operation

     This operation will upsert local entities

    Args:
        asis (Union[Unset, None, bool]):
        json_body (List['UpsertEntity']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityResponse, UpsertEntitiesResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        asis=asis,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    json_body: List["UpsertEntity"],
    asis: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[EntityResponse, UpsertEntitiesResponse401]]:
    """Insert / Update entities operation

     This operation will upsert local entities

    Args:
        asis (Union[Unset, None, bool]):
        json_body (List['UpsertEntity']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityResponse, UpsertEntitiesResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            asis=asis,
        )
    ).parsed
