from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_json_body_secrets import (
        PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBodySecrets,
    )


T = TypeVar("T", bound="PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody")


@attr.s(auto_attribs=True)
class PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBody:
    """
    Attributes:
        secrets (Union[Unset, PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBodySecrets]): A key value bag of strings
            to store sensitive information. Example: {'key': 'value'}.
    """

    secrets: Union[Unset, "PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBodySecrets"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secrets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = self.secrets.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_api_octostar_jobs_deploy_workspace_os_entity_uid_json_body_secrets import (
            PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBodySecrets,
        )

        d = src_dict.copy()
        _secrets = d.pop("secrets", UNSET)
        secrets: Union[Unset, PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBodySecrets]
        if isinstance(_secrets, Unset):
            secrets = UNSET
        else:
            secrets = PostApiOctostarJobsDeployWorkspaceOsEntityUidJsonBodySecrets.from_dict(_secrets)

        post_api_octostar_jobs_deploy_workspace_os_entity_uid_json_body = cls(
            secrets=secrets,
        )

        post_api_octostar_jobs_deploy_workspace_os_entity_uid_json_body.additional_properties = d
        return post_api_octostar_jobs_deploy_workspace_os_entity_uid_json_body

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
