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


class RequiredWebinarsUploadBrandingVirtualBackgroundRequest(TypedDict):
    # The Virtual Background's file path, in binary format.
    file: typing.IO

class OptionalWebinarsUploadBrandingVirtualBackgroundRequest(TypedDict, total=False):
    # Whether set the file as the default Virtual Background file.
    default: bool

    # Whether to set the Virtual Background file as the new default for all panelists. This includes panelists not currently assigned a default Virtual Background.
    set_default_for_all_panelists: bool

class WebinarsUploadBrandingVirtualBackgroundRequest(RequiredWebinarsUploadBrandingVirtualBackgroundRequest, OptionalWebinarsUploadBrandingVirtualBackgroundRequest):
    pass
