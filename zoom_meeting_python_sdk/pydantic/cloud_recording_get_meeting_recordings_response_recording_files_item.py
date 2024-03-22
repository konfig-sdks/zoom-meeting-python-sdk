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


class CloudRecordingGetMeetingRecordingsResponseRecordingFilesItem(BaseModel):
    # The time when recording was deleted. Returned in the response only for trash query.
    deleted_time: typing.Optional[str] = Field(None, alias='deleted_time')

    # The URL to download the recording.   If a user has authorized and installed your OAuth app that contains recording scopes, use the `download_access_token` or the the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) to download the file, and set the `access_token` as a Bearer token in the Authorization header.  `curl -H 'Authorization: Bearer <ACCESS_TOKEN>' https://{{base-domain}}/rec/archive/download/xyz`.  **Note:** This field does **not** return for [Zoom on-premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). Instead, this API returns the `file_path` field.
    download_url: typing.Optional[str] = Field(None, alias='download_url')

    # The file path to the on-premise account recording.   **Note:** This API only returns this field for [Zoom On-Premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). It does **not** return the `download_url` field.
    file_path: typing.Optional[str] = Field(None, alias='file_path')

    # The recording file size.
    file_size: typing.Optional[typing.Union[int, float]] = Field(None, alias='file_size')

    # The recording file type.    `MP4` - Video file of the recording.    `M4A` - Audio-only file of the recording.    `TIMELINE` - Timestamp file of the recording in JSON file format. To get a timeline file, the **Add a timestamp to the recording** setting must be enabled in the [recording settings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-recording#h_3f14c3a4-d16b-4a3c-bbe5-ef7d24500048). The time will display in the host's timezone, set on their Zoom profile.      `TRANSCRIPT` - Transcription file of the recording in VTT format.     `CHAT` - A TXT file containing in-meeting chat messages that were sent during the meeting.    `CC` - File containing closed captions of the recording in VTT file format.    `CSV` - File containing polling data in csv format.          A recording file object with file type of either `CC` or `TIMELINE` **does not have** these properties.      `id`, `status`, `file_size`, `recording_type`, and `play_url`.    `SUMMARY` - Summary file of the recording in JSON file format.
    file_type: typing.Optional[Literal["MP4", "M4A", "CHAT", "TRANSCRIPT", "CSV", "TB", "CC", "CHAT_MESSAGE", "SUMMARY"]] = Field(None, alias='file_type')

    # The file extension type of the recording file.
    file_extension: typing.Optional[Literal["MP4", "M4A", "TXT", "VTT", "CSV", "JSON", "JPG"]] = Field(None, alias='file_extension')

    # The recording file ID. It's included in the response of general query.
    id: typing.Optional[str] = Field(None, alias='id')

    # The meeting ID. 
    meeting_id: typing.Optional[str] = Field(None, alias='meeting_id')

    # The URL that can play a recording file.
    play_url: typing.Optional[str] = Field(None, alias='play_url')

    # The recording end time. The response is in general query.
    recording_end: typing.Optional[str] = Field(None, alias='recording_end')

    # The recording start time.
    recording_start: typing.Optional[str] = Field(None, alias='recording_start')

    # The recording type.    `shared_screen_with_speaker_view(CC)`    `shared_screen_with_speaker_view`    `shared_screen_with_gallery_view`    `speaker_view`    `gallery_view`    `shared_screen`    `audio_only`    `audio_transcript`    `chat_file`    `active_speaker`    `poll`    `timeline`    `closed_caption`    `audio_interpretation`    `summary`    `summary_next_steps`    `summary_smart_chapters`    `sign_interpretation`    `production_studio`
    recording_type: typing.Optional[Literal["shared_screen_with_speaker_view(CC)", "shared_screen_with_speaker_view", "shared_screen_with_gallery_view", "active_speaker", "gallery_view", "shared_screen", "audio_only", "audio_transcript", "chat_file", "poll", "host_video", "closed_caption", "timeline", "thumbnail", "audio_interpretation", "summary", "summary_next_steps", "summary_smart_chapters", "sign_interpretation", "production_studio"]] = Field(None, alias='recording_type')

    # The recording status.
    status: typing.Optional[Literal["completed"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
