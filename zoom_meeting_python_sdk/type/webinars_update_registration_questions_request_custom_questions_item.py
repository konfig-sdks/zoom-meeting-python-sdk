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

from zoom_meeting_python_sdk.type.webinars_update_registration_questions_request_custom_questions_item_answers import WebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItemAnswers

class RequiredWebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItem(TypedDict):
    pass

class OptionalWebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItem(TypedDict, total=False):
    # Custom question.
    title: str

    answers: WebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItemAnswers

    # State whether or not a registrant is required to answer the custom question.
    required: bool

    # The question-answer type.
    type: str

class WebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItem(RequiredWebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItem, OptionalWebinarsUpdateRegistrationQuestionsRequestCustomQuestionsItem):
    pass
