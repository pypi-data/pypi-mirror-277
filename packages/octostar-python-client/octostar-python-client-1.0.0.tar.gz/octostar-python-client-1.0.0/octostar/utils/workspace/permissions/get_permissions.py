import logging
from typing import List, Union

logger = logging.getLogger(__name__)

from .PermissionLevel import PermissionLevel
from ....api.workspace_permissions import get_permissions
from ....client import Client

def sync(
    os_workspace: Union[List[str], str],
    client: Client = None
):
    """
    Get the permissions for one or more workspaces.

    Args:
        os_workspace: the ID (or list of IDs) of the workspaces to find permissions for.
        client: The Client with which to connect to Octostar, which is also the user for
                which the permissions are given. If None, the default one is used.

    Returns:
        A dictionary, where each key is a workspace ID and each value is the permission
        level for that workspace.

    Raises:
        ValueError: If the ID is not a valid entity ID (and safe is enabled).
        ConnectionError: If the entity could not be removed (and raise_on_missing is enabled).
    """
    if not isinstance(os_workspace, list):
        os_workspace = [os_workspace]
    response = get_permissions.sync_detailed(os_workspaces=",".join(os_workspace),
                                             client=client)
    if response.status_code != 200 or response.parsed and response.parsed.status != 'success':
        raise ConnectionError(
            f"get_permissions failed, status code: {response}")
    workspaces = response.parsed.data.additional_properties
    workspaces = {k: PermissionLevel(v['value']) for k, v in workspaces.items()}
    return workspaces

async def asyncio(
    os_workspace: Union[List[str], str],
    client: Client = None
):
    """
    Get asynchronously the permissions for one or more workspaces.

    Args:
        os_workspace: the ID (or list of IDs) of the workspaces to find permissions for.
        client: The Client with which to connect to Octostar, which is also the user for
                which the permissions are given. If None, the default one is used.

    Returns:
        A dictionary, where each key is a workspace ID and each value is the permission
        level for that workspace.

    Raises:
        ValueError: If the ID is not a valid entity ID (and safe is enabled).
        ConnectionError: If the entity could not be removed (and raise_on_missing is enabled).
    """
    if not isinstance(os_workspace, list):
        os_workspace = [os_workspace]
    response = await get_permissions.asyncio_detailed(os_workspaces=",".join(os_workspace),
                                                      client=client)
    if response.status_code != 200 or response.parsed and response.parsed.status != 'success':
        raise ConnectionError(
            f"get_permissions failed, status code: {response}")
    workspaces = response.parsed.data.additional_properties
    workspaces = {k: PermissionLevel(v['value']) for k, v in workspaces.items()}
    return workspaces
