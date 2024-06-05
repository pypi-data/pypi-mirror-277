import logging

logger = logging.getLogger(__name__)

from ...api.jobs import list_jobs
from ...client import Client

def sync(
    client: Client = None
):
    """
    List all of the jobs running in Octostar.

    Args:
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of jobs, each containing their full info. Note the full info does not contain the job URL,
        use get_job_url() to retrieve it.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = list_jobs.sync_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to get jobs list with error code {response.status_code} and body {response.content.decode('utf-8')}")
    content = response.parsed
    for elem in content:
        elem.labels = elem.labels.additional_properties
    return content

async def asyncio(
    client: Client = None
):
    """
    List asynchronously all of the jobs running in Octostar.

    Args:
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of jobs, each containing their full info. Note the full info does not contain the job URL,
        use get_job_url() to retrieve it.

    Raises:
        ConnectionError: If the request was unsuccessful on the server.
    """
    response = await list_jobs.asyncio_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to get jobs list with error code {response.status_code} and body {response.content.decode('utf-8')}")
    content = response.parsed
    for elem in content:
        elem.labels = elem.labels.additional_properties
    return content