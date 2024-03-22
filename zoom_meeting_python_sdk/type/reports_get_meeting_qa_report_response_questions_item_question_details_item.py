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

from zoom_meeting_python_sdk.type.reports_get_meeting_qa_report_response_questions_item_question_details_item_answer_details import ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails

class RequiredReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItem(TypedDict):
    pass

class OptionalReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItem(TypedDict, total=False):
    # WARNING: This property is deprecated
    # The given answer. If this is a live answer, the value is 'live answered'. **Note:** All answers will be returned together and separated by semicolons. For more detailed answer information, please see the \"answer_details\" field.
    answer: str

    # Asked question.
    question: str

    # Question UUID.
    question_id: str

    # Question create time.
    create_time: str

    answer_details: ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails

class ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItem(RequiredReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItem, OptionalReportsGetMeetingQaReportResponseQuestionsItemQuestionDetailsItem):
    pass
