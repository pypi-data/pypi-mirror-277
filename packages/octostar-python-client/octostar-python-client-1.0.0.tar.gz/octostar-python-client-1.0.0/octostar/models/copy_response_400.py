from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.copy_response_400_status import CopyResponse400Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.copy_response_400_data import CopyResponse400Data


T = TypeVar("T", bound="CopyResponse400")


@attr.s(auto_attribs=True)
class CopyResponse400:
    """
    Attributes:
        status (Union[Unset, CopyResponse400Status]):
        data (Union[Unset, CopyResponse400Data]):
    """

    status: Union[Unset, CopyResponse400Status] = UNSET
    data: Union[Unset, "CopyResponse400Data"] = UNSET
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
        from ..models.copy_response_400_data import CopyResponse400Data

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CopyResponse400Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CopyResponse400Status(_status)

        _data = d.pop("data", UNSET)
        data: Union[Unset, CopyResponse400Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CopyResponse400Data.from_dict(_data)

        copy_response_400 = cls(
            status=status,
            data=data,
        )

        copy_response_400.additional_properties = d
        return copy_response_400

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
