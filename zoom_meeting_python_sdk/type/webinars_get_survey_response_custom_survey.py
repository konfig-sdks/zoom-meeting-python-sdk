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

from zoom_meeting_python_sdk.type.webinars_get_survey_response_custom_survey_questions import WebinarsGetSurveyResponseCustomSurveyQuestions

class RequiredWebinarsGetSurveyResponseCustomSurvey(TypedDict):
    pass

class OptionalWebinarsGetSurveyResponseCustomSurvey(TypedDict, total=False):
    # The survey's title, up to 64 characters.
    title: str

    # Allow participants to anonymously answer survey questions.  * `true` - Anonymous survey enabled.  * `false` - Participants cannot answer survey questions anonymously.    This value defaults to `true`.
    anonymous: bool

    # Whether to display the number in the question name.    This value defaults to `true`.
    numbered_questions: bool

    # Whether to display the question type in the question name.    This value defaults to `false`.
    show_question_type: bool

    # The survey's feedback, up to 320 characters.    This value defaults to `Thank you so much for taking the time to complete the survey, your feedback really makes a difference.`.
    feedback: str

    questions: WebinarsGetSurveyResponseCustomSurveyQuestions

class WebinarsGetSurveyResponseCustomSurvey(RequiredWebinarsGetSurveyResponseCustomSurvey, OptionalWebinarsGetSurveyResponseCustomSurvey):
    pass
