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


class RequiredMeetingsCreateMeetingResponseTrackingFieldsItem(TypedDict):
    pass

class OptionalMeetingsCreateMeetingResponseTrackingFieldsItem(TypedDict, total=False):
    # The tracking field's label.
    field: str

    # The tracking field's value.
    value: str

    # Indicates whether the [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) is visible in the meeting scheduling options in the Zoom Web Portal or not.  `true`: Tracking field is visible.       `false`: Tracking field is not visible to the users in the meeting options in the Zoom Web Portal but the field was used while scheduling this meeting via API. An invisible tracking field can be used by users while scheduling meetings via API only. 
    visible: bool

class MeetingsCreateMeetingResponseTrackingFieldsItem(RequiredMeetingsCreateMeetingResponseTrackingFieldsItem, OptionalMeetingsCreateMeetingResponseTrackingFieldsItem):
    pass
