import datetime
import typing

import kubernetes.client

class V1alpha2NamedResourcesIntSlice:
    ints: list[int]
    
    def __init__(self, *, ints: list[int]) -> None:
        ...
    def to_dict(self) -> V1alpha2NamedResourcesIntSliceDict:
        ...
class V1alpha2NamedResourcesIntSliceDict(typing.TypedDict, total=False):
    ints: list[int]
