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


class WebinarsListTrackingSourcesResponseTrackingSourcesItem(BaseModel):
    # Unique Identifier of the tracking source.
    id: typing.Optional[str] = Field(None, alias='id')

    # Number of registrations made from this source.
    registration_count: typing.Optional[int] = Field(None, alias='registration_count')

    # Name of the source (platform) where the registration URL was shared.
    source_name: typing.Optional[str] = Field(None, alias='source_name')

    # Tracking URL. The URL that was shared for the registration.
    tracking_url: typing.Optional[str] = Field(None, alias='tracking_url')

    # Number of visitors who visited the registration page from this source.
    visitor_count: typing.Optional[int] = Field(None, alias='visitor_count')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
