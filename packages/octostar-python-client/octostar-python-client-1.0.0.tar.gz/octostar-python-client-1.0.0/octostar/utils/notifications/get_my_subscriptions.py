import logging

logger = logging.getLogger(__name__)

from ...api.notifications import get_subscriptions
from ...client import Client

def sync(
    client: Client = None
):
    """
    Get the subscriptions the user is listening to.

    Args:
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of subscription IDs.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = get_subscriptions.sync_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("get_subscriptions failed with status code " + str(response.status_code))
    return response.parsed

async def asyncio(
    client: Client = None
):
    """
    Get asynchronously the subscriptions the user is listening to.

    Args:
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of subscription IDs.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await get_subscriptions.asyncio_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("get_subscriptions failed with status code " + str(response.status_code))       
    return response.parsed