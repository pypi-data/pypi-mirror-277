from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WatcherJobParams")


@attr.s(auto_attribs=True)
class WatcherJobParams:
    """
    Attributes:
        checked_entity_id (str):
        checked_entity_type (str):
    """

    checked_entity_id: str
    checked_entity_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checked_entity_id = self.checked_entity_id
        checked_entity_type = self.checked_entity_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checked_entity_id": checked_entity_id,
                "checked_entity_type": checked_entity_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        checked_entity_id = d.pop("checked_entity_id")

        checked_entity_type = d.pop("checked_entity_type")

        watcher_job_params = cls(
            checked_entity_id=checked_entity_id,
            checked_entity_type=checked_entity_type,
        )

        watcher_job_params.additional_properties = d
        return watcher_job_params

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
