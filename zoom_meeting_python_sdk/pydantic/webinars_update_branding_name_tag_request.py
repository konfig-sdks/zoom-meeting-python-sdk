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


class WebinarsUpdateBrandingNameTagRequest(BaseModel):
    # The name tag's name.  **Note:** This value cannot exceed more than 50 characters.
    name: typing.Optional[str] = Field(None, alias='name')

    # The name tag's text color.
    text_color: typing.Optional[str] = Field(None, alias='text_color')

    # The name tag's accent color.
    accent_color: typing.Optional[str] = Field(None, alias='accent_color')

    # The name tag's background color.
    background_color: typing.Optional[str] = Field(None, alias='background_color')

    # Whether set the name tag as the default name tag or not.
    is_default: typing.Optional[bool] = Field(None, alias='is_default')

    # Whether to set the name tag as the new default for all panelists or not. This includes panelists not currently assigned a default name tag.
    set_default_for_all_panelists: typing.Optional[bool] = Field(None, alias='set_default_for_all_panelists')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
