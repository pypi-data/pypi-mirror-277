from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWhoamiResponse200")


@attr.s(auto_attribs=True)
class GetWhoamiResponse200:
    """
    Attributes:
        username (Union[Unset, str]):
        email (Union[Unset, str]):
        async_channel (Union[Unset, str]):
        os_jwt (Union[Unset, str]):
    """

    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    async_channel: Union[Unset, str] = UNSET
    os_jwt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        email = self.email
        async_channel = self.async_channel
        os_jwt = self.os_jwt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
        if async_channel is not UNSET:
            field_dict["async_channel"] = async_channel
        if os_jwt is not UNSET:
            field_dict["os_jwt"] = os_jwt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        email = d.pop("email", UNSET)

        async_channel = d.pop("async_channel", UNSET)

        os_jwt = d.pop("os_jwt", UNSET)

        get_whoami_response_200 = cls(
            username=username,
            email=email,
            async_channel=async_channel,
            os_jwt=os_jwt,
        )

        get_whoami_response_200.additional_properties = d
        return get_whoami_response_200

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
