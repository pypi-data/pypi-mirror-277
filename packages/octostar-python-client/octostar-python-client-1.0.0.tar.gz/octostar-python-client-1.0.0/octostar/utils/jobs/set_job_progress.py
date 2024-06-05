import os
import logging

logger = logging.getLogger(__name__)

from ...api.jobs import set_job_progress
from ...client import Client
from ...models.progress_request import ProgressRequest

def sync(
    progress_string: str,
    job_name: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    Set or update the progress status of a job.

    Args:
        progress_string: A string indicative of the progress status.
        job_name: The running app/job ID.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if progress update was successful.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = set_job_progress.sync_detailed(job_name=job_name,
                                              json_body=ProgressRequest(progress=progress_string),
                                              client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to set job progress with error code {response.status_code} and body {response.content.decode('utf-8')}")
    return True

async def asyncio(
    progress_string: str,
    job_name: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    Set or update asynchronously the progress status of a job.

    Args:
        progress_string: A string indicative of the progress status.
        job_name: The running app/job ID.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        True if progress update was successful.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await set_job_progress.sync_detailed(job_name=job_name,
                                                    json_body=ProgressRequest(progress=progress_string),
                                                    client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to set job progress with error code {response.status_code} and body {response.content.decode('utf-8')}")
    if 'status' in response.parsed.additional_properties and response.parsed.additional_properties['status'] != 'ok':
        raise Exception("Failed to set job progress: " + str(response.parsed))
    return True