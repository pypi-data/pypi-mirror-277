import os
import logging

logger = logging.getLogger(__name__)

from ...api.jobs import list_jobs_children
from ...client import Client

def sync(
    job_name: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    List the jobs spawned by a job.

    Args:
        job_name: The running app/job ID.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of jobs, each containing their full info. Note the full info does not contain the job URL,
        use get_job_url() to retrieve it.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = list_jobs_children.sync_detailed(job_name=job_name, client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to get jobs list with error code {response.status_code} and body {response.content.decode('utf-8')}")
    content = response.parsed
    content = list(filter(lambda x: x.name != job_name, content))
    for elem in content:
        elem.labels = elem.labels.additional_properties
    return content

async def asyncio(
    job_name: str = os.environ['OS_JOB_NAME'],
    client: Client = None
):
    """
    List asynchronously the jobs spawned by a job.

    Args:
        job_name: The running app/job ID.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of jobs, each containing their full info. Note the full info does not contain the job URL,
        use get_job_url() to retrieve it.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await list_jobs_children.asyncio_detailed(job_name=job_name, client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to get jobs list with error code {response.status_code} and body {response.content.decode('utf-8')}")
    content = response.parsed
    content = list(filter(lambda x: x.name != job_name, content))
    for elem in content:
        elem.labels = elem.labels.additional_properties
    return content