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

from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_attendees_and_panelists_reminder_email_notification import WebinarsCreateWebinarResponseSettingsAttendeesAndPanelistsReminderEmailNotification
from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_follow_up_absentees_email_notification import WebinarsCreateWebinarResponseSettingsFollowUpAbsenteesEmailNotification
from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_follow_up_attendees_email_notification import WebinarsCreateWebinarResponseSettingsFollowUpAttendeesEmailNotification
from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_global_dial_in_countries import WebinarsCreateWebinarResponseSettingsGlobalDialInCountries
from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_language_interpretation import WebinarsCreateWebinarResponseSettingsLanguageInterpretation
from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_question_and_answer import WebinarsCreateWebinarResponseSettingsQuestionAndAnswer
from zoom_meeting_python_sdk.type.webinars_create_webinar_response_settings_sign_language_interpretation import WebinarsCreateWebinarResponseSettingsSignLanguageInterpretation

class RequiredWebinarsCreateWebinarResponseSettings(TypedDict):
    pass

class OptionalWebinarsCreateWebinarResponseSettings(TypedDict, total=False):
    # Allow attendees to join from multiple devices.
    allow_multiple_devices: bool

    # Alternative host emails or IDs. Multiple values separated by comma.
    alternative_hosts: str

    # Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher.
    alternative_host_update_polls: bool

    # `0` - Automatically approve.    `1` - Manually approve.    `2` - No registration required.
    approval_type: int

    attendees_and_panelists_reminder_email_notification: WebinarsCreateWebinarResponseSettingsAttendeesAndPanelistsReminderEmailNotification

    # Determine how participants can join the audio portion of the webinar.
    audio: str

    # Third party audio conference info.
    audio_conference_info: str

    # If user has configured [**Sign Into Zoom with Specified Domains**](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated.
    authentication_domains: str

    # Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f).
    authentication_name: str

    # Webinar authentication option ID.
    authentication_option: str

    # Automatic recording.   `local` - Record on local.    `cloud` -  Record on cloud.    `none` - Disabled.
    auto_recording: str

    # WARNING: This property is deprecated
    # Close registration after event date.
    close_registration: bool

    # Contact email for registration
    contact_email: str

    # Contact name for registration
    contact_name: str

    # Set the email language to one of the following: `en-US`,`de-DE`,`es-ES`,`fr-FR`,`jp-JP`,`pt-PT`,`ru-RU`,`zh-CN`, `zh-TW`, `ko-KO`, `it-IT`, `vi-VN`.
    email_language: str

    # WARNING: This property is deprecated
    # Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**   As an alternative, use the `meeting_authentication`, `authentication_option` and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the webinar.
    enforce_login: bool

    # WARNING: This property is deprecated
    # Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**   As an alternative, use the `meeting_authentication`, `authentication_option` and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the webinar.
    enforce_login_domains: str

    follow_up_absentees_email_notification: WebinarsCreateWebinarResponseSettingsFollowUpAbsenteesEmailNotification

    follow_up_attendees_email_notification: WebinarsCreateWebinarResponseSettingsFollowUpAttendeesEmailNotification

    global_dial_in_countries: WebinarsCreateWebinarResponseSettingsGlobalDialInCountries

    # Default to HD video.
    hd_video: bool

    # Whether HD video for attendees is enabled.
    hd_video_for_attendees: bool

    # Start video when host joins webinar.
    host_video: bool

    language_interpretation: WebinarsCreateWebinarResponseSettingsLanguageInterpretation

    sign_language_interpretation: WebinarsCreateWebinarResponseSettingsSignLanguageInterpretation

    # Require panelists to authenticate to join
    panelist_authentication: bool

    # Only authenticated users can join Webinar.
    meeting_authentication: bool

    # Add watermark that identifies the viewing participant.
    add_watermark: bool

    # Add audio watermark that identifies the participants.
    add_audio_watermark: bool

    # Send notification email to registrants when the host updates a webinar.
    notify_registrants: bool

    # Make the webinar on-demand
    on_demand: bool

    # Send invitation email to panelists. If `false`, do not send invitation email to panelists.
    panelists_invitation_email_notification: bool

    # Start video when panelists join webinar.
    panelists_video: bool

    # Zoom will open a survey page in attendees' browsers after leaving the webinar
    post_webinar_survey: bool

    # Enable practice session.
    practice_session: bool

    question_and_answer: WebinarsCreateWebinarResponseSettingsQuestionAndAnswer

    # Send confirmation email to registrants
    registrants_confirmation_email: bool

    # Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.
    registrants_email_notification: bool

    # Restrict number of registrants for a webinar. By default, it is set to `0`. A `0` value means that the restriction option is disabled. Provide a number higher than 0 to restrict the webinar registrants by the that number.
    registrants_restrict_number: int

    # Registration types. Only used for recurring webinars with a fixed time.    `1` - Attendees register once and can attend any of the webinar sessions.    `2` - Attendees need to register for each session in order to attend.    `3` - Attendees register once and can choose one or more sessions to attend.
    registration_type: int

    # Always send 1080p video to attendees.
    send_1080p_video_to_attendees: bool

    # Show social share buttons on the registration page.
    show_share_button: bool

    # Survey url for post webinar survey
    survey_url: str

    # Whether the **Webinar Session Branding** setting is enabled. This setting lets hosts visually customize a webinar by setting a session background. This also lets hosts use [Webinar Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) to set the Virtual Background for and apply name tags to hosts, alternative hosts, panelists, interpreters, and speakers.
    enable_session_branding: bool

class WebinarsCreateWebinarResponseSettings(RequiredWebinarsCreateWebinarResponseSettings, OptionalWebinarsCreateWebinarResponseSettings):
    pass
