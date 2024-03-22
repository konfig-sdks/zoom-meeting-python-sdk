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

from zoom_meeting_python_sdk.type.meetings_create_invite_links_response_attendees import MeetingsCreateInviteLinksResponseAttendees

class RequiredMeetingsCreateInviteLinksResponse(TypedDict):
    pass

class OptionalMeetingsCreateInviteLinksResponse(TypedDict, total=False):
    attendees: MeetingsCreateInviteLinksResponseAttendees

class MeetingsCreateInviteLinksResponse(RequiredMeetingsCreateInviteLinksResponse, OptionalMeetingsCreateInviteLinksResponse):
    pass
