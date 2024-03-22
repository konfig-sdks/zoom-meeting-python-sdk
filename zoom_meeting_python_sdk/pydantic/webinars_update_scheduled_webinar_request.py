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

from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_recurrence import WebinarsUpdateScheduledWebinarRequestRecurrence
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings import WebinarsUpdateScheduledWebinarRequestSettings
from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_tracking_fields import WebinarsUpdateScheduledWebinarRequestTrackingFields

class WebinarsUpdateScheduledWebinarRequest(BaseModel):
    # Webinar description.
    agenda: typing.Optional[str] = Field(None, alias='agenda')

    # Webinar duration, in minutes. Used for scheduled webinar only.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # [Webinar passcode](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords). By default, passcode may only contain the following characters: [a-z A-Z 0-9 @ - _ * !] and can have a maximum of 10 characters.  **Note:** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](https://developers.zoom.us) API or the [**Get account settings**](https://developers.zoom.us) API.   If **Require a passcode when scheduling new meetings** setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the passcode field will be autogenerated for the webinar in the response even if it is not provided in the API request.
    password: typing.Optional[str] = Field(None, alias='password')

    # The user's email address or `userId` to schedule a webinar for.
    schedule_for: typing.Optional[str] = Field(None, alias='schedule_for')

    recurrence: typing.Optional[WebinarsUpdateScheduledWebinarRequestRecurrence] = Field(None, alias='recurrence')

    settings: typing.Optional[WebinarsUpdateScheduledWebinarRequestSettings] = Field(None, alias='settings')

    # Webinar start time, in the format `yyyy-MM-dd'T'HH:mm:ss'Z'`. Should be in GMT time. In the format `yyyy-MM-dd'T'HH:mm:ss`. This should be in local time and the timezone should be specified. Only used for scheduled webinars and recurring webinars with a fixed time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The timezone to assign to the `start_time` value. This field is only used for scheduled or recurring webinars with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # The webinar topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    tracking_fields: typing.Optional[WebinarsUpdateScheduledWebinarRequestTrackingFields] = Field(None, alias='tracking_fields')

    # Webinar types.   `5` - webinar.    `6` - Recurring webinar with no fixed time.    `9` - Recurring webinar with a fixed time.
    type: typing.Optional[Literal[5, 6, 9]] = Field(None, alias='type')

    # Whether to set the webinar simulive.
    is_simulive: typing.Optional[bool] = Field(None, alias='is_simulive')

    # The previously recorded file's ID for `simulive`.
    record_file_id: typing.Optional[str] = Field(None, alias='record_file_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
