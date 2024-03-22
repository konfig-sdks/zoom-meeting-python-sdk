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


class RequiredWebinarsGetSessionBrandingResponseNameTagsItem(TypedDict):
    pass

class OptionalWebinarsGetSessionBrandingResponseNameTagsItem(TypedDict, total=False):
    # The name tag's ID.
    id: str

    # The name tag's name.
    name: str

    # The name tag's text color.
    text_color: str

    # The name tag's accent color.
    accent_color: str

    # The name tag's background color.
    background_color: str

    # Whether the file is the default name tag or not.
    is_default: bool

class WebinarsGetSessionBrandingResponseNameTagsItem(RequiredWebinarsGetSessionBrandingResponseNameTagsItem, OptionalWebinarsGetSessionBrandingResponseNameTagsItem):
    pass
