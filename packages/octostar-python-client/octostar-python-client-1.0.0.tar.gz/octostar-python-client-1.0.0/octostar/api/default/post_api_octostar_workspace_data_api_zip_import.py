from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.post_api_octostar_workspace_data_api_zip_import_multipart_data import (
    PostApiOctostarWorkspaceDataApiZipImportMultipartData,
)
from ...models.post_api_octostar_workspace_data_api_zip_import_response_200 import (
    PostApiOctostarWorkspaceDataApiZipImportResponse200,
)
from ...models.post_api_octostar_workspace_data_api_zip_import_response_400 import (
    PostApiOctostarWorkspaceDataApiZipImportResponse400,
)
from ...models.post_api_octostar_workspace_data_api_zip_import_response_403 import (
    PostApiOctostarWorkspaceDataApiZipImportResponse403,
)
from ...models.post_api_octostar_workspace_data_api_zip_import_response_500 import (
    PostApiOctostarWorkspaceDataApiZipImportResponse500,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client = None,
    multipart_data: PostApiOctostarWorkspaceDataApiZipImportMultipartData,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/workspace_data_api/zip_import".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Client = None, response: httpx.Response
) -> Optional[
    Union[
        PostApiOctostarWorkspaceDataApiZipImportResponse200,
        PostApiOctostarWorkspaceDataApiZipImportResponse400,
        PostApiOctostarWorkspaceDataApiZipImportResponse403,
        PostApiOctostarWorkspaceDataApiZipImportResponse500,
    ]
]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = PostApiOctostarWorkspaceDataApiZipImportResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PostApiOctostarWorkspaceDataApiZipImportResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = PostApiOctostarWorkspaceDataApiZipImportResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PostApiOctostarWorkspaceDataApiZipImportResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[
    Union[
        PostApiOctostarWorkspaceDataApiZipImportResponse200,
        PostApiOctostarWorkspaceDataApiZipImportResponse400,
        PostApiOctostarWorkspaceDataApiZipImportResponse403,
        PostApiOctostarWorkspaceDataApiZipImportResponse500,
    ]
]:
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
    multipart_data: PostApiOctostarWorkspaceDataApiZipImportMultipartData,
) -> Response[
    Union[
        PostApiOctostarWorkspaceDataApiZipImportResponse200,
        PostApiOctostarWorkspaceDataApiZipImportResponse400,
        PostApiOctostarWorkspaceDataApiZipImportResponse403,
        PostApiOctostarWorkspaceDataApiZipImportResponse500,
    ]
]:
    """Uploads a zip file for extraction.

     Allows clients to upload a zip file containing entities for processing, with optional parameters to
    specify the target, whether to include content, include dashboards, and whether to overwrite
    existing data.

    Args:
        multipart_data (PostApiOctostarWorkspaceDataApiZipImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiOctostarWorkspaceDataApiZipImportResponse200, PostApiOctostarWorkspaceDataApiZipImportResponse400, PostApiOctostarWorkspaceDataApiZipImportResponse403, PostApiOctostarWorkspaceDataApiZipImportResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
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
    multipart_data: PostApiOctostarWorkspaceDataApiZipImportMultipartData,
) -> Optional[
    Union[
        PostApiOctostarWorkspaceDataApiZipImportResponse200,
        PostApiOctostarWorkspaceDataApiZipImportResponse400,
        PostApiOctostarWorkspaceDataApiZipImportResponse403,
        PostApiOctostarWorkspaceDataApiZipImportResponse500,
    ]
]:
    """Uploads a zip file for extraction.

     Allows clients to upload a zip file containing entities for processing, with optional parameters to
    specify the target, whether to include content, include dashboards, and whether to overwrite
    existing data.

    Args:
        multipart_data (PostApiOctostarWorkspaceDataApiZipImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiOctostarWorkspaceDataApiZipImportResponse200, PostApiOctostarWorkspaceDataApiZipImportResponse400, PostApiOctostarWorkspaceDataApiZipImportResponse403, PostApiOctostarWorkspaceDataApiZipImportResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client = None,
    multipart_data: PostApiOctostarWorkspaceDataApiZipImportMultipartData,
) -> Response[
    Union[
        PostApiOctostarWorkspaceDataApiZipImportResponse200,
        PostApiOctostarWorkspaceDataApiZipImportResponse400,
        PostApiOctostarWorkspaceDataApiZipImportResponse403,
        PostApiOctostarWorkspaceDataApiZipImportResponse500,
    ]
]:
    """Uploads a zip file for extraction.

     Allows clients to upload a zip file containing entities for processing, with optional parameters to
    specify the target, whether to include content, include dashboards, and whether to overwrite
    existing data.

    Args:
        multipart_data (PostApiOctostarWorkspaceDataApiZipImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiOctostarWorkspaceDataApiZipImportResponse200, PostApiOctostarWorkspaceDataApiZipImportResponse400, PostApiOctostarWorkspaceDataApiZipImportResponse403, PostApiOctostarWorkspaceDataApiZipImportResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client = None,
    multipart_data: PostApiOctostarWorkspaceDataApiZipImportMultipartData,
) -> Optional[
    Union[
        PostApiOctostarWorkspaceDataApiZipImportResponse200,
        PostApiOctostarWorkspaceDataApiZipImportResponse400,
        PostApiOctostarWorkspaceDataApiZipImportResponse403,
        PostApiOctostarWorkspaceDataApiZipImportResponse500,
    ]
]:
    """Uploads a zip file for extraction.

     Allows clients to upload a zip file containing entities for processing, with optional parameters to
    specify the target, whether to include content, include dashboards, and whether to overwrite
    existing data.

    Args:
        multipart_data (PostApiOctostarWorkspaceDataApiZipImportMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiOctostarWorkspaceDataApiZipImportResponse200, PostApiOctostarWorkspaceDataApiZipImportResponse400, PostApiOctostarWorkspaceDataApiZipImportResponse403, PostApiOctostarWorkspaceDataApiZipImportResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
