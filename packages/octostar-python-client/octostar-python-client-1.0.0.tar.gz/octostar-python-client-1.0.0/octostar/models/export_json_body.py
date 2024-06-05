from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportJsonBody")


@attr.s(auto_attribs=True)
class ExportJsonBody:
    """The SQL query to be executed

    Attributes:
        source (str): The os_entity_uid (or comma separated list of entity_ids) of source file or folder to export.
        filename (Union[Unset, str]): The os_entity_uid of the target folder.
        include_content (Union[Unset, bool]): Whether to include entities and attachments in the export. Default is
            true.
        include_dashboards (Union[Unset, bool]): Whether to include any connected superset dashboards in the export.
            Default is true.
    """

    source: str
    filename: Union[Unset, str] = UNSET
    include_content: Union[Unset, bool] = UNSET
    include_dashboards: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source = self.source
        filename = self.filename
        include_content = self.include_content
        include_dashboards = self.include_dashboards

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if include_content is not UNSET:
            field_dict["include_content"] = include_content
        if include_dashboards is not UNSET:
            field_dict["include_dashboards"] = include_dashboards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source = d.pop("source")

        filename = d.pop("filename", UNSET)

        include_content = d.pop("include_content", UNSET)

        include_dashboards = d.pop("include_dashboards", UNSET)

        export_json_body = cls(
            source=source,
            filename=filename,
            include_content=include_content,
            include_dashboards=include_dashboards,
        )

        export_json_body.additional_properties = d
        return export_json_body

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
