from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.acknowledgement import Acknowledgement
from ...models.get_job_progress_response_401 import GetJobProgressResponse401
from ...models.internal_server_error import InternalServerError
from ...types import Response


def _get_kwargs(
    job_name: str,
    *,
    client: Client = None,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/jobs/progress/{job_name}".format(client.base_url, job_name=job_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = Acknowledgement.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetJobProgressResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = InternalServerError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]:
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
) -> Response[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]:
    """Get the job progress string value

     Fetch the progress string of a specified job.

    Args:
        job_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        job_name=job_name,
        client=client,
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
) -> Optional[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]:
    """Get the job progress string value

     Fetch the progress string of a specified job.

    Args:
        job_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        job_name=job_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    job_name: str,
    *,
    client: Client = None,
) -> Response[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]:
    """Get the job progress string value

     Fetch the progress string of a specified job.

    Args:
        job_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        job_name=job_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_name: str,
    *,
    client: Client = None,
) -> Optional[Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]]:
    """Get the job progress string value

     Fetch the progress string of a specified job.

    Args:
        job_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Acknowledgement, GetJobProgressResponse401, InternalServerError]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            job_name=job_name,
            client=client,
        )
    ).parsed
