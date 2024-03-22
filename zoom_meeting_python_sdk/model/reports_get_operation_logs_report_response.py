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


class ReportsGetOperationLogsReportResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Pagination object.
    """


    class MetaOapg:
        
        class properties:
            next_page_token = schemas.StrSchema
            
            
            class page_size(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 300
        
            @staticmethod
            def operation_logs() -> typing.Type['ReportsGetOperationLogsReportResponseOperationLogs']:
                return ReportsGetOperationLogsReportResponseOperationLogs
            __annotations__ = {
                "next_page_token": next_page_token,
                "page_size": page_size,
                "operation_logs": operation_logs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_page_token"]) -> MetaOapg.properties.next_page_token: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operation_logs"]) -> 'ReportsGetOperationLogsReportResponseOperationLogs': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["next_page_token", "page_size", "operation_logs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_page_token"]) -> typing.Union[MetaOapg.properties.next_page_token, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_size"]) -> typing.Union[MetaOapg.properties.page_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operation_logs"]) -> typing.Union['ReportsGetOperationLogsReportResponseOperationLogs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["next_page_token", "page_size", "operation_logs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        next_page_token: typing.Union[MetaOapg.properties.next_page_token, str, schemas.Unset] = schemas.unset,
        page_size: typing.Union[MetaOapg.properties.page_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        operation_logs: typing.Union['ReportsGetOperationLogsReportResponseOperationLogs', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetOperationLogsReportResponse':
        return super().__new__(
            cls,
            *args,
            next_page_token=next_page_token,
            page_size=page_size,
            operation_logs=operation_logs,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.reports_get_operation_logs_report_response_operation_logs import ReportsGetOperationLogsReportResponseOperationLogs
