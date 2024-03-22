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


class RequiredDevicesChangeDeviceAssociationRequest(TypedDict):
    pass

class OptionalDevicesChangeDeviceAssociationRequest(TypedDict, total=False):
    # The Zoom Room ID which device is being associated to. The `room_id` is required when `assign` is selected for `action` field.
    room_id: str

    # Specify one of the following values for this field:  `ZR`: Zoom Room Computer.     `ZRC`: Zoom Room Controller.     `ZRP`: Scheduling Display.     `ZRW`: Companion Whiteboard.
    app_type: str

class DevicesChangeDeviceAssociationRequest(RequiredDevicesChangeDeviceAssociationRequest, OptionalDevicesChangeDeviceAssociationRequest):
    pass
