from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.insert_entity_base import InsertEntityBase


T = TypeVar("T", bound="InsertEntityRelationshipsItem")


@attr.s(auto_attribs=True)
class InsertEntityRelationshipsItem:
    """
    Attributes:
        entity (Union[Unset, InsertEntityBase]):
        relationship_name (Union[Unset, str]):
        relationship_uid (Union[Unset, str]):
    """

    entity: Union[Unset, "InsertEntityBase"] = UNSET
    relationship_name: Union[Unset, str] = UNSET
    relationship_uid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        relationship_name = self.relationship_name
        relationship_uid = self.relationship_uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity is not UNSET:
            field_dict["entity"] = entity
        if relationship_name is not UNSET:
            field_dict["relationship_name"] = relationship_name
        if relationship_uid is not UNSET:
            field_dict["relationship_uid"] = relationship_uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.insert_entity_base import InsertEntityBase

        d = src_dict.copy()
        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, InsertEntityBase]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = InsertEntityBase.from_dict(_entity)

        relationship_name = d.pop("relationship_name", UNSET)

        relationship_uid = d.pop("relationship_uid", UNSET)

        insert_entity_relationships_item = cls(
            entity=entity,
            relationship_name=relationship_name,
            relationship_uid=relationship_uid,
        )

        insert_entity_relationships_item.additional_properties = d
        return insert_entity_relationships_item

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
