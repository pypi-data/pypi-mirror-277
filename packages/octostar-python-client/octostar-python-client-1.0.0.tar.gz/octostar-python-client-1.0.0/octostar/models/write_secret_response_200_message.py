from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_secret_response_200_message_annotations import WriteSecretResponse200MessageAnnotations


T = TypeVar("T", bound="WriteSecretResponse200Message")


@attr.s(auto_attribs=True)
class WriteSecretResponse200Message:
    """
    Attributes:
        secret_name (Union[Unset, str]):
        job_name (Union[Unset, str]):
        data (Union[Unset, List[str]]):
        annotations (Union[Unset, WriteSecretResponse200MessageAnnotations]):
        created_by (Union[Unset, str]):
        app_name (Union[Unset, str]):
    """

    secret_name: Union[Unset, str] = UNSET
    job_name: Union[Unset, str] = UNSET
    data: Union[Unset, List[str]] = UNSET
    annotations: Union[Unset, "WriteSecretResponse200MessageAnnotations"] = UNSET
    created_by: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secret_name = self.secret_name
        job_name = self.job_name
        data: Union[Unset, List[str]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        annotations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        created_by = self.created_by
        app_name = self.app_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret_name is not UNSET:
            field_dict["secret_name"] = secret_name
        if job_name is not UNSET:
            field_dict["job_name"] = job_name
        if data is not UNSET:
            field_dict["data"] = data
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if app_name is not UNSET:
            field_dict["app_name"] = app_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.write_secret_response_200_message_annotations import WriteSecretResponse200MessageAnnotations

        d = src_dict.copy()
        secret_name = d.pop("secret_name", UNSET)

        job_name = d.pop("job_name", UNSET)

        data = cast(List[str], d.pop("data", UNSET))

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, WriteSecretResponse200MessageAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = WriteSecretResponse200MessageAnnotations.from_dict(_annotations)

        created_by = d.pop("created_by", UNSET)

        app_name = d.pop("app_name", UNSET)

        write_secret_response_200_message = cls(
            secret_name=secret_name,
            job_name=job_name,
            data=data,
            annotations=annotations,
            created_by=created_by,
            app_name=app_name,
        )

        write_secret_response_200_message.additional_properties = d
        return write_secret_response_200_message

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
