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


class RequiredCloudRecordingUpdateRegistrantStatusRequestRegistrantsItem(TypedDict):
    pass

class OptionalCloudRecordingUpdateRegistrantStatusRequestRegistrantsItem(TypedDict, total=False):
    id: str

class CloudRecordingUpdateRegistrantStatusRequestRegistrantsItem(RequiredCloudRecordingUpdateRegistrantStatusRequestRegistrantsItem, OptionalCloudRecordingUpdateRegistrantStatusRequestRegistrantsItem):
    pass
