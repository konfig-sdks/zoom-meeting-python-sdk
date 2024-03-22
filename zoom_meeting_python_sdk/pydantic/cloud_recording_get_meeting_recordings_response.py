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

from zoom_meeting_python_sdk.pydantic.cloud_recording_get_meeting_recordings_response_participant_audio_files import CloudRecordingGetMeetingRecordingsResponseParticipantAudioFiles
from zoom_meeting_python_sdk.pydantic.cloud_recording_get_meeting_recordings_response_recording_files import CloudRecordingGetMeetingRecordingsResponseRecordingFiles

class CloudRecordingGetMeetingRecordingsResponse(BaseModel):
    # The user account's unique identifier.
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    # The meeting duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # The ID of the user set as host of meeting.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # The meeting ID, also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    #  The number of recording files returned in the response of this API call. This includes the `recording_files` and  `participant_audio_files` files.
    recording_count: typing.Optional[int] = Field(None, alias='recording_count')

    # The time when the meeting started.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # The recording's total file size. This includes the `recording_files` and `participant_audio_files` files.
    total_size: typing.Optional[int] = Field(None, alias='total_size')

    # The recording's associated type of meeting or webinar.   If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created via PMI (Personal Meeting ID).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.   If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time  * `9` - A recurring webinar with a fixed time.  If the recording is **not** from a meeting or webinar:   * `99` - A recording uploaded via the [**Recordings**](https://zoom.us/recording) interface on the Zoom Web Portal.
    type: typing.Optional[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]] = Field(None, alias='type')

    # The unique meeting identifier. Each instance of the meeting has its own UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The cloud recording's passcode to be used in the URL. Directly splice this recording's passcode in `play_url` or `share_url` with `?pwd=` to access and play. Example: 'https://zoom.us/rec/share/**************?pwd=yNYIS408EJygs7rE5vVsJwXIz4-VW7MH'.
    recording_play_passcode: typing.Optional[str] = Field(None, alias='recording_play_passcode')

    recording_files: typing.Optional[CloudRecordingGetMeetingRecordingsResponseRecordingFiles] = Field(None, alias='recording_files')

    # The JWT token to download the meeting's recording. This response only returns if the `download_access_token` is included in the `include_fields` query parameter.
    download_access_token: typing.Optional[str] = Field(None, alias='download_access_token')

    # The cloud recording's passcode.
    password: typing.Optional[str] = Field(None, alias='password')

    participant_audio_files: typing.Optional[CloudRecordingGetMeetingRecordingsResponseParticipantAudioFiles] = Field(None, alias='participant_audio_files')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
