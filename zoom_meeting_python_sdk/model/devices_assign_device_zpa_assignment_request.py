# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zoom_meeting_python_sdk import schemas  # noqa: F401


class DevicesAssignDeviceZpaAssignmentRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "mac_address",
            "vendor",
        }
        
        class properties:
            mac_address = schemas.StrSchema
            vendor = schemas.StrSchema
            extension_number = schemas.StrSchema
            __annotations__ = {
                "mac_address": mac_address,
                "vendor": vendor,
                "extension_number": extension_number,
            }
    
    mac_address: MetaOapg.properties.mac_address
    vendor: MetaOapg.properties.vendor
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor"]) -> MetaOapg.properties.vendor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension_number"]) -> MetaOapg.properties.extension_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mac_address", "vendor", "extension_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor"]) -> MetaOapg.properties.vendor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension_number"]) -> typing.Union[MetaOapg.properties.extension_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mac_address", "vendor", "extension_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, ],
        vendor: typing.Union[MetaOapg.properties.vendor, str, ],
        extension_number: typing.Union[MetaOapg.properties.extension_number, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DevicesAssignDeviceZpaAssignmentRequest':
        return super().__new__(
            cls,
            *args,
            mac_address=mac_address,
            vendor=vendor,
            extension_number=extension_number,
            _configuration=_configuration,
            **kwargs,
        )
