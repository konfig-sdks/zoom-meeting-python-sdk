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

from zoom_meeting_python_sdk.type.cloud_recording_list_recordings_response_meetings_item_recording_files import CloudRecordingListRecordingsResponseMeetingsItemRecordingFiles

class RequiredCloudRecordingListRecordingsResponseMeetingsItem(TypedDict):
    pass

class OptionalCloudRecordingListRecordingsResponseMeetingsItem(TypedDict, total=False):
    # Unique Identifier of the user account.
    account_id: str

    # Meeting duration.
    duration: int

    # ID of the user set as host of meeting.
    host_id: str

    # Meeting ID - also known as the meeting number.
    id: int

    # Number of recording files returned in the response of this API call. This includes the `recording_files` and  `participant_audio_files` files.
    recording_count: int

    # The time when the meeting started.
    start_time: datetime

    # Meeting topic.
    topic: str

    # The total file size of the recording. This includes the `recording_files` and `participant_audio_files` files.
    total_size: int

    # The recording's associated type of meeting or webinar:   If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created viaPersonal Meeting ID (PMI).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.   If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time  * `9` - A recurring webinar with a fixed time.  If the recording is **not** from a meeting or webinar:   * `99` - A recording uploaded via the [**Recordings**](https://zoom.us/recording) interface on the Zoom Web Portal.
    type: str

    # Unique Meeting Identifier. Each instance of the meeting will have its own UUID.
    uuid: str

    # The cloud recording's passcode to be used in the URL. This recording's passcode can be directly spliced in `play_url` or `share_url` with `?pwd=` to access and play. For example, 'https://zoom.us/rec/share/**************?pwd=yNYIS408EJygs7rE5vVsJwXIz4-VW7MH'. If you want to use this field, please contact Zoom support.
    recording_play_passcode: str

    recording_files: CloudRecordingListRecordingsResponseMeetingsItemRecordingFiles

class CloudRecordingListRecordingsResponseMeetingsItem(RequiredCloudRecordingListRecordingsResponseMeetingsItem, OptionalCloudRecordingListRecordingsResponseMeetingsItem):
    pass
