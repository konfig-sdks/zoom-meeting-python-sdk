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

from zoom_meeting_python_sdk.type.devices_list_response_devices import DevicesListResponseDevices

class RequiredDevicesListResponse(TypedDict):
    pass

class OptionalDevicesListResponse(TypedDict, total=False):
    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    next_page_token: str

    # The number of records returned within a single API call.
    page_size: int

    devices: DevicesListResponseDevices

class DevicesListResponse(RequiredDevicesListResponse, OptionalDevicesListResponse):
    pass
