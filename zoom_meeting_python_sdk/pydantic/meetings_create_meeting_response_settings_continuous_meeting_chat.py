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


class MeetingsCreateMeetingResponseSettingsContinuousMeetingChat(BaseModel):
    # Whether to enable the **Enable continuous meeting chat** setting.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    # Whether to enable the **Automatically add invited external users** setting.
    auto_add_invited_external_users: typing.Optional[bool] = Field(None, alias='auto_add_invited_external_users')

    # The channel's ID.
    channel_id: typing.Optional[str] = Field(None, alias='channel_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
