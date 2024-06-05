from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.copy_json_body_options import CopyJsonBodyOptions


T = TypeVar("T", bound="CopyJsonBody")


@attr.s(auto_attribs=True)
class CopyJsonBody:
    """The SQL query to be executed

    Attributes:
        source (str): The os_entity_uid of source file or folder to copy.
        target (str): The os_entity_uid of the target folder.
        options (Union[Unset, CopyJsonBodyOptions]):
    """

    source: str
    target: str
    options: Union[Unset, "CopyJsonBodyOptions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        target = self.target
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "target": target,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.copy_json_body_options import CopyJsonBodyOptions

        d = src_dict.copy()
        source = d.pop("source")

        target = d.pop("target")

        _options = d.pop("options", UNSET)
        options: Union[Unset, CopyJsonBodyOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = CopyJsonBodyOptions.from_dict(_options)

        copy_json_body = cls(
            source=source,
            target=target,
            options=options,
        )

        copy_json_body.additional_properties = d
        return copy_json_body

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
