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


class RequiredWebinarsUpdateRegistrationQuestionsRequestQuestionsItem(TypedDict):
    pass

class OptionalWebinarsUpdateRegistrationQuestionsRequestQuestionsItem(TypedDict, total=False):
    # Field name
    field_name: str

    # State whether the selected fields are required or optional.
    required: bool

class WebinarsUpdateRegistrationQuestionsRequestQuestionsItem(RequiredWebinarsUpdateRegistrationQuestionsRequestQuestionsItem, OptionalWebinarsUpdateRegistrationQuestionsRequestQuestionsItem):
    pass
