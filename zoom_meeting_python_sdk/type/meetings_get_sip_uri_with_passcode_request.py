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


class RequiredMeetingsGetSipUriWithPasscodeRequest(TypedDict):
    pass

class OptionalMeetingsGetSipUriWithPasscodeRequest(TypedDict, total=False):
    # If customers desire that a passcode be embedded in the SIP URI dial string, they must supply the passcode. Zoom will not validate the passcode.
    passcode: str

class MeetingsGetSipUriWithPasscodeRequest(RequiredMeetingsGetSipUriWithPasscodeRequest, OptionalMeetingsGetSipUriWithPasscodeRequest):
    pass
