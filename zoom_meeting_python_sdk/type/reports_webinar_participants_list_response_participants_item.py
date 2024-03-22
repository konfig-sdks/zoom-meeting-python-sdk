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


class RequiredReportsWebinarParticipantsListResponseParticipantsItem(TypedDict):
    pass

class OptionalReportsWebinarParticipantsListResponseParticipantsItem(TypedDict, total=False):
    # The participant's SDK identifier. This value can be alphanumeric, up to a maximum length of 35 characters.
    customer_key: str

    # The participant's attendance duration.
    duration: int

    # Whether failover occurred during the webinar.
    failover: bool

    # The participant's universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the `id` value in the [**Get a user**](https://developers.zoom.us) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.   **Note:** Use the `participant_user_id` value instead of this value. We will remove this response in a future release.
    id: str

    # The participant's join time.
    join_time: datetime

    # The participant's leave time.
    leave_time: datetime

    # The participant's display name. This returns an empty string value if the account calling the API is a BAA account.
    name: str

    # The registrant's ID. This field only returns if you provide the `registrant_id` value for the `include_fields` query parameter.
    registrant_id: str

    # The participant's status.  * `in_meeting` - In a meeting.  * `in_waiting_room` - In a waiting room.
    status: str

    # The participant's email address. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us) for details. This returns an empty string value if the account calling the API is a BAA account.
    user_email: str

    # The participant's ID. This ID is assigned to the participant upon joining the webinar and is only valid for that webinar.
    user_id: str

    # The participant's universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the `id` value in the [**Get a user**](https://developers.zoom.us) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.
    participant_user_id: str

class ReportsWebinarParticipantsListResponseParticipantsItem(RequiredReportsWebinarParticipantsListResponseParticipantsItem, OptionalReportsWebinarParticipantsListResponseParticipantsItem):
    pass
