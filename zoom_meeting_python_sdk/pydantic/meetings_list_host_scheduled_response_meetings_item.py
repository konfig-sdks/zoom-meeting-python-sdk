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


class MeetingsListHostScheduledResponseMeetingsItem(BaseModel):
    # Meeting description. The length of agenda gets truncated to 250 characters when you list all of a user's meetings. To view a meeting's complete agenda, or to retrieve details for a single meeting, use the [**Get a meeting**](https://developers.zoom.us) API.
    agenda: typing.Optional[str] = Field(None, alias='agenda')

    # Time of creation.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # Meeting duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # ID of the user who is set as the meeting's host.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # Meeting ID - also known as the meeting number in long (int64) format.
    id: typing.Optional[int] = Field(None, alias='id')

    # URL using which participants can join a meeting.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # [Personal meeting ID](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). This field is only returned if PMI was used to schedule the meeting.
    pmi: typing.Optional[str] = Field(None, alias='pmi')

    # Meeting start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Timezone to format the meeting start time. 
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # Meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # Meeting types.    `1` - Instant meeting.    `2` - Scheduled meeting.    `3` - Recurring meeting with no fixed time.    `8` - Recurring meeting with fixed time.
    type: typing.Optional[Literal[1, 2, 3, 8]] = Field(None, alias='type')

    # Unique Meeting ID. Each meeting instance will generate its own Meeting UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
