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


class WebinarsGetDetailsResponseOccurrencesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Occurrence object. This object is only returned for recurring webinars.
    """


    class MetaOapg:
        
        class properties:
            duration = schemas.IntSchema
            occurrence_id = schemas.StrSchema
            start_time = schemas.DateTimeSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "available": "AVAILABLE",
                        "deleted": "DELETED",
                    }
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("available")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("deleted")
            __annotations__ = {
                "duration": duration,
                "occurrence_id": occurrence_id,
                "start_time": start_time,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["occurrence_id"]) -> MetaOapg.properties.occurrence_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["duration", "occurrence_id", "start_time", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["occurrence_id"]) -> typing.Union[MetaOapg.properties.occurrence_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["duration", "occurrence_id", "start_time", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        occurrence_id: typing.Union[MetaOapg.properties.occurrence_id, str, schemas.Unset] = schemas.unset,
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsGetDetailsResponseOccurrencesItem':
        return super().__new__(
            cls,
            *args,
            duration=duration,
            occurrence_id=occurrence_id,
            start_time=start_time,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
