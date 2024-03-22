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


class RequiredMeetingsBatchRegistrantsCreateResponseRegistrantsItem(TypedDict):
    pass

class OptionalMeetingsBatchRegistrantsCreateResponseRegistrantsItem(TypedDict, total=False):
    # Email address of the registrant.
    email: str

    # Unique URL using which registrant can join the meeting.
    join_url: str

    # Unique identifier of the registrant.
    registrant_id: str

    # The participant PIN code is used to authenticate audio participants before they join the meeting.
    participant_pin_code: int

class MeetingsBatchRegistrantsCreateResponseRegistrantsItem(RequiredMeetingsBatchRegistrantsCreateResponseRegistrantsItem, OptionalMeetingsBatchRegistrantsCreateResponseRegistrantsItem):
    pass
