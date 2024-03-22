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

from zoom_meeting_python_sdk.type.reports_get_meeting_qa_report_response_questions import ReportsGetMeetingQaReportResponseQuestions

class RequiredReportsGetMeetingQaReportResponse(TypedDict):
    pass

class OptionalReportsGetMeetingQaReportResponse(TypedDict, total=False):
    # The meeting ID in `long` format, represented as int64 data type in JSON. Also known as the meeting number.
    id: int

    questions: ReportsGetMeetingQaReportResponseQuestions

    # Meeting start time.
    start_time: datetime

    # The meeting UUID. Each meeting instance will generate its own UUID - for example, after a meeting ends, a new UUID will be generated for the next instance of the meeting. Double-encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//'.
    uuid: str

class ReportsGetMeetingQaReportResponse(RequiredReportsGetMeetingQaReportResponse, OptionalReportsGetMeetingQaReportResponse):
    pass
