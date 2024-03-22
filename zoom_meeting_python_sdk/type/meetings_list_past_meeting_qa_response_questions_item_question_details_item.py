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


class RequiredMeetingsListPastMeetingQaResponseQuestionsItemQuestionDetailsItem(TypedDict):
    pass

class OptionalMeetingsListPastMeetingQaResponseQuestionsItemQuestionDetailsItem(TypedDict, total=False):
    # An answer submitted for the question. The value is 'live answered' if this is a live answer.
    answer: str

    # A question asked during the Q&amp;A.
    question: str

class MeetingsListPastMeetingQaResponseQuestionsItemQuestionDetailsItem(RequiredMeetingsListPastMeetingQaResponseQuestionsItemQuestionDetailsItem, OptionalMeetingsListPastMeetingQaResponseQuestionsItemQuestionDetailsItem):
    pass
