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


class RequiredReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetailsItem(TypedDict):
    pass

class OptionalReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetailsItem(TypedDict, total=False):
    # The user's given answer.
    answer: str

    # The date and time at which the user answered the poll question.
    date_time: str

    # The poll's ID.
    polling_id: str

    # The poll question.
    question: str

class ReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetailsItem(RequiredReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetailsItem, OptionalReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetailsItem):
    pass
