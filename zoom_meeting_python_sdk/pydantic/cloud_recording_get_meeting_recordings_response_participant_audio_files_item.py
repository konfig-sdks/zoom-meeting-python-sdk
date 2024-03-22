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


class CloudRecordingGetMeetingRecordingsResponseParticipantAudioFilesItem(BaseModel):
    # The URL to download the recording. If a user has authorized and installed your OAuth app that contains recording scopes, use the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) to download the file, and set the `access_token` as a Bearer token in the Authorization header.  `curl -H 'Authorization: Bearer <ACCESS_TOKEN>' https://{{base-domain}}/rec/archive/download/xyz`   **Note:** This field does **not** return for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). Instead, this API will return the `file_path` field.
    download_url: typing.Optional[str] = Field(None, alias='download_url')

    # The recording file's name.
    file_name: typing.Optional[str] = Field(None, alias='file_name')

    # The file path to the on-premise account recording.   **Note:** This API only returns this field for [Zoom on-premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). It does **not** return the `download_url` field.
    file_path: typing.Optional[str] = Field(None, alias='file_path')

    # The recording file's size, in bytes.
    file_size: typing.Optional[typing.Union[int, float]] = Field(None, alias='file_size')

    # The recording file's format.   * `MP4` - Video file. * `M4A` - Audio-only file. * `TIMELINE` - Timestamp file of the recording, in JSON file format. To get a timeline file, the **Add a timestamp to the recording** setting **must** be enabled in the [recording settings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-recording#h_3f14c3a4-d16b-4a3c-bbe5-ef7d24500048). The time will display in the host's timezone. * `TRANSCRIPT` - A transcript of the recording, in VTT format. * `CHAT` - A text file containing chat messages sent during the meeting. * `CC` - A file containing the closed captions of the recording, in VTT file format. * `CSV` - A file containing polling data, in CSV format.  A recording file object with file the `CC` or `TIMELINE` value **does not** have the `id`, `status`, `file_size`, `recording_type`, and `play_url` properties.
    file_type: typing.Optional[str] = Field(None, alias='file_type')

    # The recording file's unique ID. This is included in the general query response.
    id: typing.Optional[str] = Field(None, alias='id')

    # The URL where the recording file can be opened and played.
    play_url: typing.Optional[str] = Field(None, alias='play_url')

    # The recording file's end time. This is included in the general query response.
    recording_end: typing.Optional[datetime] = Field(None, alias='recording_end')

    # The recording file's start time.
    recording_start: typing.Optional[datetime] = Field(None, alias='recording_start')

    # The recording file's status.
    status: typing.Optional[Literal["completed"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
