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


class WebinarsListWebinarsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    List of webinars.
    """


    class MetaOapg:
        
        class properties:
            next_page_token = schemas.StrSchema
            page_count = schemas.IntSchema
            page_number = schemas.IntSchema
            
            
            class page_size(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 300
            total_records = schemas.IntSchema
        
            @staticmethod
            def webinars() -> typing.Type['WebinarsListWebinarsResponseWebinars']:
                return WebinarsListWebinarsResponseWebinars
            __annotations__ = {
                "next_page_token": next_page_token,
                "page_count": page_count,
                "page_number": page_number,
                "page_size": page_size,
                "total_records": total_records,
                "webinars": webinars,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_page_token"]) -> MetaOapg.properties.next_page_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_count"]) -> MetaOapg.properties.page_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_number"]) -> MetaOapg.properties.page_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_records"]) -> MetaOapg.properties.total_records: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webinars"]) -> 'WebinarsListWebinarsResponseWebinars': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["next_page_token", "page_count", "page_number", "page_size", "total_records", "webinars", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_page_token"]) -> typing.Union[MetaOapg.properties.next_page_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_count"]) -> typing.Union[MetaOapg.properties.page_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_number"]) -> typing.Union[MetaOapg.properties.page_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_size"]) -> typing.Union[MetaOapg.properties.page_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_records"]) -> typing.Union[MetaOapg.properties.total_records, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webinars"]) -> typing.Union['WebinarsListWebinarsResponseWebinars', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next_page_token", "page_count", "page_number", "page_size", "total_records", "webinars", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        next_page_token: typing.Union[MetaOapg.properties.next_page_token, str, schemas.Unset] = schemas.unset,
        page_count: typing.Union[MetaOapg.properties.page_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page_number: typing.Union[MetaOapg.properties.page_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page_size: typing.Union[MetaOapg.properties.page_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_records: typing.Union[MetaOapg.properties.total_records, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        webinars: typing.Union['WebinarsListWebinarsResponseWebinars', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsListWebinarsResponse':
        return super().__new__(
            cls,
            *args,
            next_page_token=next_page_token,
            page_count=page_count,
            page_number=page_number,
            page_size=page_size,
            total_records=total_records,
            webinars=webinars,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.webinars_list_webinars_response_webinars import WebinarsListWebinarsResponseWebinars
