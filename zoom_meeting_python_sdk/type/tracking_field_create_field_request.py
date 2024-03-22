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

from zoom_meeting_python_sdk.type.tracking_field_create_field_request_recommended_values import TrackingFieldCreateFieldRequestRecommendedValues

class RequiredTrackingFieldCreateFieldRequest(TypedDict):
    pass

class OptionalTrackingFieldCreateFieldRequest(TypedDict, total=False):
    # Label/ Name for the tracking field.
    field: str

    recommended_values: TrackingFieldCreateFieldRequestRecommendedValues

    # Tracking Field Required
    required: bool

    # Tracking Field Visible
    visible: bool

class TrackingFieldCreateFieldRequest(RequiredTrackingFieldCreateFieldRequest, OptionalTrackingFieldCreateFieldRequest):
    pass
