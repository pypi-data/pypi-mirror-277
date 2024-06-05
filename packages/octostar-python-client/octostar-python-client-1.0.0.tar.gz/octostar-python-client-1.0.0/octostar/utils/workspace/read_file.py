import requests
import json
import logging

logger = logging.getLogger(__name__)

from ...client import Client
from ...api.workspace_data import get_attachment


def sync(
        os_workspace: str,
        os_entity_uid: str,
        decode: bool = True,
        stream: bool = False,
        stream_lines: bool = False,
        stream_chunk_size: int = 512,
        client: Client = None):
    """
    Read the content of a file from its workspace ID and object ID. Note that querying the ontology
    for the same entry will only provide metadata information about the file, not the file contents
    themselves.

    Args:
        os_workspace: The workspace ID the object belongs to.
        os_entity_uid: The object ID.
        decode: Whether to decode the contents to UTF-8.
        stream: Whether to return the contents in chunks. Overrides stream_lines and stream_chunk_size if False.
        stream_lines: Whether to chunk the contents per line. Overrides stream_chunk_size if set.
        stream_chunk_size: How many bytes each chunk should be.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A string or bytes representation of the object file contents.

    Raises:
        ConnectionError: If the operation was unsuccessful on the server.
        ValueError: If the object has no associated file.
    """
    def _read_file_stream(response, stream_lines, stream_chunk_size):
        if stream_lines:
            attachment = requests.get(response['url'], stream=True).iter_lines(
                chunk_size=stream_chunk_size)
        else:
            attachment = requests.get(response['url'], stream=True).iter_content(
                chunk_size=stream_chunk_size)
        for elem in attachment:
            yield elem
    response = get_attachment.sync_detailed(client=client, no_redirect=False,
                                            workspace=os_workspace,
                                            file_path=os_entity_uid)
    logging.debug(response.content)
    if response.status_code != 200:
        logging.error(response.content)
        raise ConnectionError("read_file failed with status code " +
                              str(response.status_code))
    response = json.loads(response.content)
    if 'url' not in response.keys():
        logging.error(response)
        raise ValueError("read_file failed: no url provided!")
    if not stream:
        attachment = requests.get(response['url']).content
        if decode:
            attachment = attachment.decode()
    else:
        attachment = _read_file_stream(
            response, stream_lines, stream_chunk_size)
        if decode:
            attachment = map(lambda x: x.decode(), attachment)
    return attachment


def asyncio(
        os_workspace: str,
        os_entity_uid: str,
        decode: bool = True,
        stream: bool = False,
        stream_lines: bool = False,
        stream_chunk_size: int = 512,
        client: Client = None):
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()
