import os
import json
from typing import Union
from io import BytesIO
import requests
import uuid
import logging

logger = logging.getLogger(__name__)

from ...client import Client
from ...api.workspace_data import upsert_entities
from ...models.upsert_entity import UpsertEntity
from ...models.upsert_entity_base import UpsertEntityBase
from . import get_item_from_filepath


def sync(
        os_workspace: str,
        full_filename: str,
        filetype: str,
        file: Union[str, bytes, BytesIO],
        os_entity_uid: Union[str, None] = None,
        ontology_name: str = os.getenv("OS_ONTOLOGY"),
        client: Client = None):
    """
    Write a file to a workspace. This includes creating a local entity record representing the file as well as
    writing the file contents to storage so that they can be retrieved with read_file(). Note that using
    upsert_entity() only allows to save a record about a file, not the file content themselves.

    Args:
        os_workspace: The workspace ID in which to save the file.
        full_filename: The full filepath for the file. It should begin with the workspace name, followed
            by any folders and terminating with the filename. Any non-existing folder in the workspace will
            be created.
        filetype: The MIME type for the file.
        file: The file contents, either an UTF-8 string or a bytes-like.
        os_entity_uid: The entity ID for the file. Only necessary in case of an update to the file contents.
        ontology_name: The name of the ontology.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        The record of the written file.

    Raises:
        NotImplementedError: If the operation is not supported for the ontology.
        ConnectionError: If the operation was unsuccessful on the server.
    """
    def _upload_file_for_entity(entity_resp: bytes, os_entity_uid: str, file: str):
        er = json.loads(entity_resp)["s3_urls"][os_entity_uid]
        if isinstance(file, str):
            files = {"file": open(file, "rb")}
        elif isinstance(file, bytes):
            files = {'file': BytesIO(file)}
        else:
            files = {'file': file}
        data = er["fields"]
        url = er["url"]
        r = requests.post(url, data=data, files=files)
        if r.status_code == 204:
            logging.info("File upload successful")
        else:
            logging.info(f"File upload failed with status code {r.status_code} {r.text}")
            raise ConnectionError(
                f"File upload failed, status code: {r.status_code} {r.text}")

    def _write_file_nonrecursive(os_workspace, os_parent_folder, os_entity_uid, filename, entity_type, filetype, file, ontology_name, client):
        new_entity_base = UpsertEntityBase(**{
            'entity_id': os_entity_uid,
            'entity_type': entity_type,
            'entity_label': filename,
            'os_item_content_type': filetype,
            'os_workspace': os_workspace,
            'os_parent_folder': os_parent_folder,
            'os_item_type': entity_type,
            'os_entity_uid': os_entity_uid,
            'os_concept': entity_type,
            'concept_name': entity_type,
            'os_item_name': filename
        })
        if file:
            new_entity_base.additional_properties = {
                'os_has_attachment': True
            }
        new_entity = UpsertEntity(entity=new_entity_base)
        response = upsert_entities.sync_detailed(
            client=client, json_body=[new_entity])
        if response.status_code != 200:
            raise ConnectionError(response.content.decode('utf-8'))
        if file:
            if len(response.parsed.s3_urls.additional_properties.keys()) > 1:
                raise ConnectionError("Multiple S3 urls were returned for a single file!")
            for os_entity_uid in response.parsed.s3_urls.additional_properties.keys():
                _upload_file_for_entity(json.dumps(
                    response.parsed.to_dict()), os_entity_uid, file)
        return response.parsed['entities'][0]
    if ontology_name != os.getenv("OS_ONTOLOGY"):
        raise NotImplementedError(
            "This operation is currently only supported on the current ontology!")
    if not os_entity_uid:
        os_entity_uid = str(uuid.uuid4())
    filepath = full_filename.split("/")[:-1]
    filepath = [elem for elem in filepath if elem] # Ensure no null labels for folders
    folders_to_write = []
    file_folder = os_workspace
    for i in range(len(filepath), 1, -1):
        try:
            file_entity = get_item_from_filepath.sync(
                os_workspace, "/".join(filepath[:i]), False, ontology_name, client)
            if isinstance(file_entity, list):
                file_entity = file_entity[0]
            file_folder = file_entity['os_entity_uid']
            break
        except ValueError:
            folders_to_write.insert(0, filepath[i-1])
    if folders_to_write:
        for folder in folders_to_write:
            file_folder = _write_file_nonrecursive(os_workspace, file_folder, str(
                uuid.uuid4()), folder, 'os_folder', None, None, ontology_name, client)['os_entity_uid']
    return _write_file_nonrecursive(os_workspace, file_folder, os_entity_uid, full_filename.rsplit("/", 1)[-1], 'os_file', filetype, file, ontology_name, client)


def asyncio(
        os_workspace: str,
        full_filename: str,
        filetype: str,
        file: Union[str, BytesIO],
        os_entity_uid: Union[str, None] = None,
        ontology_name: str = os.getenv("OS_ONTOLOGY"),
        client: Client = None):
    """
    NOT IMPLEMENTED
    """
    raise NotImplementedError()
