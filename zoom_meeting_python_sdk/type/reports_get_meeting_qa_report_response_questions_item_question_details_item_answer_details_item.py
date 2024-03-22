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


class RequiredReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetailsItem(TypedDict):
    pass

class OptionalReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetailsItem(TypedDict, total=False):
    # The user ID of the user who answered the question. This value returns blank for external users.
    user_id: str

    # User display name, including the host or participant.
    name: str

    # Participant's email. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: str

    # The answer from host or the comment from participant.
    content: str

    # Content submit time.
    create_time: str

    # Type of answer.
    type: str

class ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetailsItem(RequiredReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetailsItem, OptionalReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetailsItem):
    pass
