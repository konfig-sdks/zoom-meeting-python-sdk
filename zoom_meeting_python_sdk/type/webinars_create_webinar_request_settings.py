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

from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_attendees_and_panelists_reminder_email_notification import WebinarsCreateWebinarRequestSettingsAttendeesAndPanelistsReminderEmailNotification
from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_follow_up_absentees_email_notification import WebinarsCreateWebinarRequestSettingsFollowUpAbsenteesEmailNotification
from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_follow_up_attendees_email_notification import WebinarsCreateWebinarRequestSettingsFollowUpAttendeesEmailNotification
from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_global_dial_in_countries import WebinarsCreateWebinarRequestSettingsGlobalDialInCountries
from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_language_interpretation import WebinarsCreateWebinarRequestSettingsLanguageInterpretation
from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_question_and_answer import WebinarsCreateWebinarRequestSettingsQuestionAndAnswer
from zoom_meeting_python_sdk.type.webinars_create_webinar_request_settings_sign_language_interpretation import WebinarsCreateWebinarRequestSettingsSignLanguageInterpretation

class RequiredWebinarsCreateWebinarRequestSettings(TypedDict):
    pass

class OptionalWebinarsCreateWebinarRequestSettings(TypedDict, total=False):
    # Allow attendees to join from multiple devices.
    allow_multiple_devices: bool

    # Alternative host emails or IDs. Multiple values separated by comma.
    alternative_hosts: str

    # Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher.
    alternative_host_update_polls: bool

    # The default value is `2`. To enable registration required, set the approval type to `0` or `1`.  Values include:      `0` - Automatically approve.    `1` - Manually approve.    `2` - No registration required.
    approval_type: int

    attendees_and_panelists_reminder_email_notification: WebinarsCreateWebinarRequestSettingsAttendeesAndPanelistsReminderEmailNotification

    # Determine how participants can join the audio portion of the meeting.(Not supported for simulive webinar.)
    audio: str

    # Third party audio conference info.
    audio_conference_info: str

    # Meeting authentication domains. This option allows you to specify the rule so that Zoom users whose email address contains a certain domain can join the webinar. You can either provide multiple comma-separated domains, use a wildcard for listing domains, or use both methods.
    authentication_domains: str

    # Specify the authentication type for users to join a Webinar with`meeting_authentication` setting set to `true`. The value of this field can be retrieved from the `id` field within `authentication_options` array in the response of [**Get user settings**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/userSettings) API.
    authentication_option: str

    # Automatic recording. Not supported for simulive webinar.     `local` - Record on local.    `cloud` -  Record on cloud.    `none` - Disabled.
    auto_recording: str

    # WARNING: This property is deprecated
    # Close registration after event date.
    close_registration: bool

    # Contact email for registration
    contact_email: str

    # Contact name for registration
    contact_name: str

    # Set the email language. `en-US`,`de-DE`,`es-ES`,`fr-FR`,`id-ID`,`jp-JP`,`nl-NL`,`pl-PL`,`pt-PT`,`ru-RU`,`tr-TR`,`zh-CN`, `zh-TW`, `ko-KO`, `it-IT`, `vi-VN`.
    email_language: str

    # WARNING: This property is deprecated
    # Only signed-in users can join this meeting.   **This field is deprecated and will not be supported in future.**          Instead of this field, use the `meeting_authentication`, `authentication_option`, or `authentication_domains` fields to establish the authentication mechanism for this Webinar. 
    enforce_login: bool

    # WARNING: This property is deprecated
    # Only signed-in users with specified domains can join meetings.  **This field is deprecated and will not be supported in future.**        Instead of this field, use the `authentication_domains` field for this webinar. 
    enforce_login_domains: str

    follow_up_absentees_email_notification: WebinarsCreateWebinarRequestSettingsFollowUpAbsenteesEmailNotification

    follow_up_attendees_email_notification: WebinarsCreateWebinarRequestSettingsFollowUpAttendeesEmailNotification

    global_dial_in_countries: WebinarsCreateWebinarRequestSettingsGlobalDialInCountries

    # Default to HD video.(Not supported for simulive webinar.)
    hd_video: bool

    # Whether HD video for attendees is enabled. This value defaults to `false`.(Not supported for simulive webinar.)
    hd_video_for_attendees: bool

    # Start video when host joins webinar.(Not supported for simulive webinar.)
    host_video: bool

    language_interpretation: WebinarsCreateWebinarRequestSettingsLanguageInterpretation

    sign_language_interpretation: WebinarsCreateWebinarRequestSettingsSignLanguageInterpretation

    # Require panelists to authenticate to join
    panelist_authentication: bool

    # Only [authenticated](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) users can join meeting if the value of this field is set to `true`.
    meeting_authentication: bool

    # Add watermark that identifies the viewing participant. Not supported for simulive webinar.
    add_watermark: bool

    # Add audio watermark that identifies the participants. Not supported for simulive webinar.
    add_audio_watermark: bool

    # Make the webinar on-demand. Not supported for simulive webinar.
    on_demand: bool

    # Send invitation email to panelists. If `false`, do not send invitation email to panelists.
    panelists_invitation_email_notification: bool

    # Start video when panelists join webinar. Not supported for simulive webinar.
    panelists_video: bool

    # Zoom will open a survey page in attendees' browsers after leaving the webinar
    post_webinar_survey: bool

    # Enable practice session.
    practice_session: bool

    question_and_answer: WebinarsCreateWebinarRequestSettingsQuestionAndAnswer

    # Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.
    registrants_email_notification: bool

    # Restrict number of registrants for a webinar. By default, it is set to `0`. A `0` value means that the restriction option is disabled. Provide a number higher than 0 to restrict the webinar registrants by the that number.
    registrants_restrict_number: int

    # Registration types. Only used for recurring webinars with a fixed time.    `1` - Attendees register once and can attend any of the webinar sessions.    `2` - Attendees need to register for each session in order to attend.    `3` - Attendees register once and can choose one or more sessions to attend.
    registration_type: int

    # Whether to always send 1080p video to attendees. This value defaults to `false`.(Not supported for simulive webinar.)
    send_1080p_video_to_attendees: bool

    # Show social share buttons on the registration page.
    show_share_button: bool

    # Survey URL for post webinar survey
    survey_url: str

    # Whether the **Webinar Session Branding** setting is enabled. This setting lets hosts visually customize a webinar by setting a session background. This also lets hosts set Virtual Background and apply name tags to hosts, alternative hosts, panelists, interpreters, and speakers.
    enable_session_branding: bool

class WebinarsCreateWebinarRequestSettings(RequiredWebinarsCreateWebinarRequestSettings, OptionalWebinarsCreateWebinarRequestSettings):
    pass
