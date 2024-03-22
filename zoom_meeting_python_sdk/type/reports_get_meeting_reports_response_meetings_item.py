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

from zoom_meeting_python_sdk.type.reports_get_meeting_reports_response_meetings_item_custom_keys import ReportsGetMeetingReportsResponseMeetingsItemCustomKeys

class RequiredReportsGetMeetingReportsResponseMeetingsItem(TypedDict):
    pass

class OptionalReportsGetMeetingReportsResponseMeetingsItem(TypedDict, total=False):
    custom_keys: ReportsGetMeetingReportsResponseMeetingsItemCustomKeys

    # The meeting's duration.
    duration: int

    # The meeting's end date and time.
    end_time: datetime

    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).
    id: int

    # The number of meeting participants.
    participants_count: int

    # The Video SDK custom session ID.
    session_key: str

    # Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app's name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the `Zoom` value.
    source: str

    # The meeting's start date and time.
    start_time: datetime

    # The meeting's topic.
    topic: str

    # The sum of meeting minutes from all meeting participants in the meeting.
    total_minutes: int

    # The type of meeting or webinar.   meeting:  * `1` &mdash; Instant meeting.  * `2` &mdash; Scheduled meeting.  * `3` &mdash; A recurring meeting with no fixed time.  * `4` &mdash; A meeting created via PMI (Personal Meeting ID).  * `7` &mdash; A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.   webinar:  * `5` &mdash; A webinar.  * `6` &mdash; A recurring webinar without a fixed time  * `9` &mdash; A recurring webinar with a fixed time. 
    type: int

    # The user's email address.
    user_email: str

    # The user's display name.
    user_name: str

    # The meeting's universally unique identifier (UUID). Each meeting instance generates a meeting UUID.
    uuid: str

    # The meeting's scheduled date and time.
    schedule_time: str

    # The date and time at which the attendee joined the waiting room.
    join_waiting_room_time: str

    # The date and time at which the attendee joined the meeting.
    join_time: str

    # The date and time at which the attendee left the meeting.
    leave_time: str

    # Host Account Name of Hosting Organization.
    host_organization: str

    # Host's name.
    host_name: str

    # Indicates whether or not the screenshare feature was used in the meeting.
    has_screen_share: bool

    # Indicates whether or not the recording feature was used in the meeting.
    has_recording: bool

    # Indicates whether or not the chat feature was used in the meeting.
    has_chat: bool

    # The meeting's encryption status.  * `1` &mdash; E2E encryption.  * `2` &mdash; Enhanced encryption.
    meeting_encryption_status: int

    # The number of meeting participants from my account.
    participants_count_my_account: int

class ReportsGetMeetingReportsResponseMeetingsItem(RequiredReportsGetMeetingReportsResponseMeetingsItem, OptionalReportsGetMeetingReportsResponseMeetingsItem):
    pass
