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

from zoom_meeting_python_sdk.pydantic.cloud_recording_list_registration_questions_response_custom_questions import CloudRecordingListRegistrationQuestionsResponseCustomQuestions
from zoom_meeting_python_sdk.pydantic.cloud_recording_list_registration_questions_response_questions import CloudRecordingListRegistrationQuestionsResponseQuestions

class CloudRecordingListRegistrationQuestionsResponse(BaseModel):
    custom_questions: typing.Optional[CloudRecordingListRegistrationQuestionsResponseCustomQuestions] = Field(None, alias='custom_questions')

    questions: typing.Optional[CloudRecordingListRegistrationQuestionsResponseQuestions] = Field(None, alias='questions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
