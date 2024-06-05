import os
import logging

logger = logging.getLogger(__name__)

from ...api.notifications import delete_stream
from ...client import Client

def sync(
    stream_id: str,
    client: Client = None
):
    """
    Delete an event stream.

    Args:
        stream_id: The unique ID for the event stream.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if the event stream has been deleted successfully.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = delete_stream.sync_detailed(stream_id=stream_id, client=client)
    if response.status_code != 200 or ('status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'success'):
        logger.error(response.content)
        raise ConnectionError("delete_stream failed with status code " + str(response.status_code))
    return True

async def asyncio(
    stream_id: str,
    client: Client = None
):
    """
    Delete asynchronously an event stream.

    Args:
        stream_id: The unique ID for the event stream.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if the event stream has been deleted successfully.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await delete_stream.asyncio_detailed(stream_id=stream_id, client=client)
    if response.status_code != 200 or ('status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'success'):
        logger.error(response.content)
        raise ConnectionError("delete_stream failed with status code " + str(response.status_code))       
    return True