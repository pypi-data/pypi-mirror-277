from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watcher_job_params import WatcherJobParams


T = TypeVar("T", bound="WatcherJob")


@attr.s(auto_attribs=True)
class WatcherJob:
    """
    Example:
        {'max_rel_depth': 2, 'relations': ['phone_call', 'has_position'], 'description': 'Check for trespassers at 5AM',
            'entry_point': 'bash /app/watcher.py', 'interval': '3m', 'name': 'Nightly_geofence_checker', 'os-ancestor': '',
            'os-app-name': 'GeofenceWatch', 'os-app-title': 'GeofenceWatch', 'os-instance-type': 'normal', 'os-job-name':
            'oj-81b5-geofen-s-car', 'os-job-type': 'frontend-job', 'os-needs-ingress': False, 'os-ontology':
            'os_ontology_v1', 'os-username': 's.scarduzio', 'os-workspace': 'eaf0363b-72bb-4322-9b0e-980ae72ea636',
            'params': {'checked_entity_id': '${item.entity_id}', 'checked_entity_type': 'string'}, 'semantically_bound':
            ['person', 'animal']}

    Attributes:
        max_rel_depth (int):
        relations (List[str]):
        description (str):
        entry_point (str):
        interval (str):
        name (str):
        os_ancestor (str):
        params (WatcherJobParams):
        os_app_name (Union[Unset, str]):
        os_app_title (Union[Unset, str]):
        os_instance_type (Union[Unset, str]):
        os_job_name (Union[Unset, str]):
        os_job_type (Union[Unset, str]):
        os_needs_ingress (Union[Unset, bool]):
        os_ontology (Union[Unset, str]):
        os_username (Union[Unset, str]):
        os_workspace (Union[Unset, str]):
        semantically_bound (Union[Unset, List[str]]):
    """

    max_rel_depth: int
    relations: List[str]
    description: str
    entry_point: str
    interval: str
    name: str
    os_ancestor: str
    params: "WatcherJobParams"
    os_app_name: Union[Unset, str] = UNSET
    os_app_title: Union[Unset, str] = UNSET
    os_instance_type: Union[Unset, str] = UNSET
    os_job_name: Union[Unset, str] = UNSET
    os_job_type: Union[Unset, str] = UNSET
    os_needs_ingress: Union[Unset, bool] = UNSET
    os_ontology: Union[Unset, str] = UNSET
    os_username: Union[Unset, str] = UNSET
    os_workspace: Union[Unset, str] = UNSET
    semantically_bound: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_rel_depth = self.max_rel_depth
        relations = self.relations

        description = self.description
        entry_point = self.entry_point
        interval = self.interval
        name = self.name
        os_ancestor = self.os_ancestor
        params = self.params.to_dict()

        os_app_name = self.os_app_name
        os_app_title = self.os_app_title
        os_instance_type = self.os_instance_type
        os_job_name = self.os_job_name
        os_job_type = self.os_job_type
        os_needs_ingress = self.os_needs_ingress
        os_ontology = self.os_ontology
        os_username = self.os_username
        os_workspace = self.os_workspace
        semantically_bound: Union[Unset, List[str]] = UNSET
        if not isinstance(self.semantically_bound, Unset):
            semantically_bound = self.semantically_bound

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_rel_depth": max_rel_depth,
                "relations": relations,
                "description": description,
                "entry_point": entry_point,
                "interval": interval,
                "name": name,
                "os-ancestor": os_ancestor,
                "params": params,
            }
        )
        if os_app_name is not UNSET:
            field_dict["Os-app-name"] = os_app_name
        if os_app_title is not UNSET:
            field_dict["Os-app-title"] = os_app_title
        if os_instance_type is not UNSET:
            field_dict["Os-instance-type"] = os_instance_type
        if os_job_name is not UNSET:
            field_dict["Os-job-name"] = os_job_name
        if os_job_type is not UNSET:
            field_dict["Os-job-type"] = os_job_type
        if os_needs_ingress is not UNSET:
            field_dict["Os-needs-ingress"] = os_needs_ingress
        if os_ontology is not UNSET:
            field_dict["Os-ontology"] = os_ontology
        if os_username is not UNSET:
            field_dict["Os-username"] = os_username
        if os_workspace is not UNSET:
            field_dict["Os-workspace"] = os_workspace
        if semantically_bound is not UNSET:
            field_dict["semantically_bound"] = semantically_bound

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.watcher_job_params import WatcherJobParams

        d = src_dict.copy()
        max_rel_depth = d.pop("max_rel_depth")

        relations = cast(List[str], d.pop("relations"))

        description = d.pop("description")

        entry_point = d.pop("entry_point")

        interval = d.pop("interval")

        name = d.pop("name")

        os_ancestor = d.pop("os-ancestor")

        params = WatcherJobParams.from_dict(d.pop("params"))

        os_app_name = d.pop("Os-app-name", UNSET)

        os_app_title = d.pop("Os-app-title", UNSET)

        os_instance_type = d.pop("Os-instance-type", UNSET)

        os_job_name = d.pop("Os-job-name", UNSET)

        os_job_type = d.pop("Os-job-type", UNSET)

        os_needs_ingress = d.pop("Os-needs-ingress", UNSET)

        os_ontology = d.pop("Os-ontology", UNSET)

        os_username = d.pop("Os-username", UNSET)

        os_workspace = d.pop("Os-workspace", UNSET)

        semantically_bound = cast(List[str], d.pop("semantically_bound", UNSET))

        watcher_job = cls(
            max_rel_depth=max_rel_depth,
            relations=relations,
            description=description,
            entry_point=entry_point,
            interval=interval,
            name=name,
            os_ancestor=os_ancestor,
            params=params,
            os_app_name=os_app_name,
            os_app_title=os_app_title,
            os_instance_type=os_instance_type,
            os_job_name=os_job_name,
            os_job_type=os_job_type,
            os_needs_ingress=os_needs_ingress,
            os_ontology=os_ontology,
            os_username=os_username,
            os_workspace=os_workspace,
            semantically_bound=semantically_bound,
        )

        watcher_job.additional_properties = d
        return watcher_job

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
