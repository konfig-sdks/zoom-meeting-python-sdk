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

from zoom_meeting_python_sdk.pydantic.reports_get_meeting_survey_report_response_survey_answers import ReportsGetMeetingSurveyReportResponseSurveyAnswers

class ReportsGetMeetingSurveyReportResponse(BaseModel):
    # The meeting ID.
    meeting_id: typing.Optional[int] = Field(None, alias='meeting_id')

    # The meeting's universally unique identifier (UUID). Each meeting instance generates a meeting UUID.
    meeting_uuid: typing.Optional[str] = Field(None, alias='meeting_uuid')

    # The meeting's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The survey's ID
    survey_id: typing.Optional[str] = Field(None, alias='survey_id')

    # The name of survey
    survey_name: typing.Optional[str] = Field(None, alias='survey_name')

    survey_answers: typing.Optional[ReportsGetMeetingSurveyReportResponseSurveyAnswers] = Field(None, alias='survey_answers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
