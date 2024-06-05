import logging
import sys
import traceback
from typing import Callable, List
from typing import Optional

from ...api.watchers import get_watcher_intents
from ...client import Client
from ...models.get_watcher_intents_response_200_message_item import GetWatcherIntentsResponse200MessageItem
from ...models.watcher_intent import WatcherIntent

logger = logging.getLogger(__name__)


async def asyncio(
        processor: Callable[[WatcherIntent], Optional[BaseException]],
        client: Client = None
):
    """
    Starts asynchronously a watcher from a user-defined processing function. A watcher will periodically run the
    processing function and may send updates or write to the DB when new data is obtained.

    Args:
        processor: A function that takes a WatcherIntent and returns None if the intent was processed successfully, throws otherwise.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of WatcherIntent objects which failed to execute.

    Raises:
        ConnectionError: If the list of currently running WatcherIntent objects could not be retrieved.
    """
    response = await get_watcher_intents.asyncio_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"get_watcher_intents failed with status code " + str(response.status_code))
    content = response.parsed
    if 'status' in content and content['status'] != 'success':
        raise ConnectionError("Failed to get list of watcher intents with body " + str(content))
    return __do_process(response.parsed.message, processor)


def sync(
        processor: Callable[[WatcherIntent], Optional[BaseException]],
        client: Client = None
):
    """
    Starts a watcher from a user-defined processing function. A watcher will periodically run the
    processing function and may send updates or write to the DB when new data is obtained.

    Args:
        processor: A function that takes a WatcherIntent and returns None if the intent was processed successfully, throws otherwise.
        client: The Client with which to connect to Octostar. If None, the default one is used.
    Returns:
        A list of WatcherIntent objects which failed to execute.

    Raises:
        ConnectionError: If the list of currently running WatcherIntent objects could not be retrieved.
    """
    response = get_watcher_intents.sync_detailed(client=client)
    if response.status_code != 200:
        logger.error(response.content)
        raise ConnectionError(f"get_watcher_intents failed with status code " + str(response.status_code))
    content = response.parsed
    if 'status' in content and content['status'] != 'success':
        raise ConnectionError("Failed to get list of watcher intents with body " + str(content))
    return __do_process(response.parsed.message, processor)


def __do_process(intent_resp: List[GetWatcherIntentsResponse200MessageItem], processor: Callable[[WatcherIntent], Optional[BaseException]]) -> List[BaseException]:
    results = []

    def error_detected(usr: str, i: WatcherIntent, e: BaseException):
        results.append(e)
        print(f'🚨 Exception caught while processing intent: {i.entity_label or i.entity_id} for user {usr}: {str(e)}')

    for entry in intent_resp:
        username = entry.username
        intents = entry.intents

        # #TODO read only the permissions claims to generate a fresh token with the same privileges of the user **at the moment they created the intent**
        # So that when we delete the user, or change permission to the intent creator, the intent will run unaltered.
        jwt = intents[0].jwt
        print(f"🙋‍♂️Working on username: {username}")

        for intent in intents:
            print(f"🏹 Working on intent: {intent.entity_label}")
            if intent.description == 'STOPPED':
                print('🛑 Skipping stopped intent')
                continue

            try:
                processed = processor(intent)
                if isinstance(processed, BaseException):
                    error_detected(username, intent, processed)
                    continue
                else:
                    print(f'👍 Processed successfully: {intent.entity_label or intent.entity_id} for user {username}')
            except BaseException as e:
                print("💣 Unhandled Exception caught while processing intent!" + str(e))
                traceback.print_exc(file=sys.stdout)  # Otherwise k8s logs won't show the traceback
                error_detected(username, intent, e)
                continue
    if not results:
        print("✌️All intents processed successfully")
    else:
        print(f"🚨{len(results)} intents failed to process")
    return results
