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

from zoom_meeting_python_sdk.type.webinars_list_participants_response_participants import WebinarsListParticipantsResponseParticipants

class RequiredWebinarsListParticipantsResponse(TypedDict):
    pass

class OptionalWebinarsListParticipantsResponse(TypedDict, total=False):
    # Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: str

    # The number of pages returned for this request.
    page_count: int

    # The total number of records returned from a single API call.
    page_size: int

    participants: WebinarsListParticipantsResponseParticipants

    # The total number of records available across all pages.
    total_records: int

class WebinarsListParticipantsResponse(RequiredWebinarsListParticipantsResponse, OptionalWebinarsListParticipantsResponse):
    pass
