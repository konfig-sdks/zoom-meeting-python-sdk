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

from zoom_meeting_python_sdk.type.webinars_get_session_branding_response_name_tags import WebinarsGetSessionBrandingResponseNameTags
from zoom_meeting_python_sdk.type.webinars_get_session_branding_response_virtual_backgrounds import WebinarsGetSessionBrandingResponseVirtualBackgrounds
from zoom_meeting_python_sdk.type.webinars_get_session_branding_response_wallpaper import WebinarsGetSessionBrandingResponseWallpaper

class RequiredWebinarsGetSessionBrandingResponse(TypedDict):
    pass

class OptionalWebinarsGetSessionBrandingResponse(TypedDict, total=False):
    wallpaper: WebinarsGetSessionBrandingResponseWallpaper

    virtual_backgrounds: WebinarsGetSessionBrandingResponseVirtualBackgrounds

    name_tags: WebinarsGetSessionBrandingResponseNameTags

class WebinarsGetSessionBrandingResponse(RequiredWebinarsGetSessionBrandingResponse, OptionalWebinarsGetSessionBrandingResponse):
    pass
