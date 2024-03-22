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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from zoom_meeting_python_sdk.pydantic.reports_get_meeting_survey_report_response_survey_answers_item import ReportsGetMeetingSurveyReportResponseSurveyAnswersItem

ReportsGetMeetingSurveyReportResponseSurveyAnswers = typing.List[ReportsGetMeetingSurveyReportResponseSurveyAnswersItem]
