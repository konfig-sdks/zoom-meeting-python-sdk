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


class DevicesGetDetailResponse(BaseModel):
    # The device's unique identifier.
    device_id: typing.Optional[str] = Field(None, alias='device_id')

    # The name of the device.
    device_name: typing.Optional[str] = Field(None, alias='device_name')

    # The device's MAC address.
    mac_address: typing.Optional[str] = Field(None, alias='mac_address')

    # The device's serial number.
    serial_number: typing.Optional[str] = Field(None, alias='serial_number')

    # The device's manufacturer.
    vendor: typing.Optional[str] = Field(None, alias='vendor')

    # The device's model.
    model: typing.Optional[str] = Field(None, alias='model')

    # The device's platform.
    platform_os: typing.Optional[str] = Field(None, alias='platform_os')

    # App version of Zoom Rooms.
    app_version: typing.Optional[str] = Field(None, alias='app_version')

    # The tag's name.
    tag: typing.Optional[str] = Field(None, alias='tag')

    # Whether the device is enrolled in ZDM (Zoom Device Management).
    enrolled_in_zdm: typing.Optional[bool] = Field(None, alias='enrolled_in_zdm')

    # Whether the device is connected to ZDM (Zoom Device Management).
    connected_to_zdm: typing.Optional[bool] = Field(None, alias='connected_to_zdm')

    # The Zoom Room's ID.
    room_id: typing.Optional[str] = Field(None, alias='room_id')

    # The Zoom Room's name.
    room_name: typing.Optional[str] = Field(None, alias='room_name')

    # Filter devices by device type.   Device Type:    `-1` - All Zoom Room device(0,1,2,3,4,6).    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.    `3` - Zoom Rooms Control System.    `4` - Zoom Rooms Whiteboard.    `5` - Zoom Phone Appliance.    `6` - Zoom Rooms Computer (with Controller).
    device_type: typing.Optional[Literal[0, 1, 2, 3, 4, 5, 6]] = Field(None, alias='device_type')

    # The SDK version.
    sdk_version: typing.Optional[str] = Field(None, alias='sdk_version')

    # Filter devices by status.    Device Status:    `0` - offline.    `1` - online.    `-1` - unlink
    device_status: typing.Optional[Literal[-1, 0, 1]] = Field(None, alias='device_status')

    # The time when the device was last online.
    last_online: typing.Optional[str] = Field(None, alias='last_online')

    # The phone device's owner.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
