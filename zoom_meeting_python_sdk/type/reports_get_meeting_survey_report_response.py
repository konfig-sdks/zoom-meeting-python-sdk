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

from zoom_meeting_python_sdk.type.reports_get_meeting_survey_report_response_survey_answers import ReportsGetMeetingSurveyReportResponseSurveyAnswers

class RequiredReportsGetMeetingSurveyReportResponse(TypedDict):
    pass

class OptionalReportsGetMeetingSurveyReportResponse(TypedDict, total=False):
    # The meeting ID.
    meeting_id: int

    # The meeting's universally unique identifier (UUID). Each meeting instance generates a meeting UUID.
    meeting_uuid: str

    # The meeting's start time.
    start_time: datetime

    # The survey's ID
    survey_id: str

    # The name of survey
    survey_name: str

    survey_answers: ReportsGetMeetingSurveyReportResponseSurveyAnswers

class ReportsGetMeetingSurveyReportResponse(RequiredReportsGetMeetingSurveyReportResponse, OptionalReportsGetMeetingSurveyReportResponse):
    pass
