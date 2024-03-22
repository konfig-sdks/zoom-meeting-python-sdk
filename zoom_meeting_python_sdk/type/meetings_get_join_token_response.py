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


class RequiredMeetingsGetJoinTokenResponse(TypedDict):
    pass

class OptionalMeetingsGetJoinTokenResponse(TypedDict, total=False):
    # The number of seconds the join token is valid for before it expires. This value always returns `120`.
    expire_in: int

    # The join token.
    token: str

class MeetingsGetJoinTokenResponse(RequiredMeetingsGetJoinTokenResponse, OptionalMeetingsGetJoinTokenResponse):
    pass
