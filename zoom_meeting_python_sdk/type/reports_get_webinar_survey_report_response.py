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

from zoom_meeting_python_sdk.type.reports_get_webinar_survey_report_response_survey_answers import ReportsGetWebinarSurveyReportResponseSurveyAnswers

class RequiredReportsGetWebinarSurveyReportResponse(TypedDict):
    pass

class OptionalReportsGetWebinarSurveyReportResponse(TypedDict, total=False):
    # The webinar ID.
    webinar_id: int

    # The webinar's universally unique identifier (UUID). Each webinar instance generates a webinar UUID.
    webinar_uuid: str

    # The webinar's start time.
    start_time: datetime

    # The survey's ID
    survey_id: str

    # The name of survey
    survey_name: str

    survey_answers: ReportsGetWebinarSurveyReportResponseSurveyAnswers

class ReportsGetWebinarSurveyReportResponse(RequiredReportsGetWebinarSurveyReportResponse, OptionalReportsGetWebinarSurveyReportResponse):
    pass
