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

from zoom_meeting_python_sdk.pydantic.meetings_add_registrant_response_occurrences import MeetingsAddRegistrantResponseOccurrences

class MeetingsAddRegistrantResponse(BaseModel):
    # The meeting ID.
    id: typing.Optional[int] = Field(None, alias='id')

    # The URL the registrant can use to join the meeting.   The API will not return this field if the meeting was [created](https://developers.zoom.us) with the `approval_type` field value of `1` (manual approval).
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The registrant's ID.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # The meeting's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The meeting's topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    occurrences: typing.Optional[MeetingsAddRegistrantResponseOccurrences] = Field(None, alias='occurrences')

    # The participant PIN code is used to authenticate audio participants before they join the meeting.
    participant_pin_code: typing.Optional[int] = Field(None, alias='participant_pin_code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
