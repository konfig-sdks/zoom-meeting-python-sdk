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

from zoom_meeting_python_sdk.pydantic.meetings_list_host_scheduled_response_meetings import MeetingsListHostScheduledResponseMeetings

class MeetingsListHostScheduledResponse(BaseModel):
    # Use the next page token to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of pages returned for the request made.
    page_count: typing.Optional[int] = Field(None, alias='page_count')

    # The page number of the current results.
    page_number: typing.Optional[int] = Field(None, alias='page_number')

    # The number of records returned with a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # The total number of all the records available across pages.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    meetings: typing.Optional[MeetingsListHostScheduledResponseMeetings] = Field(None, alias='meetings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
