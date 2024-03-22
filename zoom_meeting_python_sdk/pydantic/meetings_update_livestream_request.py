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


class MeetingsUpdateLivestreamRequest(BaseModel):
    # The live stream page URL.
    page_url: str = Field(alias='page_url')

    # Stream name and key.
    stream_key: str = Field(alias='stream_key')

    # Streaming URL.
    stream_url: str = Field(alias='stream_url')

    # The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`
    resolution: typing.Optional[str] = Field(None, alias='resolution')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
