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


class MeetingsCreateTemplateFromMeetingRequest(BaseModel):
    # The meeting ID aka the meeting number in long (int64) format.
    meeting_id: typing.Optional[int] = Field(None, alias='meeting_id')

    # The template name.
    name: typing.Optional[str] = Field(None, alias='name')

    # If the field is set to true, the recurrence meeting template will be saved as the scheduled meeting.
    save_recurrence: typing.Optional[bool] = Field(None, alias='save_recurrence')

    # Overwrite an existing meeting template if the template is created from same existing meeting.
    overwrite: typing.Optional[bool] = Field(None, alias='overwrite')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
