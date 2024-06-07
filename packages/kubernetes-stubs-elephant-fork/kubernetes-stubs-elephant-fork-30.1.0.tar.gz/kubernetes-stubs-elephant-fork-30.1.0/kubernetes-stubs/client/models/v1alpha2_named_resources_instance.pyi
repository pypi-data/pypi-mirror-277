import datetime
import typing

import kubernetes.client

class V1alpha2NamedResourcesInstance:
    attributes: typing.Optional[list[kubernetes.client.V1alpha2NamedResourcesAttribute]]
    name: str
    
    def __init__(self, *, attributes: typing.Optional[list[kubernetes.client.V1alpha2NamedResourcesAttribute]] = ..., name: str) -> None:
        ...
    def to_dict(self) -> V1alpha2NamedResourcesInstanceDict:
        ...
class V1alpha2NamedResourcesInstanceDict(typing.TypedDict, total=False):
    attributes: typing.Optional[list[kubernetes.client.V1alpha2NamedResourcesAttributeDict]]
    name: str
