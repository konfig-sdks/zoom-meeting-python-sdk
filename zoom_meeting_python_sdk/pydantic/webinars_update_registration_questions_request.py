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

from zoom_meeting_python_sdk.pydantic.webinars_update_registration_questions_request_custom_questions import WebinarsUpdateRegistrationQuestionsRequestCustomQuestions
from zoom_meeting_python_sdk.pydantic.webinars_update_registration_questions_request_questions import WebinarsUpdateRegistrationQuestionsRequestQuestions

class WebinarsUpdateRegistrationQuestionsRequest(BaseModel):
    custom_questions: typing.Optional[WebinarsUpdateRegistrationQuestionsRequestCustomQuestions] = Field(None, alias='custom_questions')

    questions: typing.Optional[WebinarsUpdateRegistrationQuestionsRequestQuestions] = Field(None, alias='questions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
