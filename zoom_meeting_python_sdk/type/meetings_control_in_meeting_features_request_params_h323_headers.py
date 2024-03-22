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


class RequiredMeetingsControlInMeetingFeaturesRequestParamsH323Headers(TypedDict):
    pass

class OptionalMeetingsControlInMeetingFeaturesRequestParamsH323Headers(TypedDict, total=False):
    # Custom name that will be used within the h323 Header.
    from_display_name: str

    # Custom remote name that will be used within the meeting.
    to_display_name: str

class MeetingsControlInMeetingFeaturesRequestParamsH323Headers(RequiredMeetingsControlInMeetingFeaturesRequestParamsH323Headers, OptionalMeetingsControlInMeetingFeaturesRequestParamsH323Headers):
    pass
