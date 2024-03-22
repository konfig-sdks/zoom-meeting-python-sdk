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

from zoom_meeting_python_sdk.type.reports_get_webinar_poll_reports_response_questions import ReportsGetWebinarPollReportsResponseQuestions

class RequiredReportsGetWebinarPollReportsResponse(TypedDict):
    pass

class OptionalReportsGetWebinarPollReportsResponse(TypedDict, total=False):
    # The webinar ID.
    id: int

    questions: ReportsGetWebinarPollReportsResponseQuestions

    # The webinar's start time.
    start_time: datetime

    # The webinar's universally unique identifier (UUID). Each webinar instance generates a webinar UUID.
    uuid: str

class ReportsGetWebinarPollReportsResponse(RequiredReportsGetWebinarPollReportsResponse, OptionalReportsGetWebinarPollReportsResponse):
    pass
