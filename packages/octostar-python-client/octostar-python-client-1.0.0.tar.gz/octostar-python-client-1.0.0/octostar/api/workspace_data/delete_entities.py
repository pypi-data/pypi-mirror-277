from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.acknowledgement import Acknowledgement
from ...models.delete_entities_response_401 import DeleteEntitiesResponse401
from ...models.delete_entities_response_409 import DeleteEntitiesResponse409
from ...models.delete_entities_response_500 import DeleteEntitiesResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client = None,
    json_body: List[str],
    recurse: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/entity".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["recurse"] = recurse

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "method": "delete",
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
) -> Optional[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = Acknowledgement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = DeleteEntitiesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = DeleteEntitiesResponse409.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = DeleteEntitiesResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]:
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
    json_body: List[str],
    recurse: Union[Unset, None, bool] = False,
) -> Response[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]:
    """Delete entity operation

     This operation will delete entities given their IDs

    Args:
        recurse (Union[Unset, None, bool]):  Example: True.
        json_body (List[str]): The list of entity wso_ids to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        recurse=recurse,
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
    json_body: List[str],
    recurse: Union[Unset, None, bool] = False,
) -> Optional[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]:
    """Delete entity operation

     This operation will delete entities given their IDs

    Args:
        recurse (Union[Unset, None, bool]):  Example: True.
        json_body (List[str]): The list of entity wso_ids to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        json_body=json_body,
        recurse=recurse,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    json_body: List[str],
    recurse: Union[Unset, None, bool] = False,
) -> Response[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]:
    """Delete entity operation

     This operation will delete entities given their IDs

    Args:
        recurse (Union[Unset, None, bool]):  Example: True.
        json_body (List[str]): The list of entity wso_ids to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        recurse=recurse,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    json_body: List[str],
    recurse: Union[Unset, None, bool] = False,
) -> Optional[Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]]:
    """Delete entity operation

     This operation will delete entities given their IDs

    Args:
        recurse (Union[Unset, None, bool]):  Example: True.
        json_body (List[str]): The list of entity wso_ids to delete

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, DeleteEntitiesResponse401, DeleteEntitiesResponse409, DeleteEntitiesResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            recurse=recurse,
        )
    ).parsed
