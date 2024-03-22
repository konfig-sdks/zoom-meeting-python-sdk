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

from zoom_meeting_python_sdk.type.reports_get_meeting_qa_report_response_questions_item_question_details import ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetails

class RequiredReportsGetMeetingQaReportResponseQuestionsItem(TypedDict):
    pass

class OptionalReportsGetMeetingQaReportResponseQuestionsItem(TypedDict, total=False):
    # The user ID of the user who asked the question. This value returns blank for external users.
    user_id: str

    # Participant's email. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: str

    # Participant's display name.       If the anonymous [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) option is enabled and if a participant submits the Q&amp;A without providing their name, the value of the `name` field is &quot;Anonymous Attendee&quot;.
    name: str

    question_details: ReportsGetMeetingQaReportResponseQuestionsItemQuestionDetails

class ReportsGetMeetingQaReportResponseQuestionsItem(RequiredReportsGetMeetingQaReportResponseQuestionsItem, OptionalReportsGetMeetingQaReportResponseQuestionsItem):
    pass
