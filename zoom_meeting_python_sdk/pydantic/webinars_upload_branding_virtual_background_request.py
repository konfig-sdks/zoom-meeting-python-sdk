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


class WebinarsUploadBrandingVirtualBackgroundRequest(BaseModel):
    # The Virtual Background's file path, in binary format.
    file: typing.IO = Field(alias='file')

    # Whether set the file as the default Virtual Background file.
    default: typing.Optional[bool] = Field(None, alias='default')

    # Whether to set the Virtual Background file as the new default for all panelists. This includes panelists not currently assigned a default Virtual Background.
    set_default_for_all_panelists: typing.Optional[bool] = Field(None, alias='set_default_for_all_panelists')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
