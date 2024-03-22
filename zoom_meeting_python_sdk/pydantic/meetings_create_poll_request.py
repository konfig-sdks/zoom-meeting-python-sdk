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

from zoom_meeting_python_sdk.pydantic.meetings_create_poll_request_questions import MeetingsCreatePollRequestQuestions

class MeetingsCreatePollRequest(BaseModel):
    # The poll's title, up to 64 characters.
    title: typing.Optional[str] = Field(None, alias='title')

    # Allow meeting participants to answer poll questions anonymously.   This value defaults to `false`.
    anonymous: typing.Optional[bool] = Field(None, alias='anonymous')

    # The type of poll:  * `1` &mdash; Poll.  * `2` &mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * `3` &mdash; Quiz. This feature must be enabled in your Zoom account.    This value defaults to `1`.
    poll_type: typing.Optional[Literal[1, 2, 3]] = Field(None, alias='poll_type')

    questions: typing.Optional[MeetingsCreatePollRequestQuestions] = Field(None, alias='questions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
