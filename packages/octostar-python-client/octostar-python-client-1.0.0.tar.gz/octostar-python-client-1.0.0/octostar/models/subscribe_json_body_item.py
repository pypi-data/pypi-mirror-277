from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscribeJsonBodyItem")


@attr.s(auto_attribs=True)
class SubscribeJsonBodyItem:
    """
    Attributes:
        channel (Union[Unset, str]): Channel to unsubscribe from.
        workspace_id (Union[Unset, str]): Workspace ID. Optional.
    """

    channel: Union[Unset, str] = UNSET
    workspace_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel = self.channel
        workspace_id = self.workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if workspace_id is not UNSET:
            field_dict["workspace_id"] = workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel = d.pop("channel", UNSET)

        workspace_id = d.pop("workspace_id", UNSET)

        subscribe_json_body_item = cls(
            channel=channel,
            workspace_id=workspace_id,
        )

        subscribe_json_body_item.additional_properties = d
        return subscribe_json_body_item

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
