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


class MeetingsGetDetailsResponseTrackingFieldsItem(BaseModel):
    # The tracking field's label.
    field: typing.Optional[str] = Field(None, alias='field')

    # The tracking field's value.
    value: typing.Optional[str] = Field(None, alias='value')

    # Indicates whether the [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) is visible in the meeting scheduling options in the Zoom Web Portal or not.  `true`: Tracking field is visible.       `false`: Tracking field is not visible to the users when they look at the meeting details in the Zoom Web Portal but the field was used while scheduling this meeting via API. An invisible tracking field can be used by users while scheduling meetings via API only. 
    visible: typing.Optional[bool] = Field(None, alias='visible')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
