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


class ReportsGetOperationLogsReportResponseOperationLogsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            action = schemas.StrSchema
            category_type = schemas.StrSchema
            operation_detail = schemas.StrSchema
            operator = schemas.StrSchema
            time = schemas.DateTimeSchema
            __annotations__ = {
                "action": action,
                "category_type": category_type,
                "operation_detail": operation_detail,
                "operator": operator,
                "time": time,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_type"]) -> MetaOapg.properties.category_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operation_detail"]) -> MetaOapg.properties.operation_detail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["time"]) -> MetaOapg.properties.time: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["action", "category_type", "operation_detail", "operator", "time", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_type"]) -> typing.Union[MetaOapg.properties.category_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operation_detail"]) -> typing.Union[MetaOapg.properties.operation_detail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["time"]) -> typing.Union[MetaOapg.properties.time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["action", "category_type", "operation_detail", "operator", "time", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        category_type: typing.Union[MetaOapg.properties.category_type, str, schemas.Unset] = schemas.unset,
        operation_detail: typing.Union[MetaOapg.properties.operation_detail, str, schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        time: typing.Union[MetaOapg.properties.time, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetOperationLogsReportResponseOperationLogsItem':
        return super().__new__(
            cls,
            *args,
            action=action,
            category_type=category_type,
            operation_detail=operation_detail,
            operator=operator,
            time=time,
            _configuration=_configuration,
            **kwargs,
        )
