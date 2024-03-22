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


class RequiredWebinarsCreateBrandingNameTagRequest(TypedDict):
    # The name tag's name.  **Note:** This value cannot exceed more than 50 characters.
    name: str

    # The name tag's text color.
    text_color: str

    # The name tag's accent color.
    accent_color: str

    # The name tag's background color.
    background_color: str

class OptionalWebinarsCreateBrandingNameTagRequest(TypedDict, total=False):
    # Whether set the name tag as the default name tag or not.
    is_default: bool

    # Whether to set the name tag as the new default for all panelists or not. This includes panelists not currently assigned a default name tag.
    set_default_for_all_panelists: bool

class WebinarsCreateBrandingNameTagRequest(RequiredWebinarsCreateBrandingNameTagRequest, OptionalWebinarsCreateBrandingNameTagRequest):
    pass
