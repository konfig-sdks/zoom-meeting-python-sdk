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


class RequiredMeetingsListHostScheduledResponseMeetingsItem(TypedDict):
    pass

class OptionalMeetingsListHostScheduledResponseMeetingsItem(TypedDict, total=False):
    # Meeting description. The length of agenda gets truncated to 250 characters when you list all of a user's meetings. To view a meeting's complete agenda, or to retrieve details for a single meeting, use the [**Get a meeting**](https://developers.zoom.us) API.
    agenda: str

    # Time of creation.
    created_at: datetime

    # Meeting duration.
    duration: int

    # ID of the user who is set as the meeting's host.
    host_id: str

    # Meeting ID - also known as the meeting number in long (int64) format.
    id: int

    # URL using which participants can join a meeting.
    join_url: str

    # [Personal meeting ID](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). This field is only returned if PMI was used to schedule the meeting.
    pmi: str

    # Meeting start time.
    start_time: datetime

    # Timezone to format the meeting start time. 
    timezone: str

    # Meeting topic.
    topic: str

    # Meeting types.    `1` - Instant meeting.    `2` - Scheduled meeting.    `3` - Recurring meeting with no fixed time.    `8` - Recurring meeting with fixed time.
    type: int

    # Unique Meeting ID. Each meeting instance will generate its own Meeting UUID.
    uuid: str

class MeetingsListHostScheduledResponseMeetingsItem(RequiredMeetingsListHostScheduledResponseMeetingsItem, OptionalMeetingsListHostScheduledResponseMeetingsItem):
    pass
