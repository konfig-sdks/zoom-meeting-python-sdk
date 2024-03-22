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

from zoom_meeting_python_sdk.pydantic.meetings_get_past_meeting_participants_response_participants import MeetingsGetPastMeetingParticipantsResponseParticipants

class MeetingsGetPastMeetingParticipantsResponse(BaseModel):
    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of pages returned for the request made.
    page_count: typing.Optional[int] = Field(None, alias='page_count')

    # The number of records returned within a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # The number of all records available across pages.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    participants: typing.Optional[MeetingsGetPastMeetingParticipantsResponseParticipants] = Field(None, alias='participants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
