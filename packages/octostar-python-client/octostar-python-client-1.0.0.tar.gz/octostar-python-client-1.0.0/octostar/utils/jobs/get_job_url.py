import logging

logger = logging.getLogger(__name__)

from ...api.jobs import get_jobs_url
from octostar.models.get_jobs_url_json_body import GetJobsUrlJsonBody
from ...client import Client

def sync(
    job_id: str,
    client: Client = None
):
    """
    Get the job URL for a job ID.

    Args:
        job_id: The ID of the job.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of jobs, each containing their full info. Note the full info does not contain the job URL,
        use get_job_url() to retrieve it.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = get_jobs_url.sync_detailed(json_body=GetJobsUrlJsonBody(job_ids=[job_id]), client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to get jobs list with error code {response.status_code} and body {response.content.decode('utf-8')}")
    content = response.parsed
    return content

async def asyncio(
    job_id: str,
    client: Client = None
):
    """
    Get asynchronously the job URL for a job ID.

    Args:
        job_id: The ID of the job.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of jobs, each containing their full info. Note the full info does not contain the job URL,
        use get_job_url() to retrieve it.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await get_jobs_url.asyncio_detailed(json_body=GetJobsUrlJsonBody(job_ids=[job_id]), client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to get jobs list with error code {response.status_code} and body {response.content.decode('utf-8')}")
    content = response.parsed
    return content