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

from zoom_meeting_python_sdk.type.meetings_get_details_response_settings_language_interpretation_interpreters import MeetingsGetDetailsResponseSettingsLanguageInterpretationInterpreters

class RequiredMeetingsGetDetailsResponseSettingsLanguageInterpretation(TypedDict):
    pass

class OptionalMeetingsGetDetailsResponseSettingsLanguageInterpretation(TypedDict, total=False):
    # Whether to enable [language interpretation](https://support.zoom.us/hc/en-us/articles/360034919791-Language-interpretation-in-meetings-and-webinars) for the meeting.
    enable: bool

    interpreters: MeetingsGetDetailsResponseSettingsLanguageInterpretationInterpreters

class MeetingsGetDetailsResponseSettingsLanguageInterpretation(RequiredMeetingsGetDetailsResponseSettingsLanguageInterpretation, OptionalMeetingsGetDetailsResponseSettingsLanguageInterpretation):
    pass
