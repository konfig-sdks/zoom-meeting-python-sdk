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


class RequiredMeetingsControlInMeetingFeaturesRequestParamsContactsItem(TypedDict):
    pass

class OptionalMeetingsControlInMeetingFeaturesRequestParamsContactsItem(TypedDict, total=False):
    # The user's email address. Use this value if you do not have the user's ID.   If you pass the `id` value, the API ignores this query parameter.
    email: str

    # The user's ID.
    id: str

class MeetingsControlInMeetingFeaturesRequestParamsContactsItem(RequiredMeetingsControlInMeetingFeaturesRequestParamsContactsItem, OptionalMeetingsControlInMeetingFeaturesRequestParamsContactsItem):
    pass
