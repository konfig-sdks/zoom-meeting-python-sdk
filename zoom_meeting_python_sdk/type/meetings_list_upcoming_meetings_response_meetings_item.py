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


class RequiredMeetingsListUpcomingMeetingsResponseMeetingsItem(TypedDict):
    pass

class OptionalMeetingsListUpcomingMeetingsResponseMeetingsItem(TypedDict, total=False):
    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-) - a unique identifier of the meeting in **long** format, represented as int64 data type in JSON. Also known as the meeting number.
    id: int

    # The meeting topic.
    topic: str

    # Meeting types. `1` - Instant meeting. `2` - Scheduled meeting. `3` - Recurring meeting with no fixed time. `8` - Recurring meeting with fixed time.
    type: int

    # The meeting's start time.
    start_time: datetime

    # Meeting duration.
    duration: int

    # The timezone to format the meeting start time.
    timezone: str

    # The meeting creation time.
    created_at: datetime

    # The URL that participants can use to join a meeting.
    join_url: str

class MeetingsListUpcomingMeetingsResponseMeetingsItem(RequiredMeetingsListUpcomingMeetingsResponseMeetingsItem, OptionalMeetingsListUpcomingMeetingsResponseMeetingsItem):
    pass
