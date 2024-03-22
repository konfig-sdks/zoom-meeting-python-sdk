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


class RequiredReportsGetCloudRecordingUsageReportResponseCloudRecordingStorageItem(TypedDict):
    pass

class OptionalReportsGetCloudRecordingUsageReportResponseCloudRecordingStorageItem(TypedDict, total=False):
    # Date of the usage
    date: date

    # Free storage
    free_usage: str

    # Paid storage
    plan_usage: str

    # Storage used on the date
    usage: str

class ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorageItem(RequiredReportsGetCloudRecordingUsageReportResponseCloudRecordingStorageItem, OptionalReportsGetCloudRecordingUsageReportResponseCloudRecordingStorageItem):
    pass
