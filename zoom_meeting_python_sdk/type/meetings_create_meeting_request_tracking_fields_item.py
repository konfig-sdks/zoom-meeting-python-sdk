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


class RequiredMeetingsCreateMeetingRequestTrackingFieldsItem(TypedDict):
    # The tracking field's label.
    field: str

class OptionalMeetingsCreateMeetingRequestTrackingFieldsItem(TypedDict, total=False):
    # The tracking field's value.
    value: str

class MeetingsCreateMeetingRequestTrackingFieldsItem(RequiredMeetingsCreateMeetingRequestTrackingFieldsItem, OptionalMeetingsCreateMeetingRequestTrackingFieldsItem):
    pass
