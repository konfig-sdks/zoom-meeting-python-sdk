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

from zoom_meeting_python_sdk.type.meetings_create_meeting_request_recurrence import MeetingsCreateMeetingRequestRecurrence
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings import MeetingsCreateMeetingRequestSettings
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_tracking_fields import MeetingsCreateMeetingRequestTrackingFields

class RequiredMeetingsCreateMeetingRequest(TypedDict):
    pass

class OptionalMeetingsCreateMeetingRequest(TypedDict, total=False):
    # The meeting's agenda. This value has a maximum length of 2,000 characters.
    agenda: str

    # Whether to generate a default passcode using the user's settings. This value defaults to `false`.   If this value is `true` and the user has the PMI setting enabled with a passcode, then the user's meetings will use the PMI passcode. It will **not** use a default passcode.
    default_password: bool

    # The meeting's scheduled duration, in minutes. This field is only used for scheduled meetings (`2`).
    duration: int

    # The passcode required to join the meeting. By default, a passcode can **only** have a maximum length of 10 characters and only contain alphanumeric characters and the `@`, `-`, `_`, and `*` characters.  * If the account owner or administrator has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode **must** meet those requirements.  * If passcode requirements are enabled, use the [**Get user settings**](https://developers.zoom.us/docs/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](https://developers.zoom.us/docs/api-reference/zoom-api/ma#operation/accountSettings) API to get the requirements.
    password: str

    # Whether to create a prescheduled meeting via the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting `type` value of `2` (scheduled meetings) and `3` (recurring meetings with no fixed time).  * `true` - Create a prescheduled meeting.  * `false` - Create a regular meeting.
    pre_schedule: bool

    recurrence: MeetingsCreateMeetingRequestRecurrence

    # The email address or user ID of the user to schedule a meeting for.
    schedule_for: str

    settings: MeetingsCreateMeetingRequestSettings

    # The meeting's start time. This field is only used for scheduled or recurring meetings with a fixed time. This supports local time and GMT formats.  * To set a meeting's start time in GMT, use the `yyyy-MM-ddTHH:mm:ssZ` date-time format. For example, `2020-03-31T12:02:00Z`.  * To set a meeting's start time using a specific timezone, use the `yyyy-MM-ddTHH:mm:ss` date-time format and specify the [timezone ID](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones) in the `timezone` field. If you do not specify a timezone, the `timezone` value defaults to your Zoom account's timezone. You can also use `UTC` for the `timezone` value. **Note:** If no `start_time` is set for a scheduled meeting, the `start_time` is set at the current time and the meeting type changes to an instant meeting, which expires after 30 days.
    start_time: datetime

    # The account admin meeting template ID used to schedule a meeting using a [meeting template](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates). For a list of account admin-provided meeting templates, use the [**List meeting templates**](https://developers.zoom.us/docs/api-reference/zoom-api/methods#operation/listMeetingTemplates) API.  * At this time, this field **only** accepts account admin meeting template IDs.  * To enable the account admin meeting templates feature, [contact Zoom support](https://support.zoom.us/hc/en-us).
    template_id: str

    # The timezone to assign to the `start_time` value. This field is only used for scheduled or recurring meetings with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: str

    # The meeting's topic.
    topic: str

    tracking_fields: MeetingsCreateMeetingRequestTrackingFields

    # The type of meeting. * `1` - An instant meeting.  * `2` - A scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `8` - A recurring meeting with fixed time.
    type: int

class MeetingsCreateMeetingRequest(RequiredMeetingsCreateMeetingRequest, OptionalMeetingsCreateMeetingRequest):
    pass
