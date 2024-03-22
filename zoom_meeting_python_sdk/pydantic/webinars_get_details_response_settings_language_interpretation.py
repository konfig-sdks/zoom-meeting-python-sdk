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

from zoom_meeting_python_sdk.pydantic.webinars_get_details_response_settings_language_interpretation_interpreters import WebinarsGetDetailsResponseSettingsLanguageInterpretationInterpreters

class WebinarsGetDetailsResponseSettingsLanguageInterpretation(BaseModel):
    # Enable [language interpretation](https://support.zoom.us/hc/en-us/articles/360034919791-Language-interpretation-in-meetings-and-webinars) for the webinar.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    interpreters: typing.Optional[WebinarsGetDetailsResponseSettingsLanguageInterpretationInterpreters] = Field(None, alias='interpreters')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
