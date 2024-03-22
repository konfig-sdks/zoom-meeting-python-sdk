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


class MeetingsUpdateDetailsRequestSettingsResourcesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class resource_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WHITEBOARD(cls):
                    return cls("whiteboard")
            resource_id = schemas.StrSchema
            
            
            class permission_level(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EDITOR(cls):
                    return cls("editor")
                
                @schemas.classproperty
                def COMMENTER(cls):
                    return cls("commenter")
                
                @schemas.classproperty
                def VIEWER(cls):
                    return cls("viewer")
            __annotations__ = {
                "resource_type": resource_type,
                "resource_id": resource_id,
                "permission_level": permission_level,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_id"]) -> MetaOapg.properties.resource_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["permission_level"]) -> MetaOapg.properties.permission_level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "resource_id", "permission_level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> typing.Union[MetaOapg.properties.resource_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_id"]) -> typing.Union[MetaOapg.properties.resource_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["permission_level"]) -> typing.Union[MetaOapg.properties.permission_level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "resource_id", "permission_level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        resource_type: typing.Union[MetaOapg.properties.resource_type, str, schemas.Unset] = schemas.unset,
        resource_id: typing.Union[MetaOapg.properties.resource_id, str, schemas.Unset] = schemas.unset,
        permission_level: typing.Union[MetaOapg.properties.permission_level, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsUpdateDetailsRequestSettingsResourcesItem':
        return super().__new__(
            cls,
            *args,
            resource_type=resource_type,
            resource_id=resource_id,
            permission_level=permission_level,
            _configuration=_configuration,
            **kwargs,
        )
