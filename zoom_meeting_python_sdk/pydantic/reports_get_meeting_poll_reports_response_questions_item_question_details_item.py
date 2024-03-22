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


class ReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetailsItem(BaseModel):
    # The user's given answer.
    answer: typing.Optional[str] = Field(None, alias='answer')

    # The date and time at which the user answered the poll question.
    date_time: typing.Optional[str] = Field(None, alias='date_time')

    # The poll's ID.
    polling_id: typing.Optional[str] = Field(None, alias='polling_id')

    # The poll question.
    question: typing.Optional[str] = Field(None, alias='question')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
