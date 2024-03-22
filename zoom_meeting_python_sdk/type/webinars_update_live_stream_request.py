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


class RequiredWebinarsUpdateLiveStreamRequest(TypedDict):
    # The webinar live stream page's URL.
    page_url: str

    # The webinar live stream name and key.
    stream_key: str

    # The webinar live stream URL.
    stream_url: str

class OptionalWebinarsUpdateLiveStreamRequest(TypedDict, total=False):
    # The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`
    resolution: str

class WebinarsUpdateLiveStreamRequest(RequiredWebinarsUpdateLiveStreamRequest, OptionalWebinarsUpdateLiveStreamRequest):
    pass
