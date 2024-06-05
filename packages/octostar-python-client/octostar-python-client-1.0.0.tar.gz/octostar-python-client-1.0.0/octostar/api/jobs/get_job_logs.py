from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.get_job_logs_response_401 import GetJobLogsResponse401
from ...models.get_job_logs_response_404 import GetJobLogsResponse404
from ...models.get_job_logs_response_500 import GetJobLogsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_name: str,
    *,
    client: Client = None,
    since_seconds: Union[Unset, None, int] = UNSET,
    tail_lines: Union[Unset, None, int] = UNSET,
    tail_bytes: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/jobs/logs/{job_name}".format(client.base_url, job_name=job_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["since_seconds"] = since_seconds

    params["tail_lines"] = tail_lines

    params["tail_bytes"] = tail_bytes

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
) -> Optional[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetJobLogsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GetJobLogsResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetJobLogsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]:
    if not client:
        client = get_default_client()
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_name: str,
    *,
    client: Client = None,
    since_seconds: Union[Unset, None, int] = UNSET,
    tail_lines: Union[Unset, None, int] = UNSET,
    tail_bytes: Union[Unset, None, int] = UNSET,
) -> Response[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]:
    """Get logs of a job

     Fetch the logs of a specific job

    Args:
        job_name (str):
        since_seconds (Union[Unset, None, int]):
        tail_lines (Union[Unset, None, int]):
        tail_bytes (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        job_name=job_name,
        client=client,
        since_seconds=since_seconds,
        tail_lines=tail_lines,
        tail_bytes=tail_bytes,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )
    if response.is_error:
        print(f"{str(response.status_code)} Error: {response.text} for request", str(kwargs))
    return _build_response(client=client, response=response)


def sync(
    job_name: str,
    *,
    client: Client = None,
    since_seconds: Union[Unset, None, int] = UNSET,
    tail_lines: Union[Unset, None, int] = UNSET,
    tail_bytes: Union[Unset, None, int] = UNSET,
) -> Optional[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]:
    """Get logs of a job

     Fetch the logs of a specific job

    Args:
        job_name (str):
        since_seconds (Union[Unset, None, int]):
        tail_lines (Union[Unset, None, int]):
        tail_bytes (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        job_name=job_name,
        client=client,
        since_seconds=since_seconds,
        tail_lines=tail_lines,
        tail_bytes=tail_bytes,
    ).parsed


async def asyncio_detailed(
    job_name: str,
    *,
    client: Client = None,
    since_seconds: Union[Unset, None, int] = UNSET,
    tail_lines: Union[Unset, None, int] = UNSET,
    tail_bytes: Union[Unset, None, int] = UNSET,
) -> Response[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]:
    """Get logs of a job

     Fetch the logs of a specific job

    Args:
        job_name (str):
        since_seconds (Union[Unset, None, int]):
        tail_lines (Union[Unset, None, int]):
        tail_bytes (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        job_name=job_name,
        client=client,
        since_seconds=since_seconds,
        tail_lines=tail_lines,
        tail_bytes=tail_bytes,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_name: str,
    *,
    client: Client = None,
    since_seconds: Union[Unset, None, int] = UNSET,
    tail_lines: Union[Unset, None, int] = UNSET,
    tail_bytes: Union[Unset, None, int] = UNSET,
) -> Optional[Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]]:
    """Get logs of a job

     Fetch the logs of a specific job

    Args:
        job_name (str):
        since_seconds (Union[Unset, None, int]):
        tail_lines (Union[Unset, None, int]):
        tail_bytes (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetJobLogsResponse401, GetJobLogsResponse404, GetJobLogsResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            job_name=job_name,
            client=client,
            since_seconds=since_seconds,
            tail_lines=tail_lines,
            tail_bytes=tail_bytes,
        )
    ).parsed
