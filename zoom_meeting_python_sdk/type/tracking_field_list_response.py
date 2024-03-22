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

from zoom_meeting_python_sdk.type.tracking_field_list_response_tracking_fields import TrackingFieldListResponseTrackingFields

class RequiredTrackingFieldListResponse(TypedDict):
    pass

class OptionalTrackingFieldListResponse(TypedDict, total=False):
    # The number of all records available across pages
    total_records: int

    tracking_fields: TrackingFieldListResponseTrackingFields

class TrackingFieldListResponse(RequiredTrackingFieldListResponse, OptionalTrackingFieldListResponse):
    pass
