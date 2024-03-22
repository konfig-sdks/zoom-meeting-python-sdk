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

from zoom_meeting_python_sdk.pydantic.reports_list_upcoming_events_report_response_upcoming_events import ReportsListUpcomingEventsReportResponseUpcomingEvents

class ReportsListUpcomingEventsReportResponse(BaseModel):
    # The report's start date. This value must be within the past six months.
    from_: typing.Optional[date] = Field(None, alias='from')

    # The next page token is used to paginate through large result sets. A next page token returns when the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of records returned in a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # The report's end date. This value must be within the past six months and cannot exceed a month from the `from` value.
    to: typing.Optional[date] = Field(None, alias='to')

    upcoming_events: typing.Optional[ReportsListUpcomingEventsReportResponseUpcomingEvents] = Field(None, alias='upcoming_events')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
