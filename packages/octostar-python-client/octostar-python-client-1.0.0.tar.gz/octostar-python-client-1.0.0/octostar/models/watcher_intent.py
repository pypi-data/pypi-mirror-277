import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WatcherIntent")


@attr.s(auto_attribs=True)
class WatcherIntent:
    """
    Attributes:
        app_name (Union[Unset, str]):  Example: TwitterCheck.
        arguments (Union[Unset, str]):  Example: Base64 encoded arguments: e.g. JSON representation of an entity.
        cron_exp (Union[Unset, str]):  Example: */1 * * * *.
        description (Union[Unset, None, str]):  Example: Check for new Twitter posts every minute.
        entity_id (Union[Unset, str]):  Example: b7a2ccae-2964-4fe6-a1eb-cff30238f5b7.
        entity_label (Union[Unset, str]):  Example: TwitterCheck - check_new_posts - john_doe_username.
        entity_type (Union[Unset, str]):  Example: os_watch_intent.
        jwt (Union[Unset, str]):  Example: Unsigned Encoded JWT token (minus the third block).
        last_run (Union[Unset, None, datetime.datetime]):  Example: 2024-01-17T12:00:00Z.
        os_created_at (Union[Unset, datetime.datetime]):  Example: 2023-12-22T08:42:21Z.
        os_entity_uid (Union[Unset, str]):  Example: b7a2ccae-2964-4fe6-a1eb-cff30238f5b7.
        os_icon (Union[Unset, None, str]):  Example: Icon URL or null.
        os_workspace (Union[Unset, str]):  Example: 5757b2af-04d2-4157-bc3a-ac86bc1283f3.
        previous_run_output (Union[Unset, str]):  Example: Base64 encoded output of previous run (varies depending on
            the watcher function).
        username (Union[Unset, str]):  Example: john_doe_username.
        watcher_name (Union[Unset, str]):  Example: check_new_posts.
    """

    app_name: Union[Unset, str] = UNSET
    arguments: Union[Unset, str] = UNSET
    cron_exp: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    entity_label: Union[Unset, str] = UNSET
    entity_type: Union[Unset, str] = UNSET
    jwt: Union[Unset, str] = UNSET
    last_run: Union[Unset, None, datetime.datetime] = UNSET
    os_created_at: Union[Unset, datetime.datetime] = UNSET
    os_entity_uid: Union[Unset, str] = UNSET
    os_icon: Union[Unset, None, str] = UNSET
    os_workspace: Union[Unset, str] = UNSET
    previous_run_output: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    watcher_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_name = self.app_name
        arguments = self.arguments
        cron_exp = self.cron_exp
        description = self.description
        entity_id = self.entity_id
        entity_label = self.entity_label
        entity_type = self.entity_type
        jwt = self.jwt
        last_run: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat() if self.last_run else None

        os_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.os_created_at, Unset):
            os_created_at = self.os_created_at.isoformat()

        os_entity_uid = self.os_entity_uid
        os_icon = self.os_icon
        os_workspace = self.os_workspace
        previous_run_output = self.previous_run_output
        username = self.username
        watcher_name = self.watcher_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if cron_exp is not UNSET:
            field_dict["cron_exp"] = cron_exp
        if description is not UNSET:
            field_dict["description"] = description
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_label is not UNSET:
            field_dict["entity_label"] = entity_label
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if jwt is not UNSET:
            field_dict["jwt"] = jwt
        if last_run is not UNSET:
            field_dict["last_run"] = last_run
        if os_created_at is not UNSET:
            field_dict["os_created_at"] = os_created_at
        if os_entity_uid is not UNSET:
            field_dict["os_entity_uid"] = os_entity_uid
        if os_icon is not UNSET:
            field_dict["os_icon"] = os_icon
        if os_workspace is not UNSET:
            field_dict["os_workspace"] = os_workspace
        if previous_run_output is not UNSET:
            field_dict["previous_run_output"] = previous_run_output
        if username is not UNSET:
            field_dict["username"] = username
        if watcher_name is not UNSET:
            field_dict["watcher_name"] = watcher_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_name = d.pop("app_name", UNSET)

        arguments = d.pop("arguments", UNSET)

        cron_exp = d.pop("cron_exp", UNSET)

        description = d.pop("description", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        entity_label = d.pop("entity_label", UNSET)

        entity_type = d.pop("entity_type", UNSET)

        jwt = d.pop("jwt", UNSET)

        _last_run = d.pop("last_run", UNSET)
        last_run: Union[Unset, None, datetime.datetime]
        if _last_run is None:
            last_run = None
        elif isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        _os_created_at = d.pop("os_created_at", UNSET)
        os_created_at: Union[Unset, datetime.datetime]
        if isinstance(_os_created_at, Unset):
            os_created_at = UNSET
        else:
            os_created_at = isoparse(_os_created_at)

        os_entity_uid = d.pop("os_entity_uid", UNSET)

        os_icon = d.pop("os_icon", UNSET)

        os_workspace = d.pop("os_workspace", UNSET)

        previous_run_output = d.pop("previous_run_output", UNSET)

        username = d.pop("username", UNSET)

        watcher_name = d.pop("watcher_name", UNSET)

        watcher_intent = cls(
            app_name=app_name,
            arguments=arguments,
            cron_exp=cron_exp,
            description=description,
            entity_id=entity_id,
            entity_label=entity_label,
            entity_type=entity_type,
            jwt=jwt,
            last_run=last_run,
            os_created_at=os_created_at,
            os_entity_uid=os_entity_uid,
            os_icon=os_icon,
            os_workspace=os_workspace,
            previous_run_output=previous_run_output,
            username=username,
            watcher_name=watcher_name,
        )

        watcher_intent.additional_properties = d
        return watcher_intent

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
