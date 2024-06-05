import logging
from contextlib import contextmanager
import os
import sys
import json
from typing import List, Literal, Union, TypedDict, Dict, Any
import traceback
from flask import jsonify
import flask

from .ontology import query_ontology
from .workspace import read_file, write_file, upsert_entity, upsert_relationship

class NifiFileMetadataBase(TypedDict):
    'item_content_type': str
    'pipeline_code': str

class NifiFileMetadata(NifiFileMetadataBase, total=False):
    'filepath': str
    'filename': str
    'filesize': int

class NifiFileEntityBase(TypedDict):
    'os_workspace': str
    'os_entity_uid': str
    'entity_type': str

class NifiFileEntity(NifiFileEntityBase, total=False):
    'fields': Dict[str, Any]

class NifiAnnotationBase(TypedDict):
    'os_entity_uid': str
    'entity_type': str

class NifiAnnotation(NifiAnnotationBase, total=False):
    'fields': Dict[str, Any]

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class NifiFile(object):
    def __init__(self, entity, metadata, linked_files=list(), contents=None, do_replace_on_s3=False, annotations=list()):
        self.entity = NifiFileEntity(entity)
        self.metadata = NifiFileMetadata(metadata)
        self.annotations = [NifiAnnotation(annotation) for annotation in annotations]
        self._contents = contents
        self.linked_files = linked_files
        self.do_replace_on_s3 = do_replace_on_s3
    def get_contents(self):
        if not self._contents:
            self._contents = read_file.sync(self.entity['os_workspace'], self.entity['os_entity_uid'], decode=False)
        return self._contents
    def set_contents(self, contents):
        self._contents = contents
    def upsert_files(nifi_files, metadata=None):
        for file in nifi_files:
            if not file.do_replace_on_s3:
                file_reference = query_ontology.sync(f"SELECT count() AS count FROM dtimbr.os_file WHERE os_entity_uid='{file.entity['os_entity_uid']}'")
                if not file_reference or file_reference[0]['count'] == 0:
                    logger.info("Will attempt to upload file even if 'do_replace_on_s3' is False because the file does not exist")
            if file.do_replace_on_s3 or not file_reference or file_reference[0]['count'] == 0:
                try:
                    write_file.sync(file.entity['os_workspace'], file.metadata['filepath'] + "/" + file.metadata['filename'],
                                    file.entity['os_item_content_type'], file.contents,
                                    file.entity['os_entity_uid'])
                    logger.info("Upserted file " + file.entity['os_entity_uid'])
                    if metadata:
                        metadata['uploaded_files'] += 1
                        metadata['uploaded_entities'] += 1
                except:
                    raise ConnectionError("Could not upload file with UUID " + file.entity['os_entity_uid'] + " to s3!")
        return metadata
    def upsert_annotations(nifi_files, metadata=None):
        for file in nifi_files:
            for annotation in file.annotations:
                fields = {k:v for k, v in annotation.items() if not k.startswith('os_') and k not in ['entity_type', 'entity_label', 'entity_id']}
                if 'entity_uid' not in fields:
                    fields['entity_uid'] = file.entity['os_entity_uid']
                if 'pipeline_code' not in fields:
                    fields['pipeline_code'] = file.metadata['pipeline_code']
                try:
                    upsert_entity.sync(file.entity['os_workspace'], annotation['entity_type'], fields, annotation['os_entity_uid'])
                    logger.info("Upserted annotation " + annotation['os_entity_uid'])
                    if metadata:
                        metadata['uploaded_annotations'] += 1
                        metadata['uploaded_entities'] += 1
                except:
                    logger.warning("Could not upload annotation " + str(annotation))
                    logger.warning(traceback.print_exc())
                try:
                    upsert_relationship.sync(file.entity['os_workspace'], file.entity['os_entity_uid'], file.entity['entity_type'],
                                             annotation['os_workspace'], annotation['os_entity_uid'], file.entity['entity_type'],
                                             "annotated_with")
                    logger.info("Upserted relationship between " + file.entity['os_entity_uid'] + " and annotation " + annotation['os_entity_uid'])
                    if metadata:
                        metadata['uploaded_relationships'] += 1
                except Exception as e:
                    logger.warning("Could not create relationship between file with UUID " + file.entity['os_entity_uid'] + " and annotation " + str(annotation))
                    logger.warning(traceback.print_exc())
                    raise e
            file.annotations = list()
        return metadata
    def upsert_file_links(nifi_files, metadata=None):
        for file in nifi_files:
            for linked_file in file.linked_files:
                try:
                    from_entity_type = 'os_file' if 'entity_type' not in file.entity else file.entity['entity_type']
                    to_entity_type = 'os_file' if 'entity_type' not in linked_file.entity else linked_file.entity['entity_type']
                    upsert_relationship.sync(file.entity['os_workspace'], file.entity['os_entity_uid'], from_entity_type,
                                             file.entity['os_workspace'], linked_file.entity['os_entity_uid'], to_entity_type,
                                             "generator_of")
                    logger.info("Upserted relationship between " + file.entity['os_entity_uid'] + " and " + linked_file.entity['os_entity_uid'])
                    if metadata:
                        metadata['uploaded_relationships'] += 1
                except:
                    logger.warning("Could not create relationship between file with UUID " + file.entity['os_entity_uid'] + " and file with UUID " + linked_file.entity['os_entity_uid'])
                    logger.warning(traceback.print_exc())
            return metadata

@contextmanager
def suppress_output():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

def receive_input(
    flask_request: Union[flask.Request, None] = None,
    transmission_means: Literal['local', 'os'] = 'os'
):
    json_data = None
    if transmission_means == 'os':        
        if flask_request:
            json_data = flask_request.json
    elif transmission_means == 'local':
        json_data = json.loads(sys.stdin.read())
    else:
        raise ValueError(f"Invalid transmission_means type {transmission_means}!")
    if not json_data:
        raise AttributeError("No valid input data could be fetched!")
    files = [NifiFile(elem['entity'],
                      elem['metadata']['filepath'],
                      elem['metadata']['filename'],
                      elem['metadata']['filesize'],
                      elem['metadata']['item_content_type'],
                      elem['metadata']['pipeline_code']) for elem in json_data]
    return files

def send_output(
    files: List[NifiFile],
    transmission_means: Literal['local', 'os'] = 'os'
):
    NifiFile.upsert_files(files)
    NifiFile.upsert_annotations(files)
    NifiFile.upsert_file_links(files)
    logger.info("All done transmitting files!")
    json_data = [{
        'entity': file.entity,
        'metadata': file.metadata
    } for file in files]
    if transmission_means == 'local':
        sys.stdout.write(bytes(json.dumps(json_data), 'utf-8'))
    elif transmission_means == 'os':
        return jsonify(json_data)
