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


class MeetingsListUpcomingMeetingsResponseMeetingsItem(BaseModel):
    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-) - a unique identifier of the meeting in **long** format, represented as int64 data type in JSON. Also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    # The meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # Meeting types. `1` - Instant meeting. `2` - Scheduled meeting. `3` - Recurring meeting with no fixed time. `8` - Recurring meeting with fixed time.
    type: typing.Optional[Literal[1, 2, 3, 8]] = Field(None, alias='type')

    # The meeting's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Meeting duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # The timezone to format the meeting start time.
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # The meeting creation time.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The URL that participants can use to join a meeting.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
