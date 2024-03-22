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

from zoom_meeting_python_sdk.pydantic.archiving_meeting_files_list200_response_archive_files import ArchivingMeetingFilesList200ResponseArchiveFiles

class ArchivingMeetingFilesList200Response(BaseModel):
    # The user's account name.
    account_name: str = Field(alias='account_name')

    archive_files: ArchivingMeetingFilesList200ResponseArchiveFiles = Field(alias='archive_files')

    # The meeting or webinar's archive completion time.
    complete_time: typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]], str] = Field(alias='complete_time')

    # The meeting or webinar's scheduled duration.
    duration: int = Field(alias='duration')

    # The meeting or webinar's duration, in seconds.
    duration_in_second: int = Field(alias='duration_in_second')

    # The host's user ID for the archived meeting or webinar.
    host_id: str = Field(alias='host_id')

    # The meeting or webinar ID, either `meetingId` or `webinarId`.
    id: int = Field(alias='id')

    # Whether the room is a [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).
    is_breakout_room: bool = Field(alias='is_breakout_room')

    # Whether the meeting or webinar is internal or external.  * `internal` - An internal meeting or webinar.  * `external` - An external meeting or webinar.    The `id`, `host_id`, and `topic` PII (Personal Identifiable Information) values in this response are removed when this value is `external`.
    meeting_type: Literal["internal", "external"] = Field(alias='meeting_type')

    # The number of archived files returned in the API call response.
    recording_count: int = Field(alias='recording_count')

    # The meeting or webinar's start time.
    start_time: datetime = Field(alias='start_time')

    # The meeting or webinar's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: str = Field(alias='timezone')

    # The meeting or webinar topic.
    topic: str = Field(alias='topic')

    # The total size of the archive file, in bytes.
    total_size: int = Field(alias='total_size')

    # The type of archived meeting or webinar.    If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created via PMI (Personal Meeting ID).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.    If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time.  * `9` - A recurring webinar with a fixed time.    If the recording is **not** from a meeting or webinar:   * `100` - A [breakout room](https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-breakout-rooms).
    type: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 100] = Field(alias='type')

    # The universally unique identifier (UUID) of the recorded meeting or webinar instance. Each meeting or webinar instance generates a UUID.
    uuid: str = Field(alias='uuid')

    # The archive's processing status.  * `completed` - The archive's processing is complete.  * `processing` - The archive is processing.
    status: Literal["completed", "processing"] = Field(alias='status')

    # The parent meeting's universally unique ID (UUID). Each meeting or webinar instance generates a UUID. If the `is_breakout_room` value is `true`, the API returns this value.
    parent_meeting_id: typing.Optional[str] = Field(None, alias='parent_meeting_id')

    # Primary group IDs of participants who belong to your account. Each group ID is separated by a comma.
    group_id: typing.Optional[str] = Field(None, alias='group_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
