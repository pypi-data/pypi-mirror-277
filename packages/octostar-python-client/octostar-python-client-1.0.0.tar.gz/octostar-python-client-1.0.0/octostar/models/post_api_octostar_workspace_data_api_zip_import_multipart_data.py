from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.post_api_octostar_workspace_data_api_zip_import_multipart_data_include_dashboards_type_1 import (
    PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1,
)
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PostApiOctostarWorkspaceDataApiZipImportMultipartData")


@attr.s(auto_attribs=True)
class PostApiOctostarWorkspaceDataApiZipImportMultipartData:
    """
    Attributes:
        zip_ (Union[Unset, File]): The zip file to upload.
        target (Union[Unset, str]): Optional target entity ID for the upload.
        overwrite (Union[Unset, bool]): Whether to overwrite existing entities and/or dashboards.
        include_content (Union[Unset, bool]): Whether to include content in the import (if included in zip). Default:
            True.
        include_dashboards (Union[PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1, Unset,
            bool]): Whether to include dashboards in the import (if included in zip), or include them only if missing.
    """

    zip_: Union[Unset, File] = UNSET
    target: Union[Unset, str] = UNSET
    overwrite: Union[Unset, bool] = False
    include_content: Union[Unset, bool] = True
    include_dashboards: Union[
        PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1, Unset, bool
    ] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zip_: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.zip_, Unset):
            zip_ = self.zip_.to_tuple()

        target = self.target
        overwrite = self.overwrite
        include_content = self.include_content
        include_dashboards: Union[Unset, bool, str]
        if isinstance(self.include_dashboards, Unset):
            include_dashboards = UNSET

        elif isinstance(
            self.include_dashboards, PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1
        ):
            include_dashboards = UNSET
            if not isinstance(self.include_dashboards, Unset):
                include_dashboards = self.include_dashboards.value

        else:
            include_dashboards = self.include_dashboards

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if target is not UNSET:
            field_dict["target"] = target
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if include_content is not UNSET:
            field_dict["include_content"] = include_content
        if include_dashboards is not UNSET:
            field_dict["include_dashboards"] = include_dashboards

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        zip_: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.zip_, Unset):
            zip_ = self.zip_.to_tuple()

        target = self.target if isinstance(self.target, Unset) else (None, str(self.target).encode(), "text/plain")
        overwrite = (
            self.overwrite if isinstance(self.overwrite, Unset) else (None, str(self.overwrite).encode(), "text/plain")
        )
        include_content = (
            self.include_content
            if isinstance(self.include_content, Unset)
            else (None, str(self.include_content).encode(), "text/plain")
        )
        include_dashboards: Union[Unset, bool, str]
        if isinstance(self.include_dashboards, Unset):
            include_dashboards = UNSET

        elif isinstance(
            self.include_dashboards, PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1
        ):
            include_dashboards = UNSET
            if not isinstance(self.include_dashboards, Unset):
                include_dashboards = (None, str(self.include_dashboards.value).encode(), "text/plain")

        else:
            include_dashboards = self.include_dashboards

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if target is not UNSET:
            field_dict["target"] = target
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if include_content is not UNSET:
            field_dict["include_content"] = include_content
        if include_dashboards is not UNSET:
            field_dict["include_dashboards"] = include_dashboards

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _zip_ = d.pop("zip", UNSET)
        zip_: Union[Unset, File]
        if isinstance(_zip_, Unset):
            zip_ = UNSET
        else:
            zip_ = File(payload=BytesIO(_zip_))

        target = d.pop("target", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        include_content = d.pop("include_content", UNSET)

        def _parse_include_dashboards(
            data: object,
        ) -> Union[PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1, Unset, bool]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _include_dashboards_type_1 = data
                include_dashboards_type_1: Union[
                    Unset, PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1
                ]
                if isinstance(_include_dashboards_type_1, Unset):
                    include_dashboards_type_1 = UNSET
                else:
                    include_dashboards_type_1 = (
                        PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1(
                            _include_dashboards_type_1
                        )
                    )

                return include_dashboards_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[PostApiOctostarWorkspaceDataApiZipImportMultipartDataIncludeDashboardsType1, Unset, bool], data
            )

        include_dashboards = _parse_include_dashboards(d.pop("include_dashboards", UNSET))

        post_api_octostar_workspace_data_api_zip_import_multipart_data = cls(
            zip_=zip_,
            target=target,
            overwrite=overwrite,
            include_content=include_content,
            include_dashboards=include_dashboards,
        )

        post_api_octostar_workspace_data_api_zip_import_multipart_data.additional_properties = d
        return post_api_octostar_workspace_data_api_zip_import_multipart_data

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
