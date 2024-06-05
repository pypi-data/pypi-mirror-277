from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_secret_response_200_message import GetSecretResponse200Message


T = TypeVar("T", bound="GetSecretResponse200")


@attr.s(auto_attribs=True)
class GetSecretResponse200:
    """
    Attributes:
        status (Union[Unset, str]):
        message (Union[Unset, GetSecretResponse200Message]):
    """

    status: Union[Unset, str] = UNSET
    message: Union[Unset, "GetSecretResponse200Message"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_secret_response_200_message import GetSecretResponse200Message

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _message = d.pop("message", UNSET)
        message: Union[Unset, GetSecretResponse200Message]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = GetSecretResponse200Message.from_dict(_message)

        get_secret_response_200 = cls(
            status=status,
            message=message,
        )

        get_secret_response_200.additional_properties = d
        return get_secret_response_200

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
