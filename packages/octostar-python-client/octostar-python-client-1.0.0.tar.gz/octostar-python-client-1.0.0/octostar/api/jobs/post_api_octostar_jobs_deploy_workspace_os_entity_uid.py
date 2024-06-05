from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client, get_default_client
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_json_body import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody,
)
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_200 import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
)
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_400 import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
)
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_403 import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
)
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_404 import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
)
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_409 import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
)
from ...models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_500 import (
    PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
)
from ...types import Response


def _get_kwargs(
    workspace: str,
    os_entity_uid: str,
    *,
    client: Client = None,
    json_body: PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody,
) -> Dict[str, Any]:
    if not client:
        client = get_default_client()
    url = "{}/api/octostar/jobs/deploy/{workspace}/{os_entity_uid}".format(
        client.base_url, workspace=workspace, os_entity_uid=os_entity_uid
    )

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
) -> Optional[
    Union[
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
    ]
]:
    if not client:
        client = get_default_client()
    if response.status_code == HTTPStatus.OK:
        response_200 = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client = None, response: httpx.Response
) -> Response[
    Union[
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
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
    workspace: str,
    os_entity_uid: str,
    *,
    client: Client = None,
    json_body: PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody,
) -> Response[
    Union[
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
    ]
]:
    """Deploys a the app for a given workspace and entity, returns the entity.

     This endpoint deploys a specified manifest by workspace and os_entity_uid. It checks for user
    permissions,
    retrieves app entity data, processes manifest and related files from storage, and potentially
    initiates deployment
    based on the manifest configurations. It handles manifest retrieval, deprecation of `app.zip`, and
    conditional
    processing based on manifest properties.

    Args:
        workspace (str):
        os_entity_uid (str):
        json_body (PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace=workspace,
        os_entity_uid=os_entity_uid,
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
    workspace: str,
    os_entity_uid: str,
    *,
    client: Client = None,
    json_body: PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody,
) -> Optional[
    Union[
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
    ]
]:
    """Deploys a the app for a given workspace and entity, returns the entity.

     This endpoint deploys a specified manifest by workspace and os_entity_uid. It checks for user
    permissions,
    retrieves app entity data, processes manifest and related files from storage, and potentially
    initiates deployment
    based on the manifest configurations. It handles manifest retrieval, deprecation of `app.zip`, and
    conditional
    processing based on manifest properties.

    Args:
        workspace (str):
        os_entity_uid (str):
        json_body (PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500]
    """

    if not client:
        client = get_default_client()
    return sync_detailed(
        workspace=workspace,
        os_entity_uid=os_entity_uid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    os_entity_uid: str,
    *,
    client: Client = None,
    json_body: PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody,
) -> Response[
    Union[
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
    ]
]:
    """Deploys a the app for a given workspace and entity, returns the entity.

     This endpoint deploys a specified manifest by workspace and os_entity_uid. It checks for user
    permissions,
    retrieves app entity data, processes manifest and related files from storage, and potentially
    initiates deployment
    based on the manifest configurations. It handles manifest retrieval, deprecation of `app.zip`, and
    conditional
    processing based on manifest properties.

    Args:
        workspace (str):
        os_entity_uid (str):
        json_body (PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500]]
    """

    if not client:
        client = get_default_client()
    kwargs = _get_kwargs(
        workspace=workspace,
        os_entity_uid=os_entity_uid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    os_entity_uid: str,
    *,
    client: Client = None,
    json_body: PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody,
) -> Optional[
    Union[
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409,
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500,
    ]
]:
    """Deploys a the app for a given workspace and entity, returns the entity.

     This endpoint deploys a specified manifest by workspace and os_entity_uid. It checks for user
    permissions,
    retrieves app entity data, processes manifest and related files from storage, and potentially
    initiates deployment
    based on the manifest configurations. It handles manifest retrieval, deprecation of `app.zip`, and
    conditional
    processing based on manifest properties.

    Args:
        workspace (str):
        os_entity_uid (str):
        json_body (PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse400, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse403, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse404, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse409, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse500]
    """

    if not client:
        client = get_default_client()
    return (
        await asyncio_detailed(
            workspace=workspace,
            os_entity_uid=os_entity_uid,
            client=client,
            json_body=json_body,
        )
    ).parsed
