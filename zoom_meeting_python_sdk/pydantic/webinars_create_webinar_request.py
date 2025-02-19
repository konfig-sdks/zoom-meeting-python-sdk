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

from zoom_meeting_python_sdk.pydantic.webinars_create_webinar_request_recurrence import WebinarsCreateWebinarRequestRecurrence
from zoom_meeting_python_sdk.pydantic.webinars_create_webinar_request_settings import WebinarsCreateWebinarRequestSettings
from zoom_meeting_python_sdk.pydantic.webinars_create_webinar_request_tracking_fields import WebinarsCreateWebinarRequestTrackingFields

class WebinarsCreateWebinarRequest(BaseModel):
    # Webinar description.
    agenda: typing.Optional[str] = Field(None, alias='agenda')

    # Webinar duration in minutes. Used for scheduled webinars only.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Webinar passcode. Passcode may only contain the characters [a-z A-Z 0-9 @ - _ * !]. Maximum of 10 characters.  If **Require a passcode when scheduling new meetings** setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the passcode field will be autogenerated for the Webinar in the response even if it is not provided in the API request.     **Note:** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling the [**Get account settings**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma#operation/accountSettings) API.
    password: typing.Optional[str] = Field(None, alias='password')

    recurrence: typing.Optional[WebinarsCreateWebinarRequestRecurrence] = Field(None, alias='recurrence')

    # The email address or user ID of the user to schedule a webinar for.
    schedule_for: typing.Optional[str] = Field(None, alias='schedule_for')

    settings: typing.Optional[WebinarsCreateWebinarRequestSettings] = Field(None, alias='settings')

    # Webinar start time. We support two formats for `start_time` - local time and GMT.       To set time as GMT the format should be `yyyy-MM-dd`T`HH:mm:ssZ`.  To set time using a specific timezone, use `yyyy-MM-dd`T`HH:mm:ss` format and specify the timezone [ID](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones) in the `timezone` field OR leave it blank and the timezone set on your Zoom account will be used. You can also set the time as UTC as the timezone field.  The `start_time` should only be used for scheduled and / or recurring webinars with fixed time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The webinar template ID to schedule a webinar using a [webinar template](https://support.zoom.us/hc/en-us/articles/115001079746-Webinar-Templates) or a [admin webinar template](https://support.zoom.us/hc/en-us/articles/8137753618957-Configuring-admin-webinar-templates). For a list of webinar templates, use the [**List webinar templates**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/listWebinarTemplates) API.
    template_id: typing.Optional[str] = Field(None, alias='template_id')

    # The timezone to assign to the `start_time` value. This field is only used for scheduled or recurring webinars with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # Webinar topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    tracking_fields: typing.Optional[WebinarsCreateWebinarRequestTrackingFields] = Field(None, alias='tracking_fields')

    # Webinar types.  `5` - Webinar.    `6` - Recurring webinar with no fixed time.    `9` - Recurring webinar with a fixed time.
    type: typing.Optional[Literal[5, 6, 9]] = Field(None, alias='type')

    # Whether to set the webinar simulive.
    is_simulive: typing.Optional[bool] = Field(None, alias='is_simulive')

    # The previously recorded file's ID for `simulive`.
    record_file_id: typing.Optional[str] = Field(None, alias='record_file_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
