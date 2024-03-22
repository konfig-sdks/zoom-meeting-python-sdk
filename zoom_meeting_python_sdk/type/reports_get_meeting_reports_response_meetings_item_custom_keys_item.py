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


class RequiredReportsGetMeetingReportsResponseMeetingsItemCustomKeysItem(TypedDict):
    pass

class OptionalReportsGetMeetingReportsResponseMeetingsItemCustomKeysItem(TypedDict, total=False):
    # The custom key name.
    key: str

    # The custom key's value.
    value: str

class ReportsGetMeetingReportsResponseMeetingsItemCustomKeysItem(RequiredReportsGetMeetingReportsResponseMeetingsItemCustomKeysItem, OptionalReportsGetMeetingReportsResponseMeetingsItemCustomKeysItem):
    pass
