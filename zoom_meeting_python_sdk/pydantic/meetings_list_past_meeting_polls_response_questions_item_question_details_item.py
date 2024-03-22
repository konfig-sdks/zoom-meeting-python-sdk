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


class MeetingsListPastMeetingPollsResponseQuestionsItemQuestionDetailsItem(BaseModel):
    # Answer submitted by the user.
    answer: typing.Optional[str] = Field(None, alias='answer')

    # Date and time at which the answer to the poll was submitted.
    date_time: typing.Optional[datetime] = Field(None, alias='date_time')

    # Unique identifier of the poll.
    polling_id: typing.Optional[str] = Field(None, alias='polling_id')

    # Question asked during the poll.
    question: typing.Optional[str] = Field(None, alias='question')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
