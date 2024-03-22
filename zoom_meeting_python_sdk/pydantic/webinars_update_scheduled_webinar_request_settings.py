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

from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_attendees_and_panelists_reminder_email_notification import WebinarsUpdateScheduledWebinarRequestSettingsAttendeesAndPanelistsReminderEmailNotification
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_follow_up_absentees_email_notification import WebinarsUpdateScheduledWebinarRequestSettingsFollowUpAbsenteesEmailNotification
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_follow_up_attendees_email_notification import WebinarsUpdateScheduledWebinarRequestSettingsFollowUpAttendeesEmailNotification
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_global_dial_in_countries import WebinarsUpdateScheduledWebinarRequestSettingsGlobalDialInCountries
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_language_interpretation import WebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretation
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_question_and_answer import WebinarsUpdateScheduledWebinarRequestSettingsQuestionAndAnswer
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_sign_language_interpretation import WebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation

class WebinarsUpdateScheduledWebinarRequestSettings(BaseModel):
    # Allow attendees to join from multiple devices.
    allow_multiple_devices: typing.Optional[bool] = Field(None, alias='allow_multiple_devices')

    # Alternative host emails or IDs. Separate multiple values by commas.
    alternative_hosts: typing.Optional[str] = Field(None, alias='alternative_hosts')

    # Whether the **Allow alternative hosts to add or edit polls** feature is enabled. This requires Zoom version 5.8.0 or higher.
    alternative_host_update_polls: typing.Optional[bool] = Field(None, alias='alternative_host_update_polls')

    # `0` - Automatically approve.    `1` - Manually approve.    `2` - No registration required.
    approval_type: typing.Optional[Literal[0, 1, 2]] = Field(None, alias='approval_type')

    attendees_and_panelists_reminder_email_notification: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsAttendeesAndPanelistsReminderEmailNotification] = Field(None, alias='attendees_and_panelists_reminder_email_notification')

    # Determine how participants can join the audio portion of the webinar.
    audio: typing.Optional[Literal["both", "telephony", "voip", "thirdParty"]] = Field(None, alias='audio')

    # Third party audio conference info.
    audio_conference_info: typing.Optional[str] = Field(None, alias='audio_conference_info')

    # If user has configured [**Sign Into Zoom with Specified Domains**](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f) option, this will list the domains that are authenticated.
    authentication_domains: typing.Optional[str] = Field(None, alias='authentication_domains')

    # Authentication name set in the [authentication profile](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars#h_5c0df2e1-cfd2-469f-bb4a-c77d7c0cca6f).
    authentication_name: typing.Optional[str] = Field(None, alias='authentication_name')

    # Webinar authentication option ID.
    authentication_option: typing.Optional[str] = Field(None, alias='authentication_option')

    # Automatic recording.   `local` - Record on local.    `cloud` -  Record on cloud.    `none` - Disabled.
    auto_recording: typing.Optional[Literal["local", "cloud", "none"]] = Field(None, alias='auto_recording')

    # WARNING: This property is deprecated
    # Close registration after event date.
    close_registration: typing.Optional[bool] = Field(None, alias='close_registration')

    # Contact email for registration
    contact_email: typing.Optional[str] = Field(None, alias='contact_email')

    # Contact name for registration
    contact_name: typing.Optional[str] = Field(None, alias='contact_name')

    # Set the email language to one of the following. `en-US`,`de-DE`,`es-ES`,`fr-FR`,`jp-JP`,`pt-PT`,`ru-RU`,`zh-CN`, `zh-TW`, `ko-KO`, `it-IT`, `vi-VN`.
    email_language: typing.Optional[str] = Field(None, alias='email_language')

    # WARNING: This property is deprecated
    # Only signed in users can join this meeting.  **This field is deprecated and will not be supported in the future.**    As an alternative, use the ``meeting_authentication`, `authentication_option`, and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the webinar.
    enforce_login: typing.Optional[bool] = Field(None, alias='enforce_login')

    # WARNING: This property is deprecated
    # Only signed in users with specified domains can join meetings.  **This field is deprecated and will not be supported in the future.**   As an alternative, use the `meeting_authentication`, `authentication_option`, and `authentication_domains` fields to understand the [authentication configurations](https://support.zoom.us/hc/en-us/articles/360037117472-Authentication-Profiles-for-Meetings-and-Webinars) set for the webinar.
    enforce_login_domains: typing.Optional[str] = Field(None, alias='enforce_login_domains')

    follow_up_absentees_email_notification: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsFollowUpAbsenteesEmailNotification] = Field(None, alias='follow_up_absentees_email_notification')

    follow_up_attendees_email_notification: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsFollowUpAttendeesEmailNotification] = Field(None, alias='follow_up_attendees_email_notification')

    global_dial_in_countries: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsGlobalDialInCountries] = Field(None, alias='global_dial_in_countries')

    # Default to HD video.
    hd_video: typing.Optional[bool] = Field(None, alias='hd_video')

    # Whether HD video for attendees is enabled.
    hd_video_for_attendees: typing.Optional[bool] = Field(None, alias='hd_video_for_attendees')

    # Start video when host joins the webinar.
    host_video: typing.Optional[bool] = Field(None, alias='host_video')

    language_interpretation: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretation] = Field(None, alias='language_interpretation')

    sign_language_interpretation: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation] = Field(None, alias='sign_language_interpretation')

    # Require panelists to authenticate to join.
    panelist_authentication: typing.Optional[bool] = Field(None, alias='panelist_authentication')

    # Only authenticated users can join the webinar.
    meeting_authentication: typing.Optional[bool] = Field(None, alias='meeting_authentication')

    # Add watermark that identifies the viewing participant.
    add_watermark: typing.Optional[bool] = Field(None, alias='add_watermark')

    # Add audio watermark that identifies the participants.
    add_audio_watermark: typing.Optional[bool] = Field(None, alias='add_audio_watermark')

    # Send notification email to registrants when the host updates a webinar.
    notify_registrants: typing.Optional[bool] = Field(None, alias='notify_registrants')

    # Make the webinar on-demand.
    on_demand: typing.Optional[bool] = Field(None, alias='on_demand')

    # Send invitation email to panelists. If `false`, do not send invitation email to panelists.
    panelists_invitation_email_notification: typing.Optional[bool] = Field(None, alias='panelists_invitation_email_notification')

    # Start video when panelists join the webinar.
    panelists_video: typing.Optional[bool] = Field(None, alias='panelists_video')

    # Zoom will open a survey page in attendees' browsers after leaving the webinar.
    post_webinar_survey: typing.Optional[bool] = Field(None, alias='post_webinar_survey')

    # Enable practice session.
    practice_session: typing.Optional[bool] = Field(None, alias='practice_session')

    question_and_answer: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettingsQuestionAndAnswer] = Field(None, alias='question_and_answer')

    # Send confirmation email to registrants
    registrants_confirmation_email: typing.Optional[bool] = Field(None, alias='registrants_confirmation_email')

    # Send email notifications to registrants about approval, cancellation, denial of the registration. The value of this field must be set to true in order to use the `registrants_confirmation_email` field.
    registrants_email_notification: typing.Optional[bool] = Field(None, alias='registrants_email_notification')

    # Restrict number of registrants for a webinar. By default, it is set to `0`. A `0` value means that the restriction option is disabled. Provide a number higher than 0 to restrict the webinar registrants by the that number.
    registrants_restrict_number: typing.Optional[int] = Field(None, alias='registrants_restrict_number')

    # Registration types. Only used for recurring webinars with a fixed time.    `1` - Attendees register once and can attend any of the webinar sessions.    `2` - Attendees need to register for each session in order to attend.    `3` - Attendees register once and can choose one or more sessions to attend.
    registration_type: typing.Optional[Literal[1, 2, 3]] = Field(None, alias='registration_type')

    # Always send 1080p video to attendees.
    send_1080p_video_to_attendees: typing.Optional[bool] = Field(None, alias='send_1080p_video_to_attendees')

    # Show social share buttons on the registration page.
    show_share_button: typing.Optional[bool] = Field(None, alias='show_share_button')

    # Survey url for post webinar survey
    survey_url: typing.Optional[str] = Field(None, alias='survey_url')

    # Whether the **Webinar Session Branding** setting is enabled. This setting lets hosts visually customize a webinar by setting a session background. This also lets hosts use [Webinar Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) to set the virtual background for and apply name tags to hosts, alternative hosts, panelists, interpreters, and speakers.
    enable_session_branding: typing.Optional[bool] = Field(None, alias='enable_session_branding')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
