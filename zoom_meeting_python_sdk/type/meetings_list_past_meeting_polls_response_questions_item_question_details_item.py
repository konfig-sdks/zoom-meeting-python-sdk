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


class RequiredMeetingsListPastMeetingPollsResponseQuestionsItemQuestionDetailsItem(TypedDict):
    pass

class OptionalMeetingsListPastMeetingPollsResponseQuestionsItemQuestionDetailsItem(TypedDict, total=False):
    # Answer submitted by the user.
    answer: str

    # Date and time at which the answer to the poll was submitted.
    date_time: datetime

    # Unique identifier of the poll.
    polling_id: str

    # Question asked during the poll.
    question: str

class MeetingsListPastMeetingPollsResponseQuestionsItemQuestionDetailsItem(RequiredMeetingsListPastMeetingPollsResponseQuestionsItemQuestionDetailsItem, OptionalMeetingsListPastMeetingPollsResponseQuestionsItemQuestionDetailsItem):
    pass
