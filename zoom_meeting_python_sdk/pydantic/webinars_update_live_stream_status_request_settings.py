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


class WebinarsUpdateLiveStreamStatusRequestSettings(BaseModel):
    # Display the name of the active speaker during a live stream.
    active_speaker_name: typing.Optional[bool] = Field(None, alias='active_speaker_name')

    # Display the live stream's name.
    display_name: typing.Optional[str] = Field(None, alias='display_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
