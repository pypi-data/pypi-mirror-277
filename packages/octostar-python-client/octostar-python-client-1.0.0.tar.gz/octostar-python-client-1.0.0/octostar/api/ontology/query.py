from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.query_json_body import QueryJsonBody
from ...models.query_response_400 import QueryResponse400
from ...models.query_response_401 import QueryResponse401
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client = None,
    json_body: QueryJsonBody,
    ontology: str,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/timbr/query".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ontology"] = ontology

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
) -> Optional[Union[QueryResponse400, QueryResponse401]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = QueryResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = QueryResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[QueryResponse400, QueryResponse401]]:
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
    json_body: QueryJsonBody,
    ontology: str,
) -> Response[Union[QueryResponse400, QueryResponse401]]:
    """Execute SQL query

     This operation will execute the provided SQL query

    Args:
        ontology (str):
        json_body (QueryJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QueryResponse400, QueryResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        ontology=ontology,
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
    json_body: QueryJsonBody,
    ontology: str,
) -> Optional[Union[QueryResponse400, QueryResponse401]]:
    """Execute SQL query

     This operation will execute the provided SQL query

    Args:
        ontology (str):
        json_body (QueryJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QueryResponse400, QueryResponse401]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        json_body=json_body,
        ontology=ontology,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    json_body: QueryJsonBody,
    ontology: str,
) -> Response[Union[QueryResponse400, QueryResponse401]]:
    """Execute SQL query

     This operation will execute the provided SQL query

    Args:
        ontology (str):
        json_body (QueryJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[QueryResponse400, QueryResponse401]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        ontology=ontology,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    json_body: QueryJsonBody,
    ontology: str,
) -> Optional[Union[QueryResponse400, QueryResponse401]]:
    """Execute SQL query

     This operation will execute the provided SQL query

    Args:
        ontology (str):
        json_body (QueryJsonBody): The SQL query to be executed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[QueryResponse400, QueryResponse401]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            ontology=ontology,
        )
    ).parsed
