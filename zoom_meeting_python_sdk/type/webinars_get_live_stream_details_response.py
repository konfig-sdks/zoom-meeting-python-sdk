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


class RequiredWebinarsGetLiveStreamDetailsResponse(TypedDict):
    pass

class OptionalWebinarsGetLiveStreamDetailsResponse(TypedDict, total=False):
    # Live streaming page URL. This is the URL using which anyone can view the live stream of the webinar.
    page_url: str

    # Stream key.
    stream_key: str

    # Stream URL.
    stream_url: str

    # The number of pixels in each dimension that the video camera can display.
    resolution: str

class WebinarsGetLiveStreamDetailsResponse(RequiredWebinarsGetLiveStreamDetailsResponse, OptionalWebinarsGetLiveStreamDetailsResponse):
    pass
