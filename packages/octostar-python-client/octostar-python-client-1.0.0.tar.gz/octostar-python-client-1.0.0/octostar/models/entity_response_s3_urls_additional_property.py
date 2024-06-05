from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_response_s3_urls_additional_property_fields import EntityResponseS3UrlsAdditionalPropertyFields


T = TypeVar("T", bound="EntityResponseS3UrlsAdditionalProperty")


@attr.s(auto_attribs=True)
class EntityResponseS3UrlsAdditionalProperty:
    """
    Attributes:
        fields (Union[Unset, EntityResponseS3UrlsAdditionalPropertyFields]):
        url (Union[Unset, str]):
    """

    fields: Union[Unset, "EntityResponseS3UrlsAdditionalPropertyFields"] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_response_s3_urls_additional_property_fields import (
            EntityResponseS3UrlsAdditionalPropertyFields,
        )

        d = src_dict.copy()
        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, EntityResponseS3UrlsAdditionalPropertyFields]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = EntityResponseS3UrlsAdditionalPropertyFields.from_dict(_fields)

        url = d.pop("url", UNSET)

        entity_response_s3_urls_additional_property = cls(
            fields=fields,
            url=url,
        )

        entity_response_s3_urls_additional_property.additional_properties = d
        return entity_response_s3_urls_additional_property

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
