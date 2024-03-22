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


class RequiredDevicesAssignDeviceZpaAssignmentRequest(TypedDict):
    # The device's mac address.
    mac_address: str

    # The device's manufacturer.
    vendor: str

class OptionalDevicesAssignDeviceZpaAssignmentRequest(TypedDict, total=False):
    # The extension number.
    extension_number: str

class DevicesAssignDeviceZpaAssignmentRequest(RequiredDevicesAssignDeviceZpaAssignmentRequest, OptionalDevicesAssignDeviceZpaAssignmentRequest):
    pass
