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

from zoom_meeting_python_sdk.pydantic.reports_get_meeting_qa_report_response_questions import ReportsGetMeetingQaReportResponseQuestions

class ReportsGetMeetingQaReportResponse(BaseModel):
    # The meeting ID in `long` format, represented as int64 data type in JSON. Also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    questions: typing.Optional[ReportsGetMeetingQaReportResponseQuestions] = Field(None, alias='questions')

    # Meeting start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The meeting UUID. Each meeting instance will generate its own UUID - for example, after a meeting ends, a new UUID will be generated for the next instance of the meeting. Double-encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//'.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
