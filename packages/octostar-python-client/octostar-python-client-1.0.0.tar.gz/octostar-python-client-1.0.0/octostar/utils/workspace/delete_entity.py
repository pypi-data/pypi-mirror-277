import logging

logger = logging.getLogger(__name__)

from ...api.workspace_data import delete_entities
from ..ontology import query_ontology
from ...client import Client


def sync(
    os_entity_uid: str,
    safe: bool = False,
    raise_on_missing: bool = False,
    client: Client = None
):
    """
    Delete a local entity given its IDs.

    Args:
        os_entity_uid: the ID of the entity to delete.
        safe: Whether to raise a ValueError before removal if the entity does not exist.
        raise_on_missing: Whether to raise a ConnectionError if the entity could not be deleted.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The number of successfully deleted entities.

    Raises:
        ValueError: If the ID is not a valid entity ID (and safe is enabled).
        ConnectionError: If the entity could not be removed (and raise_on_missing is enabled).
    """
    if safe:
        uids = query_ontology.sync(
            f"SELECT * FROM `dtimbr`.`os_thing` WHERE CAST(os_entity_uid AS String)='{os_entity_uid}' AND entity_type != 'os_workspace_relationship'")
        if not uids:
            raise ValueError("Attempting to remove an entity which does not exist!")
    response = delete_entities.sync_detailed(json_body=[os_entity_uid],
                                             client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"delete_entity failed with status code " + str(response.status_code))
    if int(response.parsed.message) < 1:
        logger.warning("Deleted only " + response.parsed.message + "/1 entities")
        if raise_on_missing:
            raise ConnectionError("Failed to delete entity with uid " + os_entity_uid + ", (likely it did not exist prior to this call)") 
    return True

async def asyncio(
    os_entity_uid: str,
    safe: bool = False,
    raise_on_missing: bool = False,
    client: Client = None
):
    """
    Delete asynchronously a local entity given its IDs.

    Args:
        os_entity_uid: the ID of the entity to delete.
        safe: Whether to raise a ValueError before removal if the entity does not exist.
        raise_on_missing: Whether to raise a ConnectionError if the entity could not be deleted.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The number of successfully deleted entities.

    Raises:
        ValueError: If the ID is not a valid entity ID (and safe is enabled).
        ConnectionError: If the entity could not be removed (and raise_on_missing is enabled).
    """
    if safe:
        uids = await query_ontology.asyncio(f"SELECT * FROM `dtimbr`.`os_thing` WHERE CAST(os_entity_uid AS String)='{os_entity_uid}' AND entity_type != 'os_workspace_relationship'")
    if not uids:
        raise ValueError("Attempting to remove an entity which does not exist!")
    response = await delete_entities.asyncio_detailed(json_body=[os_entity_uid],
                                                      client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"delete_entity failed with status code " + str(response.status_code))
    if int(response.parsed.message) < 1:
        logger.warning("Deleted only " + response.parsed.message + "/1 entities")
        if raise_on_missing:
            raise ConnectionError("Failed to delete entity with uid " + os_entity_uid + ", (likely it did not exist prior to this call)")  
    return True
