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


class RequiredWebinarsUploadBrandingWallpaperRequest(TypedDict):
    # The wallpaper's file path, in binary format.
    file: typing.IO

class OptionalWebinarsUploadBrandingWallpaperRequest(TypedDict, total=False):
    pass

class WebinarsUploadBrandingWallpaperRequest(RequiredWebinarsUploadBrandingWallpaperRequest, OptionalWebinarsUploadBrandingWallpaperRequest):
    pass
