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

from zoom_meeting_python_sdk.pydantic.reports_get_daily_usage_report_response_dates import ReportsGetDailyUsageReportResponseDates

class ReportsGetDailyUsageReportResponse(BaseModel):
    dates: typing.Optional[ReportsGetDailyUsageReportResponseDates] = Field(None, alias='dates')

    # Month for this report.
    month: typing.Optional[int] = Field(None, alias='month')

    # Year for this report.
    year: typing.Optional[int] = Field(None, alias='year')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
