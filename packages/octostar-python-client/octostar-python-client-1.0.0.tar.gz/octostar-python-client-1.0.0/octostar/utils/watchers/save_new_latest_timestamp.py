import base64
import json
import sys
import traceback

from ...api.workspace_data import upsert_entities
from ...models.upsert_entity import UpsertEntity
from ...models.watcher_intent import WatcherIntent


def retrieve_latest_timestamp(intent: WatcherIntent) -> int:
    pro = intent.previous_run_output
    if not pro:
        return 0
    pro_decoded = json.loads(base64.b64decode(pro))
    if not pro_decoded:
        return 0
    return int(pro_decoded['last_ts'])


def handleException(e: BaseException):
    print("💣 Unhandled Exception caught while processing intent!" + str(e))
    traceback.print_exc(file=sys.stdout)  # Otherwise k8s logs won't show the traceback
    raise e


def mkUpsertEntity(intent: WatcherIntent, last_ts: int) -> UpsertEntity:
    return UpsertEntity.from_dict({"entity": {
        "entity_id": intent.entity_id,
        "entity_type": intent.entity_type,
        "os_entity_uid": intent.os_entity_uid,
        "os_workspace": intent.os_workspace,
        "previous_run_output": base64.b64encode(json.dumps({"last_ts": last_ts}).encode()).decode('utf-8'),
    }})


async def asyncio(
    intent: WatcherIntent,
    last_ts: int,
    client = None
):
    """
    Updates asynchronously a watcher with a new latest timestamp. This is typically called within the
    process function defined for the watcher whenever the watcher finds new data or is updated in some way.

    Args:
        intent: The WatcherIntent object to update.
        last_ts: The new latest timestamp to apply to the watcher.

    Raises:
        BaseException: Generic exception if the operation fails.
    """
    if last_ts is None:
        last_ts = retrieve_latest_timestamp(intent)
    try:
        await upsert_entities.asyncio(json_body=[mkUpsertEntity(intent, last_ts)], client=client)
        print('💿Async-saved new latest timestamp ' + str(last_ts) + ' for intent ' + str(intent.entity_label))
    except BaseException as e:
        handleException(e)


def sync(
    intent: WatcherIntent,
    last_ts: int,
    client = None
):
    """
    Updates a watcher with a new latest timestamp. This is typically called within the
    process function defined for the watcher whenever the watcher finds new data or is updated in some way.

    Args:
        intent: The WatcherIntent object to update.
        last_ts: The new latest timestamp to apply to the watcher.
        client: The Client with which to connect to Octostar. If None, the default one is used.

    Raises:
        BaseException: Generic exception if the operation fails.
    """
    if last_ts is None:
        last_ts = retrieve_latest_timestamp(intent)
    try:
        upsert_entities.sync(json_body=[mkUpsertEntity(intent, last_ts)], client=client)
        print('💿Sync-saved new latest timestamp ' + str(last_ts) + ' for intent ' + str(intent.entity_label))
    except BaseException as e:
        handleException(e)
