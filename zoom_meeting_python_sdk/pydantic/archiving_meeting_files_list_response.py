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

from zoom_meeting_python_sdk.pydantic.archiving_meeting_files_list_response_meetings import ArchivingMeetingFilesListResponseMeetings

class ArchivingMeetingFilesListResponse(BaseModel):
    # The queried start date.
    from_: typing.Optional[datetime] = Field(None, alias='from')

    meetings: typing.Optional[ArchivingMeetingFilesListResponseMeetings] = Field(None, alias='meetings')

    # Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.   **Note:** if you use `next_page_token` as a parameter, your other request parameters should be changeless to make sure that the large result set is what you want. For example, if your `to` parameter is for a future time, Zoom resets this value to the current time and returns this value in the response body, along with the `next_page_token` value. Use these same `to` and `next_page_token` values in requests for the remaining results set; otherwise you will get an invalid token error.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of records returned within a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # The queried end date.
    to: typing.Optional[datetime] = Field(None, alias='to')

    # The total number of returned meeting records.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
