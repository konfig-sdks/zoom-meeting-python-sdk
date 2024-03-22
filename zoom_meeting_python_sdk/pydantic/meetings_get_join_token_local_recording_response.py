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


class MeetingsGetJoinTokenLocalRecordingResponse(BaseModel):
    # The number of seconds the join token is valid for before it expires. This value always returns `120`.
    expire_in: typing.Optional[Literal[120]] = Field(None, alias='expire_in')

    # The join token.
    token: typing.Optional[str] = Field(None, alias='token')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
