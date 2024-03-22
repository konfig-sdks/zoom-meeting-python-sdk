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

from zoom_meeting_python_sdk.type.webinars_update_scheduled_webinar_request_settings_sign_language_interpretation_interpreters import WebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretationInterpreters

class RequiredWebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation(TypedDict):
    pass

class OptionalWebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation(TypedDict, total=False):
    # Whether to enable [sign language interpretation](https://support.zoom.us/hc/en-us/articles/9644962487309-Using-sign-language-interpretation-in-a-meeting-or-webinar) for the webinar.
    enable: bool

    interpreters: WebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretationInterpreters

class WebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation(RequiredWebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation, OptionalWebinarsUpdateScheduledWebinarRequestSettingsSignLanguageInterpretation):
    pass
