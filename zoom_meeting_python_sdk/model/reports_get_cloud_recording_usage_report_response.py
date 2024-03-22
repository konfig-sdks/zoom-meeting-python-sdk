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


class ReportsGetCloudRecordingUsageReportResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            _from = schemas.DateSchema
            to = schemas.DateSchema
        
            @staticmethod
            def cloud_recording_storage() -> typing.Type['ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage']:
                return ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage
            __annotations__ = {
                "from": _from,
                "to": to,
                "cloud_recording_storage": cloud_recording_storage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloud_recording_storage"]) -> 'ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["from", "to", "cloud_recording_storage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> typing.Union[MetaOapg.properties._from, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> typing.Union[MetaOapg.properties.to, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloud_recording_storage"]) -> typing.Union['ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from", "to", "cloud_recording_storage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        to: typing.Union[MetaOapg.properties.to, str, date, schemas.Unset] = schemas.unset,
        cloud_recording_storage: typing.Union['ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetCloudRecordingUsageReportResponse':
        return super().__new__(
            cls,
            *args,
            to=to,
            cloud_recording_storage=cloud_recording_storage,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.reports_get_cloud_recording_usage_report_response_cloud_recording_storage import ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage
