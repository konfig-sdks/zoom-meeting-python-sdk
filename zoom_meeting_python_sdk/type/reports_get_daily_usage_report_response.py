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

from zoom_meeting_python_sdk.type.reports_get_daily_usage_report_response_dates import ReportsGetDailyUsageReportResponseDates

class RequiredReportsGetDailyUsageReportResponse(TypedDict):
    pass

class OptionalReportsGetDailyUsageReportResponse(TypedDict, total=False):
    dates: ReportsGetDailyUsageReportResponseDates

    # Month for this report.
    month: int

    # Year for this report.
    year: int

class ReportsGetDailyUsageReportResponse(RequiredReportsGetDailyUsageReportResponse, OptionalReportsGetDailyUsageReportResponse):
    pass
