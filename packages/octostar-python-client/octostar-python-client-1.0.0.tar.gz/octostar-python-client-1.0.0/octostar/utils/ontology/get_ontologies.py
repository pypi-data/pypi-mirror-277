import logging

logger = logging.getLogger(__name__)

from ...api.ontology import get_ontologies
from ...client import Client

def sync(
    client: Client = None
):
    """
    Query for the list of ontologies.

    Args:
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of strings, the names of the ontologies.

    Raises:
        ConnectionError: If the query was unsuccessful.
    """
    response = get_ontologies.sync_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"get_ontologies failed with status code " + str(response.status_code))   
    content = response.parsed
    if 'status' in content and content['status'] != 'success':
        raise ConnectionError("Failed to get list of ontologies with body " + str(content))
    return response.parsed['data']

async def asyncio(
    client: Client = None
):
    """
    Query asynchronously for the list of ontologies.

    Args:
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of strings, the names of the ontologies.

    Raises:
        ConnectionError: If the query was unsuccessful.
    """
    response = await get_ontologies.asyncio_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"get_ontologies failed with status code " + str(response.status_code))
    content = response.parsed
    if 'status' in content and content['status'] != 'success':
        raise ConnectionError("Failed to get list of ontologies with body " + str(content))
    return response.parsed['data']