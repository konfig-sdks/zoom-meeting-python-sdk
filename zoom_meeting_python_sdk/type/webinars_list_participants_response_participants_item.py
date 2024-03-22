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


class RequiredWebinarsListParticipantsResponseParticipantsItem(TypedDict):
    pass

class OptionalWebinarsListParticipantsResponseParticipantsItem(TypedDict, total=False):
    # The participant's unique identifier.
    id: str

    # The participant's name.
    name: str

    # The participant's ID. This ID is assigned to the participant upon joining the webinar and is only valid for that webinar.
    user_id: str

    # The participant's unique registrant ID. This field only returns if you pass the `registrant_id` value for the `include_fields` query parameter.   This field does not return if the `type` query parameter is the `live` value.
    registrant_id: str

    # Email address of the participant. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    user_email: str

    # The participant's join time.
    join_time: datetime

    # The participant's leave time.
    leave_time: datetime

    # The participant's attendance duration.
    duration: int

    # Whether failover occurred during the webinar.
    failover: bool

    # The participant's status.  * `in_meeting` - In a meeting.  * `in_waiting_room` - In a waiting room.
    status: str

class WebinarsListParticipantsResponseParticipantsItem(RequiredWebinarsListParticipantsResponseParticipantsItem, OptionalWebinarsListParticipantsResponseParticipantsItem):
    pass
