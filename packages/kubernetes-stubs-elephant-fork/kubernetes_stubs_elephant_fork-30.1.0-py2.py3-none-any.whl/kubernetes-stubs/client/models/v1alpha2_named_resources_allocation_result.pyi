import datetime
import typing

import kubernetes.client

class V1alpha2NamedResourcesAllocationResult:
    name: str
    
    def __init__(self, *, name: str) -> None:
        ...
    def to_dict(self) -> V1alpha2NamedResourcesAllocationResultDict:
        ...
class V1alpha2NamedResourcesAllocationResultDict(typing.TypedDict, total=False):
    name: str
