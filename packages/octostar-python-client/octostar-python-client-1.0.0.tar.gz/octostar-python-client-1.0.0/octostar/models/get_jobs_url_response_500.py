from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetJobsUrlResponse500")


@attr.s(auto_attribs=True)
class GetJobsUrlResponse500:
    """
    Attributes:
        error (Union[Unset, str]):
        traceback (Union[Unset, str]):
    """

    error: Union[Unset, str] = UNSET
    traceback: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        traceback = self.traceback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if traceback is not UNSET:
            field_dict["traceback"] = traceback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        traceback = d.pop("traceback", UNSET)

        get_jobs_url_response_500 = cls(
            error=error,
            traceback=traceback,
        )

        get_jobs_url_response_500.additional_properties = d
        return get_jobs_url_response_500

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
