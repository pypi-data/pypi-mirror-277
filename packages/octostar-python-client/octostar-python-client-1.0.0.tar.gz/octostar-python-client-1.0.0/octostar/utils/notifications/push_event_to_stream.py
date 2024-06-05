import os
import logging
from typing import Union

logger = logging.getLogger(__name__)

from ...api.notifications import push_event_to_stream
from ...models.octostar_event import OctostarEvent
from ...models.octostar_event_octostar_payload import OctostarEventOctostarPayload
from ...models.octostar_event_octostar_payload_level import OctostarEventOctostarPayloadLevel
from ...client import Client
from ...types import UNSET

import octostar

def sync(
    message: str,
    description: Union[str, None] = None,
    level: Union[str, None] = None,
    channel: str = 'octostar:desktop:builtins:showToast',
    stream_id: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    Add a new event to an event stream.

    Args:
        message: The main content to write to the event.
        description: The secondary content to write to the event.
        level: A string detailing the event level. Can be "debug", "error", "info" or "warning".
        channel: The event channel. See OsMessageType for its possible values.
        stream_id: The unique ID for the event stream.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if the event was added successfully to the stream.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = push_event_to_stream.sync_detailed(stream_id=stream_id, client=client, json_body=OctostarEvent(
        octostar_stream=channel,
        octostar_payload=OctostarEventOctostarPayload(
            message=message,
            description=description if description else UNSET,
            level=OctostarEventOctostarPayloadLevel(level) if level else UNSET
        )
    ))
    if response.status_code != 200 or ('status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'success'):
        logger.error(response.content)
        raise ConnectionError("push_event_to_stream failed with status code " + str(response.status_code))       
    return True

async def asyncio(
    message: str,
    description: Union[str, None] = None,
    level: Union[str, None] = None,
    channel: str = 'octostar:desktop:builtins:showToast',
    stream_id: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    Add asynchronously a new event to an event stream.

    Args:
        message: The main content to write to the event.
        description: The secondary content to write to the event.
        level: A string detailing the event level. Can be "debug", "error", "info" or "warning".
        channel: The event channel. See OsMessageType for its possible values.
        stream_id: The unique ID for the event stream.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if the event was added successfully to the stream.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await push_event_to_stream.asyncio_detailed(stream_id=stream_id, client=client, json_body=OctostarEvent(
        octostar_stream=channel,
        octostar_payload=OctostarEventOctostarPayload(
            message=message,
            description=description if description else UNSET,
            level=OctostarEventOctostarPayloadLevel(level) if level else UNSET
        )
    ))
    if response.status_code != 200 or ('status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'success'):
        logger.error(response.content)
        raise ConnectionError("push_event_to_stream failed with status code " + str(response.status_code))       
    return True