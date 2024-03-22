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


class WebinarsUpdateScheduledWebinarRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Webinar object.
    """


    class MetaOapg:
        
        class properties:
            agenda = schemas.StrSchema
            duration = schemas.IntSchema
            
            
            class password(
                schemas.StrSchema
            ):
                pass
            schedule_for = schemas.StrSchema
        
            @staticmethod
            def recurrence() -> typing.Type['WebinarsUpdateScheduledWebinarRequestRecurrence']:
                return WebinarsUpdateScheduledWebinarRequestRecurrence
        
            @staticmethod
            def settings() -> typing.Type['WebinarsUpdateScheduledWebinarRequestSettings']:
                return WebinarsUpdateScheduledWebinarRequestSettings
            start_time = schemas.DateTimeSchema
            timezone = schemas.StrSchema
            topic = schemas.StrSchema
        
            @staticmethod
            def tracking_fields() -> typing.Type['WebinarsUpdateScheduledWebinarRequestTrackingFields']:
                return WebinarsUpdateScheduledWebinarRequestTrackingFields
            
            
            class type(
                schemas.EnumBase,
                schemas.IntSchema
            ):
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls(5)
                
                @schemas.classproperty
                def POSITIVE_6(cls):
                    return cls(6)
                
                @schemas.classproperty
                def POSITIVE_9(cls):
                    return cls(9)
            is_simulive = schemas.BoolSchema
            record_file_id = schemas.StrSchema
            __annotations__ = {
                "agenda": agenda,
                "duration": duration,
                "password": password,
                "schedule_for": schedule_for,
                "recurrence": recurrence,
                "settings": settings,
                "start_time": start_time,
                "timezone": timezone,
                "topic": topic,
                "tracking_fields": tracking_fields,
                "type": type,
                "is_simulive": is_simulive,
                "record_file_id": record_file_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agenda"]) -> MetaOapg.properties.agenda: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule_for"]) -> MetaOapg.properties.schedule_for: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurrence"]) -> 'WebinarsUpdateScheduledWebinarRequestRecurrence': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'WebinarsUpdateScheduledWebinarRequestSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic"]) -> MetaOapg.properties.topic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tracking_fields"]) -> 'WebinarsUpdateScheduledWebinarRequestTrackingFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_simulive"]) -> MetaOapg.properties.is_simulive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["record_file_id"]) -> MetaOapg.properties.record_file_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["agenda", "duration", "password", "schedule_for", "recurrence", "settings", "start_time", "timezone", "topic", "tracking_fields", "type", "is_simulive", "record_file_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agenda"]) -> typing.Union[MetaOapg.properties.agenda, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule_for"]) -> typing.Union[MetaOapg.properties.schedule_for, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurrence"]) -> typing.Union['WebinarsUpdateScheduledWebinarRequestRecurrence', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['WebinarsUpdateScheduledWebinarRequestSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic"]) -> typing.Union[MetaOapg.properties.topic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tracking_fields"]) -> typing.Union['WebinarsUpdateScheduledWebinarRequestTrackingFields', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_simulive"]) -> typing.Union[MetaOapg.properties.is_simulive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["record_file_id"]) -> typing.Union[MetaOapg.properties.record_file_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["agenda", "duration", "password", "schedule_for", "recurrence", "settings", "start_time", "timezone", "topic", "tracking_fields", "type", "is_simulive", "record_file_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        agenda: typing.Union[MetaOapg.properties.agenda, str, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        schedule_for: typing.Union[MetaOapg.properties.schedule_for, str, schemas.Unset] = schemas.unset,
        recurrence: typing.Union['WebinarsUpdateScheduledWebinarRequestRecurrence', schemas.Unset] = schemas.unset,
        settings: typing.Union['WebinarsUpdateScheduledWebinarRequestSettings', schemas.Unset] = schemas.unset,
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        topic: typing.Union[MetaOapg.properties.topic, str, schemas.Unset] = schemas.unset,
        tracking_fields: typing.Union['WebinarsUpdateScheduledWebinarRequestTrackingFields', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_simulive: typing.Union[MetaOapg.properties.is_simulive, bool, schemas.Unset] = schemas.unset,
        record_file_id: typing.Union[MetaOapg.properties.record_file_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsUpdateScheduledWebinarRequest':
        return super().__new__(
            cls,
            *args,
            agenda=agenda,
            duration=duration,
            password=password,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            is_simulive=is_simulive,
            record_file_id=record_file_id,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.webinars_update_scheduled_webinar_request_recurrence import WebinarsUpdateScheduledWebinarRequestRecurrence
from zoom_meeting_python_sdk.model.webinars_update_scheduled_webinar_request_settings import WebinarsUpdateScheduledWebinarRequestSettings
from zoom_meeting_python_sdk.model.webinars_update_scheduled_webinar_request_tracking_fields import WebinarsUpdateScheduledWebinarRequestTrackingFields
