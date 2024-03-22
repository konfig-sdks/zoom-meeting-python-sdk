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


class DevicesCreateNewDeviceRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "device_name",
            "mac_address",
            "vendor",
            "device_type",
            "model",
            "serial_number",
        }
        
        class properties:
            device_name = schemas.StrSchema
            mac_address = schemas.StrSchema
            serial_number = schemas.StrSchema
            vendor = schemas.StrSchema
            model = schemas.StrSchema
            
            
            class device_type(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        0: "POSITIVE_0",
                        1: "POSITIVE_1",
                        5: "POSITIVE_5",
                    }
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls(5)
            room_id = schemas.StrSchema
            user_email = schemas.StrSchema
            tag = schemas.StrSchema
            zdm_group_id = schemas.StrSchema
            extension_number = schemas.StrSchema
            __annotations__ = {
                "device_name": device_name,
                "mac_address": mac_address,
                "serial_number": serial_number,
                "vendor": vendor,
                "model": model,
                "device_type": device_type,
                "room_id": room_id,
                "user_email": user_email,
                "tag": tag,
                "zdm_group_id": zdm_group_id,
                "extension_number": extension_number,
            }
    
    device_name: MetaOapg.properties.device_name
    mac_address: MetaOapg.properties.mac_address
    vendor: MetaOapg.properties.vendor
    device_type: MetaOapg.properties.device_type
    model: MetaOapg.properties.model
    serial_number: MetaOapg.properties.serial_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serial_number"]) -> MetaOapg.properties.serial_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor"]) -> MetaOapg.properties.vendor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["room_id"]) -> MetaOapg.properties.room_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zdm_group_id"]) -> MetaOapg.properties.zdm_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extension_number"]) -> MetaOapg.properties.extension_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_name", "mac_address", "serial_number", "vendor", "model", "device_type", "room_id", "user_email", "tag", "zdm_group_id", "extension_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> MetaOapg.properties.mac_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial_number"]) -> MetaOapg.properties.serial_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor"]) -> MetaOapg.properties.vendor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["room_id"]) -> typing.Union[MetaOapg.properties.room_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_email"]) -> typing.Union[MetaOapg.properties.user_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zdm_group_id"]) -> typing.Union[MetaOapg.properties.zdm_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extension_number"]) -> typing.Union[MetaOapg.properties.extension_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_name", "mac_address", "serial_number", "vendor", "model", "device_type", "room_id", "user_email", "tag", "zdm_group_id", "extension_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        device_name: typing.Union[MetaOapg.properties.device_name, str, ],
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, ],
        vendor: typing.Union[MetaOapg.properties.vendor, str, ],
        device_type: typing.Union[MetaOapg.properties.device_type, decimal.Decimal, int, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        serial_number: typing.Union[MetaOapg.properties.serial_number, str, ],
        room_id: typing.Union[MetaOapg.properties.room_id, str, schemas.Unset] = schemas.unset,
        user_email: typing.Union[MetaOapg.properties.user_email, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        zdm_group_id: typing.Union[MetaOapg.properties.zdm_group_id, str, schemas.Unset] = schemas.unset,
        extension_number: typing.Union[MetaOapg.properties.extension_number, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DevicesCreateNewDeviceRequest':
        return super().__new__(
            cls,
            *args,
            device_name=device_name,
            mac_address=mac_address,
            vendor=vendor,
            device_type=device_type,
            model=model,
            serial_number=serial_number,
            room_id=room_id,
            user_email=user_email,
            tag=tag,
            zdm_group_id=zdm_group_id,
            extension_number=extension_number,
            _configuration=_configuration,
            **kwargs,
        )
