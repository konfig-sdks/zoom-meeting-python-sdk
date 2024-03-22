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

from zoom_meeting_python_sdk.pydantic.webinars_list_past_webinar_qa_response_questions import WebinarsListPastWebinarQaResponseQuestions

class WebinarsListPastWebinarQaResponse(BaseModel):
    # Webinar ID in **long** format, represented as int64 data type in JSON, also known as the webinar number.
    id: typing.Optional[int] = Field(None, alias='id')

    questions: typing.Optional[WebinarsListPastWebinarQaResponseQuestions] = Field(None, alias='questions')

    # The webinar's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Webinar UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
