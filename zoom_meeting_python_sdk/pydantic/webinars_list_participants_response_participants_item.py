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


class WebinarsListParticipantsResponseParticipantsItem(BaseModel):
    # The participant's unique identifier.
    id: typing.Optional[str] = Field(None, alias='id')

    # The participant's name.
    name: typing.Optional[str] = Field(None, alias='name')

    # The participant's ID. This ID is assigned to the participant upon joining the webinar and is only valid for that webinar.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # The participant's unique registrant ID. This field only returns if you pass the `registrant_id` value for the `include_fields` query parameter.   This field does not return if the `type` query parameter is the `live` value.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # Email address of the participant. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # The participant's join time.
    join_time: typing.Optional[datetime] = Field(None, alias='join_time')

    # The participant's leave time.
    leave_time: typing.Optional[datetime] = Field(None, alias='leave_time')

    # The participant's attendance duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Whether failover occurred during the webinar.
    failover: typing.Optional[bool] = Field(None, alias='failover')

    # The participant's status.  * `in_meeting` - In a meeting.  * `in_waiting_room` - In a waiting room.
    status: typing.Optional[Literal["in_meeting", "in_waiting_room"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
