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


class RequiredMeetingsGetDetailsResponseSettingsGlobalDialInNumbersItem(TypedDict):
    pass

class OptionalMeetingsGetDetailsResponseSettingsGlobalDialInNumbersItem(TypedDict, total=False):
    # City of the number, if any. For example, Chicago.
    city: str

    # Country code. For example, BR.
    country: str

    # Full name of country. For example, Brazil.
    country_name: str

    # Phone number. For example, +1 2332357613.
    number: str

    # Type of number. 
    type: str

class MeetingsGetDetailsResponseSettingsGlobalDialInNumbersItem(RequiredMeetingsGetDetailsResponseSettingsGlobalDialInNumbersItem, OptionalMeetingsGetDetailsResponseSettingsGlobalDialInNumbersItem):
    pass
