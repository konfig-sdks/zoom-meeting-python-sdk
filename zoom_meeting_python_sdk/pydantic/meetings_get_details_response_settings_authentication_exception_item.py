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


class MeetingsGetDetailsResponseSettingsAuthenticationExceptionItem(BaseModel):
    # Email address of the participant.
    email: typing.Optional[str] = Field(None, alias='email')

    # Name of the participant.
    name: typing.Optional[str] = Field(None, alias='name')

    # URL for participants to join the meeting
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
