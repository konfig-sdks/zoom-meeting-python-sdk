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


class RequiredArchivingMeetingFilesListResponseMeetingsItemArchiveFilesItem(TypedDict):
    # The URL to download the the archive file.    **OAuth apps**    If a user has authorized and installed your OAuth app that contains recording scopes, use the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) to download the file. For example, `https://{{base-domain}}/rec/archive/download/xxx--header 'Authorization: Bearer {{OAuth-access-token}}'`    **Note:** This field does **not** return for [Zoom on-premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). Instead, this API will return the `file_path` field.
    download_url: str

    # The archived file's extension.
    file_extension: str

    # The archived file's size, in bytes.
    file_size: int

    # The archive file's type.  * `MP4` - Video file.  * `M4A` - Audio-only file.  * `CHAT` - A TXT file containing in-meeting chat messages.  * `CC` - A file containing the closed captions of the recording, in VTT file format.  *  `CHAT_MESSAGE` - A JSON file encoded in base64 format containing chat messages. The file also includes waiting room chats, deleted messages, meeting emojis and non-verbal feedback.
    file_type: str

    # The archive file's unique ID.
    id: str

    # Whether the archive file is an individual recording file.  * `true` - An individual recording file.   * `false` - An entire meeting file.
    individual: bool

    # The join time for the generated recording file. If this value is returned when the individual value is `true`, it is the recording file's participant join time. When the individual value is `false`, it returns the join time for the archiving gateway.
    participant_join_time: datetime

    # The leave time for the generated recording file. If this value is returned when the individual value is `true`, it is the recording file's participant leave time. When the individual value is `false`, it returns the leave time for the archiving gateway.
    participant_leave_time: datetime

    # The archive file's recording type.  * `shared_screen_with_speaker_view`  * `audio_only`  * `chat_file`  * `closed_caption`  * `chat_message`    For more information, read our [Managing and sharing cloud recordings](https://support.zoom.us/hc/en-us/articles/205347605-Managing-and-sharing-cloud-recordings#h_9898497b-e736-4980-a749-d55608f10773) documentation.
    recording_type: str

    # The archived file's processing status.  * `completed` - The processing of the file is complete.  * `processing` - The file is processing.  * `failed` - The processing of the file failed.
    status: str

    # The archived file's encryption fingerprint, using the SHA256 hash algorithm.
    encryption_fingerprint: str

class OptionalArchivingMeetingFilesListResponseMeetingsItemArchiveFilesItem(TypedDict, total=False):
    # The file path to the on-premise account archive file.    **Note:** The API only returns this field for [Zoom on-premise accounts](https://support.zoom.us/hc/en-us/articles/360034064852-Zoom-On-Premise-Deployment). It does **not** return the `download_url` field.
    file_path: str

    # The individual recording file's participant email address. This value is returned when the `individual` value is `true`. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    participant_email: str

    # The number of `TXT` or `JSON` file messages. This field returns only when the `file_extension` is `JSON` or `TXT`.
    number_of_messages: int

    # The region where the file is stored. This field returns only `Enable Distributed Compliance Archiving` op feature is enabled.
    storage_location: str

    # Whether to auto delete the archived file.  **Prerequisites:**   Enable the \"Tag Archiving Files for Deletion\" feature in OP. Contact [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to open.
    auto_delete: bool

class ArchivingMeetingFilesListResponseMeetingsItemArchiveFilesItem(RequiredArchivingMeetingFilesListResponseMeetingsItemArchiveFilesItem, OptionalArchivingMeetingFilesListResponseMeetingsItemArchiveFilesItem):
    pass
