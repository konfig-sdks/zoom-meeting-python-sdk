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

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_settings_sign_language_interpretation_interpreters import MeetingsCreateMeetingRequestSettingsSignLanguageInterpretationInterpreters

class MeetingsCreateMeetingRequestSettingsSignLanguageInterpretation(BaseModel):
    # Whether to enable [sign language interpretation](https://support.zoom.us/hc/en-us/articles/9644962487309-Using-sign-language-interpretation-in-a-meeting-or-webinar) for the meeting.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    interpreters: typing.Optional[MeetingsCreateMeetingRequestSettingsSignLanguageInterpretationInterpreters] = Field(None, alias='interpreters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
