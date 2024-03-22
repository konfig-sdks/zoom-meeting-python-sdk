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


class RequiredWebinarsListPastWebinarQaResponseQuestionsItemQuestionDetailsItem(TypedDict):
    pass

class OptionalWebinarsListPastWebinarQaResponseQuestionsItemQuestionDetailsItem(TypedDict, total=False):
    # Answer submitted for the question. The value will be 'live answered' if this is a live answer.
    answer: str

    # Question asked during the Q&amp;A.
    question: str

class WebinarsListPastWebinarQaResponseQuestionsItemQuestionDetailsItem(RequiredWebinarsListPastWebinarQaResponseQuestionsItemQuestionDetailsItem, OptionalWebinarsListPastWebinarQaResponseQuestionsItemQuestionDetailsItem):
    pass
