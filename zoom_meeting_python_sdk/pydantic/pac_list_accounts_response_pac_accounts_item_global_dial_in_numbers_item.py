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


class PacListAccountsResponsePacAccountsItemGlobalDialInNumbersItem(BaseModel):
    # The global dial-in country code.
    country: typing.Optional[str] = Field(None, alias='country')

    # The global dial-in number.
    number: typing.Optional[str] = Field(None, alias='number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
