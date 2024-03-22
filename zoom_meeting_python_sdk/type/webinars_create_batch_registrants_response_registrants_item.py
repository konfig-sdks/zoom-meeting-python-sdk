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


class RequiredWebinarsCreateBatchRegistrantsResponseRegistrantsItem(TypedDict):
    pass

class OptionalWebinarsCreateBatchRegistrantsResponseRegistrantsItem(TypedDict, total=False):
    # The registrant's email address.
    email: str

    # Unique URL using which registrant can join the webinar.
    join_url: str

    # The registrant's unique identifier.
    registrant_id: str

class WebinarsCreateBatchRegistrantsResponseRegistrantsItem(RequiredWebinarsCreateBatchRegistrantsResponseRegistrantsItem, OptionalWebinarsCreateBatchRegistrantsResponseRegistrantsItem):
    pass
