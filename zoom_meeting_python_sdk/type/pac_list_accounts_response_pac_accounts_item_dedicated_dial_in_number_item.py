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


class RequiredPacListAccountsResponsePacAccountsItemDedicatedDialInNumberItem(TypedDict):
    pass

class OptionalPacListAccountsResponsePacAccountsItemDedicatedDialInNumberItem(TypedDict, total=False):
    # The dial-in country code.
    country: str

    # The dial-in number.
    number: str

class PacListAccountsResponsePacAccountsItemDedicatedDialInNumberItem(RequiredPacListAccountsResponsePacAccountsItemDedicatedDialInNumberItem, OptionalPacListAccountsResponsePacAccountsItemDedicatedDialInNumberItem):
    pass
