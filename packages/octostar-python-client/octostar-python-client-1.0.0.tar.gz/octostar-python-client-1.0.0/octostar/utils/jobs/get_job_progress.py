import os
import logging

logger = logging.getLogger(__name__)

from ...api.jobs import get_job_progress
from ...client import Client

def sync(
    job_name: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    Get the progress status of a job. Note the progress status is determined by the job
    and its behavior is dependant on the implementation of the job itself.

    Args:
        job_name: The running app/job ID.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A string containing the progress status (usually containing some percentage value).

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = get_job_progress.sync_detailed(job_name=job_name, client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("get_job_progress failed with status code " + str(response.status_code))
    content = response.parsed
    if 'status' in content.additional_properties and content.additional_properties['status'] != 'ok':
        raise ConnectionError("get_job_progress failed: " + str(content))
    return content.message

async def asyncio(
    job_name: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    Get asynchronously the progress status of a job. Note the progress status is determined by the job
    and its behavior is dependant on the implementation of the job itself.

    Args:
        job_name: The running app/job ID.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A string containing the progress status (usually containing some percentage value).

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await get_job_progress.asyncio_detailed(job_name=job_name, client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("get_job_progress failed with status code " + str(response.status_code))
    content = response.parsed
    if 'status' in content.additional_properties and content.additional_properties['status'] != 'ok':
        raise ConnectionError("get_job_progress failed: " + str(content))
    return content.message