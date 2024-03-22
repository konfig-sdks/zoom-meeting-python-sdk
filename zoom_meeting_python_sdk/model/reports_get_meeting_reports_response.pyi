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


class ReportsGetMeetingReportsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Pagination Object.
    """


    class MetaOapg:
        
        class properties:
            next_page_token = schemas.StrSchema
            page_count = schemas.IntSchema
            page_number = schemas.IntSchema
            
            
            class page_size(
                schemas.IntSchema
            ):
                pass
            total_records = schemas.IntSchema
            _from = schemas.DateSchema
        
            @staticmethod
            def meetings() -> typing.Type['ReportsGetMeetingReportsResponseMeetings']:
                return ReportsGetMeetingReportsResponseMeetings
            to = schemas.DateSchema
            __annotations__ = {
                "next_page_token": next_page_token,
                "page_count": page_count,
                "page_number": page_number,
                "page_size": page_size,
                "total_records": total_records,
                "from": _from,
                "meetings": meetings,
                "to": to,
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
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meetings"]) -> 'ReportsGetMeetingReportsResponseMeetings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["next_page_token", "page_count", "page_number", "page_size", "total_records", "from", "meetings", "to", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meetings"]) -> typing.Union['ReportsGetMeetingReportsResponseMeetings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next_page_token", "page_count", "page_number", "page_size", "total_records", "from", "meetings", "to", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        next_page_token: typing.Union[MetaOapg.properties.next_page_token, str, schemas.Unset] = schemas.unset,
        page_count: typing.Union[MetaOapg.properties.page_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page_number: typing.Union[MetaOapg.properties.page_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page_size: typing.Union[MetaOapg.properties.page_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_records: typing.Union[MetaOapg.properties.total_records, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        meetings: typing.Union['ReportsGetMeetingReportsResponseMeetings', schemas.Unset] = schemas.unset,
        to: typing.Union[MetaOapg.properties.to, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetMeetingReportsResponse':
        return super().__new__(
            cls,
            *args,
            next_page_token=next_page_token,
            page_count=page_count,
            page_number=page_number,
            page_size=page_size,
            total_records=total_records,
            meetings=meetings,
            to=to,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.reports_get_meeting_reports_response_meetings import ReportsGetMeetingReportsResponseMeetings
