from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="GetJobsUrlJsonBody")


@attr.s(auto_attribs=True)
class GetJobsUrlJsonBody:
    """The job ids to get the urls for.

    Attributes:
        job_ids (List[str]):
    """

    job_ids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_ids = self.job_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_ids": job_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_ids = cast(List[str], d.pop("job_ids"))

        get_jobs_url_json_body = cls(
            job_ids=job_ids,
        )

        get_jobs_url_json_body.additional_properties = d
        return get_jobs_url_json_body

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
