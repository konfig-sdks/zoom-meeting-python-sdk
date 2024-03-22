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


class RequiredDevicesGetDetailResponse(TypedDict):
    pass

class OptionalDevicesGetDetailResponse(TypedDict, total=False):
    # The device's unique identifier.
    device_id: str

    # The name of the device.
    device_name: str

    # The device's MAC address.
    mac_address: str

    # The device's serial number.
    serial_number: str

    # The device's manufacturer.
    vendor: str

    # The device's model.
    model: str

    # The device's platform.
    platform_os: str

    # App version of Zoom Rooms.
    app_version: str

    # The tag's name.
    tag: str

    # Whether the device is enrolled in ZDM (Zoom Device Management).
    enrolled_in_zdm: bool

    # Whether the device is connected to ZDM (Zoom Device Management).
    connected_to_zdm: bool

    # The Zoom Room's ID.
    room_id: str

    # The Zoom Room's name.
    room_name: str

    # Filter devices by device type.   Device Type:    `-1` - All Zoom Room device(0,1,2,3,4,6).    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.    `3` - Zoom Rooms Control System.    `4` - Zoom Rooms Whiteboard.    `5` - Zoom Phone Appliance.    `6` - Zoom Rooms Computer (with Controller).
    device_type: int

    # The SDK version.
    sdk_version: str

    # Filter devices by status.    Device Status:    `0` - offline.    `1` - online.    `-1` - unlink
    device_status: int

    # The time when the device was last online.
    last_online: str

    # The phone device's owner.
    user_email: str

class DevicesGetDetailResponse(RequiredDevicesGetDetailResponse, OptionalDevicesGetDetailResponse):
    pass
