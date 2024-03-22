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


class WebinarsGetDetailsResponseSettingsSignLanguageInterpretationInterpretersItem(BaseModel):
    # The interpreter's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # The interpreter's sign language.    To get this value, use the `sign_language_interpretation` object's `languages` and `custom_languages` values in the [**Get user settings**](/api-reference/zoom-api/methods#operation/userSettings) API response.
    sign_language: typing.Optional[str] = Field(None, alias='sign_language')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
