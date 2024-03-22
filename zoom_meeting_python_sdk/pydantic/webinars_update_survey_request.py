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

from zoom_meeting_python_sdk.pydantic.webinars_update_survey_request_custom_survey import WebinarsUpdateSurveyRequestCustomSurvey

class WebinarsUpdateSurveyRequest(BaseModel):
    custom_survey: typing.Optional[WebinarsUpdateSurveyRequestCustomSurvey] = Field(None, alias='custom_survey')

    # Whether the **Show in the browser when the webinar ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.
    show_in_the_browser: typing.Optional[bool] = Field(None, alias='show_in_the_browser')

    # Whether the **Show the link on the follow-up email** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `false`.
    show_in_the_follow_up_email: typing.Optional[bool] = Field(None, alias='show_in_the_follow_up_email')

    # The link to the third party webinar survey.
    third_party_survey: typing.Optional[str] = Field(None, alias='third_party_survey')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
