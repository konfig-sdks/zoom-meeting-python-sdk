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


class WebinarsCreateWebinarResponseSettingsLanguageInterpretationInterpretersItem(BaseModel):
    # The interpreter's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # A comma-separated list of the interpreter's languages. The string must contain two [country IDs](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).   For example, if the interpreter will translate from English to Chinese, then this value will be `US,CN`.
    languages: typing.Optional[str] = Field(None, alias='languages')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
