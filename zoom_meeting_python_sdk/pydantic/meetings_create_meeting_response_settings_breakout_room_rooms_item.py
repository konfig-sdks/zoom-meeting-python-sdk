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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_breakout_room_rooms_item_participants import MeetingsCreateMeetingResponseSettingsBreakoutRoomRoomsItemParticipants

class MeetingsCreateMeetingResponseSettingsBreakoutRoomRoomsItem(BaseModel):
    # The breakout room's name.
    name: typing.Optional[str] = Field(None, alias='name')

    participants: typing.Optional[MeetingsCreateMeetingResponseSettingsBreakoutRoomRoomsItemParticipants] = Field(None, alias='participants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
