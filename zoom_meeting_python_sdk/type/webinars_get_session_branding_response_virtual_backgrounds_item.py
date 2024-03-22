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


class RequiredWebinarsGetSessionBrandingResponseVirtualBackgroundsItem(TypedDict):
    pass

class OptionalWebinarsGetSessionBrandingResponseVirtualBackgroundsItem(TypedDict, total=False):
    # The Virtual Background's file ID.
    id: str

    # The Virtual Background's file name.
    name: str

    # Whether the file is the default Virtual Background file.
    is_default: bool

class WebinarsGetSessionBrandingResponseVirtualBackgroundsItem(RequiredWebinarsGetSessionBrandingResponseVirtualBackgroundsItem, OptionalWebinarsGetSessionBrandingResponseVirtualBackgroundsItem):
    pass
