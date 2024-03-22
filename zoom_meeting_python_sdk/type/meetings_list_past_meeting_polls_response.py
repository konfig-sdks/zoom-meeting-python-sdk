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

from zoom_meeting_python_sdk.type.meetings_list_past_meeting_polls_response_questions import MeetingsListPastMeetingPollsResponseQuestions

class RequiredMeetingsListPastMeetingPollsResponse(TypedDict):
    pass

class OptionalMeetingsListPastMeetingPollsResponse(TypedDict, total=False):
    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in **long** format(represented as int64 data type in JSON), also known as the meeting number.
    id: int

    questions: MeetingsListPastMeetingPollsResponseQuestions

    # The start time of the meeting.
    start_time: datetime

    # Meeting UUID.
    uuid: str

class MeetingsListPastMeetingPollsResponse(RequiredMeetingsListPastMeetingPollsResponse, OptionalMeetingsListPastMeetingPollsResponse):
    pass
