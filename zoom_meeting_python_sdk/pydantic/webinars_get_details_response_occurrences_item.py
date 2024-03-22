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


class WebinarsGetDetailsResponseOccurrencesItem(BaseModel):
    # Duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Occurrence ID: Unique Identifier that identifies an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences.
    occurrence_id: typing.Optional[str] = Field(None, alias='occurrence_id')

    # Start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Occurrence status:   `available` - Available occurrence.    `deleted` -  Deleted occurrence.
    status: typing.Optional[Literal["available", "deleted"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
