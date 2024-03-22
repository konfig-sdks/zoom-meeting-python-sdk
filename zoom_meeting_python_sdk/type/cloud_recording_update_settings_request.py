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


class RequiredCloudRecordingUpdateSettingsRequest(TypedDict):
    pass

class OptionalCloudRecordingUpdateSettingsRequest(TypedDict, total=False):
    # The approval type for the registration.     `0`- Automatically approve the registration when a user registers.     `1` - Manually approve or deny the registration of a user.     `2` - No registration required to view the recording.
    approval_type: int

    # The authentication domains.
    authentication_domains: str

    # The authentication options.
    authentication_option: str

    # This field determines whether the registration is required to view the recording.
    on_demand: bool

    # This field enables passcode protection for the recording by setting a passcode.   The passcode must have a minimum of **eight** characters with a mix of numbers, letters and special characters.          **Note:** If the account owner or the admin has set minimum passcode strength requirements for recordings through Account Settings, the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](/api-reference/zoom-api/ma#operation/accountSettings) API.
    password: str

    # This field indicates that only authenticated users can view.
    recording_authentication: bool

    # This field sends an email to host when someone registers to view the recording. This setting applies for On-demand recordings only.
    send_email_to_host: bool

    # This field determines how the meeting recording is shared.
    share_recording: str

    # This field shows social share buttons on registration page. This setting applies for On-demand recordings only.
    show_social_share_buttons: bool

    # The name of the recording.
    topic: str

    # This field determines whether a viewer can download the recording file or not.
    viewer_download: bool

class CloudRecordingUpdateSettingsRequest(RequiredCloudRecordingUpdateSettingsRequest, OptionalCloudRecordingUpdateSettingsRequest):
    pass
