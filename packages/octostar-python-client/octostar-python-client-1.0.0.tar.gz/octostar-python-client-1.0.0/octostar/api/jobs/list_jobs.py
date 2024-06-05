from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.job_status import JobStatus
from ...models.list_jobs_response_401 import ListJobsResponse401
from ...models.list_jobs_response_500 import ListJobsResponse500
from ...types import Response


def _get_kwargs(
    *,
    client: Client = None,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/jobs/list".format(client.base_url)

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
) -> Optional[Union[ListJobsResponse401, ListJobsResponse500, List["JobStatus"]]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_job_status_list_item_data in _response_200:
            componentsschemas_job_status_list_item = JobStatus.from_dict(componentsschemas_job_status_list_item_data)

            response_200.append(componentsschemas_job_status_list_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ListJobsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ListJobsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[ListJobsResponse401, ListJobsResponse500, List["JobStatus"]]]:
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
) -> Response[Union[ListJobsResponse401, ListJobsResponse500, List["JobStatus"]]]:
    """List running jobs

     list all the jobs you are authorized to see. If you are an admin, you will see all the jobs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListJobsResponse401, ListJobsResponse500, List['JobStatus']]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
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
    *,
    client: Client = None,
) -> Optional[Union[ListJobsResponse401, ListJobsResponse500, List["JobStatus"]]]:
    """List running jobs

     list all the jobs you are authorized to see. If you are an admin, you will see all the jobs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListJobsResponse401, ListJobsResponse500, List['JobStatus']]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
) -> Response[Union[ListJobsResponse401, ListJobsResponse500, List["JobStatus"]]]:
    """List running jobs

     list all the jobs you are authorized to see. If you are an admin, you will see all the jobs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListJobsResponse401, ListJobsResponse500, List['JobStatus']]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
) -> Optional[Union[ListJobsResponse401, ListJobsResponse500, List["JobStatus"]]]:
    """List running jobs

     list all the jobs you are authorized to see. If you are an admin, you will see all the jobs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListJobsResponse401, ListJobsResponse500, List['JobStatus']]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
