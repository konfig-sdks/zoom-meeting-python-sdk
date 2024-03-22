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

from zoom_meeting_python_sdk.pydantic.cloud_recording_list_recordings_response_meetings_item_recording_files import CloudRecordingListRecordingsResponseMeetingsItemRecordingFiles

class CloudRecordingListRecordingsResponseMeetingsItem(BaseModel):
    # Unique Identifier of the user account.
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    # Meeting duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # ID of the user set as host of meeting.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # Meeting ID - also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    # Number of recording files returned in the response of this API call. This includes the `recording_files` and  `participant_audio_files` files.
    recording_count: typing.Optional[int] = Field(None, alias='recording_count')

    # The time when the meeting started.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # The total file size of the recording. This includes the `recording_files` and `participant_audio_files` files.
    total_size: typing.Optional[int] = Field(None, alias='total_size')

    # The recording's associated type of meeting or webinar:   If the recording is of a meeting:  * `1` - Instant meeting.  * `2` - Scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `4` - A meeting created viaPersonal Meeting ID (PMI).  * `7` - A [Personal Audio Conference](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) (PAC).  * `8` - Recurring meeting with a fixed time.   If the recording is of a webinar:  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time  * `9` - A recurring webinar with a fixed time.  If the recording is **not** from a meeting or webinar:   * `99` - A recording uploaded via the [**Recordings**](https://zoom.us/recording) interface on the Zoom Web Portal.
    type: typing.Optional[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9", "99"]] = Field(None, alias='type')

    # Unique Meeting Identifier. Each instance of the meeting will have its own UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The cloud recording's passcode to be used in the URL. This recording's passcode can be directly spliced in `play_url` or `share_url` with `?pwd=` to access and play. For example, 'https://zoom.us/rec/share/**************?pwd=yNYIS408EJygs7rE5vVsJwXIz4-VW7MH'. If you want to use this field, please contact Zoom support.
    recording_play_passcode: typing.Optional[str] = Field(None, alias='recording_play_passcode')

    recording_files: typing.Optional[CloudRecordingListRecordingsResponseMeetingsItemRecordingFiles] = Field(None, alias='recording_files')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
