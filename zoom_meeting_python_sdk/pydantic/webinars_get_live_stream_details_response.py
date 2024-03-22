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


class WebinarsGetLiveStreamDetailsResponse(BaseModel):
    # Live streaming page URL. This is the URL using which anyone can view the live stream of the webinar.
    page_url: typing.Optional[str] = Field(None, alias='page_url')

    # Stream key.
    stream_key: typing.Optional[str] = Field(None, alias='stream_key')

    # Stream URL.
    stream_url: typing.Optional[str] = Field(None, alias='stream_url')

    # The number of pixels in each dimension that the video camera can display.
    resolution: typing.Optional[str] = Field(None, alias='resolution')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
