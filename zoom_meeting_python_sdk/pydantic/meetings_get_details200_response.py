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


class MeetingsGetDetails200Response(BaseModel):
    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).
    id: typing.Optional[int] = Field(None, alias='id')

    # The meeting's UUID. You **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) this value if the meeting UUID begins with a `/` character or contains the `//` character.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The meeting's duration, in minutes.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # The meeting's start date and time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The meeting's end date and time.
    end_time: typing.Optional[datetime] = Field(None, alias='end_time')

    # The host's ID.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # The meeting host's department.
    dept: typing.Optional[str] = Field(None, alias='dept')

    # The number of meeting participants.
    participants_count: typing.Optional[int] = Field(None, alias='participants_count')

    # Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app's name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the `Zoom` value.
    source: typing.Optional[str] = Field(None, alias='source')

    # The meeting's topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # The total number of minutes attended by the meeting's host and participants.
    total_minutes: typing.Optional[int] = Field(None, alias='total_minutes')

    # The meeting type:  * `0` &mdash; A prescheduled meeting.  * `1` &mdash; An instant meeting.  * `2` &mdash; A scheduled meeting.  * `3` &mdash; A recurring meeting with no fixed time.  * `4` &mdash; A [personal meeting room](https://support.zoom.us/hc/en-us/articles/201362843).  * `7` &mdash; A [PAC (Personal Audio Conference)](https://support.zoom.us/hc/en-us/articles/205172455-Hosting-a-Personal-Audio-Conference-PAC-meeting) meeting.  * `8` &mdash; A recurring meeting with a fixed time.
    type: typing.Optional[Literal[0, 1, 2, 3, 4, 7, 8]] = Field(None, alias='type')

    # The user's email address.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # The user's display name.
    user_name: typing.Optional[str] = Field(None, alias='user_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
