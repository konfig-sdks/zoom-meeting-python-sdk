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


class RequiredDevicesUpgradeZpaOsAppRequest(TypedDict):
    # The ZDM group ID.
    zdm_group_id: str

    data: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

class OptionalDevicesUpgradeZpaOsAppRequest(TypedDict, total=False):
    pass

class DevicesUpgradeZpaOsAppRequest(RequiredDevicesUpgradeZpaOsAppRequest, OptionalDevicesUpgradeZpaOsAppRequest):
    pass
