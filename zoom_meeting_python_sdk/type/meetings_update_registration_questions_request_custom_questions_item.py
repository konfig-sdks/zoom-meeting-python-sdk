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

from zoom_meeting_python_sdk.type.meetings_update_registration_questions_request_custom_questions_item_answers import MeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItemAnswers

class RequiredMeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItem(TypedDict):
    pass

class OptionalMeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItem(TypedDict, total=False):
    # Title of the custom question.
    title: str

    answers: MeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItemAnswers

    # Indicates whether or not the custom question is required to be answered by participants or not.
    required: bool

    # Type of the question being asked.
    type: str

class MeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItem(RequiredMeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItem, OptionalMeetingsUpdateRegistrationQuestionsRequestCustomQuestionsItem):
    pass
