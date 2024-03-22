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


class WebinarsListTrackingSourcesResponseTrackingSourcesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            registration_count = schemas.IntSchema
            source_name = schemas.StrSchema
            tracking_url = schemas.StrSchema
            visitor_count = schemas.IntSchema
            __annotations__ = {
                "id": id,
                "registration_count": registration_count,
                "source_name": source_name,
                "tracking_url": tracking_url,
                "visitor_count": visitor_count,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_count"]) -> MetaOapg.properties.registration_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_name"]) -> MetaOapg.properties.source_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tracking_url"]) -> MetaOapg.properties.tracking_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visitor_count"]) -> MetaOapg.properties.visitor_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "registration_count", "source_name", "tracking_url", "visitor_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_count"]) -> typing.Union[MetaOapg.properties.registration_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_name"]) -> typing.Union[MetaOapg.properties.source_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tracking_url"]) -> typing.Union[MetaOapg.properties.tracking_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visitor_count"]) -> typing.Union[MetaOapg.properties.visitor_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "registration_count", "source_name", "tracking_url", "visitor_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        registration_count: typing.Union[MetaOapg.properties.registration_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        source_name: typing.Union[MetaOapg.properties.source_name, str, schemas.Unset] = schemas.unset,
        tracking_url: typing.Union[MetaOapg.properties.tracking_url, str, schemas.Unset] = schemas.unset,
        visitor_count: typing.Union[MetaOapg.properties.visitor_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsListTrackingSourcesResponseTrackingSourcesItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            registration_count=registration_count,
            source_name=source_name,
            tracking_url=tracking_url,
            visitor_count=visitor_count,
            _configuration=_configuration,
            **kwargs,
        )
