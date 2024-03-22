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


class MeetingsGetPastMeetingParticipantsResponseParticipantsItem(BaseModel):
    # Universally unique identifier of the Participant. It is the same as the User ID of the participant if the participant joins the meeting by logging into Zoom. If the participant joins the meeting without logging in, the value of this field will be blank.
    id: typing.Optional[str] = Field(None, alias='id')

    # Participant display name.
    name: typing.Optional[str] = Field(None, alias='name')

    # Participant ID. This is a unique ID assigned to the participant joining a meeting and is valid for that meeting only.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # The participant's unique registrant ID. This field only returns if you pass the `registrant_id` value for the `include_fields` query parameter.   This field does not return if the `type` query parameter is the `live` value.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # Email address of the user. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # Participant join time.
    join_time: typing.Optional[datetime] = Field(None, alias='join_time')

    # Participant leave time.
    leave_time: typing.Optional[datetime] = Field(None, alias='leave_time')

    # Participant duration. Duration, in seconds, calculated by subtracting the `leave_time` from the `join_time` for the `user_id`. If the participant leaves and rejoins the same meeting, they will be assigned a different `user_id` and Zoom displays their new duration in a separate object. Note that because of this, the duration may not reflect the total time the user was in the meeting.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Indicates if failover happened during the meeting.
    failover: typing.Optional[bool] = Field(None, alias='failover')

    # The participant's status.  * `in_meeting` - In a meeting.  * `in_waiting_room` - In a waiting room.
    status: typing.Optional[Literal["in_meeting", "in_waiting_room"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
