from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.export_response_500_status import ExportResponse500Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_response_500_data import ExportResponse500Data


T = TypeVar("T", bound="ExportResponse500")


@attr.s(auto_attribs=True)
class ExportResponse500:
    """
    Attributes:
        status (Union[Unset, ExportResponse500Status]):
        data (Union[Unset, ExportResponse500Data]):
    """

    status: Union[Unset, ExportResponse500Status] = UNSET
    data: Union[Unset, "ExportResponse500Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.export_response_500_data import ExportResponse500Data

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, ExportResponse500Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ExportResponse500Status(_status)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ExportResponse500Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ExportResponse500Data.from_dict(_data)

        export_response_500 = cls(
            status=status,
            data=data,
        )

        export_response_500.additional_properties = d
        return export_response_500

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
