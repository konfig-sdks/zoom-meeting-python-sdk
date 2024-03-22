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


class TspGetAccountInfoResponseDialInNumbersItem(BaseModel):
    # Country Code
    code: typing.Optional[str] = Field(None, alias='code')

    # Dial-in number, length is less than 16
    number: typing.Optional[str] = Field(None, alias='number')

    # Dial-in number type.
    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
