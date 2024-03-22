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

from zoom_meeting_python_sdk.pydantic.webinars_add_registrant_response_occurrences import WebinarsAddRegistrantResponseOccurrences

class WebinarsAddRegistrantResponse(BaseModel):
    # The webinar's ID.
    id: typing.Optional[int] = Field(None, alias='id')

    # The URL the registrant can use to join the webinar.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The registrant's ID.
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # The webinar's start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # The webinar's topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    occurrences: typing.Optional[WebinarsAddRegistrantResponseOccurrences] = Field(None, alias='occurrences')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
