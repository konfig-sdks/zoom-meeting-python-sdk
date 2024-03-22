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

from zoom_meeting_python_sdk.type.tracking_field_list_response_tracking_fields_item_recommended_values import TrackingFieldListResponseTrackingFieldsItemRecommendedValues

class RequiredTrackingFieldListResponseTrackingFieldsItem(TypedDict):
    pass

class OptionalTrackingFieldListResponseTrackingFieldsItem(TypedDict, total=False):
    # ID of Tracking Field
    id: str

    # Label/ Name for the tracking field.
    field: str

    recommended_values: TrackingFieldListResponseTrackingFieldsItemRecommendedValues

    # Tracking Field Required
    required: bool

    # Tracking Field Visible
    visible: bool

class TrackingFieldListResponseTrackingFieldsItem(RequiredTrackingFieldListResponseTrackingFieldsItem, OptionalTrackingFieldListResponseTrackingFieldsItem):
    pass
