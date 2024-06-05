from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watcher_job import WatcherJob


T = TypeVar("T", bound="GetWatcherJobsResponse200")


@attr.s(auto_attribs=True)
class GetWatcherJobsResponse200:
    """
    Attributes:
        message (Union[Unset, List['WatcherJob']]):
        status (Union[Unset, str]):
    """

    message: Union[Unset, List["WatcherJob"]] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.message, Unset):
            message = []
            for message_item_data in self.message:
                message_item = message_item_data.to_dict()

                message.append(message_item)

        status = self.status

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
        from ..models.watcher_job import WatcherJob

        d = src_dict.copy()
        message = []
        _message = d.pop("message", UNSET)
        for message_item_data in _message or []:
            message_item = WatcherJob.from_dict(message_item_data)

            message.append(message_item)

        status = d.pop("status", UNSET)

        get_watcher_jobs_response_200 = cls(
            message=message,
            status=status,
        )

        get_watcher_jobs_response_200.additional_properties = d
        return get_watcher_jobs_response_200

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
