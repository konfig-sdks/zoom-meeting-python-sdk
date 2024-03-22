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


class DevicesGetDetailResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the device.
    """


    class MetaOapg:
        
        class properties:
            device_id = schemas.StrSchema
            device_name = schemas.StrSchema
            mac_address = schemas.StrSchema
            serial_number = schemas.StrSchema
            vendor = schemas.StrSchema
            model = schemas.StrSchema
            platform_os = schemas.StrSchema
            app_version = schemas.StrSchema
            tag = schemas.StrSchema
            enrolled_in_zdm = schemas.BoolSchema
            connected_to_zdm = schemas.BoolSchema
            room_id = schemas.StrSchema
            room_name = schemas.StrSchema
            
            
            class device_type(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        0: "POSITIVE_0",
                        1: "POSITIVE_1",
                        2: "POSITIVE_2",
                        3: "POSITIVE_3",
                        4: "POSITIVE_4",
                        5: "POSITIVE_5",
                        6: "POSITIVE_6",
                    }
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls(5)
                
                @schemas.classproperty
                def POSITIVE_6(cls):
                    return cls(6)
            sdk_version = schemas.StrSchema
            
            
            class device_status(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        -1: "NEGATIVE_1",
                        0: "POSITIVE_0",
                        1: "POSITIVE_1",
                    }
                
                @schemas.classproperty
                def NEGATIVE_1(cls):
                    return cls(-1)
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
            last_online = schemas.StrSchema
            user_email = schemas.StrSchema
            __annotations__ = {
                "device_id": device_id,
                "device_name": device_name,
                "mac_address": mac_address,
                "serial_number": serial_number,
                "vendor": vendor,
                "model": model,
                "platform_os": platform_os,
                "app_version": app_version,
                "tag": tag,
                "enrolled_in_zdm": enrolled_in_zdm,
                "connected_to_zdm": connected_to_zdm,
                "room_id": room_id,
                "room_name": room_name,
                "device_type": device_type,
                "sdk_version": sdk_version,
                "device_status": device_status,
                "last_online": last_online,
                "user_email": user_email,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["platform_os"]) -> MetaOapg.properties.platform_os: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_version"]) -> MetaOapg.properties.app_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enrolled_in_zdm"]) -> MetaOapg.properties.enrolled_in_zdm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connected_to_zdm"]) -> MetaOapg.properties.connected_to_zdm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["room_id"]) -> MetaOapg.properties.room_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["room_name"]) -> MetaOapg.properties.room_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sdk_version"]) -> MetaOapg.properties.sdk_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_status"]) -> MetaOapg.properties.device_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_online"]) -> MetaOapg.properties.last_online: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "device_name", "mac_address", "serial_number", "vendor", "model", "platform_os", "app_version", "tag", "enrolled_in_zdm", "connected_to_zdm", "room_id", "room_name", "device_type", "sdk_version", "device_status", "last_online", "user_email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> typing.Union[MetaOapg.properties.device_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mac_address"]) -> typing.Union[MetaOapg.properties.mac_address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serial_number"]) -> typing.Union[MetaOapg.properties.serial_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor"]) -> typing.Union[MetaOapg.properties.vendor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> typing.Union[MetaOapg.properties.model, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform_os"]) -> typing.Union[MetaOapg.properties.platform_os, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_version"]) -> typing.Union[MetaOapg.properties.app_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enrolled_in_zdm"]) -> typing.Union[MetaOapg.properties.enrolled_in_zdm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connected_to_zdm"]) -> typing.Union[MetaOapg.properties.connected_to_zdm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["room_id"]) -> typing.Union[MetaOapg.properties.room_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["room_name"]) -> typing.Union[MetaOapg.properties.room_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_type"]) -> typing.Union[MetaOapg.properties.device_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sdk_version"]) -> typing.Union[MetaOapg.properties.sdk_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_status"]) -> typing.Union[MetaOapg.properties.device_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_online"]) -> typing.Union[MetaOapg.properties.last_online, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_email"]) -> typing.Union[MetaOapg.properties.user_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "device_name", "mac_address", "serial_number", "vendor", "model", "platform_os", "app_version", "tag", "enrolled_in_zdm", "connected_to_zdm", "room_id", "room_name", "device_type", "sdk_version", "device_status", "last_online", "user_email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        device_id: typing.Union[MetaOapg.properties.device_id, str, schemas.Unset] = schemas.unset,
        device_name: typing.Union[MetaOapg.properties.device_name, str, schemas.Unset] = schemas.unset,
        mac_address: typing.Union[MetaOapg.properties.mac_address, str, schemas.Unset] = schemas.unset,
        serial_number: typing.Union[MetaOapg.properties.serial_number, str, schemas.Unset] = schemas.unset,
        vendor: typing.Union[MetaOapg.properties.vendor, str, schemas.Unset] = schemas.unset,
        model: typing.Union[MetaOapg.properties.model, str, schemas.Unset] = schemas.unset,
        platform_os: typing.Union[MetaOapg.properties.platform_os, str, schemas.Unset] = schemas.unset,
        app_version: typing.Union[MetaOapg.properties.app_version, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        enrolled_in_zdm: typing.Union[MetaOapg.properties.enrolled_in_zdm, bool, schemas.Unset] = schemas.unset,
        connected_to_zdm: typing.Union[MetaOapg.properties.connected_to_zdm, bool, schemas.Unset] = schemas.unset,
        room_id: typing.Union[MetaOapg.properties.room_id, str, schemas.Unset] = schemas.unset,
        room_name: typing.Union[MetaOapg.properties.room_name, str, schemas.Unset] = schemas.unset,
        device_type: typing.Union[MetaOapg.properties.device_type, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sdk_version: typing.Union[MetaOapg.properties.sdk_version, str, schemas.Unset] = schemas.unset,
        device_status: typing.Union[MetaOapg.properties.device_status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_online: typing.Union[MetaOapg.properties.last_online, str, schemas.Unset] = schemas.unset,
        user_email: typing.Union[MetaOapg.properties.user_email, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DevicesGetDetailResponse':
        return super().__new__(
            cls,
            *args,
            device_id=device_id,
            device_name=device_name,
            mac_address=mac_address,
            serial_number=serial_number,
            vendor=vendor,
            model=model,
            platform_os=platform_os,
            app_version=app_version,
            tag=tag,
            enrolled_in_zdm=enrolled_in_zdm,
            connected_to_zdm=connected_to_zdm,
            room_id=room_id,
            room_name=room_name,
            device_type=device_type,
            sdk_version=sdk_version,
            device_status=device_status,
            last_online=last_online,
            user_email=user_email,
            _configuration=_configuration,
            **kwargs,
        )
