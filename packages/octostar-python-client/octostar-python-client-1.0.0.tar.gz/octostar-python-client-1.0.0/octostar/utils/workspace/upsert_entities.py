from typing import Dict, TypedDict, Union, List, Any
import os
import uuid

from ...api.workspace_data import upsert_entities
from ...models.upsert_entity import UpsertEntity
from ...models.upsert_entity_base import UpsertEntityBase
from ...client import Client

class _EntityBaseRequired(TypedDict):
    entity_type: str
    fields: Dict[str, Any]
    
class EntityBase(_EntityBaseRequired, total=False):
    os_entity_uid: str

def sync(os_workspace: Union[str, List[str]],
         entities: List[EntityBase],
         ontology_name: str = os.getenv("OS_ONTOLOGY"),
         client: Client = None):
    """
    Create or update a set of local entities in a workspace.

    Args:
        os_workspace: The workspace ID, or a list of workspace IDs (one per entity).
        entities: The entities to update or create, as a list of dictionaries.
            Each dictionary must contain:
                entity_type: The concept name for the entity.
                fields: A dictionary of fields for the entity, according to the concept definition in the ontology.
            Each dictionary can optionally contain:
                os_entity_uid: The ID for the entity. Only necessary in case of an update.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The list of created/updated entity records.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology.
        ConnectionError: If the operation was unsuccessful on the server.
    """
    assert(len(entities) > 0)
    for entity in entities:
        entity['os_entity_uid'] = entity.get('os_entity_uid', None) or str(uuid.uuid4())
        if 'fields' not in entity:
            entity['fields'] = dict()
    if isinstance(os_workspace, str):
        os_workspace = [os_workspace]*len(entities)
    assert(len(os_workspace) == len(entities))
    if ontology_name != os.getenv("OS_ONTOLOGY"):
        raise NotImplementedError(
            "This operation is currently only supported on the current ontology!")
    new_entities_base = [UpsertEntityBase(**{
        'entity_id': entities[i]['os_entity_uid'],
        'entity_type': entities[i]['entity_type'],
        'os_workspace': os_workspace[i],
        'os_entity_uid': entities[i]['os_entity_uid'],
        'os_concept': entities[i]['entity_type'],
        'concept_name': entities[i]['entity_type']
    }) for i in range(len(entities))]
    new_entities = [UpsertEntity(entity=new_entity_base) for new_entity_base in new_entities_base]
    for i in range(len(new_entities)):
        new_entities[i].entity.additional_properties = entities[i]['fields']
    response = upsert_entities.sync_detailed(
        client=client, json_body=new_entities)
    if response.status_code != 200 or response.parsed and response.parsed.status != 'success':
        raise ConnectionError(
            f"upsert_entities failed, status code: {response.status_code} {response.text}")
    return response.parsed['entities']

def asyncio(
        os_workspace: str,
        os_entity_types: List[str],
        fields: List[Dict[str, Any]],
        os_entity_uids: Union[List[str], None] = None,
        ontology_name: str = os.getenv("OS_ONTOLOGY"),
        client: Client = None
):
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()