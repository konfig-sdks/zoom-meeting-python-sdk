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


class RequiredWebinarsCreateWebinarRequestTrackingFieldsItem(TypedDict):
    # Tracking fields type.
    field: str

class OptionalWebinarsCreateWebinarRequestTrackingFieldsItem(TypedDict, total=False):
    # Tracking fields value.
    value: str

class WebinarsCreateWebinarRequestTrackingFieldsItem(RequiredWebinarsCreateWebinarRequestTrackingFieldsItem, OptionalWebinarsCreateWebinarRequestTrackingFieldsItem):
    pass
