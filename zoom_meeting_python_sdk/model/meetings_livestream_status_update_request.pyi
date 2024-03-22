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


class MeetingsLivestreamStatusUpdateRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Meeting live stream status.
    """


    class MetaOapg:
        
        class properties:
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def START(cls):
                    return cls("start")
                
                @schemas.classproperty
                def STOP(cls):
                    return cls("stop")
        
            @staticmethod
            def settings() -> typing.Type['MeetingsLivestreamStatusUpdateRequestSettings']:
                return MeetingsLivestreamStatusUpdateRequestSettings
            __annotations__ = {
                "action": action,
                "settings": settings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'MeetingsLivestreamStatusUpdateRequestSettings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["action", "settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['MeetingsLivestreamStatusUpdateRequestSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["action", "settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        settings: typing.Union['MeetingsLivestreamStatusUpdateRequestSettings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsLivestreamStatusUpdateRequest':
        return super().__new__(
            cls,
            *args,
            action=action,
            settings=settings,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_livestream_status_update_request_settings import MeetingsLivestreamStatusUpdateRequestSettings
