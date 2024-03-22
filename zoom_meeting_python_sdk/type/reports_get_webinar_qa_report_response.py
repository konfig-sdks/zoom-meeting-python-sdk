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

from zoom_meeting_python_sdk.type.reports_get_webinar_qa_report_response_questions import ReportsGetWebinarQaReportResponseQuestions

class RequiredReportsGetWebinarQaReportResponse(TypedDict):
    pass

class OptionalReportsGetWebinarQaReportResponse(TypedDict, total=False):
    # Webinar ID in `long` format, represented as int64 data type in JSON. Also known as the webinar number.
    id: int

    questions: ReportsGetWebinarQaReportResponseQuestions

    # Webinar start time.
    start_time: datetime

    # Webinar UUID. Each webinar instance will generate its own UUID - after a webinar ends, a new UUID will be generated for the next instance of the webinar. Double-encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.
    uuid: str

class ReportsGetWebinarQaReportResponse(RequiredReportsGetWebinarQaReportResponse, OptionalReportsGetWebinarQaReportResponse):
    pass
