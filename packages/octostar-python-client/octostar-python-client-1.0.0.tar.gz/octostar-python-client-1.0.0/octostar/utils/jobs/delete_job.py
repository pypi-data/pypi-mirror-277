import logging

logger = logging.getLogger(__name__)

from ...api.jobs import delete_job
from ...client import Client

def sync(
    job_name: str,
    client: Client = None
):
    """
    Cancel a currently running job.

    Args:
        job_name: The unique job name to cancel.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An acknowledgment.

    Raises:
        ConnectionError: If the operation was unsuccessful on the server.
    """
    response = delete_job.sync_detailed(job_name=job_name, client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("delete_job failed with status code " + str(response.status_code))
    return response.parsed

async def asyncio(
    job_name: str,
    client: Client = None
):
    """
    Cancel asynchronously a currently running job.

    Args:
        job_name: The job ID to cancel.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An acknowledgment.

    Raises:
        ConnectionError: If the operation was unsuccessful on the server.
    """
    response = await delete_job.asyncio_detailed(job_name=job_name, client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError("delete_job failed with status code " + str(response.status_code))       
    return response.parsed