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

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_settings_breakout_room_rooms import MeetingsCreateMeetingRequestSettingsBreakoutRoomRooms

class MeetingsCreateMeetingRequestSettingsBreakoutRoom(BaseModel):
    # Whether to enable the [**Breakout Room pre-assign**](https://support.zoom.us/hc/en-us/articles/360032752671-Pre-assigning-participants-to-breakout-rooms) option.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    rooms: typing.Optional[MeetingsCreateMeetingRequestSettingsBreakoutRoomRooms] = Field(None, alias='rooms')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
