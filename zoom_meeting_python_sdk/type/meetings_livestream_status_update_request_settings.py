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


class RequiredMeetingsLivestreamStatusUpdateRequestSettings(TypedDict):
    pass

class OptionalMeetingsLivestreamStatusUpdateRequestSettings(TypedDict, total=False):
    # Display the name of the active speaker during a live stream.
    active_speaker_name: bool

    # Display name of the live stream.
    display_name: str

class MeetingsLivestreamStatusUpdateRequestSettings(RequiredMeetingsLivestreamStatusUpdateRequestSettings, OptionalMeetingsLivestreamStatusUpdateRequestSettings):
    pass
