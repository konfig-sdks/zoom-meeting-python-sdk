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


class RequiredMeetingsUpdateDetailsRequestSettingsGlobalDialInNumbersItem(TypedDict):
    pass

class OptionalMeetingsUpdateDetailsRequestSettingsGlobalDialInNumbersItem(TypedDict, total=False):
    # City of the number, if any, such as Chicago.
    city: str

    # Country code, such as BR.
    country: str

    # Full name of country, such as Brazil.
    country_name: str

    # Phone number, such as +1 2332357613.
    number: str

    # Type of number. 
    type: str

class MeetingsUpdateDetailsRequestSettingsGlobalDialInNumbersItem(RequiredMeetingsUpdateDetailsRequestSettingsGlobalDialInNumbersItem, OptionalMeetingsUpdateDetailsRequestSettingsGlobalDialInNumbersItem):
    pass
