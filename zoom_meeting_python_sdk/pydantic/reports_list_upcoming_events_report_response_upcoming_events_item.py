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


class ReportsListUpcomingEventsReportResponseUpcomingEventsItem(BaseModel):
    # The event host's department.
    dept: typing.Optional[str] = Field(None, alias='dept')

    # The event host's ID.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # The event host's name.
    host_name: typing.Optional[str] = Field(None, alias='host_name')

    # The event's unique ID.
    id: typing.Optional[str] = Field(None, alias='id')

    # The event's start time.
    start_time: typing.Optional[str] = Field(None, alias='start_time')

    # The event's topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
