import datetime
import typing

import kubernetes.client

class V1alpha2DriverAllocationResult:
    named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesAllocationResult]
    vendor_request_parameters: typing.Optional[typing.Any]
    
    def __init__(self, *, named_resources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesAllocationResult] = ..., vendor_request_parameters: typing.Optional[typing.Any] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha2DriverAllocationResultDict:
        ...
class V1alpha2DriverAllocationResultDict(typing.TypedDict, total=False):
    namedResources: typing.Optional[kubernetes.client.V1alpha2NamedResourcesAllocationResultDict]
    vendorRequestParameters: typing.Optional[typing.Any]
