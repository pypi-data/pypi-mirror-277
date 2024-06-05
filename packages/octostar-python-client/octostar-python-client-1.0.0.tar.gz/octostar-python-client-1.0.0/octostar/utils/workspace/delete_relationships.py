import logging
from typing import List

logger = logging.getLogger(__name__)

from ...api.workspace_data import delete_entities
from ..ontology import query_ontology
from ...client import Client

def sync(
    os_relationship_uids: List[str],
    safe: bool = False,
    raise_on_missing: bool = False,
    client: Client = None
):
    """
    Delete a list of local relationships given their IDs.

    Args:
        os_relationships_uids: The list of IDs.
        safe: Whether to raise a ValueError before removal if some relationships in the list do not exist.
        raise_on_missing: Whether to raise a ConnectionError if some of the relationships could not be deleted.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The number of successfully deleted relationships.

    Raises:
        ValueError: If the list of IDs contain invalid entries (and safe is enabled).
        ConnectionError: If some of the relationships could not be removed (and raise_on_missing is enabled).
    """
    assert(len(os_relationship_uids) > 0)
    if safe:
        uids_text = ", ".join(["'" + os_rel_uid + "'" for os_rel_uid in os_relationship_uids])
        uids = query_ontology.sync(f"SELECT * FROM `dtimbr`.`os_workspace_relationship` WHERE CAST(os_entity_uid AS String) IN {uids_text}")
        if len(uids) < len(os_relationship_uids):
            raise ValueError("Attempting to remove a relationship which does not exist!")
    response = delete_entities.sync_detailed(json_body=os_relationship_uids,
                                             client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"delete_relationships failed with status code " + str(response.status_code))
    if int(response.parsed.message) < len(os_relationship_uids):
        logger.warning("Deleted only " + response.parsed.message + "/" + str(len(os_relationship_uids)) + " relationships")
        if raise_on_missing:
            raise ConnectionError("Failed to delete some relationships! (likely they did not exist prior to this call")
    return int(response.parsed.message)


async def asyncio(
    os_relationship_uids: List[str],
    safe: bool = False,
    raise_on_missing: bool = False,
    client: Client = None
):
    """
    Delete asynchronously a list of local relationships given their IDs.

    Args:
        os_relationships_uids: The list of IDs.
        safe: Whether to raise a ValueError before removal if some relationships in the list do not exist.
        raise_on_missing: Whether to raise a ConnectionError if some of the relationships could not be deleted.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The number of successfully deleted relationships.

    Raises:
        ValueError: If the list of IDs contain invalid entries (and safe is enabled).
        ConnectionError: If some of the relationships could not be removed (and raise_on_missing is enabled).
    """
    assert(len(os_relationship_uids) > 0)
    if safe:
        uids_text = ", ".join(["'" + os_rel_uid + "'" for os_rel_uid in os_relationship_uids])
        uids = await query_ontology.asyncio(f"SELECT * FROM `dtimbr`.`os_workspace_relationship` WHERE CAST(os_entity_uid AS String) IN {uids_text}")
        if len(uids) < len(os_relationship_uids):
            raise ValueError("Attempting to remove a relationship which does not exist!")
    response = await delete_entities.asyncio_detailed(json_body=os_relationship_uids,
                                                      client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"delete_relationships failed with status code " + str(response.status_code))
    if int(response.parsed.message) < len(os_relationship_uids):
        logger.warning("Deleted only " + response.parsed.message + "/" + str(len(os_relationship_uids)) + " relationships")
        if raise_on_missing:
            raise ConnectionError("Failed to delete some relationships! (likely they did not exist prior to this call")  
    return int(response.parsed.message)
