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


class WebinarsCreateWebinarRequestSettingsAttendeesAndPanelistsReminderEmailNotification(BaseModel):
    # * `true`: Send reminder email to attendees and panelists.  * `false`: Do not send reminder email to attendees and panelists.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    # `0` - No plan.    `1` - Send 1 hour before webinar.    `2` - Send 1 day before webinar.    `3` - Send 1 hour and 1 day before webinar.    `4` - Send 1 week before webinar.    `5` - Send 1 hour and 1 week before webinar.    `6` - Send 1 day and 1 week before webinar.    `7` - Send 1 hour, 1 day and 1 week before webinar.
    type: typing.Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
