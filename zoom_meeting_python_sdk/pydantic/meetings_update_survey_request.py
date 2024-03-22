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

from zoom_meeting_python_sdk.pydantic.meetings_update_survey_request_custom_survey import MeetingsUpdateSurveyRequestCustomSurvey

class MeetingsUpdateSurveyRequest(BaseModel):
    custom_survey: typing.Optional[MeetingsUpdateSurveyRequestCustomSurvey] = Field(None, alias='custom_survey')

    # Whether the **Show in the browser when the meeting ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.
    show_in_the_browser: typing.Optional[bool] = Field(None, alias='show_in_the_browser')

    # The link to the third party meeting survey.
    third_party_survey: typing.Optional[str] = Field(None, alias='third_party_survey')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
