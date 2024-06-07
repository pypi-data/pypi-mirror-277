import datetime
import typing

import kubernetes.client

class V1alpha2ResourceClassParametersList:
    api_version: typing.Optional[str]
    items: list[kubernetes.client.V1alpha2ResourceClassParameters]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMeta]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., items: list[kubernetes.client.V1alpha2ResourceClassParameters], kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes.client.V1ListMeta] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha2ResourceClassParametersListDict:
        ...
class V1alpha2ResourceClassParametersListDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    items: list[kubernetes.client.V1alpha2ResourceClassParametersDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ListMetaDict]
