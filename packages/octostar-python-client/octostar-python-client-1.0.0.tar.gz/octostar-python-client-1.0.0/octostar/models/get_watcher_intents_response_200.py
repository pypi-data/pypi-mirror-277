from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_watcher_intents_response_200_status import GetWatcherIntentsResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_watcher_intents_response_200_message_item import GetWatcherIntentsResponse200MessageItem


T = TypeVar("T", bound="GetWatcherIntentsResponse200")


@attr.s(auto_attribs=True)
class GetWatcherIntentsResponse200:
    """
    Attributes:
        message (Union[Unset, List['GetWatcherIntentsResponse200MessageItem']]):
        status (Union[Unset, GetWatcherIntentsResponse200Status]):
    """

    message: Union[Unset, List["GetWatcherIntentsResponse200MessageItem"]] = UNSET
    status: Union[Unset, GetWatcherIntentsResponse200Status] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.message, Unset):
            message = []
            for message_item_data in self.message:
                message_item = message_item_data.to_dict()

                message.append(message_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_watcher_intents_response_200_message_item import GetWatcherIntentsResponse200MessageItem

        d = src_dict.copy()
        message = []
        _message = d.pop("message", UNSET)
        for message_item_data in _message or []:
            message_item = GetWatcherIntentsResponse200MessageItem.from_dict(message_item_data)

            message.append(message_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GetWatcherIntentsResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetWatcherIntentsResponse200Status(_status)

        get_watcher_intents_response_200 = cls(
            message=message,
            status=status,
        )

        get_watcher_intents_response_200.additional_properties = d
        return get_watcher_intents_response_200

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
