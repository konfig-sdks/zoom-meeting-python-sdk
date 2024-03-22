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


class MeetingsBatchRegistrantsCreateRequestRegistrantsItem(BaseModel):
    # Email address of the registrant.
    email: str = Field(alias='email')

    # First name of the registrant.
    first_name: str = Field(alias='first_name')

    # Last name of the registrant.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
