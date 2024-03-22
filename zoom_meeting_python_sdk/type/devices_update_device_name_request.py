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


class RequiredDevicesUpdateDeviceNameRequest(TypedDict):
    # The name of the device.
    device_name: str

class OptionalDevicesUpdateDeviceNameRequest(TypedDict, total=False):
    # The name of the tag.
    tag: str

    # id of the Zoom Room.
    room_id: str

    # Device Type:    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.
    device_type: int

class DevicesUpdateDeviceNameRequest(RequiredDevicesUpdateDeviceNameRequest, OptionalDevicesUpdateDeviceNameRequest):
    pass
