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

from zoom_meeting_python_sdk.type.webinars_list_registration_questions_response_custom_questions_item_answers import WebinarsListRegistrationQuestionsResponseCustomQuestionsItemAnswers

class RequiredWebinarsListRegistrationQuestionsResponseCustomQuestionsItem(TypedDict):
    pass

class OptionalWebinarsListRegistrationQuestionsResponseCustomQuestionsItem(TypedDict, total=False):
    # Custom question.
    title: str

    answers: WebinarsListRegistrationQuestionsResponseCustomQuestionsItemAnswers

    # State whether or not the custom question is required to be answered by a registrant.
    required: bool

    # The question-answer type.
    type: str

class WebinarsListRegistrationQuestionsResponseCustomQuestionsItem(RequiredWebinarsListRegistrationQuestionsResponseCustomQuestionsItem, OptionalWebinarsListRegistrationQuestionsResponseCustomQuestionsItem):
    pass
