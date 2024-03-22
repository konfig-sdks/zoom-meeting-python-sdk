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

from zoom_meeting_python_sdk.type.devices_list_zdm_group_info_response_groups import DevicesListZdmGroupInfoResponseGroups

class RequiredDevicesListZdmGroupInfoResponse(TypedDict):
    pass

class OptionalDevicesListZdmGroupInfoResponse(TypedDict, total=False):
    groups: DevicesListZdmGroupInfoResponseGroups

    # Use the next page token to paginate through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: str

    # The total number of records returned from a single API call.
    page_size: int

class DevicesListZdmGroupInfoResponse(RequiredDevicesListZdmGroupInfoResponse, OptionalDevicesListZdmGroupInfoResponse):
    pass
