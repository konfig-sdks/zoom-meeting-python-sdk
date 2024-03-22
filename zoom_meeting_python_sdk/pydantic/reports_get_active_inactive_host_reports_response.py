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

from zoom_meeting_python_sdk.pydantic.reports_get_active_inactive_host_reports_response_users import ReportsGetActiveInactiveHostReportsResponseUsers

class ReportsGetActiveInactiveHostReportsResponse(BaseModel):
    # Start date for this report.
    from_: typing.Optional[date] = Field(None, alias='from')

    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of pages returned for the request made.
    page_count: typing.Optional[int] = Field(None, alias='page_count')

    # The page number of the current results.
    page_number: typing.Optional[int] = Field(None, alias='page_number')

    # The number of records returned with a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # End date for this report.
    to: typing.Optional[date] = Field(None, alias='to')

    # The total number of all the records available across pages.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    # Number of meeting minutes for this range.
    total_meeting_minutes: typing.Optional[int] = Field(None, alias='total_meeting_minutes')

    # Number of meetings for this range.
    total_meetings: typing.Optional[int] = Field(None, alias='total_meetings')

    # Number of participants for this range.
    total_participants: typing.Optional[int] = Field(None, alias='total_participants')

    users: typing.Optional[ReportsGetActiveInactiveHostReportsResponseUsers] = Field(None, alias='users')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
