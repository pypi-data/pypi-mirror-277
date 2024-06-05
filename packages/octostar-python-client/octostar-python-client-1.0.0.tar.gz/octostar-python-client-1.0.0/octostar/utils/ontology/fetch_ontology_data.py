import os
from typing import Union
import logging

logger = logging.getLogger(__name__)

from ...api.ontology import fetch_ontology_data
from ...client import Client

def sync(
    ontology_name: str = os.environ['OS_ONTOLOGY'],
    client: Client = None
):
    """
    Query for the structure of an ontology.

    Args:
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A dictionary containing a list of concepts and a list of relationships.
        Each of these entries is in itself a dictionary.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology.
        ConnectionError: If the query was unsuccessful.
    """
    if ontology_name != os.environ['OS_ONTOLOGY']:
        raise NotImplementedError("Only the active ontology is currently supported for this method!")
    response = fetch_ontology_data.sync_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"fetch_ontology_data failed with status code " + str(response.status_code))   
    return response.parsed.additional_properties

async def asyncio(
    ontology_name: str = os.environ['OS_ONTOLOGY'],
    client: Client = None
):
    """
    Query asynchronously for the structure of an ontology.

    Args:
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A dictionary containing a list of concepts and a list of relationships.
        Each of these entries is in itself a dictionary.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology.
        ConnectionError: If the query was unsuccessful.
    """
    if ontology_name != os.environ['OS_ONTOLOGY']:
        raise NotImplementedError("Only the active ontology is currently supported for this method!")
    response = await fetch_ontology_data.asyncio_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"fetch_ontology_data failed with status code " + str(response.status_code))   
    return response.parsed.additional_properties