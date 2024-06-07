import datetime
import typing

import kubernetes.client

class V1alpha2VendorParameters:
    driver_name: typing.Optional[str]
    parameters: typing.Optional[typing.Any]
    
    def __init__(self, *, driver_name: typing.Optional[str] = ..., parameters: typing.Optional[typing.Any] = ...) -> None:
        ...
    def to_dict(self) -> V1alpha2VendorParametersDict:
        ...
class V1alpha2VendorParametersDict(typing.TypedDict, total=False):
    driverName: typing.Optional[str]
    parameters: typing.Optional[typing.Any]
