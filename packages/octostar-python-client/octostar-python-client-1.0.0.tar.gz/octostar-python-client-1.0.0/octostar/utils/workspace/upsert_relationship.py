from typing import Dict, Union, Any, Optional
import uuid
import os

from ...api.workspace_data import upsert_entities
from ..ontology import query_ontology
from ...models.upsert_entity import UpsertEntity
from ...models.upsert_entity_base import UpsertEntityBase
from ...types import Unset, UNSET
from ...client import Client


def sync(os_entity_uid_from: str,
        entity_type_from: str,
        os_entity_uid_to: str,
        entity_type_to: str,
        os_relationship_name: str,
        os_relationship_workspace: str,
        relationship_fields: Dict[str, Any] = dict(),
        os_relationship_uid: Optional[str] = None,
        allow_multi_cardinality: bool = True,
        ontology_name: str = os.getenv("OS_ONTOLOGY"),
        client: Client = None):
    """
    Create or update a local relationship between two entities, a source and a target.

    Args:
        os_entity_uid_from: The source entity ID.
        entity_type_from: The source entity concept name.
        os_entity_uid_to: The target entity ID.
        entity_type_to: The target entity concept name.
        os_relationship_name: The name of the relationship, from source to target.
        os_relationship_workspace: The workspace for the relationship.
        relationship_fields: A dictionary of additional properties for the relationship.
        os_relationship_uid: The ID for the relationship. Only necessary in case of an update.
        allow_multi_cardinality: If True, allows multiple relationships from the same source, target, and relationship name. Otherwise, it updates them.
            Note this uniqueness is only applied per-workspace.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar.
    Returns:
        The created/updated relationship record.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology or for the given data.
        ConnectionError: If the operation was unsuccessful on the server.
        ValueError: If relationship uniqueness is enforced when the relationship is already not unique.
    """
    if not os_relationship_uid:
        os_relationship_uid = str(uuid.uuid4())
    if ontology_name != os.getenv("OS_ONTOLOGY"):
        raise NotImplementedError(
            "This operation is currently only supported on the current ontology!")
    if not allow_multi_cardinality:
        check_existence_query = f'''SELECT os_entity_uid FROM dtimbr.os_workspace_relationship
            WHERE os_workspace='{os_relationship_workspace}' AND
                  os_relationship_name='{os_relationship_name}' AND 
                  os_entity_uid_from='{os_entity_uid_from}' AND 
                  os_entity_type_from='{entity_type_from}' AND 
                  os_entity_uid_to='{os_entity_uid_to}' AND
                  os_entity_type_to='{entity_type_to}' '''
        result = query_ontology.sync(check_existence_query)
        if result:
            if len(result) > 1:
                raise ValueError("Cannot enforce cardinality = 1 when cardinality is already greater than 1!")
            os_relationship_uid = result[0]['os_entity_uid']
    relationship_entity = UpsertEntityBase(**{
        'entity_id': os_relationship_uid,
        'entity_type': 'os_workspace_relationship',
        'os_workspace': os_relationship_workspace,
        'os_entity_uid': os_relationship_uid,
        'os_concept': 'os_workspace_relationship',
        'concept_name': 'os_workspace_relationship',
    })
    new_relationship = UpsertEntity(
        entity=relationship_entity)
    new_relationship.entity.additional_properties = {
        **relationship_fields,
        'os_entity_uid_from': os_entity_uid_from,
        'os_entity_type_from': entity_type_from,
        'os_entity_uid_to': os_entity_uid_to,
        'os_entity_type_to': entity_type_to,
        'os_relationship_name': os_relationship_name,
    }
    response = upsert_entities.sync_detailed(
        client=client, json_body=[new_relationship])
    if response.status_code != 200 or response.parsed and response.parsed.status != 'success':
        raise ConnectionError(
            f"upsert_relationship failed, status code: {response.status_code} {response.text}")
    return response.parsed['entities'][0]


async def asyncio(os_workspace_from: str,
        os_entity_uid_from: str,
        entity_type_from: str,
        os_workspace_to: Union[None, str],
        os_entity_uid_to: str,
        entity_type_to: str,
        os_relationship_name: str,
        relationship_fields: Dict[str, Any] = dict(),
        os_relationship_uid: Union[str, Unset] = UNSET,
        ontology_name: str = os.getenv("OS_ONTOLOGY"),
        client: Client = None):
    """
    NOT IMPLEMENTED
    """    
    raise NotImplementedError()
