import os
import logging

logger = logging.getLogger(__name__)

from ...api.jobs import execute_new_job
from ...models.execute_new_job_json_body import ExecuteNewJobJsonBody
from ...client import Client

def sync(
    commands: str,
    ontology_name: str = os.getenv("OS_ONTOLOGY"),
    s3_archive_link: str = os.getenv("OS_SELF_ARCHIVE"),
    client: Client = None
):
    """
    Start a new job.

    Args:
        commands: The job ID to cancel.
        ontology_name: The name of the ontology.
        s3_archive_link: A URL to an S3 zip archive containing a valid app. The app will not execute
        through main.sh but via the provided commands.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An acknowledgment.

    Raises:
        ConnectionError: If the operation was unsuccessful on the server.
    """
    response = execute_new_job.sync_detailed(
        json_body=ExecuteNewJobJsonBody(
            ontology=ontology_name,
            archive=s3_archive_link,
            commands=commands,
            ancestor=os.getenv('OS_ANCESTOR') or os.getenv('OS_JOB_NAME')
        ),
        client=client
    )
    if response.status_code.value != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to execute job with error code {response.status_code} and body {response.content.decode('utf-8')}")
    return response.parsed


async def asyncio(
    commands: str,
    ontology_name: str = os.getenv("OS_ONTOLOGY"),
    s3_archive_link: str = os.getenv("OS_SELF_ARCHIVE"),
    client: Client = None
):
    """
    Start asynchronously a new job.

    Args:
        commands: A list of bash commands, to be executed in order.
        ontology_name: The name of the ontology.
        s3_archive_link: A URL to an S3 zip archive containing a valid app. The app will not execute
        through main.sh but via the provided commands.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        An acknowledgment.

    Raises:
        ConnectionError: If the operation was unsuccessful on the server.
    """
    response = await execute_new_job.asyncio_detailed(
                json_body=ExecuteNewJobJsonBody(
                    ontology=ontology_name,
                    archive=s3_archive_link,
                    commands=commands,
                    ancestor=os.getenv('OS_ANCESTOR') or os.getenv('OS_JOB_NAME')
                ),
                client=client
            )
    if response.status_code.value != 200:
        logger.error(response.content)
        raise ConnectionError(f"Failed to execute job with error code {response.status_code} and body {response.content.decode('utf-8')}")
    return response.parsed
