from typing import Dict, Union, Any
import uuid
import os

from ...api.workspace_data import upsert_entities
from ...models.upsert_entity import UpsertEntity
from ...models.upsert_entity_base import UpsertEntityBase
from ...client import Client


def sync(os_workspace: str,
         os_entity_type: str,
         fields: Dict[str, Any],
         os_entity_uid: Union[str, None] = None,
         ontology_name: str = os.getenv("OS_ONTOLOGY"),
         client: Client = None):
    """
    Create or update a local entity in a workspace.

    Args:
        os_workspace: The workspace ID.
        os_entity_type: The concept name for the entity.
        fields: A dictionary of fields for the entity, according to the concept definition in the ontology.
        os_entity_uid: The ID for the entity. Only necessary in case of an update.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The created/updated entity record.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology.
        ConnectionError: If the operation was unsuccessful on the server.
    """
    if not os_entity_uid:
        os_entity_uid = str(uuid.uuid4())
    if ontology_name != os.getenv("OS_ONTOLOGY"):
        raise NotImplementedError(
            "This operation is currently only supported on the current ontology!")
    new_entity_base = UpsertEntityBase(**{
        'entity_id': os_entity_uid,
        'entity_type': os_entity_type,
        'os_workspace': os_workspace,
        'os_entity_uid': os_entity_uid,
        'os_concept': os_entity_type,
        'concept_name': os_entity_type
    })
    new_entity = UpsertEntity(entity=new_entity_base)
    new_entity.entity.additional_properties = fields
    response = upsert_entities.sync_detailed(
        client=client, json_body=[new_entity])
    if response.status_code != 200 or response.parsed and response.parsed.status != 'success':
        raise ConnectionError(
            f"upsert_entity failed, status code: {response.status_code} {response.text}")
    return response.parsed['entities'][0]


async def asyncio(os_workspace: str,
                  os_entity_type: str,
                  fields: Dict[str, Any],
                  os_entity_uid: Union[str, None] = None,
                  ontology_name: str = os.getenv("OS_ONTOLOGY"),
                  client: Client = None):
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()
