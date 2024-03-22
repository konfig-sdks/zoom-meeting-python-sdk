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

from zoom_meeting_python_sdk.pydantic.meetings_update_details_request_recurrence import MeetingsUpdateDetailsRequestRecurrence
from zoom_meeting_python_sdk.pydantic.meetings_update_details_request_settings import MeetingsUpdateDetailsRequestSettings
from zoom_meeting_python_sdk.pydantic.meetings_update_details_request_tracking_fields import MeetingsUpdateDetailsRequestTrackingFields

class MeetingsUpdateDetailsRequest(BaseModel):
    # Meeting description.
    agenda: typing.Optional[str] = Field(None, alias='agenda')

    # Meeting duration in minutes. Used for scheduled meetings only.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Meeting passcode. Passcodes may only contain these characters [a-z A-Z 0-9 @ - _ *] and can have a maximum of 10 characters.  **Note** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, view those requirements by calling either the [**Get user settings**](https://developers.zoom.us) API or the [**Get account settings**](https://developers.zoom.us) API.
    password: typing.Optional[str] = Field(None, alias='password')

    # Whether to create a prescheduled meeting through the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting `type` value of `2` - scheduled meetings- and `3` - recurring meetings with no fixed time.  * `true` - Create a prescheduled meeting.  * `false` - Create a regular meeting.
    pre_schedule: typing.Optional[bool] = Field(None, alias='pre_schedule')

    # The email address or `userId` of the user to schedule a meeting for.
    schedule_for: typing.Optional[str] = Field(None, alias='schedule_for')

    recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = Field(None, alias='recurrence')

    settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = Field(None, alias='settings')

    # Meeting start time. When using a format like `yyyy-MM-dd'T'HH:mm:ss'Z'`, always use GMT time. When using a format like `yyyy-MM-dd'T'HH:mm:ss`, use local time and specify the time zone. Only used for scheduled meetings and recurring meetings with a fixed time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Unique identifier of the meeting template.   [Schedule the meeting from a meeting template](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates#h_86f06cff-0852-4998-81c5-c83663c176fb). Retrieve this field's value by calling the [List meeting templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listMeetingTemplates) API.
    template_id: typing.Optional[str] = Field(None, alias='template_id')

    # The timezone to assign to the `start_time` value. Only use this field ifor scheduled or recurring meetings with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # Meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = Field(None, alias='tracking_fields')

    # Meeting types.  `1` - Instant meeting.    `2` - Scheduled meeting.    `3` - Recurring meeting with no fixed time.    `8` - Recurring meeting with a fixed time.
    type: typing.Optional[Literal[1, 2, 3, 8]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
