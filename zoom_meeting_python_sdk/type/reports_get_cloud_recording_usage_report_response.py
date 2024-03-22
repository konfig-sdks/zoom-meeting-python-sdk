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

from zoom_meeting_python_sdk.type.reports_get_cloud_recording_usage_report_response_cloud_recording_storage import ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage

RequiredReportsGetCloudRecordingUsageReportResponse = TypedDict("RequiredReportsGetCloudRecordingUsageReportResponse", {
    })

OptionalReportsGetCloudRecordingUsageReportResponse = TypedDict("OptionalReportsGetCloudRecordingUsageReportResponse", {
    # Start date for this report
    "from": date,

    # End date for this report
    "to": date,

    "cloud_recording_storage": ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorage,
    }, total=False)

class ReportsGetCloudRecordingUsageReportResponse(RequiredReportsGetCloudRecordingUsageReportResponse, OptionalReportsGetCloudRecordingUsageReportResponse):
    pass
