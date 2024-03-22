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


class RequiredTspAddUserTspAccountResponseDialInNumbersItem(TypedDict):
    pass

class OptionalTspAddUserTspAccountResponseDialInNumbersItem(TypedDict, total=False):
    # Country code.
    code: str

    # Country Label, if passed, will display in place of code.
    country_label: str

    # Dial-in number: length is less than 16.
    number: str

    # Dial-in number types:    `toll` - Toll number.    `tollfree` -Toll free number.     `media_link` - Media link.
    type: str

class TspAddUserTspAccountResponseDialInNumbersItem(RequiredTspAddUserTspAccountResponseDialInNumbersItem, OptionalTspAddUserTspAccountResponseDialInNumbersItem):
    pass
