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

from zoom_meeting_python_sdk.pydantic.meetings_list_upcoming_meetings_response_meetings import MeetingsListUpcomingMeetingsResponseMeetings

class MeetingsListUpcomingMeetingsResponse(BaseModel):
    # The total number of all records available across all pages.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    meetings: typing.Optional[MeetingsListUpcomingMeetingsResponseMeetings] = Field(None, alias='meetings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
