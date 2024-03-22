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


class RequiredTspGetAccountInfoResponseDialInNumbersItem(TypedDict):
    pass

class OptionalTspGetAccountInfoResponseDialInNumbersItem(TypedDict, total=False):
    # Country Code
    code: str

    # Dial-in number, length is less than 16
    number: str

    # Dial-in number type.
    type: str

class TspGetAccountInfoResponseDialInNumbersItem(RequiredTspGetAccountInfoResponseDialInNumbersItem, OptionalTspGetAccountInfoResponseDialInNumbersItem):
    pass
