import logging

logger = logging.getLogger(__name__)

from ...api.notifications import pull_events_from_stream
from ...client import Client

import octostar


def sync(
    stream_id: str,
    client: Client = None
):
    """
    Get the latest event in a stream.

    Args:
        stream_id: The unique ID for the event stream.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An Octostar event instance (containing the event info and contents).

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = pull_events_from_stream.sync_detailed(stream_id=stream_id,
                                                     count=1,
                                                     client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("pull_event_from_stream failed with status code " + str(response.status_code))
    events = response.parsed
    if events:
        return events[0]
    else:
        return events

async def asyncio(
    stream_id: str,
    client: Client = None
):
    """
    Get asynchronously the latest event in a stream.

    Args:
        stream_id: The unique ID for the event stream.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An Octostar event instance (containing the event info and contents).

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await pull_events_from_stream.asyncio_detailed(stream_id=stream_id,
                                                              count=1,
                                                              client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("pull_event_from_stream failed with status code " + str(response.status_code))
    events = response.parsed
    if events:
        return events[0]
    else:
        return events