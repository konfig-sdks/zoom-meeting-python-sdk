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

from zoom_meeting_python_sdk.type.devices_get_zpa_version_info_response_app_versions import DevicesGetZpaVersionInfoResponseAppVersions
from zoom_meeting_python_sdk.type.devices_get_zpa_version_info_response_firmware_versions import DevicesGetZpaVersionInfoResponseFirmwareVersions

class RequiredDevicesGetZpaVersionInfoResponse(TypedDict):
    pass

class OptionalDevicesGetZpaVersionInfoResponse(TypedDict, total=False):
    firmware_versions: DevicesGetZpaVersionInfoResponseFirmwareVersions

    app_versions: DevicesGetZpaVersionInfoResponseAppVersions

class DevicesGetZpaVersionInfoResponse(RequiredDevicesGetZpaVersionInfoResponse, OptionalDevicesGetZpaVersionInfoResponse):
    pass
