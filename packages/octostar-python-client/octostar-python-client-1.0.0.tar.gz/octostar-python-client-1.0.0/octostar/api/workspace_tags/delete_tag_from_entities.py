from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.acknowledgement import Acknowledgement
from ...models.delete_tag_from_entities_response_401 import DeleteTagFromEntitiesResponse401
from ...models.entity import Entity
from ...types import Response


def _get_kwargs(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/v1/octostar/workspace-tags/{workspace_id}/{tag}".format(
        client.base_url, workspace_id=workspace_id, tag=tag
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Union[Dict[str, Any], List[Dict[str, Any]]]

    if isinstance(json_body, Entity):
        json_json_body = json_body.to_dict()

    else:
        json_json_body = []
        for componentsschemas_entities_type_1_item_data in json_body:
            componentsschemas_entities_type_1_item = componentsschemas_entities_type_1_item_data.to_dict()

            json_json_body.append(componentsschemas_entities_type_1_item)

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = Acknowledgement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Acknowledgement.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = DeleteTagFromEntitiesResponse401.from_dict(response.json())

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
) -> Response[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]:
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
) -> Response[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]:
    """Remove tag from entities sent in the body

    Args:
        workspace_id (str):
        tag (str):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        tag=tag,
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
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
) -> Optional[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]:
    """Remove tag from entities sent in the body

    Args:
        workspace_id (str):
        tag (str):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        workspace_id=workspace_id,
        tag=tag,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    tag: str,
    *,
    client: Client = None,
    json_body: Union["Entity", List["Entity"]],
) -> Response[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]:
    """Remove tag from entities sent in the body

    Args:
        workspace_id (str):
        tag (str):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        tag=tag,
        client=client,
        json_body=json_body,
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
) -> Optional[Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]]:
    """Remove tag from entities sent in the body

    Args:
        workspace_id (str):
        tag (str):
        json_body (Union['Entity', List['Entity']]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, Any, DeleteTagFromEntitiesResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            tag=tag,
            client=client,
            json_body=json_body,
        )
    ).parsed
