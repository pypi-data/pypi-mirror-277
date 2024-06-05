from typing import Dict, TypedDict, Union, List, Any, Optional
import os
import uuid

from ....api.workspace_tags import delete_tag_from_entities
from ....models.entity import Entity as TagEntity
from ....client import Client
from ....types import UNSET

class Entity(TypedDict):
    os_entity_uid: str
    entity_type: str

def sync(os_workspace: str,
         entities: List[Entity],
         tag_uid: str,
         ontology_name: str = os.getenv("OS_ONTOLOGY"),
         client: Client = None):
    """
    Remove a tag from a list of entities.

    Args:
        os_workspace: The workspace ID of the tag.
        entities: The entities to tag, as a list of dictionaries.
            Each dictionary must contain:
                os_entity_uid: The unique ID for the entity.
                entity_type: The concept name for the entity.
        tag_uid: The unique ID of the tag.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology.
        ConnectionError: If the operation was unsuccessful on the server.
    """
    assert(len(entities) > 0)
    if ontology_name != os.getenv("OS_ONTOLOGY"):
        raise NotImplementedError(
            "This operation is currently only supported on the current ontology!")
    entities_to_untag = [TagEntity(entity['os_entity_uid'], entity['entity_type']) for entity in entities]
    response = delete_tag_from_entities.sync_detailed(os_workspace, tag_uid, json_body=entities_to_untag, client=client)
    if response.status_code != 200:
        raise ConnectionError(
            f"tag_entities failed, status code: {response.status_code} {response.content}")

def asyncio(os_workspace: str,
         entities: List[Entity],
         existing_tag_uid: Optional[str] = None,
         new_tag_name: Optional[str] = None,
         new_tag_color: Optional[str] = None,
         new_tag_group: Optional[str] = None,
         new_tag_order: Optional[int] = -1,
         ontology_name: str = os.getenv("OS_ONTOLOGY"),
         client: Client = None):
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()