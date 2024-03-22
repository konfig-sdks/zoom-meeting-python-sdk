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


class RequiredMeetingsUpdateMeetingStatusRequest(TypedDict):
    pass

class OptionalMeetingsUpdateMeetingStatusRequest(TypedDict, total=False):
    # `end` - End a meeting.     `recover` - [Recover](https://support.zoom.us/hc/en-us/articles/360038297111-Recover-a-deleted-meeting) a deleted meeting. 
    action: str

class MeetingsUpdateMeetingStatusRequest(RequiredMeetingsUpdateMeetingStatusRequest, OptionalMeetingsUpdateMeetingStatusRequest):
    pass
