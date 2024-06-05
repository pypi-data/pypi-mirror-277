from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_secret_response_200_message_data_item import GetSecretResponse200MessageDataItem


T = TypeVar("T", bound="GetSecretResponse200Message")


@attr.s(auto_attribs=True)
class GetSecretResponse200Message:
    """
    Attributes:
        job_name (Union[Unset, str]):
        app_name (Union[Unset, str]):
        os_workspace (Union[Unset, str]):
        os_entity_id (Union[Unset, str]):
        created_by (Union[Unset, str]):
        secret_name (Union[Unset, str]):
        data (Union[Unset, List['GetSecretResponse200MessageDataItem']]):
    """

    job_name: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    os_workspace: Union[Unset, str] = UNSET
    os_entity_id: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    secret_name: Union[Unset, str] = UNSET
    data: Union[Unset, List["GetSecretResponse200MessageDataItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        app_name = self.app_name
        os_workspace = self.os_workspace
        os_entity_id = self.os_entity_id
        created_by = self.created_by
        secret_name = self.secret_name
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_name is not UNSET:
            field_dict["job_name"] = job_name
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if os_workspace is not UNSET:
            field_dict["os_workspace"] = os_workspace
        if os_entity_id is not UNSET:
            field_dict["os_entity_id"] = os_entity_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if secret_name is not UNSET:
            field_dict["secret_name"] = secret_name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_secret_response_200_message_data_item import GetSecretResponse200MessageDataItem

        d = src_dict.copy()
        job_name = d.pop("job_name", UNSET)

        app_name = d.pop("app_name", UNSET)

        os_workspace = d.pop("os_workspace", UNSET)

        os_entity_id = d.pop("os_entity_id", UNSET)

        created_by = d.pop("created_by", UNSET)

        secret_name = d.pop("secret_name", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetSecretResponse200MessageDataItem.from_dict(data_item_data)

            data.append(data_item)

        get_secret_response_200_message = cls(
            job_name=job_name,
            app_name=app_name,
            os_workspace=os_workspace,
            os_entity_id=os_entity_id,
            created_by=created_by,
            secret_name=secret_name,
            data=data,
        )

        get_secret_response_200_message.additional_properties = d
        return get_secret_response_200_message

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
