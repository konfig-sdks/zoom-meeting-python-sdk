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

from zoom_meeting_python_sdk.pydantic.reports_get_webinar_qa_report_response_questions import ReportsGetWebinarQaReportResponseQuestions

class ReportsGetWebinarQaReportResponse(BaseModel):
    # Webinar ID in `long` format, represented as int64 data type in JSON. Also known as the webinar number.
    id: typing.Optional[int] = Field(None, alias='id')

    questions: typing.Optional[ReportsGetWebinarQaReportResponseQuestions] = Field(None, alias='questions')

    # Webinar start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Webinar UUID. Each webinar instance will generate its own UUID - after a webinar ends, a new UUID will be generated for the next instance of the webinar. Double-encode your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
