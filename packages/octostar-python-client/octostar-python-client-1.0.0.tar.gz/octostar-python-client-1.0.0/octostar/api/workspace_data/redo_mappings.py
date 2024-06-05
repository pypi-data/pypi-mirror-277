from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.redo_mappings_response_200 import RedoMappingsResponse200
from ...models.redo_mappings_response_400 import RedoMappingsResponse400
from ...models.redo_mappings_response_401 import RedoMappingsResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/redo_mappings".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ontology"] = ontology

    params["code"] = code

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
) -> Optional[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RedoMappingsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = RedoMappingsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = RedoMappingsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]:
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
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
) -> Response[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]:
    """Recreate mappings

     Generates new mappings for local data and relationships

    Args:
        ontology (str):
        code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        ontology=ontology,
        code=code,
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
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
) -> Optional[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]:
    """Recreate mappings

     Generates new mappings for local data and relationships

    Args:
        ontology (str):
        code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        ontology=ontology,
        code=code,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
) -> Response[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]:
    """Recreate mappings

     Generates new mappings for local data and relationships

    Args:
        ontology (str):
        code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        ontology=ontology,
        code=code,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    ontology: str,
    code: Union[Unset, None, str] = UNSET,
) -> Optional[Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]]:
    """Recreate mappings

     Generates new mappings for local data and relationships

    Args:
        ontology (str):
        code (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RedoMappingsResponse200, RedoMappingsResponse400, RedoMappingsResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            ontology=ontology,
            code=code,
        )
    ).parsed
