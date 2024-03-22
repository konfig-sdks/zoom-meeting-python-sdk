# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from zoom_meeting_python_sdk.pydantic.reports_get_cloud_recording_usage_report_response_cloud_recording_storage import ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage

class ReportsGetCloudRecordingUsageReportResponse(BaseModel):
    # Start date for this report
    from_: typing.Optional[date] = Field(None, alias='from')

    # End date for this report
    to: typing.Optional[date] = Field(None, alias='to')

    cloud_recording_storage: typing.Optional[ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage] = Field(None, alias='cloud_recording_storage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
