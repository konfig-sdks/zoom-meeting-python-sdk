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

from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_approved_or_denied_countries_or_regions import MeetingsGetDetailsResponseSettingsApprovedOrDeniedCountriesOrRegions
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_authentication_exception import MeetingsGetDetailsResponseSettingsAuthenticationException
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_breakout_room import MeetingsGetDetailsResponseSettingsBreakoutRoom
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_continuous_meeting_chat import MeetingsGetDetailsResponseSettingsContinuousMeetingChat
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_custom_keys import MeetingsGetDetailsResponseSettingsCustomKeys
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_global_dial_in_countries import MeetingsGetDetailsResponseSettingsGlobalDialInCountries
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_global_dial_in_numbers import MeetingsGetDetailsResponseSettingsGlobalDialInNumbers
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_language_interpretation import MeetingsGetDetailsResponseSettingsLanguageInterpretation
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_resources import MeetingsGetDetailsResponseSettingsResources
from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_sign_language_interpretation import MeetingsGetDetailsResponseSettingsSignLanguageInterpretation

class RequiredMeetingsGetDetailsResponseSettings(TypedDict):
    pass

class OptionalMeetingsGetDetailsResponseSettings(TypedDict, total=False):
    # Allow attendees to join the meeting from multiple devices. This setting only works for meetings that require [registration](https://support.zoom.us/hc/en-us/articles/211579443-Setting-up-registration-for-a-meeting).
    allow_multiple_devices: bool

    # A semicolon-separated list of the meeting's alternative hosts' email addresses or IDs.
    alternative_hosts: str

    # Flag to determine whether to send email notifications to alternative hosts, default value is true.
    alternative_hosts_email_notification: bool

    # Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher.
    alternative_host_update_polls: bool

    # Enable registration and set approval for the registration. Note that this feature requires the host to be of **Licensed** user type. **Registration cannot be enabled for a basic user.**            `0` - Automatically approve.    `1` - Manually approve.    `2` - No registration required.
    approval_type: int

    approved_or_denied_countries_or_regions: MeetingsGetDetailsResponseSettingsApprovedOrDeniedCountriesOrRegions

    # Determine how participants can join the audio portion of the meeting.    `both` - Both Telephony and VoIP.    `telephony` - Telephony only.    `voip` - VoIP only.    `thirdParty` - Third party audio conference.
    audio: str

    # Third party audio conference info.
    audio_conference_info: str

    # If user has configured [Sign Into Zoom with Specified Domains](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated.
    authentication_domains: str

    authentication_exception: MeetingsGetDetailsResponseSettingsAuthenticationException

    # Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f).
    authentication_name: str

    # Meeting authentication option id.
    authentication_option: str

    # Automatic recording:    `local` - Record on local.    `cloud` -  Record on cloud.    `none` - Disabled.
    auto_recording: str

    breakout_room: MeetingsGetDetailsResponseSettingsBreakoutRoom

    # Indicates the type of calendar integration used to schedule the meeting.  * `1` - [Zoom Outlook add-in](https://support.zoom.us/hc/en-us/articles/360031592971-Getting-started-with-Outlook-plugin-and-add-in)  * `2` - [Zoom for Google Workspace add-on](https://support.zoom.us/hc/en-us/articles/360020187492-Using-the-Zoom-for-Google-Workspace-add-on)  Works with the `private_meeting` field to determine whether to share details of meetings or not.
    calendar_type: int

    # Close registration after event date
    close_registration: bool

    # WARNING: This property is deprecated
    # Host meeting in China.
    cn_meeting: bool

    # Contact email for registration
    contact_email: str

    # Contact name for registration
    contact_name: str

    custom_keys: MeetingsGetDetailsResponseSettingsCustomKeys

    # Whether to send email notifications to [alternative hosts](https://support.zoom.us/hc/en-us/articles/208220166) and [users with scheduling privileges](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-privilege). This value defaults to `true`.
    email_notification: bool

    # Choose between enhanced encryption and [end-to-end encryption](https://support.zoom.us/hc/en-us/articles/360048660871) when starting or a meeting. When using end-to-end encryption, several features (e.g. cloud recording, phone/SIP/H.323 dial-in) will be **automatically disabled**.    `enhanced_encryption` - Enhanced encryption. Encryption is stored in the cloud if you enable this option.       `e2ee` - [End-to-end encryption](https://support.zoom.us/hc/en-us/articles/360048660871). The encryption key is stored in your local device and can not be obtained by anyone else. Enabling this setting also **disables** the join before host, cloud recording, streaming, live transcription, breakout rooms, polling, 1:1 private chat, and meeting reactions features.
    encryption_type: str

    # WARNING: This property is deprecated
    # Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**          As an alternative, use the `meeting_authentication`, `authentication_option`, and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the meeting.
    enforce_login: bool

    # WARNING: This property is deprecated
    # Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**          As an alternative, use the `meeting_authentication`, `authentication_option`, and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the meeting.
    enforce_login_domains: str

    # Whether the [**Focus Mode** feature](https://support.zoom.us/hc/en-us/articles/360061113751-Using-focus-mode) is enabled when the meeting starts.
    focus_mode: bool

    global_dial_in_countries: MeetingsGetDetailsResponseSettingsGlobalDialInCountries

    global_dial_in_numbers: MeetingsGetDetailsResponseSettingsGlobalDialInNumbers

    # Start video when the host joins the meeting.
    host_video: bool

    # WARNING: This property is deprecated
    # Host meeting in India.
    in_meeting: bool

    # If the value of `join_before_host` field is set to true, this field can be used to indicate time limits when a participant may join a meeting before a host.  *  `0` - Allow participant to join anytime. *  `5` - Allow participant to join 5 minutes before meeting start time.  * `10` - Allow participant to join 10 minutes before meeting start time.
    jbh_time: int

    # Allow participants to join the meeting before the host starts the meeting. Only used for scheduled or recurring meetings.
    join_before_host: bool

    language_interpretation: MeetingsGetDetailsResponseSettingsLanguageInterpretation

    sign_language_interpretation: MeetingsGetDetailsResponseSettingsSignLanguageInterpretation

    # `true` - Only authenticated users can join meetings.
    meeting_authentication: bool

    # Mute participants upon entry.
    mute_upon_entry: bool

    # Start video when participants join the meeting.
    participant_video: bool

    # Whether the meeting is set as private.
    private_meeting: bool

    # Whether to send registrants an email confirmation. * `true` - Send a confirmation email. * `false` - Do not send a confirmation email.
    registrants_confirmation_email: bool

    # Whether to send registrants email notifications about their registration approval, cancellation, or rejection.  * `true` - Send an email notification. * `false` - Do not send an email notification.   Set this value to `true` to also use the `registrants_confirmation_email` parameter.
    registrants_email_notification: bool

    # Registration type. Used for recurring meeting with fixed time only.   `1` Attendees register once and can attend any of the occurrences.    `2` Attendees need to register for each occurrence to attend.    `3` Attendees register once and can choose one or more occurrences to attend.
    registration_type: int

    # Show social share buttons on the meeting registration page. This setting only works for meetings that require [registration](https://support.zoom.us/hc/en-us/articles/211579443-Setting-up-registration-for-a-meeting).
    show_share_button: bool

    # Use a [personal meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi). Only used for scheduled meetings and recurring meetings with no fixed time.
    use_pmi: bool

    # Enable waiting room
    waiting_room: bool

    # Add watermark when viewing a shared screen.
    watermark: bool

    # Whether the **Allow host to save video order** feature is enabled.
    host_save_video_order: bool

    # Whether to set the meeting as an internal meeting.
    internal_meeting: bool

    continuous_meeting_chat: MeetingsGetDetailsResponseSettingsContinuousMeetingChat

    # Whether to set the meeting as a participant focused meeting.
    participant_focused_meeting: bool

    # Whether to push meeting changes to the calendar.    To enable this feature, configure the **Configure Calendar and Contacts Service** in the user's profile page of the Zoom web portal and enable the **Automatically sync Zoom calendar events information bi-directionally between Zoom and integrated calendars.** setting in the **Settings** page of the Zoom web portal. * `true` - Push meeting changes to the calendar. * `false` - Do not push meeting changes to the calendar.
    push_change_to_calendar: bool

    resources: MeetingsGetDetailsResponseSettingsResources

    # Whether to automatically start a meeting summary.
    auto_start_meeting_summary: bool

    # Whether to automatically start AI Companion questions.
    auto_start_ai_companion_questions: bool

class MeetingsGetDetailsResponseSettings(RequiredMeetingsGetDetailsResponseSettings, OptionalMeetingsGetDetailsResponseSettings):
    pass
