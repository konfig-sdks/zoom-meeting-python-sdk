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


class MeetingsControlInMeetingFeaturesRequestParamsH323Headers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Enable customers to leverage services that require customization of the FROM header to identify the caller. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field and the `h323` value for the `call_type` field.
    """


    class MetaOapg:
        
        class properties:
            
            
            class from_display_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
            class to_display_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            __annotations__ = {
                "from_display_name": from_display_name,
                "to_display_name": to_display_name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_display_name"]) -> MetaOapg.properties.from_display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_display_name"]) -> MetaOapg.properties.to_display_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["from_display_name", "to_display_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_display_name"]) -> typing.Union[MetaOapg.properties.from_display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_display_name"]) -> typing.Union[MetaOapg.properties.to_display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from_display_name", "to_display_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        from_display_name: typing.Union[MetaOapg.properties.from_display_name, str, schemas.Unset] = schemas.unset,
        to_display_name: typing.Union[MetaOapg.properties.to_display_name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsControlInMeetingFeaturesRequestParamsH323Headers':
        return super().__new__(
            cls,
            *args,
            from_display_name=from_display_name,
            to_display_name=to_display_name,
            _configuration=_configuration,
            **kwargs,
        )
