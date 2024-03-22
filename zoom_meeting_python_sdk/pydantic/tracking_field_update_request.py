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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from zoom_meeting_python_sdk.pydantic.tracking_field_update_request_recommended_values import TrackingFieldUpdateRequestRecommendedValues

class TrackingFieldUpdateRequest(BaseModel):
    # Label/ Name for the tracking field.
    field: typing.Optional[str] = Field(None, alias='field')

    recommended_values: typing.Optional[TrackingFieldUpdateRequestRecommendedValues] = Field(None, alias='recommended_values')

    # Tracking Field Required
    required: typing.Optional[bool] = Field(None, alias='required')

    # Tracking Field Visible
    visible: typing.Optional[bool] = Field(None, alias='visible')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
