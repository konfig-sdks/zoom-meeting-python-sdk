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


class WebinarsGetSessionBrandingResponseVirtualBackgroundsItem(BaseModel):
    # The Virtual Background's file ID.
    id: typing.Optional[str] = Field(None, alias='id')

    # The Virtual Background's file name.
    name: typing.Optional[str] = Field(None, alias='name')

    # Whether the file is the default Virtual Background file.
    is_default: typing.Optional[bool] = Field(None, alias='is_default')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
