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


class RequiredMeetingsCreateMeetingRequestSettingsAuthenticationExceptionItem(TypedDict):
    pass

class OptionalMeetingsCreateMeetingRequestSettingsAuthenticationExceptionItem(TypedDict, total=False):
    # The participant's email address.
    email: str

    # The participant's name.
    name: str

class MeetingsCreateMeetingRequestSettingsAuthenticationExceptionItem(RequiredMeetingsCreateMeetingRequestSettingsAuthenticationExceptionItem, OptionalMeetingsCreateMeetingRequestSettingsAuthenticationExceptionItem):
    pass
