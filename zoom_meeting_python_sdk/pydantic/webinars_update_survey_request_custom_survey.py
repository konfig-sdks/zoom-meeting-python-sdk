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

from zoom_meeting_python_sdk.pydantic.webinars_update_survey_request_custom_survey_questions import WebinarsUpdateSurveyRequestCustomSurveyQuestions

class WebinarsUpdateSurveyRequestCustomSurvey(BaseModel):
    # The survey's title, up to 64 characters.
    title: typing.Optional[str] = Field(None, alias='title')

    # Allow participants to anonymously answer survey questions.  * `true` - Anonymous survey enabled.  * `false` - Participants cannot answer survey questions anonymously.    This value defaults to `true`.
    anonymous: typing.Optional[bool] = Field(None, alias='anonymous')

    # Whether to display the number in the question name.    This value defaults to `true`.
    numbered_questions: typing.Optional[bool] = Field(None, alias='numbered_questions')

    # Whether to display the question type in the question name.    This value defaults to `false`.
    show_question_type: typing.Optional[bool] = Field(None, alias='show_question_type')

    # The survey's feedback, up to 320 characters.    This value defaults to `Thank you so much for taking the time to complete the survey, your feedback really makes a difference.`.
    feedback: typing.Optional[str] = Field(None, alias='feedback')

    questions: typing.Optional[WebinarsUpdateSurveyRequestCustomSurveyQuestions] = Field(None, alias='questions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
