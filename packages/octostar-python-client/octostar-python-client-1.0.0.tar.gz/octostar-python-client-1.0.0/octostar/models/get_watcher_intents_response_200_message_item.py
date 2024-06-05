from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watcher_intent import WatcherIntent


T = TypeVar("T", bound="GetWatcherIntentsResponse200MessageItem")


@attr.s(auto_attribs=True)
class GetWatcherIntentsResponse200MessageItem:
    """
    Attributes:
        username (Union[Unset, str]):
        intents (Union[Unset, List['WatcherIntent']]):
    """

    username: Union[Unset, str] = UNSET
    intents: Union[Unset, List["WatcherIntent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        intents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.intents, Unset):
            intents = []
            for intents_item_data in self.intents:
                intents_item = intents_item_data.to_dict()

                intents.append(intents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if intents is not UNSET:
            field_dict["intents"] = intents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.watcher_intent import WatcherIntent

        d = src_dict.copy()
        username = d.pop("username", UNSET)

        intents = []
        _intents = d.pop("intents", UNSET)
        for intents_item_data in _intents or []:
            intents_item = WatcherIntent.from_dict(intents_item_data)

            intents.append(intents_item)

        get_watcher_intents_response_200_message_item = cls(
            username=username,
            intents=intents,
        )

        get_watcher_intents_response_200_message_item.additional_properties = d
        return get_watcher_intents_response_200_message_item

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
