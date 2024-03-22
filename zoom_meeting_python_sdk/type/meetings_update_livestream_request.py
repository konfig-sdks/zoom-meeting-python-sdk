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


class RequiredMeetingsUpdateLivestreamRequest(TypedDict):
    # The live stream page URL.
    page_url: str

    # Stream name and key.
    stream_key: str

    # Streaming URL.
    stream_url: str

class OptionalMeetingsUpdateLivestreamRequest(TypedDict, total=False):
    # The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`
    resolution: str

class MeetingsUpdateLivestreamRequest(RequiredMeetingsUpdateLivestreamRequest, OptionalMeetingsUpdateLivestreamRequest):
    pass
