from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_secret_json_body_data_item import WriteSecretJsonBodyDataItem


T = TypeVar("T", bound="WriteSecretJsonBody")


@attr.s(auto_attribs=True)
class WriteSecretJsonBody:
    """
    Attributes:
        job_name (str):
        data (List['WriteSecretJsonBodyDataItem']):
        os_workspace (Union[Unset, str]):
        os_entity_id (Union[Unset, str]):
    """

    job_name: str
    data: List["WriteSecretJsonBodyDataItem"]
    os_workspace: Union[Unset, str] = UNSET
    os_entity_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()

            data.append(data_item)

        os_workspace = self.os_workspace
        os_entity_id = self.os_entity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_name": job_name,
                "data": data,
            }
        )
        if os_workspace is not UNSET:
            field_dict["os_workspace"] = os_workspace
        if os_entity_id is not UNSET:
            field_dict["os_entity_id"] = os_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.write_secret_json_body_data_item import WriteSecretJsonBodyDataItem

        d = src_dict.copy()
        job_name = d.pop("job_name")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WriteSecretJsonBodyDataItem.from_dict(data_item_data)

            data.append(data_item)

        os_workspace = d.pop("os_workspace", UNSET)

        os_entity_id = d.pop("os_entity_id", UNSET)

        write_secret_json_body = cls(
            job_name=job_name,
            data=data,
            os_workspace=os_workspace,
            os_entity_id=os_entity_id,
        )

        write_secret_json_body.additional_properties = d
        return write_secret_json_body

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
