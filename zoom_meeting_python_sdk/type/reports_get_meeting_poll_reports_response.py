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

from zoom_meeting_python_sdk.type.reports_get_meeting_poll_reports_response_questions import ReportsGetMeetingPollReportsResponseQuestions

class RequiredReportsGetMeetingPollReportsResponse(TypedDict):
    pass

class OptionalReportsGetMeetingPollReportsResponse(TypedDict, total=False):
    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).
    id: int

    # The meeting's universally unique identifier (UUID). Each meeting instance generates a meeting UUID.
    uuid: str

    # The meeting's start time.
    start_time: datetime

    questions: ReportsGetMeetingPollReportsResponseQuestions

class ReportsGetMeetingPollReportsResponse(RequiredReportsGetMeetingPollReportsResponse, OptionalReportsGetMeetingPollReportsResponse):
    pass
