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

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_authentication_exception import MeetingsCreateMeetingResponseSettingsAuthenticationException
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_breakout_room import MeetingsCreateMeetingResponseSettingsBreakoutRoom
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_continuous_meeting_chat import MeetingsCreateMeetingResponseSettingsContinuousMeetingChat
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_custom_keys import MeetingsCreateMeetingResponseSettingsCustomKeys
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_global_dial_in_countries import MeetingsCreateMeetingResponseSettingsGlobalDialInCountries
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_global_dial_in_numbers import MeetingsCreateMeetingResponseSettingsGlobalDialInNumbers
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_language_interpretation import MeetingsCreateMeetingResponseSettingsLanguageInterpretation
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_resources import MeetingsCreateMeetingResponseSettingsResources
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_sign_language_interpretation import MeetingsCreateMeetingResponseSettingsSignLanguageInterpretation

class MeetingsCreateMeetingResponseSettings(BaseModel):
    # Allow attendees to join the meeting from multiple devices. This setting only works for meetings that require [registration](https://support.zoom.us/hc/en-us/articles/211579443-Setting-up-registration-for-a-meeting).
    allow_multiple_devices: typing.Optional[bool] = Field(None, alias='allow_multiple_devices')

    # A semicolon-separated list of the meeting's alternative hosts' email addresses or IDs.
    alternative_hosts: typing.Optional[str] = Field(None, alias='alternative_hosts')

    # Flag to determine whether to send email notifications to alternative hosts, default value is true.
    alternative_hosts_email_notification: typing.Optional[bool] = Field(None, alias='alternative_hosts_email_notification')

    # Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher.
    alternative_host_update_polls: typing.Optional[bool] = Field(None, alias='alternative_host_update_polls')

    # Enable registration and set approval for the registration. Note that this feature requires the host to be of **Licensed** user type. **Registration cannot be enabled for a basic user.**            `0` - Automatically approve.    `1` - Manually approve.    `2` - No registration required.
    approval_type: typing.Optional[Literal[0, 1, 2]] = Field(None, alias='approval_type')

    approved_or_denied_countries_or_regions: typing.Optional[MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions] = Field(None, alias='approved_or_denied_countries_or_regions')

    # Determine how participants can join the audio portion of the meeting.    `both` - Both Telephony and VoIP.    `telephony` - Telephony only.    `voip` - VoIP only.    `thirdParty` - Third party audio conference.
    audio: typing.Optional[Literal["both", "telephony", "voip", "thirdParty"]] = Field(None, alias='audio')

    # Third party audio conference info.
    audio_conference_info: typing.Optional[str] = Field(None, alias='audio_conference_info')

    # If user has configured [Sign Into Zoom with Specified Domains](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated.
    authentication_domains: typing.Optional[str] = Field(None, alias='authentication_domains')

    authentication_exception: typing.Optional[MeetingsCreateMeetingResponseSettingsAuthenticationException] = Field(None, alias='authentication_exception')

    # Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f).
    authentication_name: typing.Optional[str] = Field(None, alias='authentication_name')

    # Meeting authentication option ID.
    authentication_option: typing.Optional[str] = Field(None, alias='authentication_option')

    # Automatic recording.  `local` - Record on local.    `cloud` -  Record on cloud.    `none` - Disabled.
    auto_recording: typing.Optional[Literal["local", "cloud", "none"]] = Field(None, alias='auto_recording')

    breakout_room: typing.Optional[MeetingsCreateMeetingResponseSettingsBreakoutRoom] = Field(None, alias='breakout_room')

    # The type of calendar integration used to schedule the meeting.  * `1` - [Zoom Outlook add-in](https://support.zoom.us/hc/en-us/articles/360031592971-Getting-started-with-Outlook-plugin-and-add-in)  * `2` - [Zoom for Google Workspace add-on](https://support.zoom.us/hc/en-us/articles/360020187492-Using-the-Zoom-for-Google-Workspace-add-on)  Works with the `private_meeting` field to determine whether to share details of meetings or not.
    calendar_type: typing.Optional[Literal[1, 2]] = Field(None, alias='calendar_type')

    # Close registration after event date.
    close_registration: typing.Optional[bool] = Field(None, alias='close_registration')

    # WARNING: This property is deprecated
    # Host meeting in China.
    cn_meeting: typing.Optional[bool] = Field(None, alias='cn_meeting')

    # Contact email for registration
    contact_email: typing.Optional[str] = Field(None, alias='contact_email')

    # Contact name for registration
    contact_name: typing.Optional[str] = Field(None, alias='contact_name')

    custom_keys: typing.Optional[MeetingsCreateMeetingResponseSettingsCustomKeys] = Field(None, alias='custom_keys')

    # Whether to send email notifications to [alternative hosts](https://support.zoom.us/hc/en-us/articles/208220166) and [users with scheduling privileges](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-privilege). This value defaults to `true`.
    email_notification: typing.Optional[bool] = Field(None, alias='email_notification')

    # Choose between enhanced encryption and [end-to-end encryption](https://support.zoom.us/hc/en-us/articles/360048660871) when starting or a meeting. When using end-to-end encryption, several features (e.g. cloud recording, phone/SIP/H.323 dial-in) will be **automatically disabled**.   `enhanced_encryption` - Enhanced encryption. Encryption is stored in the cloud if you enable this option.       `e2ee` - [End-to-end encryption](https://support.zoom.us/hc/en-us/articles/360048660871). The encryption key is stored in your local device and can not be obtained by anyone else. Enabling this setting also **disables** the join before host, cloud recording, streaming, live transcription, breakout rooms, polling, 1:1 private chat, and meeting reactions features.
    encryption_type: typing.Optional[Literal["enhanced_encryption", "e2ee"]] = Field(None, alias='encryption_type')

    # WARNING: This property is deprecated
    # Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**          As an alternative, use the `meeting_authentication`, `authentication_option`, and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the meeting.
    enforce_login: typing.Optional[bool] = Field(None, alias='enforce_login')

    # WARNING: This property is deprecated
    # Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**          As an alternative, use the `meeting_authentication`, `authentication_option`, and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the meeting.
    enforce_login_domains: typing.Optional[str] = Field(None, alias='enforce_login_domains')

    # Whether the [**Focus Mode** feature](https://support.zoom.us/hc/en-us/articles/360061113751-Using-focus-mode) is enabled when the meeting starts.
    focus_mode: typing.Optional[bool] = Field(None, alias='focus_mode')

    global_dial_in_countries: typing.Optional[MeetingsCreateMeetingResponseSettingsGlobalDialInCountries] = Field(None, alias='global_dial_in_countries')

    global_dial_in_numbers: typing.Optional[MeetingsCreateMeetingResponseSettingsGlobalDialInNumbers] = Field(None, alias='global_dial_in_numbers')

    # Start video when the host joins the meeting.
    host_video: typing.Optional[bool] = Field(None, alias='host_video')

    # WARNING: This property is deprecated
    # Host meeting in India.
    in_meeting: typing.Optional[bool] = Field(None, alias='in_meeting')

    # If the value of `join_before_host` field is set to `true`, use this field to indicate time limits when a participant may join a meeting before a host.  *  `0` - Allow participant to join anytime. *  `5`- Allow participant to join 5 minutes before meeting start time.  * `10` - Allow participant to join 10 minutes before meeting start time.
    jbh_time: typing.Optional[Literal[0, 5, 10]] = Field(None, alias='jbh_time')

    # Allow participants to join the meeting before the host starts the meeting. Only used for scheduled or recurring meetings.
    join_before_host: typing.Optional[bool] = Field(None, alias='join_before_host')

    language_interpretation: typing.Optional[MeetingsCreateMeetingResponseSettingsLanguageInterpretation] = Field(None, alias='language_interpretation')

    sign_language_interpretation: typing.Optional[MeetingsCreateMeetingResponseSettingsSignLanguageInterpretation] = Field(None, alias='sign_language_interpretation')

    # `true` - Only authenticated users can join meetings.
    meeting_authentication: typing.Optional[bool] = Field(None, alias='meeting_authentication')

    # Mute participants upon entry.
    mute_upon_entry: typing.Optional[bool] = Field(None, alias='mute_upon_entry')

    # Start video when participants join the meeting.
    participant_video: typing.Optional[bool] = Field(None, alias='participant_video')

    # Whether the meeting is set as private.
    private_meeting: typing.Optional[bool] = Field(None, alias='private_meeting')

    # Whether to send registrants an email confirmation. * `true` - Send a confirmation email. * `false` - Do not send a confirmation email.
    registrants_confirmation_email: typing.Optional[bool] = Field(None, alias='registrants_confirmation_email')

    # Whether to send registrants email notifications about their registration approval, cancellation, or rejection.  * `true` - Send an email notification. * `false` - Do not send an email notification.   Set this value to `true` to also use the `registrants_confirmation_email` parameter.
    registrants_email_notification: typing.Optional[bool] = Field(None, alias='registrants_email_notification')

    # Registration type. Used for recurring meeting with fixed time only.   `1` - Attendees register once and can attend any of the occurrences.    `2` - Attendees need to register for each occurrence to attend.    `3` - Attendees register once and can choose one or more occurrences to attend.
    registration_type: typing.Optional[Literal[1, 2, 3]] = Field(None, alias='registration_type')

    # Show social share buttons on the meeting registration page. This setting only works for meetings that require [registration](https://support.zoom.us/hc/en-us/articles/211579443-Setting-up-registration-for-a-meeting).
    show_share_button: typing.Optional[bool] = Field(None, alias='show_share_button')

    # Use a [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time.
    use_pmi: typing.Optional[bool] = Field(None, alias='use_pmi')

    # Enable the waiting room.
    waiting_room: typing.Optional[bool] = Field(None, alias='waiting_room')

    # Add a watermark when viewing a shared screen.
    watermark: typing.Optional[bool] = Field(None, alias='watermark')

    # Whether the **Allow host to save video order** feature is enabled.
    host_save_video_order: typing.Optional[bool] = Field(None, alias='host_save_video_order')

    # Whether to set the meeting as an internal meeting.
    internal_meeting: typing.Optional[bool] = Field(None, alias='internal_meeting')

    continuous_meeting_chat: typing.Optional[MeetingsCreateMeetingResponseSettingsContinuousMeetingChat] = Field(None, alias='continuous_meeting_chat')

    # Whether to set the meeting as a participant focused meeting.
    participant_focused_meeting: typing.Optional[bool] = Field(None, alias='participant_focused_meeting')

    # Whether to push meeting changes to the calendar.    To enable this feature, configure the **Configure Calendar and Contacts Service** in the user's profile page of the Zoom web portal and enable the **Automatically sync Zoom calendar events information bi-directionally between Zoom and integrated calendars.** setting in the **Settings** page of the Zoom web portal. * `true` - Push meeting changes to the calendar. * `false` - Do not push meeting changes to the calendar.
    push_change_to_calendar: typing.Optional[bool] = Field(None, alias='push_change_to_calendar')

    resources: typing.Optional[MeetingsCreateMeetingResponseSettingsResources] = Field(None, alias='resources')

    # Whether to automatically start a meeting summary.
    auto_start_meeting_summary: typing.Optional[bool] = Field(None, alias='auto_start_meeting_summary')

    # Whether to automatically start AI Companion questions.
    auto_start_ai_companion_questions: typing.Optional[bool] = Field(None, alias='auto_start_ai_companion_questions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
