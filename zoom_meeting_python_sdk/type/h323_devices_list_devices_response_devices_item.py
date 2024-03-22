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


class RequiredH323DevicesListDevicesResponseDevicesItem(TypedDict):
    # Device encryption:    `auto` - auto.    `yes` - yes.    `no` - no.
    encryption: str

    # Device IP.
    ip: str

    # Device name.
    name: str

    # Device protocol:    `H.323` - H.323.    `SIP` - SIP.
    protocol: str

class OptionalH323DevicesListDevicesResponseDevicesItem(TypedDict, total=False):
    # Device ID.
    id: str

class H323DevicesListDevicesResponseDevicesItem(RequiredH323DevicesListDevicesResponseDevicesItem, OptionalH323DevicesListDevicesResponseDevicesItem):
    pass
