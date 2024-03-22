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


class RequiredDevicesListZdmGroupInfoResponseGroupsItem(TypedDict):
    pass

class OptionalDevicesListZdmGroupInfoResponseGroupsItem(TypedDict, total=False):
    # The ZDM group's describe.
    description: str

    # The ZDM group's unique ID.
    zdm_group_id: str

    # The ZDM group's name.
    name: str

class DevicesListZdmGroupInfoResponseGroupsItem(RequiredDevicesListZdmGroupInfoResponseGroupsItem, OptionalDevicesListZdmGroupInfoResponseGroupsItem):
    pass
