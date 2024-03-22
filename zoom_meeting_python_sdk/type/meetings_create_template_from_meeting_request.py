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


class RequiredMeetingsCreateTemplateFromMeetingRequest(TypedDict):
    pass

class OptionalMeetingsCreateTemplateFromMeetingRequest(TypedDict, total=False):
    # The meeting ID aka the meeting number in long (int64) format.
    meeting_id: int

    # The template name.
    name: str

    # If the field is set to true, the recurrence meeting template will be saved as the scheduled meeting.
    save_recurrence: bool

    # Overwrite an existing meeting template if the template is created from same existing meeting.
    overwrite: bool

class MeetingsCreateTemplateFromMeetingRequest(RequiredMeetingsCreateTemplateFromMeetingRequest, OptionalMeetingsCreateTemplateFromMeetingRequest):
    pass
