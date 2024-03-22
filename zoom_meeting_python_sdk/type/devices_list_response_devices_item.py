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


class RequiredDevicesListResponseDevicesItem(TypedDict):
    pass

class OptionalDevicesListResponseDevicesItem(TypedDict, total=False):
    # Unique identifier of the device.
    device_id: str

    # The name of the device.
    device_name: str

    # The mac address of the device.
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

    # The name of the tag.
    tag: str

    # Whether the device enrolled in ZDM (Zoom Device Management).
    enrolled_in_zdm: bool

    # Whether the device connected to ZDM (Zoom Device Management).
    connected_to_zdm: bool

    # id of the Zoom Room.
    room_id: str

    # Name of the Zoom Room.
    room_name: str

    # Filter devices by device type.     Device Type:    `-1` - All Zoom Room device(0,1,2,3,4,6).    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.    `3` - Zoom Rooms Control System.    `4` -  Zoom Rooms Whiteboard.    `5` - Zoom Phone Appliance.    `6` - Zoom Rooms Computer (with Controller).
    device_type: int

    # The version of the SDK.
    skd_version: str

    # Filter devices by status.      Device Status:    `0` - offline.    `1` - online.    `-1` - unlink
    device_status: int

    # The time when device was online last time.
    last_online: str

    # The owner of the phone device
    user_email: str

class DevicesListResponseDevicesItem(RequiredDevicesListResponseDevicesItem, OptionalDevicesListResponseDevicesItem):
    pass
