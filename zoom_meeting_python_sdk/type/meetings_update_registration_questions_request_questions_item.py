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


class RequiredMeetingsUpdateRegistrationQuestionsRequestQuestionsItem(TypedDict):
    pass

class OptionalMeetingsUpdateRegistrationQuestionsRequestQuestionsItem(TypedDict, total=False):
    # Field name of the question.
    field_name: str

    # Indicates whether or not the displayed fields are required to be filled out by registrants.
    required: bool

class MeetingsUpdateRegistrationQuestionsRequestQuestionsItem(RequiredMeetingsUpdateRegistrationQuestionsRequestQuestionsItem, OptionalMeetingsUpdateRegistrationQuestionsRequestQuestionsItem):
    pass
