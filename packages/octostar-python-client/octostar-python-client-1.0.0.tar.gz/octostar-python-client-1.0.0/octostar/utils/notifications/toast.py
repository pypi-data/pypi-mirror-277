from typing import Union
import logging

logger = logging.getLogger(__name__)

from ...api.notifications import toast
from ...types import UNSET
from ...client import Client
from ...models.octostar_event_octostar_payload_level import OctostarEventOctostarPayloadLevel

def sync(
    message: str,
    description: Union[str, None] = None,
    level: Union[str, None] = None,
    client: Client = None
):
    """
    Send a simple notification to the user in the browser.

    Args:
        message: The main string in the notification.
        description: The secondary string in the notification.
        level: A string detailing the icon to show in the notification. Can be "debug", "error", "info" or "warning".
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if the operation was successful.

    Raises:
        AttributeError: If the level string is invalid.
        ConnectionError: If the request was unsuccessful on the server.
    """
    if level and level not in ['debug', 'error', 'info', 'warning']:
        raise AttributeError("Invalid level!")
    response = toast.sync_detailed(message=message,
                                   description=UNSET if not description else description,
                                   level=OctostarEventOctostarPayloadLevel(level) if level else UNSET,
                                   client=client)
    if response.status_code != 200 or ('status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'success'):
        logger.error(response.content)
        raise ConnectionError(f"toast failed with status code " + str(response.status_code))
    return True

async def asyncio(
    message: str,
    description: Union[str, None] = None,
    level: Union[str, None] = None,
    client: Client = None
):
    """
    Send asynchronously a simple notification to the user in the browser.

    Args:
        message: The main string in the notification.
        description: The secondary string in the notification.
        level: A string detailing the icon to show in the notification. Can be "debug", "error", "info" or "warning".
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if the operation was successful.

    Raises:
        AttributeError: If the level string is invalid.
        ConnectionError: If the request was unsuccessful on the server.
    """
    if level and level not in ['debug', 'error', 'info', 'warning']:
        raise AttributeError("Invalid level!")
    response = await toast.sync_detailed(message=message,
                                         description=UNSET if not description else description,
                                         level=OctostarEventOctostarPayloadLevel(level) if level else UNSET,
                                         client=client)
    if response.status_code != 200 or ('status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'success'):
        logger.error(response.content)
        raise ConnectionError(f"toast failed with status code " + str(response.status_code))
    return True