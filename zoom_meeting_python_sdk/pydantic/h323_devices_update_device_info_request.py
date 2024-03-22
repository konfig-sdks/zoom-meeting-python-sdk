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


class H323DevicesUpdateDeviceInfoRequest(BaseModel):
    # Device encryption:    `auto` - auto.    `yes` - yes.    `no` - no.
    encryption: Literal["auto", "true", "false"] = Field(alias='encryption')

    # Device IP.
    ip: str = Field(alias='ip')

    # Device name.
    name: str = Field(alias='name')

    # Device protocol:    `H.323` - H.323.    `SIP` - SIP.
    protocol: Literal["H.323", "SIP"] = Field(alias='protocol')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
