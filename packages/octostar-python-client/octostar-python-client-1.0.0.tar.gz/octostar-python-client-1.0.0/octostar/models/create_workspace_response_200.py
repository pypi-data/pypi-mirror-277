from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkspaceResponse200")


@attr.s(auto_attribs=True)
class CreateWorkspaceResponse200:
    """
    Attributes:
        entity_type (Union[Unset, str]): The type of the workspace
        entity_id (Union[Unset, str]): The ID of the workspace
        entity_label (Union[Unset, str]): The label of the workspace
    """

    entity_type: Union[Unset, str] = UNSET
    entity_id: Union[Unset, str] = UNSET
    entity_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_type = self.entity_type
        entity_id = self.entity_id
        entity_label = self.entity_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_label is not UNSET:
            field_dict["entity_label"] = entity_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity_type = d.pop("entity_type", UNSET)

        entity_id = d.pop("entity_id", UNSET)

        entity_label = d.pop("entity_label", UNSET)

        create_workspace_response_200 = cls(
            entity_type=entity_type,
            entity_id=entity_id,
            entity_label=entity_label,
        )

        create_workspace_response_200.additional_properties = d
        return create_workspace_response_200

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
