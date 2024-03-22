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


class RequiredTspSetGlobalDialInUrlRequest(TypedDict):
    pass

class OptionalTspSetGlobalDialInUrlRequest(TypedDict, total=False):
    # The global dial-in URL for a TSP enabled account. The URL must be valid with a max-length of 512 characters.
    audio_url: str

class TspSetGlobalDialInUrlRequest(RequiredTspSetGlobalDialInUrlRequest, OptionalTspSetGlobalDialInUrlRequest):
    pass
