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


class WebinarsCreateBatchRegistrantsResponseRegistrantsItem(BaseModel):
    # The registrant's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # Unique URL using which registrant can join the webinar.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The registrant's unique identifier.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
