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

from zoom_meeting_python_sdk.type.webinars_add_registrant_response_occurrences import WebinarsAddRegistrantResponseOccurrences

class RequiredWebinarsAddRegistrantResponse(TypedDict):
    pass

class OptionalWebinarsAddRegistrantResponse(TypedDict, total=False):
    # The webinar's ID.
    id: int

    # The URL the registrant can use to join the webinar.
    join_url: str

    # The registrant's ID.
    registrant_id: str

    # The webinar's start time.
    start_time: datetime

    # The webinar's topic.
    topic: str

    occurrences: WebinarsAddRegistrantResponseOccurrences

class WebinarsAddRegistrantResponse(RequiredWebinarsAddRegistrantResponse, OptionalWebinarsAddRegistrantResponse):
    pass
