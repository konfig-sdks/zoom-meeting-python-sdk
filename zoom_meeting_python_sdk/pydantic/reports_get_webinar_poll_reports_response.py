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

from zoom_meeting_python_sdk.pydantic.reports_get_webinar_poll_reports_response_questions import ReportsGetWebinarPollReportsResponseQuestions

class ReportsGetWebinarPollReportsResponse(BaseModel):
    # The webinar ID.
    id: typing.Optional[int] = Field(None, alias='id')

    questions: typing.Optional[ReportsGetWebinarPollReportsResponseQuestions] = Field(None, alias='questions')

    # The webinar's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The webinar's universally unique identifier (UUID). Each webinar instance generates a webinar UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
