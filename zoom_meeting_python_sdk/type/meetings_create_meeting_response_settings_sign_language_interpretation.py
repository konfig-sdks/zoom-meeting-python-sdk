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

from zoom_meeting_python_sdk.type.meetings_create_meeting_response_settings_sign_language_interpretation_interpreters import MeetingsCreateMeetingResponseSettingsSignLanguageInterpretationInterpreters

class RequiredMeetingsCreateMeetingResponseSettingsSignLanguageInterpretation(TypedDict):
    pass

class OptionalMeetingsCreateMeetingResponseSettingsSignLanguageInterpretation(TypedDict, total=False):
    # Whether to enable [sign language interpretation](https://support.zoom.us/hc/en-us/articles/9644962487309-Using-sign-language-interpretation-in-a-meeting-or-webinar) for the meeting.
    enable: bool

    interpreters: MeetingsCreateMeetingResponseSettingsSignLanguageInterpretationInterpreters

class MeetingsCreateMeetingResponseSettingsSignLanguageInterpretation(RequiredMeetingsCreateMeetingResponseSettingsSignLanguageInterpretation, OptionalMeetingsCreateMeetingResponseSettingsSignLanguageInterpretation):
    pass
