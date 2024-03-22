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

from zoom_meeting_python_sdk.pydantic.webinars_list_participants_response_participants import WebinarsListParticipantsResponseParticipants

class WebinarsListParticipantsResponse(BaseModel):
    # Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of pages returned for this request.
    page_count: typing.Optional[int] = Field(None, alias='page_count')

    # The total number of records returned from a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    participants: typing.Optional[WebinarsListParticipantsResponseParticipants] = Field(None, alias='participants')

    # The total number of records available across all pages.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
