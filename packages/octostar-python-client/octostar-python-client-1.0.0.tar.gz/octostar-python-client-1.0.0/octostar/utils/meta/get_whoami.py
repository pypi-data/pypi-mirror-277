import os

from ...api.metadata import get_whoami

def sync():
    """
    Get information about the user.

    Returns:
        A dictionary containing the username, its signed JWT and a few other info.
    """
    return get_whoami.sync_detailed().parsed

async def asyncio():
    """
    Get asynchronously information about the user.

    Returns:
        A dictionary containing the username, its signed JWT and a few other info.
    """
    out = get_whoami.asyncio_detailed()
    return (await out).parsed