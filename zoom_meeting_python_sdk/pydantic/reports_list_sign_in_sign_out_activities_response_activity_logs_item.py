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


class ReportsListSignInSignOutActivitiesResponseActivityLogsItem(BaseModel):
    # Zoom client version of the user.
    version: typing.Optional[str] = Field(None, alias='version')

    # The client interface type using which the activity was performed.
    client_type: typing.Optional[str] = Field(None, alias='client_type')

    # Email address of the user used for the activity.
    email: typing.Optional[str] = Field(None, alias='email')

    # The IP address of the user's device.
    ip_address: typing.Optional[str] = Field(None, alias='ip_address')

    # Time during which the activity occurred.
    time: typing.Optional[datetime] = Field(None, alias='time')

    # The type of activity.  * `Sign in` &mdash; Sign in activity by user.  * `Sign out` &mdash; Sign out activity by user.
    type: typing.Optional[Literal["Sign in", "Sign out"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
