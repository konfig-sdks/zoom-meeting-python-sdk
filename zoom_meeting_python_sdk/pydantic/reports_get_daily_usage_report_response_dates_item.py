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


class ReportsGetDailyUsageReportResponseDatesItem(BaseModel):
    # Date for this object.
    date: typing.Optional[date] = Field(None, alias='date')

    # Number of meeting minutes on this date.
    meeting_minutes: typing.Optional[int] = Field(None, alias='meeting_minutes')

    # Number of meetings on this date.
    meetings: typing.Optional[int] = Field(None, alias='meetings')

    # Number of new users on this date.
    new_users: typing.Optional[int] = Field(None, alias='new_users')

    # Number of participants on this date.
    participants: typing.Optional[int] = Field(None, alias='participants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
