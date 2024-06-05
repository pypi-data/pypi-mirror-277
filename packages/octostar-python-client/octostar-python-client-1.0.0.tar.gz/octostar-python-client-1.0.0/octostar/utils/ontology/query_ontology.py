import os
import json
import logging

from ...api.ontology import query
from ...models.query_json_body import QueryJsonBody
from ...client import Client

logger = logging.getLogger(__name__)

def sync(
	sql_query: str,
	ontology_name: str=os.getenv('OS_ONTOLOGY'),
	client: Client = None
	):
    """
    Query an ontology for entities or data.

    Args:
        sql_query: A string which is a valid timbr/SQL query.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of dictionaries, each containing a result row with named columns.
        The result can be passed e.g. to pd.DataFrame().

    Raises:
        ConnectionError: If the query was unsuccessful.
    """
    response = query.sync_detailed(client=client, json_body=QueryJsonBody(query=sql_query), ontology=ontology_name)
    logger.debug(response.content.decode("utf-8"))
    if response.status_code != 200:
        logger.error(response.content.decode("utf-8"))
        raise ConnectionError("query_ontology failed! " + str(response.content.decode("utf-8")))
    response = json.loads(response.content)
    if 'status' not in response.keys() or response['status'] != 'success' or 'data' not in response or not isinstance(response['data'], list):
        logger.error(response)
        raise ConnectionError("query_ontology failed! " + str(response))
    return response['data']
    
async def asyncio(
	sql_query: str,
	ontology_name: str = os.getenv('OS_ONTOLOGY'),
	client: Client = None
	):
    """
    Query asynchronously an ontology for entities or data.

    Args:
        sql_query: A string which is a valid timbr/SQL query.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of dictionaries, each containing a result row with named columns.
        The result can be passed e.g. to pd.DataFrame().

    Raises:
        ConnectionError: If the query was unsuccessful.
    """
    response = await query.asyncio_detailed(client=client, json_body=QueryJsonBody(query=sql_query), ontology=ontology_name)
    logger.debug(response.content.decode("utf-8"))
    if response.status_code != 200:
        logger.error(response.content.decode("utf-8"))
        raise Exception("query_ontology failed! " + str(response.content.decode("utf-8")))
    response = json.loads(response.content)
    if 'status' not in response.keys() or response['status'] != 'success' or 'data' not in response or not isinstance(response['data'], list):
        logger.error(response)
        raise Exception("query_ontology failed! " + str(response))
    return response['data']