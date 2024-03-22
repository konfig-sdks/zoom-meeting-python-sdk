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


class MeetingsBatchRegistrantsCreateResponseRegistrantsItem(BaseModel):
    # Email address of the registrant.
    email: typing.Optional[str] = Field(None, alias='email')

    # Unique URL using which registrant can join the meeting.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # Unique identifier of the registrant.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # The participant PIN code is used to authenticate audio participants before they join the meeting.
    participant_pin_code: typing.Optional[int] = Field(None, alias='participant_pin_code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
