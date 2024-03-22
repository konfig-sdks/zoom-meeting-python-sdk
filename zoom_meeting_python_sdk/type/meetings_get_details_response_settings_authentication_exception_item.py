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


class RequiredMeetingsGetDetailsResponseSettingsAuthenticationExceptionItem(TypedDict):
    pass

class OptionalMeetingsGetDetailsResponseSettingsAuthenticationExceptionItem(TypedDict, total=False):
    # Email address of the participant.
    email: str

    # Name of the participant.
    name: str

    # URL for participants to join the meeting
    join_url: str

class MeetingsGetDetailsResponseSettingsAuthenticationExceptionItem(RequiredMeetingsGetDetailsResponseSettingsAuthenticationExceptionItem, OptionalMeetingsGetDetailsResponseSettingsAuthenticationExceptionItem):
    pass
