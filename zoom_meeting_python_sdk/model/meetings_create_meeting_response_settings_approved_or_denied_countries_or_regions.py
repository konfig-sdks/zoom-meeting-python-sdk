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


class MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Approve or block users from specific regions or countries from joining this meeting. 

    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def approved_list() -> typing.Type['MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList']:
                return MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList
        
            @staticmethod
            def denied_list() -> typing.Type['MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList']:
                return MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList
            enable = schemas.BoolSchema
            
            
            class method(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "approve": "APPROVE",
                        "deny": "DENY",
                    }
                
                @schemas.classproperty
                def APPROVE(cls):
                    return cls("approve")
                
                @schemas.classproperty
                def DENY(cls):
                    return cls("deny")
            __annotations__ = {
                "approved_list": approved_list,
                "denied_list": denied_list,
                "enable": enable,
                "method": method,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved_list"]) -> 'MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["denied_list"]) -> 'MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable"]) -> MetaOapg.properties.enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["approved_list", "denied_list", "enable", "method", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved_list"]) -> typing.Union['MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["denied_list"]) -> typing.Union['MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable"]) -> typing.Union[MetaOapg.properties.enable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> typing.Union[MetaOapg.properties.method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["approved_list", "denied_list", "enable", "method", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        approved_list: typing.Union['MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList', schemas.Unset] = schemas.unset,
        denied_list: typing.Union['MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList', schemas.Unset] = schemas.unset,
        enable: typing.Union[MetaOapg.properties.enable, bool, schemas.Unset] = schemas.unset,
        method: typing.Union[MetaOapg.properties.method, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions':
        return super().__new__(
            cls,
            *args,
            approved_list=approved_list,
            denied_list=denied_list,
            enable=enable,
            method=method,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions_approved_list import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList
from zoom_meeting_python_sdk.model.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions_denied_list import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList
