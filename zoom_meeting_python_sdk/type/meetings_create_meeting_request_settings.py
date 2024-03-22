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

from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_additional_data_center_regions import MeetingsCreateMeetingRequestSettingsAdditionalDataCenterRegions
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_approved_or_denied_countries_or_regions import MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_authentication_exception import MeetingsCreateMeetingRequestSettingsAuthenticationException
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_breakout_room import MeetingsCreateMeetingRequestSettingsBreakoutRoom
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_continuous_meeting_chat import MeetingsCreateMeetingRequestSettingsContinuousMeetingChat
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_global_dial_in_countries import MeetingsCreateMeetingRequestSettingsGlobalDialInCountries
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_language_interpretation import MeetingsCreateMeetingRequestSettingsLanguageInterpretation
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_meeting_invitees import MeetingsCreateMeetingRequestSettingsMeetingInvitees
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_resources import MeetingsCreateMeetingRequestSettingsResources
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_sign_language_interpretation import MeetingsCreateMeetingRequestSettingsSignLanguageInterpretation

class RequiredMeetingsCreateMeetingRequestSettings(TypedDict):
    pass

class OptionalMeetingsCreateMeetingRequestSettings(TypedDict, total=False):
    additional_data_center_regions: MeetingsCreateMeetingRequestSettingsAdditionalDataCenterRegions

    # Whether to allow attendees to join a meeting from multiple devices. This setting is only applied to meetings with registration enabled.
    allow_multiple_devices: bool

    # A semicolon-separated list of the meeting's alternative hosts' email addresses or IDs.
    alternative_hosts: str

    # Whether to send email notifications to alternative hosts. This value defaults to `true`.
    alternative_hosts_email_notification: bool

    # Enable meeting registration approval. * `0` - Automatically approve registration. * `1` - Manually approve registration. * `2` - No registration required.  This value defaults to `2`.
    approval_type: int

    approved_or_denied_countries_or_regions: MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions

    # How participants join the audio portion of the meeting. * `both` - Both telephony and VoIP.  * `telephony` - Telephony only.  * `voip` - VoIP only.  * `thirdParty` - Third party audio conference.
    audio: str

    # Third party audio conference info.
    audio_conference_info: str

    # The meeting's authenticated domains. Only Zoom users whose email address contains an authenticated domain can join the meeting. Comma-separate multiple domains or use a wildcard for listing domains.
    authentication_domains: str

    authentication_exception: MeetingsCreateMeetingRequestSettingsAuthenticationException

    # If the `meeting_authentication` value is `true`, the type of authentication required for users to join a meeting.  To get this value, use the `authentication_options` array's `id` value in the [**Get user settings**](https://developers.zoom.us/docs/api-reference/zoom-api/methods#operation/userSettings) API response.
    authentication_option: str

    # The automatic recording settings.  * `local` - Record the meeting locally.  * `cloud` - Record the meeting to the cloud.  * `none` - Auto-recording disabled.  This value defaults to `none`.
    auto_recording: str

    breakout_room: MeetingsCreateMeetingRequestSettingsBreakoutRoom

    # Indicates the type of calendar integration used to schedule the meeting. * `1` - [Zoom Outlook add-in](https://support.zoom.us/hc/en-us/articles/360031592971-Getting-started-with-Outlook-plugin-and-add-in)  * `2` - [Zoom for Google Workspace add-on](https://support.zoom.us/hc/en-us/articles/360020187492-Using-the-Zoom-for-Google-Workspace-add-on)  Works with the `private_meeting` field to determine whether to share details of meetings or not.
    calendar_type: int

    # Whether to close registration after the event date. This value defaults to `false`.
    close_registration: bool

    # WARNING: This property is deprecated
    # Whether to host the meeting in China (CN). This value defaults to `false`.
    cn_meeting: bool

    # The contact email address for meeting registration.
    contact_email: str

    # The contact name for meeting registration.
    contact_name: str

    # Whether to send email notifications to [alternative hosts](https://support.zoom.us/hc/en-us/articles/208220166) and [users with scheduling privileges](https://support.zoom.us/hc/en-us/articles/201362803-Scheduling-privilege). This value defaults to `true`.
    email_notification: bool

    # The type of [end-to-end (E2EE) encryption](https://support.zoom.us/hc/en-us/articles/360048660871) to use for the meeting.  * `enhanced_encryption` - Enhanced encryption. Encryption is stored in the cloud when you enable this option.  * `e2ee` - End-to-end encryption. The encryption key is stored on your local device and **cannot** be obtained by anyone else. When you use E2EE encryption, [certain features](https://support.zoom.us/hc/en-us/articles/360048660871), such as cloud recording or phone and SIP/H.323 dial-in, are **disabled**.
    encryption_type: str

    # Whether to enable the [**Focus Mode** feature](https://support.zoom.us/hc/en-us/articles/360061113751-Using-focus-mode) when the meeting starts.
    focus_mode: bool

    global_dial_in_countries: MeetingsCreateMeetingRequestSettingsGlobalDialInCountries

    # Whether to start meetings with the host video on.
    host_video: bool

    # WARNING: This property is deprecated
    # Whether to host the meeting in India (IN). This value defaults to `false`.
    in_meeting: bool

    # If the value of the `join_before_host` field is `true`, this field indicates the time limits when a participant can join a meeting before the meeting's host.  * `0` - Allow the participant to join the meeting at anytime. * `5` - Allow the participant to join 5 minutes before the meeting's start time. * `10` - Allow the participant to join 10 minutes before the meeting's start time.
    jbh_time: int

    # Whether participants can join the meeting before its host. This field is only used for scheduled meetings (`2`) or recurring meetings (`3` and `8`). This value defaults to `false`.  If the [**Waiting Room** feature](https://support.zoom.us/hc/en-us/articles/115000332726-Waiting-Room) is enabled, this setting is **disabled**.
    join_before_host: bool

    language_interpretation: MeetingsCreateMeetingRequestSettingsLanguageInterpretation

    sign_language_interpretation: MeetingsCreateMeetingRequestSettingsSignLanguageInterpretation

    # If true, only [authenticated](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) users can join the meeting.
    meeting_authentication: bool

    meeting_invitees: MeetingsCreateMeetingRequestSettingsMeetingInvitees

    # Whether to mute participants upon entry.
    mute_upon_entry: bool

    # Whether to start meetings with the participant video on.
    participant_video: bool

    # Whether to set the meeting as private.
    private_meeting: bool

    # Whether to send registrants an email confirmation.  * `true` - Send a confirmation email.  * `false` - Do not send a confirmation email.
    registrants_confirmation_email: bool

    # Whether to send registrants email notifications about their registration approval, cancellation, or rejection.  * `true` - Send an email notification. * `false` - Do not send an email notification.   Set this value to `true` to also use the `registrants_confirmation_email` parameter.
    registrants_email_notification: bool

    # The meeting's registration type.  * `1` - Attendees register once and can attend any meeting occurrence.  * `2` - Attendees must register for each meeting occurrence.  * `3` - Attendees register once and can select one or more meeting occurrences to attend.  This field is only for recurring meetings with fixed times (`8`). This value defaults to `1`.
    registration_type: int

    # Whether to include social media sharing buttons on the meeting's registration page. This setting is only applied to meetings with registration enabled.
    show_share_button: bool

    # Whether to use a [Personal Meeting ID (PMI)](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#understanding-personal-meeting-id-pmi) instead of a generated meeting ID. This field is only used for scheduled meetings (`2`), instant meetings (`1`), or recurring meetings with no fixed time (`3`). This value defaults to `false`.
    use_pmi: bool

    # Whether to enable the [**Waiting Room** feature](https://support.zoom.us/hc/en-us/articles/115000332726-Waiting-Room). If this value is `true`, this **disables** the `join_before_host` setting.
    waiting_room: bool

    # Whether to add a watermark when viewing a shared screen.
    watermark: bool

    # Whether the **Allow host to save video order** feature is enabled.
    host_save_video_order: bool

    # Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher.
    alternative_host_update_polls: bool

    # Whether to set the meeting as an internal meeting.
    internal_meeting: bool

    continuous_meeting_chat: MeetingsCreateMeetingRequestSettingsContinuousMeetingChat

    # Whether to set the meeting as a participant focused meeting.
    participant_focused_meeting: bool

    # Whether to push meeting changes to the calendar.    To enable this feature, configure the **Configure Calendar and Contacts Service** in the user's profile page of the Zoom web portal and enable the **Automatically sync Zoom calendar events information bi-directionally between Zoom and integrated calendars.** setting in the **Settings** page of the Zoom web portal. * `true` - Push meeting changes to the calendar. * `false` - Do not push meeting changes to the calendar.
    push_change_to_calendar: bool

    resources: MeetingsCreateMeetingRequestSettingsResources

    # Whether to automatically start a meeting summary.
    auto_start_meeting_summary: bool

    # Whether to automatically start AI Companion questions.
    auto_start_ai_companion_questions: bool

class MeetingsCreateMeetingRequestSettings(RequiredMeetingsCreateMeetingRequestSettings, OptionalMeetingsCreateMeetingRequestSettings):
    pass
