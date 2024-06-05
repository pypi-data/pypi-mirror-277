from typing import Dict, Union, List, Any, TypedDict, Optional
import uuid
import os
import itertools

from ...api.workspace_data import upsert_entities
from ..ontology import query_ontology
from ...models.upsert_entity import UpsertEntity
from ...models.upsert_entity_base import UpsertEntityBase
from ...models.upsert_entity_relationships_item import UpsertEntityRelationshipsItem
from ...client import Client


class EntityBase(TypedDict):
    entity_type: str
    os_entity_uid: str

def sync(entities_from: List[EntityBase],
         entities_to: List[EntityBase],
         os_relationship_names: Union[str, List[str]],
         os_relationship_workspaces: Union[str, List[str]],
         relationship_fields: Optional[List[Dict[str, Any]]] = None,
         os_relationship_uids: Optional[List[Optional[str]]] = None,
         allow_multi_cardinality: bool = True,
         ontology_name: str = os.getenv("OS_ONTOLOGY"),
         client: Client = None):
    """
    Create or update a set of local relationships between pairs of entities (sources and targets).

    Args:
        entities_from: The source entities, as a list of dictionaries.
            Each dictionary must contain:
                os_workspace: The workspace ID belonging to the entity. This will also be the workspace ID of
                    the corresponding relationship.
                entity_type: The concept name for the entity.
                os_entity_uid: The ID for the entity. Only necessary in case of an update.         
        entities_to: The target entities, as a list of dictionaries. These entities are aligned with the
            source entities to create relationships between them. For these entities, os_workspace can be None
            if the target is a global entity.
        os_relationship_name: A single string used as the name of all relationships, or a list of relationship names.
        os_relationship_workspaces: A single string used as the workspace ID of all relationships, or a list of workspace IDs (one per relationship).
        relationship_fields: A list of dictionaries, each with the additional properties for a relationship.
        os_relationship_uids: The list of IDs for the relationships. Only necessary in case of an update.
        allow_multi_cardinality: If True, allows multiple relationships from the same source, target, and relationship name. Otherwise, it updates them.
            Note this uniqueness is only applied per-workspace.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The list of created/updated relationship records.

    Raises:
        AssertionError: If the length of the input lists do not match or if some source entities
            do not have a workspace ID.
        NotImplementedError: If the operation is not supported for the ontology or for the given data.
        ConnectionError: If the operation was unsuccessful on the server.
        ValueError: If relationship uniqueness is enforced when the relationship is already not unique.
    """
    if ontology_name != os.getenv("OS_ONTOLOGY"):
        raise NotImplementedError(
            "This operation is currently only supported on the current ontology!")
    assert(len(entities_from) > 0)
    assert(len(entities_from) == len(entities_to))
    if isinstance(os_relationship_workspaces, str):
        os_relationship_workspaces = [os_relationship_workspaces for _ in range(len(entities_from))]
    assert(len(os_relationship_workspaces) == len(entities_from))
    if not os_relationship_uids:
        os_relationship_uids = [str(uuid.uuid4()) for _ in range(len(entities_from))]
    for i in range(len(os_relationship_uids)):
        if not os_relationship_uids[i]:
            os_relationship_uids[i] = str(uuid.uuid4())
    assert(len(os_relationship_uids) == len(entities_from))
    if isinstance(os_relationship_names, str):
        os_relationship_names = [os_relationship_names for _ in range(len(entities_from))]
    assert(len(entities_from) == len(os_relationship_names))
    if not relationship_fields:
        relationship_fields = [dict() for _ in range(len(entities_from))]
    for i in range(len(relationship_fields)):
        if not relationship_fields[i]:
            relationship_fields[i] = dict()
    assert(len(relationship_fields) == len(entities_from))
    # ensure each relationship exists uniquely, fetch the IDs in that case
    if not allow_multi_cardinality:
        check_existence_table = [(
            os_relationship_workspaces[i],
            os_relationship_names[i],
            entities_from[i]["os_entity_uid"],
            entities_from[i]["entity_type"],
            entities_to[i]["os_entity_uid"],
            entities_to[i]["entity_type"]
            ) for i in range(len(entities_from))]
        check_existence_subquery = ''
        for i in range(len(check_existence_table)):
            elem = check_existence_table[i]
            if i == 0:
                check_existence_subquery = f'''SELECT '{i}' AS n,
'{elem[0]}' AS os_workspace,
'{elem[1]}' AS os_relationship_name,
'{elem[2]}' AS os_entity_uid_from,
'{elem[3]}' AS os_entity_type_from,
'{elem[4]}' AS os_entity_uid_to,
'{elem[5]}' AS os_entity_type_to '''
            else:
                check_existence_subquery += f'''SELECT '{i}', '{elem[0]}', '{elem[1]}', '{elem[2]}', '{elem[3]}', '{elem[4]}', '{elem[5]}' '''
            if i < len(check_existence_table)-1:
                check_existence_subquery += " UNION ALL "
        check_existence_query = '''SELECT
os_entity_uid,
v.n AS n,
v.os_relationship_name AS os_relationship_name,
v.os_workspace AS os_workspace,
v.os_entity_uid_from AS os_entity_uid_from,
v.os_entity_type_from AS os_entity_type_from,
v.os_entity_uid_to AS os_entity_uid_to,
v.os_entity_type_to AS os_entity_type_to
FROM dtimbr.os_workspace_relationship AS o RIGHT JOIN (''' + check_existence_subquery + '''
) AS v ON
v.os_workspace = o.os_workspace AND v.os_relationship_name = o.os_relationship_name
AND v.os_entity_uid_from = o.os_entity_uid_from AND
v.os_entity_type_from = o.os_entity_type_from AND v.os_entity_uid_to = o.os_entity_uid_to
AND v.os_entity_type_to = o.os_entity_type_to'''
        result = query_ontology.sync(check_existence_query)
        result = list(sorted(result, key=lambda x: x['n']))
        for i, result_i in itertools.groupby(result, key=lambda x: x['n']):
            result_i = list(result_i)
            if result_i:
                if len(result_i) > 1:
                    raise ValueError("Cannot enforce cardinality = 1 when cardinality is already greater than 1!")
                os_relationship_uids[int(i)] = result_i[0]['os_entity_uid']
    relationship_entities = [UpsertEntityBase(**{
        'entity_id': os_relationship_uids[i],
        'entity_type': 'os_workspace_relationship',
        'os_workspace': os_relationship_workspaces[i],
        'os_entity_uid': os_relationship_uids[i],
        'os_concept': 'os_workspace_relationship',
        'concept_name': 'os_workspace_relationship',
    }) for i in range(len(entities_from))]
    new_relationships = [UpsertEntity(
        entity=relationship_entities[i]) for i in range(len(relationship_entities))]
    for i in range(len(new_relationships)):
        new_relationship = new_relationships[i]
        new_relationship.entity.additional_properties = {
            **relationship_fields[i],
            'os_entity_uid_from': entities_from[i]['os_entity_uid'],
            'os_entity_type_from': entities_from[i]['entity_type'],
            'os_entity_uid_to': entities_to[i]['os_entity_uid'],
            'os_entity_type_to': entities_to[i]['entity_type'],
            'os_relationship_name': os_relationship_names[i],
        }
    response = upsert_entities.sync_detailed(
        client=client, json_body=new_relationships)
    if response.status_code != 200 or response.parsed and response.parsed.status != 'success':
        raise ConnectionError(
            f"upsert_relationships failed, status code: {response.status_code} {response.text}")
    return response.parsed['entities']
    
def asyncio(entities_from: List[EntityBase],
            entities_to: List[EntityBase],
            os_relationship_names: Union[str, List[str]],
            os_relationship_workspaces: Union[str, List[str]],
            relationship_fields: Optional[List[Dict[str, Any]]] = None,
            os_relationship_uids: Optional[List[Optional[str]]] = None,
            allow_multi_cardinality: bool = False,
            ontology_name: str = os.getenv("OS_ONTOLOGY"),
            client: Client = None):
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()