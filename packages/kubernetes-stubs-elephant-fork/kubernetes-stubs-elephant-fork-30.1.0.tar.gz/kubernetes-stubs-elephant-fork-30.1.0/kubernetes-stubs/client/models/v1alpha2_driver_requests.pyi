import datetime
import typing

import kubernetes.client

class V1alpha2DriverRequests:
    driver_name: typing.Optional[str]
    requests: typing.Optional[list[kubernetes.client.V1alpha2ResourceRequest]]
    vendor_parameters: typing.Optional[typing.Any]
    
    def __init__(self, *, driver_name: typing.Optional[str] = ..., requests: typing.Optional[list[kubernetes.client.V1alpha2ResourceRequest]] = ..., vendor_parameters: typing.Optional[typing.Any] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha2DriverRequestsDict:
        ...
class V1alpha2DriverRequestsDict(typing.TypedDict, total=False):
    driverName: typing.Optional[str]
    requests: typing.Optional[list[kubernetes.client.V1alpha2ResourceRequestDict]]
    vendorParameters: typing.Optional[typing.Any]
