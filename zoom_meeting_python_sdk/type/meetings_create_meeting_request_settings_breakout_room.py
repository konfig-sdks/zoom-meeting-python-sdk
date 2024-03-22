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

from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_breakout_room_rooms import MeetingsCreateMeetingRequestSettingsBreakoutRoomRooms

class RequiredMeetingsCreateMeetingRequestSettingsBreakoutRoom(TypedDict):
    pass

class OptionalMeetingsCreateMeetingRequestSettingsBreakoutRoom(TypedDict, total=False):
    # Whether to enable the [**Breakout Room pre-assign**](https://support.zoom.us/hc/en-us/articles/360032752671-Pre-assigning-participants-to-breakout-rooms) option.
    enable: bool

    rooms: MeetingsCreateMeetingRequestSettingsBreakoutRoomRooms

class MeetingsCreateMeetingRequestSettingsBreakoutRoom(RequiredMeetingsCreateMeetingRequestSettingsBreakoutRoom, OptionalMeetingsCreateMeetingRequestSettingsBreakoutRoom):
    pass
