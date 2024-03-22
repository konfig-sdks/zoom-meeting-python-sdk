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


class MeetingsCreateMeetingRequestTrackingFieldsItem(BaseModel):
    # The tracking field's label.
    field: str = Field(alias='field')

    # The tracking field's value.
    value: typing.Optional[str] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
