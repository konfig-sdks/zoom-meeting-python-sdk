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


class MeetingsGetDetailsResponseSettingsGlobalDialInNumbersItem(BaseModel):
    # City of the number, if any. For example, Chicago.
    city: typing.Optional[str] = Field(None, alias='city')

    # Country code. For example, BR.
    country: typing.Optional[str] = Field(None, alias='country')

    # Full name of country. For example, Brazil.
    country_name: typing.Optional[str] = Field(None, alias='country_name')

    # Phone number. For example, +1 2332357613.
    number: typing.Optional[str] = Field(None, alias='number')

    # Type of number. 
    type: typing.Optional[Literal["toll", "tollfree"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
