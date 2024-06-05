from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.acknowledgement import Acknowledgement
from ...models.entity import Entity
from ...models.successful_insertion import SuccessfulInsertion
from ...models.tag_entities_response_401 import TagEntitiesResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
    color: Union[Unset, None, str] = UNSET,
    group: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, float] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/v1/octostar/workspace-tags/{workspace_id}/{tag}".format(
        client.base_url, workspace_id=workspace_id, tag=tag
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["color"] = color

    params["group"] = group

    params["order"] = order

    params["delete_before_insert"] = delete_before_insert

    params["batch_size"] = batch_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body: Union[Dict[str, Any], List[Dict[str, Any]]]

    if isinstance(json_body, Entity):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = []
        for componentsschemas_entities_type_1_item_data in json_body:
            componentsschemas_entities_type_1_item = componentsschemas_entities_type_1_item_data.to_dict()

            json_json_body.append(componentsschemas_entities_type_1_item)

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
) -> Optional[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessfulInsertion.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = TagEntitiesResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Acknowledgement.from_dict(response.json())

        return response_400
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
) -> Response[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
    color: Union[Unset, None, str] = UNSET,
    group: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, float] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]:
    """Tag workspace records

    Args:
        workspace_id (str):
        tag (str):
        color (Union[Unset, None, str]):
        group (Union[Unset, None, str]):
        order (Union[Unset, None, float]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        tag=tag,
        client=client,
        json_body=json_body,
        color=color,
        group=group,
        order=order,
        delete_before_insert=delete_before_insert,
        batch_size=batch_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    if response.is_error:
        print(f"{str(response.status_code)} Error: {response.text} for request", str(kwargs))
    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
    color: Union[Unset, None, str] = UNSET,
    group: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, float] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]:
    """Tag workspace records

    Args:
        workspace_id (str):
        tag (str):
        color (Union[Unset, None, str]):
        group (Union[Unset, None, str]):
        order (Union[Unset, None, float]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        workspace_id=workspace_id,
        tag=tag,
        client=client,
        json_body=json_body,
        color=color,
        group=group,
        order=order,
        delete_before_insert=delete_before_insert,
        batch_size=batch_size,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
    color: Union[Unset, None, str] = UNSET,
    group: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, float] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]:
    """Tag workspace records

    Args:
        workspace_id (str):
        tag (str):
        color (Union[Unset, None, str]):
        group (Union[Unset, None, str]):
        order (Union[Unset, None, float]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        tag=tag,
        client=client,
        json_body=json_body,
        color=color,
        group=group,
        order=order,
        delete_before_insert=delete_before_insert,
        batch_size=batch_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
    color: Union[Unset, None, str] = UNSET,
    group: Union[Unset, None, str] = UNSET,
    order: Union[Unset, None, float] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]]:
    """Tag workspace records

    Args:
        workspace_id (str):
        tag (str):
        color (Union[Unset, None, str]):
        group (Union[Unset, None, str]):
        order (Union[Unset, None, float]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, SuccessfulInsertion, TagEntitiesResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            tag=tag,
            client=client,
            json_body=json_body,
            color=color,
            group=group,
            order=order,
            delete_before_insert=delete_before_insert,
            batch_size=batch_size,
        )
    ).parsed
