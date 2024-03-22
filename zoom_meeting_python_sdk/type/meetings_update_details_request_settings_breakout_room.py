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

from zoom_meeting_python_sdk.type.meetings_update_details_request_settings_breakout_room_rooms import MeetingsUpdateDetailsRequestSettingsBreakoutRoomRooms

class RequiredMeetingsUpdateDetailsRequestSettingsBreakoutRoom(TypedDict):
    pass

class OptionalMeetingsUpdateDetailsRequestSettingsBreakoutRoom(TypedDict, total=False):
    # Set this field's value to `true` to enable the [breakout room pre-assign](https://support.zoom.us/hc/en-us/articles/360032752671-Pre-assigning-participants-to-breakout-rooms#h_36f71353-4190-48a2-b999-ca129861c1f4) option.
    enable: bool

    rooms: MeetingsUpdateDetailsRequestSettingsBreakoutRoomRooms

class MeetingsUpdateDetailsRequestSettingsBreakoutRoom(RequiredMeetingsUpdateDetailsRequestSettingsBreakoutRoom, OptionalMeetingsUpdateDetailsRequestSettingsBreakoutRoom):
    pass
