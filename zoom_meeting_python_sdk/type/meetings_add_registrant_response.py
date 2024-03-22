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

from zoom_meeting_python_sdk.type.meetings_add_registrant_response_occurrences import MeetingsAddRegistrantResponseOccurrences

class RequiredMeetingsAddRegistrantResponse(TypedDict):
    pass

class OptionalMeetingsAddRegistrantResponse(TypedDict, total=False):
    # The meeting ID.
    id: int

    # The URL the registrant can use to join the meeting.   The API will not return this field if the meeting was [created](https://developers.zoom.us) with the `approval_type` field value of `1` (manual approval).
    join_url: str

    # The registrant's ID.
    registrant_id: str

    # The meeting's start time.
    start_time: datetime

    # The meeting's topic.
    topic: str

    occurrences: MeetingsAddRegistrantResponseOccurrences

    # The participant PIN code is used to authenticate audio participants before they join the meeting.
    participant_pin_code: int

class MeetingsAddRegistrantResponse(RequiredMeetingsAddRegistrantResponse, OptionalMeetingsAddRegistrantResponse):
    pass
