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


class RequiredReportsGetDailyUsageReportResponseDatesItem(TypedDict):
    pass

class OptionalReportsGetDailyUsageReportResponseDatesItem(TypedDict, total=False):
    # Date for this object.
    date: date

    # Number of meeting minutes on this date.
    meeting_minutes: int

    # Number of meetings on this date.
    meetings: int

    # Number of new users on this date.
    new_users: int

    # Number of participants on this date.
    participants: int

class ReportsGetDailyUsageReportResponseDatesItem(RequiredReportsGetDailyUsageReportResponseDatesItem, OptionalReportsGetDailyUsageReportResponseDatesItem):
    pass
