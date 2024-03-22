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

from zoom_meeting_python_sdk.pydantic.webinars_list_tracking_sources_response_tracking_sources import WebinarsListTrackingSourcesResponseTrackingSources

class WebinarsListTrackingSourcesResponse(BaseModel):
    # The total number of registration records for this Webinar.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    tracking_sources: typing.Optional[WebinarsListTrackingSourcesResponseTrackingSources] = Field(None, alias='tracking_sources')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
