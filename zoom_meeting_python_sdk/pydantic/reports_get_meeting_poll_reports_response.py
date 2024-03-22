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

from zoom_meeting_python_sdk.pydantic.reports_get_meeting_poll_reports_response_questions import ReportsGetMeetingPollReportsResponseQuestions

class ReportsGetMeetingPollReportsResponse(BaseModel):
    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).
    id: typing.Optional[int] = Field(None, alias='id')

    # The meeting's universally unique identifier (UUID). Each meeting instance generates a meeting UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The meeting's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    questions: typing.Optional[ReportsGetMeetingPollReportsResponseQuestions] = Field(None, alias='questions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
