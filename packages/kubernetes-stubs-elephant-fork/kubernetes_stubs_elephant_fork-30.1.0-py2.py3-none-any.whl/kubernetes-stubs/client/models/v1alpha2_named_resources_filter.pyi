import datetime
import typing

import kubernetes.client

class V1alpha2NamedResourcesFilter:
    selector: str
    
    def __init__(self, *, selector: str) -> None:
        ...
    def to_dict(self) -> V1alpha2NamedResourcesFilterDict:
        ...
class V1alpha2NamedResourcesFilterDict(typing.TypedDict, total=False):
    selector: str
