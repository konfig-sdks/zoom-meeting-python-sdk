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


class WebinarsListWebinarsResponseWebinarsItem(BaseModel):
    # Webinar description. The agenda length gets truncated to 250 characters when you list all webinars for a user. To view the complete agenda, retrieve details for a single webinar, use the [**Get a webinar**](https://developers.zoom.us) API.
    agenda: typing.Optional[str] = Field(None, alias='agenda')

    # The webinar's creation time.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # The webinar's duration, in minutes.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # The host's ID.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # The webinar ID.
    id: typing.Optional[int] = Field(None, alias='id')

    # The URL to join the webinar.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The webinar's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The webinar's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: typing.Optional[str] = Field(None, alias='timezone')

    # The webinar's topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # The webinar type.  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time.  * `9` - A recurring webinar with a fixed time.
    type: typing.Optional[Literal[5, 6, 9]] = Field(None, alias='type')

    # The webinar's universally unique identifier (UUID). Each webinar instance generates a webinar UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # Whether the webinar is `simulive`.
    is_simulive: typing.Optional[bool] = Field(None, alias='is_simulive')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
