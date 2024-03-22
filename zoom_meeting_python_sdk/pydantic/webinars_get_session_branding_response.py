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

from zoom_meeting_python_sdk.pydantic.webinars_get_session_branding_response_name_tags import WebinarsGetSessionBrandingResponseNameTags
from zoom_meeting_python_sdk.pydantic.webinars_get_session_branding_response_virtual_backgrounds import WebinarsGetSessionBrandingResponseVirtualBackgrounds
from zoom_meeting_python_sdk.pydantic.webinars_get_session_branding_response_wallpaper import WebinarsGetSessionBrandingResponseWallpaper

class WebinarsGetSessionBrandingResponse(BaseModel):
    wallpaper: typing.Optional[WebinarsGetSessionBrandingResponseWallpaper] = Field(None, alias='wallpaper')

    virtual_backgrounds: typing.Optional[WebinarsGetSessionBrandingResponseVirtualBackgrounds] = Field(None, alias='virtual_backgrounds')

    name_tags: typing.Optional[WebinarsGetSessionBrandingResponseNameTags] = Field(None, alias='name_tags')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
