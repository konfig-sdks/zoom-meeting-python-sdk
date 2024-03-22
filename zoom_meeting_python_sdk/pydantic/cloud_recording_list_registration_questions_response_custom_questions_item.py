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

from zoom_meeting_python_sdk.pydantic.cloud_recording_list_registration_questions_response_custom_questions_item_answers import CloudRecordingListRegistrationQuestionsResponseCustomQuestionsItemAnswers

class CloudRecordingListRegistrationQuestionsResponseCustomQuestionsItem(BaseModel):
    # Title of the question.
    title: typing.Optional[str] = Field(None, alias='title')

    answers: typing.Optional[CloudRecordingListRegistrationQuestionsResponseCustomQuestionsItemAnswers] = Field(None, alias='answers')

    # State whether registrants are required to answer custom questions or not.
    required: typing.Optional[bool] = Field(None, alias='required')

    # The type of registration question and answers.
    type: typing.Optional[Literal["short", "single", "multiple"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
