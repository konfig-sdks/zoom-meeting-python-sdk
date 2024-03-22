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

from zoom_meeting_python_sdk.pydantic.meetings_list_past_meeting_qa_response_questions import MeetingsListPastMeetingQaResponseQuestions

class MeetingsListPastMeetingQaResponse(BaseModel):
    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in **long** format, represented as int64 data type in JSON, also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    questions: typing.Optional[MeetingsListPastMeetingQaResponseQuestions] = Field(None, alias='questions')

    # The meeting's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Meeting UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
