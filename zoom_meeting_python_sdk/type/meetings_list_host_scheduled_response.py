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

from zoom_meeting_python_sdk.type.meetings_list_host_scheduled_response_meetings import MeetingsListHostScheduledResponseMeetings

class RequiredMeetingsListHostScheduledResponse(TypedDict):
    pass

class OptionalMeetingsListHostScheduledResponse(TypedDict, total=False):
    # Use the next page token to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: str

    # The number of pages returned for the request made.
    page_count: int

    # The page number of the current results.
    page_number: int

    # The number of records returned with a single API call.
    page_size: int

    # The total number of all the records available across pages.
    total_records: int

    meetings: MeetingsListHostScheduledResponseMeetings

class MeetingsListHostScheduledResponse(RequiredMeetingsListHostScheduledResponse, OptionalMeetingsListHostScheduledResponse):
    pass
