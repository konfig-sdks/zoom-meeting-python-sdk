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


class RequiredReportsGetMeetingParticipantReportsResponseParticipantsItem(TypedDict):
    pass

class OptionalReportsGetMeetingParticipantReportsResponseParticipantsItem(TypedDict, total=False):
    # The participant's SDK identifier. This value can be alphanumeric, up to a maximum length of 35 characters.
    customer_key: str

    # Participant duration.
    duration: int

    # Indicates if failover happened during the meeting.
    failover: bool

    # The participant's universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the `id` value in the [**Get a user**](https://developers.zoom.us) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.   **Note:** Use the `participant_user_id` value instead of this value. We will remove this response in a future release.
    id: str

    # Participant join time.
    join_time: datetime

    # Participant leave time.
    leave_time: datetime

    # Participant display name.  This returns an empty string value if the account calling the API is a BAA account.
    name: str

    # Unique identifier of the registrant. This field is only returned if you entered &quot;registrant_id&quot; as the value of `include_fields` query parameter.
    registrant_id: str

    # The participant's status.  * `in_meeting` - In a meeting.  * `in_waiting_room` - In a waiting room.
    status: str

    # Participant email.  If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us) for details. This returns an empty string value if the account calling the API is a BAA account.
    user_email: str

    # Participant ID. This is a unique ID assigned to the participant joining a meeting and is valid for that meeting only.
    user_id: str

    # The [breakout room](https://support.zoom.us/hc/en-us/articles/206476313-Managing-breakout-rooms) ID. Each breakout room is assigned a unique ID.
    bo_mtg_id: str

    # The participant's universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the `id` value in the [**Get a user**](https://developers.zoom.us) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.
    participant_user_id: str

class ReportsGetMeetingParticipantReportsResponseParticipantsItem(RequiredReportsGetMeetingParticipantReportsResponseParticipantsItem, OptionalReportsGetMeetingParticipantReportsResponseParticipantsItem):
    pass
