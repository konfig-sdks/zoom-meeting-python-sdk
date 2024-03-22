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

from zoom_meeting_python_sdk.pydantic.webinars_update_scheduled_webinar_request_settings_language_interpretation_interpreters_item import WebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem

WebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpreters = typing.List[WebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem]
