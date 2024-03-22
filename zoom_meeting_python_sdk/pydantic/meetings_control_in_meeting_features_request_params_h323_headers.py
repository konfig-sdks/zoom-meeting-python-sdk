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


class MeetingsControlInMeetingFeaturesRequestParamsH323Headers(BaseModel):
    # Custom name that will be used within the h323 Header.
    from_display_name: typing.Optional[str] = Field(None, alias='from_display_name')

    # Custom remote name that will be used within the meeting.
    to_display_name: typing.Optional[str] = Field(None, alias='to_display_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
