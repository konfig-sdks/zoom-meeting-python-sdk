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

from zoom_meeting_python_sdk.pydantic.tracking_field_list_response_tracking_fields import TrackingFieldListResponseTrackingFields

class TrackingFieldListResponse(BaseModel):
    # The number of all records available across pages
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    tracking_fields: typing.Optional[TrackingFieldListResponseTrackingFields] = Field(None, alias='tracking_fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
