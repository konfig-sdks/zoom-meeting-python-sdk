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


class RequiredWebinarsUploadBrandingWallpaperResponse(TypedDict):
    pass

class OptionalWebinarsUploadBrandingWallpaperResponse(TypedDict, total=False):
    # The wallpaper file's ID.
    id: str

    # The wallpaper file's name.
    name: str

    # The wallpaper file's size, in bytes.
    size: int

    # The wallpaper file's file type:  * `image` &mdash; An image file.
    type: str

class WebinarsUploadBrandingWallpaperResponse(RequiredWebinarsUploadBrandingWallpaperResponse, OptionalWebinarsUploadBrandingWallpaperResponse):
    pass
