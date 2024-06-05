from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSecretJsonBody")


@attr.s(auto_attribs=True)
class DeleteSecretJsonBody:
    """
    Attributes:
        job_name (str):
        os_workspace (Union[Unset, str]):
        os_entity_id (Union[Unset, str]):
    """

    job_name: str
    os_workspace: Union[Unset, str] = UNSET
    os_entity_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        os_workspace = self.os_workspace
        os_entity_id = self.os_entity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_name": job_name,
            }
        )
        if os_workspace is not UNSET:
            field_dict["os_workspace"] = os_workspace
        if os_entity_id is not UNSET:
            field_dict["os_entity_id"] = os_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_name = d.pop("job_name")

        os_workspace = d.pop("os_workspace", UNSET)

        os_entity_id = d.pop("os_entity_id", UNSET)

        delete_secret_json_body = cls(
            job_name=job_name,
            os_workspace=os_workspace,
            os_entity_id=os_entity_id,
        )

        delete_secret_json_body.additional_properties = d
        return delete_secret_json_body

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
