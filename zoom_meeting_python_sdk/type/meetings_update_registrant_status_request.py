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

from zoom_meeting_python_sdk.type.meetings_update_registrant_status_request_registrants import MeetingsUpdateRegistrantStatusRequestRegistrants

class RequiredMeetingsUpdateRegistrantStatusRequest(TypedDict):
    # Registrant Status:    `approve` - Approve registrant.    `cancel` - Cancel previously approved registrant's registration.    `deny` - Deny registrant.
    action: str

class OptionalMeetingsUpdateRegistrantStatusRequest(TypedDict, total=False):
    registrants: MeetingsUpdateRegistrantStatusRequestRegistrants

class MeetingsUpdateRegistrantStatusRequest(RequiredMeetingsUpdateRegistrantStatusRequest, OptionalMeetingsUpdateRegistrantStatusRequest):
    pass
