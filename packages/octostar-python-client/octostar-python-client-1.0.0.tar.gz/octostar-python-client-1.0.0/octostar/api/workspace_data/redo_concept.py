from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.entity_response import EntityResponse
from ...models.redo_concept_response_400 import RedoConceptResponse400
from ...models.redo_concept_response_401 import RedoConceptResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    concept: str,
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/redo_concept/{concept}".format(client.base_url, concept=concept)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ontology"] = ontology

    params["code"] = code

    params["force"] = force

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
) -> Optional[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RedoConceptResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = RedoConceptResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = EntityResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    concept: str,
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Response[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]:
    """Rebuild local data table

     Gets the local data from the table, drops, rebuild table, inserts. Use this carefully.

    Args:
        concept (str):
        ontology (str):
        code (Union[Unset, None, str]):
        force (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        concept=concept,
        client=client,
        ontology=ontology,
        code=code,
        force=force,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    if response.is_error:
        print(f"{str(response.status_code)} Error: {response.text} for request", str(kwargs))
    return _build_response(client=client, response=response)


def sync(
    concept: str,
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]:
    """Rebuild local data table

     Gets the local data from the table, drops, rebuild table, inserts. Use this carefully.

    Args:
        concept (str):
        ontology (str):
        code (Union[Unset, None, str]):
        force (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        concept=concept,
        client=client,
        ontology=ontology,
        code=code,
        force=force,
    ).parsed


async def asyncio_detailed(
    concept: str,
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Response[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]:
    """Rebuild local data table

     Gets the local data from the table, drops, rebuild table, inserts. Use this carefully.

    Args:
        concept (str):
        ontology (str):
        code (Union[Unset, None, str]):
        force (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        concept=concept,
        client=client,
        ontology=ontology,
        code=code,
        force=force,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    concept: str,
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]]:
    """Rebuild local data table

     Gets the local data from the table, drops, rebuild table, inserts. Use this carefully.

    Args:
        concept (str):
        ontology (str):
        code (Union[Unset, None, str]):
        force (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityResponse, RedoConceptResponse400, RedoConceptResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            concept=concept,
            client=client,
            ontology=ontology,
            code=code,
            force=force,
        )
    ).parsed
