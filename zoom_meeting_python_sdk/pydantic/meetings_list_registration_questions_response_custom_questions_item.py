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

from zoom_meeting_python_sdk.pydantic.meetings_list_registration_questions_response_custom_questions_item_answers import MeetingsListRegistrationQuestionsResponseCustomQuestionsItemAnswers

class MeetingsListRegistrationQuestionsResponseCustomQuestionsItem(BaseModel):
    # Title of the custom question.
    title: typing.Optional[str] = Field(None, alias='title')

    answers: typing.Optional[MeetingsListRegistrationQuestionsResponseCustomQuestionsItemAnswers] = Field(None, alias='answers')

    # Indicates whether or not the custom question is required to be answered by participants or not.
    required: typing.Optional[bool] = Field(None, alias='required')

    # Type of the question being asked.
    type: typing.Optional[Literal["short", "single"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
