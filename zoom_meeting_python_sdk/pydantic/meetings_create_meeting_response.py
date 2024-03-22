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

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_occurrences import MeetingsCreateMeetingResponseOccurrences
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_recurrence import MeetingsCreateMeetingResponseRecurrence
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings import MeetingsCreateMeetingResponseSettings
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_tracking_fields import MeetingsCreateMeetingResponseTrackingFields

class MeetingsCreateMeetingResponse(BaseModel):
    # The ID of the user who scheduled this meeting on behalf of the host.
    assistant_id: typing.Optional[str] = Field(None, alias='assistant_id')

    # The meeting host's email address.
    host_email: typing.Optional[str] = Field(None, alias='host_email')

    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in **long** format(represented as int64 data type in JSON), also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    # The URL that registrants can use to register for a meeting. This field is only returned for meetings that have enabled registration.
    registration_url: typing.Optional[str] = Field(None, alias='registration_url')

    # Agenda
    agenda: typing.Optional[str] = Field(None, alias='agenda')

    # The date and time when this meeting was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The meeting duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # H.323/SIP room system passcode
    h323_password: typing.Optional[str] = Field(None, alias='h323_password')

    # URL for participants to join the meeting. This URL should only be shared with users that you would like to invite for the meeting.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The URL to join the chat.
    chat_join_url: typing.Optional[str] = Field(None, alias='chat_join_url')

    occurrences: typing.Optional[MeetingsCreateMeetingResponseOccurrences] = Field(None, alias='occurrences')

    # The meeting passcode. This passcode may only contain these characters: `[a-z A-Z 0-9 @ - _ * !]`  If **Require a passcode when scheduling new meetings** setting has been enabled and [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the passcode field will be autogenerated in the response even if it is not provided in the API request.    
    password: typing.Optional[str] = Field(None, alias='password')

    # [Personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time.
    pmi: typing.Optional[str] = Field(None, alias='pmi')

    # Whether the prescheduled meeting was created via the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This only supports the meeting `type` value of `2` (scheduled meetings) and `3` (recurring meetings with no fixed time).  * `true` - A GSuite prescheduled meeting.  * `false` - A regular meeting.
    pre_schedule: typing.Optional[bool] = Field(None, alias='pre_schedule')

    recurrence: typing.Optional[MeetingsCreateMeetingResponseRecurrence] = Field(None, alias='recurrence')

    settings: typing.Optional[MeetingsCreateMeetingResponseSettings] = Field(None, alias='settings')

    # Meeting start date-time in UTC/GMT, such as `2020-03-31T12:02:00Z`.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # URL to start the meeting. This URL should only be used by the host of the meeting and **should not be shared with anyone other than the host** of the meeting, since anyone with this URL will be able to log in to the Zoom Client as the host of the meeting.
    start_url: typing.Optional[str] = Field(None, alias='start_url')

    # Timezone to format `start_time`.
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # Meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    tracking_fields: typing.Optional[MeetingsCreateMeetingResponseTrackingFields] = Field(None, alias='tracking_fields')

    # Meeting type.
    type: typing.Optional[Literal[1, 2, 3, 8]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
