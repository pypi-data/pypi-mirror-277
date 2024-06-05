from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobExecutionResult")


@attr.s(auto_attribs=True)
class JobExecutionResult:
    """
    Attributes:
        job_name (Union[Unset, str]):  Example: oj-os-ontology-v1-s-scarduzio-c3c61.
        pod_name (Union[Unset, str]):  Example: oj-os-ontology-v1-s-scarduzio-c3c61-kg5gl.
        ancestor (Union[Unset, str]):
        status (Union[Unset, str]):
        app_name (Union[Unset, str]):
    """

    job_name: Union[Unset, str] = UNSET
    pod_name: Union[Unset, str] = UNSET
    ancestor: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        pod_name = self.pod_name
        ancestor = self.ancestor
        status = self.status
        app_name = self.app_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_name is not UNSET:
            field_dict["job_name"] = job_name
        if pod_name is not UNSET:
            field_dict["pod_name"] = pod_name
        if ancestor is not UNSET:
            field_dict["ancestor"] = ancestor
        if status is not UNSET:
            field_dict["status"] = status
        if app_name is not UNSET:
            field_dict["app_name"] = app_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_name = d.pop("job_name", UNSET)

        pod_name = d.pop("pod_name", UNSET)

        ancestor = d.pop("ancestor", UNSET)

        status = d.pop("status", UNSET)

        app_name = d.pop("app_name", UNSET)

        job_execution_result = cls(
            job_name=job_name,
            pod_name=pod_name,
            ancestor=ancestor,
            status=status,
            app_name=app_name,
        )

        job_execution_result.additional_properties = d
        return job_execution_result

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
