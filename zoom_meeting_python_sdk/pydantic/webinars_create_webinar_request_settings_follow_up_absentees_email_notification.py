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


class WebinarsCreateWebinarRequestSettingsFollowUpAbsenteesEmailNotification(BaseModel):
    # * `true` - Send follow-up email to absentees.  * `false` - Do not send follow-up email to absentees.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    # `0` - No plan.    `1` - Send 1 days after the scheduled end date.    `2` - Send 2 days after the scheduled end date.    `3` - Send 3 days after the scheduled end date.    `4` - Send 4 days after the scheduled end date.    `5` - Send 5 days after the scheduled end date.    `6` - Send 6 days after the scheduled end date.    `7` - Send 7 days after the scheduled end date.
    type: typing.Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
