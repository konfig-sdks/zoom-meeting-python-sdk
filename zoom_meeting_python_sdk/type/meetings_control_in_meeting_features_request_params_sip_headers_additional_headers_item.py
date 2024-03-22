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


class RequiredMeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem(TypedDict):
    pass

class OptionalMeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem(TypedDict, total=False):
    # Additional custom SIP header's key.
    key: str

    # Additional custom SIP header's value.
    value: str

class MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem(RequiredMeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem, OptionalMeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem):
    pass
