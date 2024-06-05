from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspaceJsonBody")


@attr.s(auto_attribs=True)
class CreateWorkspaceJsonBody:
    """
    Attributes:
        os_item_name (Union[Unset, str]): The name of the workspace
    """

    os_item_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        os_item_name = self.os_item_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if os_item_name is not UNSET:
            field_dict["os_item_name"] = os_item_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        os_item_name = d.pop("os_item_name", UNSET)

        create_workspace_json_body = cls(
            os_item_name=os_item_name,
        )

        create_workspace_json_body.additional_properties = d
        return create_workspace_json_body

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
