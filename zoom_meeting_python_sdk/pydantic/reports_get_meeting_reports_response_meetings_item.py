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

from zoom_meeting_python_sdk.pydantic.reports_get_meeting_reports_response_meetings_item_custom_keys import ReportsGetMeetingReportsResponseMeetingsItemCustomKeys

class ReportsGetMeetingReportsResponseMeetingsItem(BaseModel):
    custom_keys: typing.Optional[ReportsGetMeetingReportsResponseMeetingsItemCustomKeys] = Field(None, alias='custom_keys')

    # The meeting's duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # The meeting's end date and time.
    end_time: typing.Optional[datetime] = Field(None, alias='end_time')

    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).
    id: typing.Optional[int] = Field(None, alias='id')

    # The number of meeting participants.
    participants_count: typing.Optional[int] = Field(None, alias='participants_count')

    # The Video SDK custom session ID.
    session_key: typing.Optional[str] = Field(None, alias='session_key')

    # Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app's name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the `Zoom` value.
    source: typing.Optional[str] = Field(None, alias='source')

    # The meeting's start date and time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The meeting's topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # The sum of meeting minutes from all meeting participants in the meeting.
    total_minutes: typing.Optional[int] = Field(None, alias='total_minutes')

    # The type of meeting or webinar.   meeting:  * `1` &mdash; Instant meeting.  * `2` &mdash; Scheduled meeting.  * `3` &mdash; A recurring meeting with no fixed time.  * `4` &mdash; A meeting created via PMI (Personal Meeting ID).  * `7` &mdash; A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.   webinar:  * `5` &mdash; A webinar.  * `6` &mdash; A recurring webinar without a fixed time  * `9` &mdash; A recurring webinar with a fixed time. 
    type: typing.Optional[Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]] = Field(None, alias='type')

    # The user's email address.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # The user's display name.
    user_name: typing.Optional[str] = Field(None, alias='user_name')

    # The meeting's universally unique identifier (UUID). Each meeting instance generates a meeting UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The meeting's scheduled date and time.
    schedule_time: typing.Optional[str] = Field(None, alias='schedule_time')

    # The date and time at which the attendee joined the waiting room.
    join_waiting_room_time: typing.Optional[str] = Field(None, alias='join_waiting_room_time')

    # The date and time at which the attendee joined the meeting.
    join_time: typing.Optional[str] = Field(None, alias='join_time')

    # The date and time at which the attendee left the meeting.
    leave_time: typing.Optional[str] = Field(None, alias='leave_time')

    # Host Account Name of Hosting Organization.
    host_organization: typing.Optional[str] = Field(None, alias='host_organization')

    # Host's name.
    host_name: typing.Optional[str] = Field(None, alias='host_name')

    # Indicates whether or not the screenshare feature was used in the meeting.
    has_screen_share: typing.Optional[bool] = Field(None, alias='has_screen_share')

    # Indicates whether or not the recording feature was used in the meeting.
    has_recording: typing.Optional[bool] = Field(None, alias='has_recording')

    # Indicates whether or not the chat feature was used in the meeting.
    has_chat: typing.Optional[bool] = Field(None, alias='has_chat')

    # The meeting's encryption status.  * `1` &mdash; E2E encryption.  * `2` &mdash; Enhanced encryption.
    meeting_encryption_status: typing.Optional[Literal[1, 2]] = Field(None, alias='meeting_encryption_status')

    # The number of meeting participants from my account.
    participants_count_my_account: typing.Optional[int] = Field(None, alias='participants_count_my_account')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
