from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.insert_entity_request import InsertEntityRequest
from ...models.insert_records_response_401 import InsertRecordsResponse401
from ...models.successful_insertion import SuccessfulInsertion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    client: Client = None,
    json_body: InsertEntityRequest,
    bypass_record_validation: Union[Unset, None, bool] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/v1/octostar/workspace-records/insert/{workspace_id}".format(
        client.base_url, workspace_id=workspace_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["bypass_record_validation"] = bypass_record_validation

    params["delete_before_insert"] = delete_before_insert

    params["batch_size"] = batch_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

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
) -> Optional[Union[InsertRecordsResponse401, SuccessfulInsertion]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = SuccessfulInsertion.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = InsertRecordsResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[InsertRecordsResponse401, SuccessfulInsertion]]:
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
    *,
    client: Client = None,
    json_body: InsertEntityRequest,
    bypass_record_validation: Union[Unset, None, bool] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[InsertRecordsResponse401, SuccessfulInsertion]]:
    """Insert workspace records

     This operation will insert given records and their relationships to workspace

    Args:
        workspace_id (str):
        bypass_record_validation (Union[Unset, None, bool]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (InsertEntityRequest): Entities to insert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InsertRecordsResponse401, SuccessfulInsertion]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
        bypass_record_validation=bypass_record_validation,
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
    *,
    client: Client = None,
    json_body: InsertEntityRequest,
    bypass_record_validation: Union[Unset, None, bool] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[InsertRecordsResponse401, SuccessfulInsertion]]:
    """Insert workspace records

     This operation will insert given records and their relationships to workspace

    Args:
        workspace_id (str):
        bypass_record_validation (Union[Unset, None, bool]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (InsertEntityRequest): Entities to insert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InsertRecordsResponse401, SuccessfulInsertion]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
        bypass_record_validation=bypass_record_validation,
        delete_before_insert=delete_before_insert,
        batch_size=batch_size,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: Client = None,
    json_body: InsertEntityRequest,
    bypass_record_validation: Union[Unset, None, bool] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Response[Union[InsertRecordsResponse401, SuccessfulInsertion]]:
    """Insert workspace records

     This operation will insert given records and their relationships to workspace

    Args:
        workspace_id (str):
        bypass_record_validation (Union[Unset, None, bool]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (InsertEntityRequest): Entities to insert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InsertRecordsResponse401, SuccessfulInsertion]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
        bypass_record_validation=bypass_record_validation,
        delete_before_insert=delete_before_insert,
        batch_size=batch_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: Client = None,
    json_body: InsertEntityRequest,
    bypass_record_validation: Union[Unset, None, bool] = UNSET,
    delete_before_insert: Union[Unset, None, bool] = UNSET,
    batch_size: Union[Unset, None, int] = UNSET,
) -> Optional[Union[InsertRecordsResponse401, SuccessfulInsertion]]:
    """Insert workspace records

     This operation will insert given records and their relationships to workspace

    Args:
        workspace_id (str):
        bypass_record_validation (Union[Unset, None, bool]):
        delete_before_insert (Union[Unset, None, bool]):
        batch_size (Union[Unset, None, int]):
        json_body (InsertEntityRequest): Entities to insert.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InsertRecordsResponse401, SuccessfulInsertion]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            json_body=json_body,
            bypass_record_validation=bypass_record_validation,
            delete_before_insert=delete_before_insert,
            batch_size=batch_size,
        )
    ).parsed
