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


class RequiredDevicesCreateNewDeviceRequest(TypedDict):
    # The device's name.
    device_name: str

    # The device's mac address.
    mac_address: str

    # The device's serial number.
    serial_number: str

    # The device's manufacturer.
    vendor: str

    # The device's model.
    model: str

    # Device type.    `0` - Zoom Rooms computer.    `1` - Zoom Rooms controller.    `5` - Zoom Phone appliance.
    device_type: int

class OptionalDevicesCreateNewDeviceRequest(TypedDict, total=False):
    # The Zoom Room's ID. Only for Zoom Room devices.
    room_id: str

    # User email for assigning the Zoom Phone device. Only for Zoom Phone devices.
    user_email: str

    # The name of the tag.
    tag: str

    # The ZDM group ID.
    zdm_group_id: str

    # The extension number.
    extension_number: str

class DevicesCreateNewDeviceRequest(RequiredDevicesCreateNewDeviceRequest, OptionalDevicesCreateNewDeviceRequest):
    pass
