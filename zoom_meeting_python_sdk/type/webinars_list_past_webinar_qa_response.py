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

from zoom_meeting_python_sdk.type.webinars_list_past_webinar_qa_response_questions import WebinarsListPastWebinarQaResponseQuestions

class RequiredWebinarsListPastWebinarQaResponse(TypedDict):
    pass

class OptionalWebinarsListPastWebinarQaResponse(TypedDict, total=False):
    # Webinar ID in **long** format, represented as int64 data type in JSON, also known as the webinar number.
    id: int

    questions: WebinarsListPastWebinarQaResponseQuestions

    # The webinar's start time.
    start_time: datetime

    # Webinar UUID.
    uuid: str

class WebinarsListPastWebinarQaResponse(RequiredWebinarsListPastWebinarQaResponse, OptionalWebinarsListPastWebinarQaResponse):
    pass
