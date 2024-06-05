from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_200_data import (
        PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200Data,
    )


T = TypeVar("T", bound="PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200")


@attr.s(auto_attribs=True)
class PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200:
    """
    Attributes:
        status (Union[Unset, str]):
        data (Union[Unset, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200Data]):
    """

    status: Union[Unset, str] = UNSET
    data: Union[Unset, "PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
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
        from ..models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_200_data import (
            PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200Data,
        )

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = PostApiOctostarJobsDeployWorkspaceOsEntityUidResponse200Data.from_dict(_data)

        post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_200 = cls(
            status=status,
            data=data,
        )

        post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_200.additional_properties = d
        return post_api_octostar_jobs_deploy_workspace_os_entity_uid_response_200

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
