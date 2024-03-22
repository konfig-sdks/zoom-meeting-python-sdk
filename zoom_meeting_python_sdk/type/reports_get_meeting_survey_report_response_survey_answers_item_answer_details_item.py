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


class RequiredReportsGetMeetingSurveyReportResponseSurveyAnswersItemAnswerDetailsItem(TypedDict):
    pass

class OptionalReportsGetMeetingSurveyReportResponseSurveyAnswersItemAnswerDetailsItem(TypedDict, total=False):
    # The survey question.
    question: str

    # The question's ID
    question_id: str

    # The user's given answer.
    answer: str

    # The date and time at which the user answered the survey question.
    date_time: str

class ReportsGetMeetingSurveyReportResponseSurveyAnswersItemAnswerDetailsItem(RequiredReportsGetMeetingSurveyReportResponseSurveyAnswersItemAnswerDetailsItem, OptionalReportsGetMeetingSurveyReportResponseSurveyAnswersItemAnswerDetailsItem):
    pass
