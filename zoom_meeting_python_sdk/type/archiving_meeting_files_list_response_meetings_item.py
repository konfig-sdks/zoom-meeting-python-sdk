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

from zoom_meeting_python_sdk.type.archiving_meeting_files_list_response_meetings_item_archive_files import ArchivingMeetingFilesListResponseMeetingsItemArchiveFiles

class RequiredArchivingMeetingFilesListResponseMeetingsItem(TypedDict):
    # The user's account name.
    account_name: str

    archive_files: ArchivingMeetingFilesListResponseMeetingsItemArchiveFiles

    # The meeting or webinar's archive completion time.
    complete_time: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], str]

    # The meeting or webinar's scheduled duration.
    duration: int

    # The meeting or webinar's duration, in seconds.
    duration_in_second: int

    # The ID of the user set as the host of the archived meeting or webinar.
    host_id: str

    # The meeting or webinar ID, either `meetingId` or `webinarId`.
    id: int

    # Whether the room is a [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).
    is_breakout_room: bool

    # Whether the meeting or webinar is internal or external.  * `internal` - An internal meeting or webinar.  * `external` - An external meeting or webinar.    The `id`, `host_id`, and `topic` PII (Personal Identifiable Information) values in this response are removed when this value is `external`.
    meeting_type: str

    # The number of archived files returned in the API call response.
    recording_count: int

    # The meeting or webinar's start time.
    start_time: datetime

    # The meeting or webinar's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: str

    # The meeting or webinar topic.
    topic: str

    # The total size of the archive file, in bytes.
    total_size: int

    # The type of archived meeting or webinar.    Meeting recordings use these archive types.  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created via PMI (Personal Meeting ID).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.    Webinar recordings use these archive types.  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time.  * `9` - A recurring webinar with a fixed time.    If the recording is **not** from a meeting or webinar:   * `100` - A [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).
    type: int

    # The recorded meeting or webinar instance's universally unique identifier (UUID). Each meeting or webinar instance generates a UUID.
    uuid: str

    # The archive's processing status.  * `completed` - The archive's processing is complete.  * `processing` - The archive is processing.
    status: str

class OptionalArchivingMeetingFilesListResponseMeetingsItem(TypedDict, total=False):
    # The parent meeting's universally unique ID (UUID). Each meeting or webinar instance generates a UUID. If the `is_breakout_room` value is `true`, the API returns this value.
    parent_meeting_id: str

    # Primary group IDs of participants who belong to your account. Each group ID is separated by a comma.
    group_id: str

class ArchivingMeetingFilesListResponseMeetingsItem(RequiredArchivingMeetingFilesListResponseMeetingsItem, OptionalArchivingMeetingFilesListResponseMeetingsItem):
    pass
