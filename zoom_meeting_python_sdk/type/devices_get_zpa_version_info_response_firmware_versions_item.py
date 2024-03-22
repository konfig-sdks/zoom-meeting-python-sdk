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


class RequiredDevicesGetZpaVersionInfoResponseFirmwareVersionsItem(TypedDict):
    pass

class OptionalDevicesGetZpaVersionInfoResponseFirmwareVersionsItem(TypedDict, total=False):
    # The package version.
    version: str

    # The device's manufacturer.
    vendor: str

    # The device's model name.
    model: str

    # The prompt information for this version.
    warn_info: str

class DevicesGetZpaVersionInfoResponseFirmwareVersionsItem(RequiredDevicesGetZpaVersionInfoResponseFirmwareVersionsItem, OptionalDevicesGetZpaVersionInfoResponseFirmwareVersionsItem):
    pass
