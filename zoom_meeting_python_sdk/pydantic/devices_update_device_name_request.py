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


class DevicesUpdateDeviceNameRequest(BaseModel):
    # The name of the device.
    device_name: str = Field(alias='device_name')

    # The name of the tag.
    tag: typing.Optional[str] = Field(None, alias='tag')

    # id of the Zoom Room.
    room_id: typing.Optional[str] = Field(None, alias='room_id')

    # Device Type:    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.
    device_type: typing.Optional[Literal[0, 1, 3]] = Field(None, alias='device_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
