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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class ReportsGetMeetingParticipantReportsResponseParticipantsItem(BaseModel):
    # The participant's SDK identifier. This value can be alphanumeric, up to a maximum length of 35 characters.
    customer_key: typing.Optional[str] = Field(None, alias='customer_key')

    # Participant duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Indicates if failover happened during the meeting.
    failover: typing.Optional[bool] = Field(None, alias='failover')

    # The participant's universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the `id` value in the [**Get a user**](https://developers.zoom.us) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.   **Note:** Use the `participant_user_id` value instead of this value. We will remove this response in a future release.
    id: typing.Optional[str] = Field(None, alias='id')

    # Participant join time.
    join_time: typing.Optional[datetime] = Field(None, alias='join_time')

    # Participant leave time.
    leave_time: typing.Optional[datetime] = Field(None, alias='leave_time')

    # Participant display name.  This returns an empty string value if the account calling the API is a BAA account.
    name: typing.Optional[str] = Field(None, alias='name')

    # Unique identifier of the registrant. This field is only returned if you entered &quot;registrant_id&quot; as the value of `include_fields` query parameter.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # The participant's status.  * `in_meeting` - In a meeting.  * `in_waiting_room` - In a waiting room.
    status: typing.Optional[Literal["in_meeting", "in_waiting_room"]] = Field(None, alias='status')

    # Participant email.  If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us) for details. This returns an empty string value if the account calling the API is a BAA account.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # Participant ID. This is a unique ID assigned to the participant joining a meeting and is valid for that meeting only.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # The [breakout room](https://support.zoom.us/hc/en-us/articles/206476313-Managing-breakout-rooms) ID. Each breakout room is assigned a unique ID.
    bo_mtg_id: typing.Optional[str] = Field(None, alias='bo_mtg_id')

    # The participant's universally unique ID (UUID).  * If the participant joins the meeting by logging into Zoom, this value is the `id` value in the [**Get a user**](https://developers.zoom.us) API response.  * If the participant joins the meeting **without** logging into Zoom, this returns an empty string value.
    participant_user_id: typing.Optional[str] = Field(None, alias='participant_user_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
