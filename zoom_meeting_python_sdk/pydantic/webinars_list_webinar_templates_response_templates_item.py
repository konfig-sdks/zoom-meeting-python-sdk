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


class WebinarsListWebinarTemplatesResponseTemplatesItem(BaseModel):
    # The webinar template's ID.
    id: typing.Optional[str] = Field(None, alias='id')

    # The webinar template's name.
    name: typing.Optional[str] = Field(None, alias='name')

    # The webinar template type.  `1`: Webinar template    `2`: Admin webinar template
    type: typing.Optional[int] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
