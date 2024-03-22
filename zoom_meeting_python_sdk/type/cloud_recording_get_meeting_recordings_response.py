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

from zoom_meeting_python_sdk.type.cloud_recording_get_meeting_recordings_response_participant_audio_files import CloudRecordingGetMeetingRecordingsResponseParticipantAudioFiles
from zoom_meeting_python_sdk.type.cloud_recording_get_meeting_recordings_response_recording_files import CloudRecordingGetMeetingRecordingsResponseRecordingFiles

class RequiredCloudRecordingGetMeetingRecordingsResponse(TypedDict):
    pass

class OptionalCloudRecordingGetMeetingRecordingsResponse(TypedDict, total=False):
    # The user account's unique identifier.
    account_id: str

    # The meeting duration.
    duration: int

    # The ID of the user set as host of meeting.
    host_id: str

    # The meeting ID, also known as the meeting number.
    id: int

    #  The number of recording files returned in the response of this API call. This includes the `recording_files` and  `participant_audio_files` files.
    recording_count: int

    # The time when the meeting started.
    start_time: datetime

    # The meeting topic.
    topic: str

    # The recording's total file size. This includes the `recording_files` and `participant_audio_files` files.
    total_size: int

    # The recording's associated type of meeting or webinar.   If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created via PMI (Personal Meeting ID).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.   If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time  * `9` - A recurring webinar with a fixed time.  If the recording is **not** from a meeting or webinar:   * `99` - A recording uploaded via the [**Recordings**](https://zoom.us/recording) interface on the Zoom Web Portal.
    type: str

    # The unique meeting identifier. Each instance of the meeting has its own UUID.
    uuid: str

    # The cloud recording's passcode to be used in the URL. Directly splice this recording's passcode in `play_url` or `share_url` with `?pwd=` to access and play. Example: 'https://zoom.us/rec/share/**************?pwd=yNYIS408EJygs7rE5vVsJwXIz4-VW7MH'.
    recording_play_passcode: str

    recording_files: CloudRecordingGetMeetingRecordingsResponseRecordingFiles

    # The JWT token to download the meeting's recording. This response only returns if the `download_access_token` is included in the `include_fields` query parameter.
    download_access_token: str

    # The cloud recording's passcode.
    password: str

    participant_audio_files: CloudRecordingGetMeetingRecordingsResponseParticipantAudioFiles

class CloudRecordingGetMeetingRecordingsResponse(RequiredCloudRecordingGetMeetingRecordingsResponse, OptionalCloudRecordingGetMeetingRecordingsResponse):
    pass
