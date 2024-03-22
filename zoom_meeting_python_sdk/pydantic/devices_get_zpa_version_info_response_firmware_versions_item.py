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


class DevicesGetZpaVersionInfoResponseFirmwareVersionsItem(BaseModel):
    # The package version.
    version: typing.Optional[str] = Field(None, alias='version')

    # The device's manufacturer.
    vendor: typing.Optional[str] = Field(None, alias='vendor')

    # The device's model name.
    model: typing.Optional[str] = Field(None, alias='model')

    # The prompt information for this version.
    warn_info: typing.Optional[str] = Field(None, alias='warn_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
