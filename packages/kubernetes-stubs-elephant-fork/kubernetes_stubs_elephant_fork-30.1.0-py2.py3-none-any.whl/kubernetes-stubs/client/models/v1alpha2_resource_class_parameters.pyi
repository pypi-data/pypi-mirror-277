import datetime
import typing

import kubernetes.client

class V1alpha2ResourceClassParameters:
    api_version: typing.Optional[str]
    filters: typing.Optional[list[kubernetes.client.V1alpha2ResourceFilter]]
    generated_from: typing.Optional[kubernetes.client.V1alpha2ResourceClassParametersReference]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMeta]
    vendor_parameters: typing.Optional[list[kubernetes.client.V1alpha2VendorParameters]]
    
    def __init__(self, *, api_version: typing.Optional[str] = ..., filters: typing.Optional[list[kubernetes.client.V1alpha2ResourceFilter]] = ..., generated_from: typing.Optional[kubernetes.client.V1alpha2ResourceClassParametersReference] = ..., kind: typing.Optional[str] = ..., metadata: typing.Optional[kubernetes.client.V1ObjectMeta] = ..., vendor_parameters: typing.Optional[list[kubernetes.client.V1alpha2VendorParameters]] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha2ResourceClassParametersDict:
        ...
class V1alpha2ResourceClassParametersDict(typing.TypedDict, total=False):
    apiVersion: typing.Optional[str]
    filters: typing.Optional[list[kubernetes.client.V1alpha2ResourceFilterDict]]
    generatedFrom: typing.Optional[kubernetes.client.V1alpha2ResourceClassParametersReferenceDict]
    kind: typing.Optional[str]
    metadata: typing.Optional[kubernetes.client.V1ObjectMetaDict]
    vendorParameters: typing.Optional[list[kubernetes.client.V1alpha2VendorParametersDict]]
