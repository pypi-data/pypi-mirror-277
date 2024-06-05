import os
import logging
import re

logger = logging.getLogger(__name__)

from ...api.jobs import get_job_logs
from ...client import Client

def sync(
    job_name: str = os.environ['OS_JOB_NAME'],
    since_seconds: int = None,
    tail_lines: int = None,
    tail_bytes: int = None,
    client: Client = None
):
    """
    Get the logs of a running app/job given its ID.

    Args:
        job_name: The running app/job ID.
        since_seconds: The maximum amount of seconds prior to now to get logs for.
        tail_lines: The maximum amount of log lines to retrieve.
        tail_bytes: The maximum amount of bytes to retrieve. Applies after tail_lines.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An UTF-8 string with the app logs.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = get_job_logs.sync_detailed(job_name=job_name,
                                          since_seconds=since_seconds,
                                          tail_lines=tail_lines,
                                          tail_bytes=tail_bytes,
                                          client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("get_job_logs failed with status code " + str(response.status_code))
    logs = response.content
    try:
        escaped_logs = logs.decode("utf-8", "replace")
        escaped_logs = re.sub(r'\\.',lambda x:{'\\n':'\n',
                                               '\\t':'\t',
                                               '\\r':'\r',
                                               '\\"':'\"',
                                               "\\'":"\'"}.get(x[0],x[0]), escaped_logs)
        return escaped_logs
    except Exception:
        logger.warning("Could not decode logs! Returning raw bytes")
        return logs
        
async def asyncio(
    job_name: str = os.environ['OS_JOB_NAME'],
    since_seconds: int = None,
    tail_lines: int = None,
    tail_bytes: int = None,
    client: Client = None
):
    """
    Get asynchronously the logs of a running app/job given its ID.

    Args:
        job_name: The running app/job ID.
        since_seconds: The maximum amount of seconds prior to now to get logs for.
        tail_lines: The maximum amount of log lines to retrieve.
        tail_bytes: The maximum amount of bytes to retrieve. Applies after tail_lines.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An UTF-8 string with the app logs.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await get_job_logs.sync_detailed(job_name=job_name,
                                          since_seconds=since_seconds,
                                          tail_lines=tail_lines,
                                          tail_bytes=tail_bytes,
                                          client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("get_job_logs failed with status code " + str(response.status_code))
    logs = response.content
    try:
        escaped_logs = logs.decode("utf-8", "replace")
        escaped_logs = re.sub(r'\\.',lambda x:{'\\n':'\n',
                                               '\\t':'\t',
                                               '\\r':'\r',
                                               '\\"':'\"',
                                               "\\'":"\'"}.get(x[0],x[0]), escaped_logs)
        return escaped_logs
    except Exception:
        logger.warning("Could not decode logs! Returning raw bytes")
        return logs