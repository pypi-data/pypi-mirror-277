import datetime
import typing

import kubernetes.client

class V1alpha1ParentReference:
    group: typing.Optional[str]
    name: str
    namespace: typing.Optional[str]
    resource: str
    
    def __init__(self, *, group: typing.Optional[str] = ..., name: str, namespace: typing.Optional[str] = ..., resource: str) -> None:
        ...
    def to_dict(self) -> V1alpha1ParentReferenceDict:
        ...
class V1alpha1ParentReferenceDict(typing.TypedDict, total=False):
    group: typing.Optional[str]
    name: str
    namespace: typing.Optional[str]
    resource: str
