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

from zoom_meeting_python_sdk.type.meetings_get_details_response_occurrences import MeetingsGetDetailsResponseOccurrences
from zoom_meeting_python_sdk.type.meetings_get_details_response_recurrence import MeetingsGetDetailsResponseRecurrence
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings import MeetingsGetDetailsResponseSettings
from zoom_meeting_python_sdk.type.meetings_get_details_response_tracking_fields import MeetingsGetDetailsResponseTrackingFields

class RequiredMeetingsGetDetailsResponse(TypedDict):
    pass

class OptionalMeetingsGetDetailsResponse(TypedDict, total=False):
    # The ID of the user who scheduled this meeting on behalf of the host.
    assistant_id: str

    # The meeting host's email address.
    host_email: str

    # The ID of the user who is set as the meeting host.
    host_id: str

    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in **long** format, represented as int64 data type in JSON, also known as the meeting number.
    id: int

    # Unique meeting ID. Each meeting instance generates its own meeting UUID - after a meeting ends, a new UUID is generated for the next instance of the meeting. Retrieve a list of UUIDs from past meeting instances using the [**List past meeting instances**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/pastMeetings) API. [Double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a `/` or contains `//` in it. 
    uuid: str

    # The meeting description.
    agenda: str

    # The creation time. 
    created_at: datetime

    # The meeting duration.
    duration: int

    # Encrypted passcode for third party endpoints (H323/SIP).
    encrypted_password: str

    # H.323/SIP room system passcode.
    h323_password: str

    # The URL for participants to join the meeting. This URL should only be shared with users invited to the meeting.
    join_url: str

    # The URL to join the chat.
    chat_join_url: str

    occurrences: MeetingsGetDetailsResponseOccurrences

    # Meeting passcode.
    password: str

    # [Personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time.
    pmi: str

    # Whether the prescheduled meeting was created via the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting `type` value of `2` (scheduled meetings) and `3` (recurring meetings with no fixed time):  * `true` - A GSuite prescheduled meeting.  * `false` - A regular meeting.
    pre_schedule: bool

    recurrence: MeetingsGetDetailsResponseRecurrence

    settings: MeetingsGetDetailsResponseSettings

    # Meeting start time in GMT or UTC. Start time will not be returned if the meeting is an **instant** meeting.  
    start_time: datetime

    # The `start_url` of a meeting is a URL that a host or an alternative host can start the meeting.   The expiration time for the `start_url` field listed in the response of the [**Create a meeting**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/meetingCreate) API is two hours for all regular users.    For users created using the `custCreate` option via the [**Create users**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/userCreate) API, the expiration time of the `start_url` field is 90 days.   For security reasons, to retrieve the updated value for the `start_url` field programmatically after the expiry time, you must call the [**Get a meeting](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/meeting) API and refer to the value of the `start_url` field in the response.    This URL should only be used by the host of the meeting and **should not be shared with anyone other than the host** of the meeting as anyone with this URL will be able to login to the Zoom Client as the host of the meeting.
    start_url: str

    # Meeting status
    status: str

    # The timezone to format the meeting start time.
    timezone: str

    # Meeting topic.
    topic: str

    tracking_fields: MeetingsGetDetailsResponseTrackingFields

    # Meeting types.   `1` - Instant meeting.    `2` - Scheduled meeting.    `3` - Recurring meeting with no fixed time.    `4` - PMI Meeting     `8` - Recurring meeting with a fixed time.
    type: int

class MeetingsGetDetailsResponse(RequiredMeetingsGetDetailsResponse, OptionalMeetingsGetDetailsResponse):
    pass
