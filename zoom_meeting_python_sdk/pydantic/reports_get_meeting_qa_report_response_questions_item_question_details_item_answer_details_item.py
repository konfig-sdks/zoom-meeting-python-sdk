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


class ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetailsItem(BaseModel):
    # The user ID of the user who answered the question. This value returns blank for external users.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # User display name, including the host or participant.
    name: typing.Optional[str] = Field(None, alias='name')

    # Participant's email. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: typing.Optional[str] = Field(None, alias='email')

    # The answer from host or the comment from participant.
    content: typing.Optional[str] = Field(None, alias='content')

    # Content submit time.
    create_time: typing.Optional[str] = Field(None, alias='create_time')

    # Type of answer.
    type: typing.Optional[Literal["default", "host_answered", "participant_commented"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
