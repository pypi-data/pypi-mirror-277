import logging
from typing import List

logger = logging.getLogger(__name__)

from ...api.workspace_data import delete_entities
from ..ontology import query_ontology
from ...client import Client


def sync(
    os_entity_uids: List[str],
    safe: bool = False,
    raise_on_missing: bool = False,
    client: Client = None
):
    """
    Delete a list of local entities given their IDs.

    Args:
        os_entity_uids: The list of IDs.
        safe: whether to raise a ValueError before removal if some entities in the list do not exist.
        raise_on_missing: whether to raise a ConnectionError if some of the entities could not be deleted.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The number of successfully deleted entities.

    Raises:
        ValueError: If the list of IDs contain invalid entries (and safe is enabled).
        ConnectionError: If some of the entities could not be removed (and raise_on_missing is enabled).
    """
    assert(len(os_entity_uids) > 0)
    if safe:
        uids_text = ", ".join(["'" + os_entity_uid + "'" for os_entity_uid in os_entity_uids])
        uids = query_ontology.sync(
            f"SELECT * FROM `dtimbr`.`os_thing` WHERE CAST(os_entity_uid AS String) IN {uids_text} AND entity_type != 'os_workspace_relationship'")
        if len(uids) < len(os_entity_uids):
            raise ValueError("Attempting to remove an entity which does not exist!")
    response = delete_entities.sync_detailed(json_body=os_entity_uids,
                                             client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"delete_entities failed with status code " + str(response.status_code))
    if int(response.parsed.message) < len(os_entity_uids):
        logger.warning("Deleted only " + response.parsed.message + "/" + str(len(os_entity_uids)) + " entities")
        if raise_on_missing:
            raise ConnectionError("Failed to delete some entities! (likely they did not exist prior to this call")
    return int(response.parsed.message)

async def asyncio(
    os_entity_uids: List[str],
    safe: bool = False,
    raise_on_missing: bool = False,
    client: Client = None
):
    """
    Delete asynchronously a list of local entities given their IDs.

    Args:
        os_entity_uids: The list of IDs.
        safe: Whether to raise a ValueError before removal if some entities in the list do not exist.
        raise_on_missing: Whether to raise a ConnectionError if some of the entities could not be deleted.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The number of successfully deleted entities.

    Raises:
        ValueError: If the list of IDs contain invalid entries (and safe is enabled).
        ConnectionError: If some of the entities could not be removed (and raise_on_missing is enabled).
    """
    assert(len(os_entity_uids) > 0)
    if safe:
        uids_text = ", ".join(["'" + os_entity_uid + "'" for os_entity_uid in os_entity_uids])
        uids = await query_ontology.asyncio(
            f"SELECT * FROM `dtimbr`.`os_thing` WHERE CAST(os_entity_uid AS String) IN {uids_text} AND entity_type != 'os_workspace_relationship'")
        if len(uids) < len(os_entity_uids):
            raise ValueError("Attempting to remove an entity which does not exist!")
    response = await delete_entities.sync_detailed(json_body=os_entity_uids,
                                                   client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"delete_entities failed with status code " + str(response.status_code))   
    if int(response.parsed.message) < len(os_entity_uids):
        logger.warning("Deleted only " + response.parsed.message + "/" + str(len(os_entity_uids)) + " entities")
        if raise_on_missing:
            raise ConnectionError("Failed to delete some entities! (likely they did not exist prior to this call")  
    return int(response.parsed.message)