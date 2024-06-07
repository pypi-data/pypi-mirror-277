import datetime
import typing

import kubernetes.client

class V1alpha2NamedResourcesRequest:
    selector: str
    
    def __init__(self, *, selector: str) -> None:
        ...
    def to_dict(self) -> V1alpha2NamedResourcesRequestDict:
        ...
class V1alpha2NamedResourcesRequestDict(typing.TypedDict, total=False):
    selector: str
