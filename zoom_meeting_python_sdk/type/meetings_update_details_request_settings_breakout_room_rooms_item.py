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

from zoom_meeting_python_sdk.type.meetings_update_details_request_settings_breakout_room_rooms_item_participants import MeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItemParticipants

class RequiredMeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItem(TypedDict):
    pass

class OptionalMeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItem(TypedDict, total=False):
    # The breakout room's name.
    name: str

    participants: MeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItemParticipants

class MeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItem(RequiredMeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItem, OptionalMeetingsUpdateDetailsRequestSettingsBreakoutRoomRoomsItem):
    pass
