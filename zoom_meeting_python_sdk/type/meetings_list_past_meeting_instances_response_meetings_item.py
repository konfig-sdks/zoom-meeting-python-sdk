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


class RequiredMeetingsListPastMeetingInstancesResponseMeetingsItem(TypedDict):
    pass

class OptionalMeetingsListPastMeetingInstancesResponseMeetingsItem(TypedDict, total=False):
    # Start time
    start_time: datetime

    # Meeting UUID. Unique meeting ID. Each meeting instance will generate its own Meeting UUID (i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). [Double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a '/'or contains '//' in it.  
    uuid: str

class MeetingsListPastMeetingInstancesResponseMeetingsItem(RequiredMeetingsListPastMeetingInstancesResponseMeetingsItem, OptionalMeetingsListPastMeetingInstancesResponseMeetingsItem):
    pass
