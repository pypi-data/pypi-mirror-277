from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.get_jobs_url_json_body import GetJobsUrlJsonBody
from ...models.get_jobs_url_response_401 import GetJobsUrlResponse401
from ...models.get_jobs_url_response_500 import GetJobsUrlResponse500
from ...models.job_with_url import JobWithURL
from ...types import Response


def _get_kwargs(
    *,
    client: Client = None,
    json_body: GetJobsUrlJsonBody,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/jobs/get_url".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List["JobWithURL"]]]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_job_with_url_list_item_data in _response_200:
            componentsschemas_job_with_url_list_item = JobWithURL.from_dict(
                componentsschemas_job_with_url_list_item_data
            )

            response_200.append(componentsschemas_job_with_url_list_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GetJobsUrlResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GetJobsUrlResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List["JobWithURL"]]]:
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
    json_body: GetJobsUrlJsonBody,
) -> Response[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List["JobWithURL"]]]:
    """job urls from their names

     retrieves the url of jobs given their names.

    Args:
        json_body (GetJobsUrlJsonBody): The job ids to get the urls for.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List['JobWithURL']]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
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
    *,
    client: Client = None,
    json_body: GetJobsUrlJsonBody,
) -> Optional[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List["JobWithURL"]]]:
    """job urls from their names

     retrieves the url of jobs given their names.

    Args:
        json_body (GetJobsUrlJsonBody): The job ids to get the urls for.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List['JobWithURL']]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    json_body: GetJobsUrlJsonBody,
) -> Response[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List["JobWithURL"]]]:
    """job urls from their names

     retrieves the url of jobs given their names.

    Args:
        json_body (GetJobsUrlJsonBody): The job ids to get the urls for.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List['JobWithURL']]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    json_body: GetJobsUrlJsonBody,
) -> Optional[Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List["JobWithURL"]]]:
    """job urls from their names

     retrieves the url of jobs given their names.

    Args:
        json_body (GetJobsUrlJsonBody): The job ids to get the urls for.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetJobsUrlResponse401, GetJobsUrlResponse500, List['JobWithURL']]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
