import datetime
import typing

import kubernetes.client

class V1alpha2NamedResourcesStringSlice:
    strings: list[str]
    
    def __init__(self, *, strings: list[str]) -> None:
        ...
    def to_dict(self) -> V1alpha2NamedResourcesStringSliceDict:
        ...
class V1alpha2NamedResourcesStringSliceDict(typing.TypedDict, total=False):
    strings: list[str]
