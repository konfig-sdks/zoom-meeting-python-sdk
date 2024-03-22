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

from zoom_meeting_python_sdk.type.webinars_create_invite_links_request_attendees import WebinarsCreateInviteLinksRequestAttendees

class RequiredWebinarsCreateInviteLinksRequest(TypedDict):
    pass

class OptionalWebinarsCreateInviteLinksRequest(TypedDict, total=False):
    attendees: WebinarsCreateInviteLinksRequestAttendees

    # The invite link's expiration time, in seconds.   This value defaults to `7200`.
    ttl: int

class WebinarsCreateInviteLinksRequest(RequiredWebinarsCreateInviteLinksRequest, OptionalWebinarsCreateInviteLinksRequest):
    pass
