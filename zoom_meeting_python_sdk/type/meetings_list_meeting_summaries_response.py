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

from zoom_meeting_python_sdk.type.meetings_list_meeting_summaries_response_summaries import MeetingsListMeetingSummariesResponseSummaries

RequiredMeetingsListMeetingSummariesResponse = TypedDict("RequiredMeetingsListMeetingSummariesResponse", {
    })

OptionalMeetingsListMeetingSummariesResponse = TypedDict("OptionalMeetingsListMeetingSummariesResponse", {
    # The number of records returned with a single API call.
    "page_size": int,

    # The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    "next_page_token": str,

    # The start date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.
    "from": datetime,

    # The end date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.
    "to": datetime,

    "summaries": MeetingsListMeetingSummariesResponseSummaries,
    }, total=False)

class MeetingsListMeetingSummariesResponse(RequiredMeetingsListMeetingSummariesResponse, OptionalMeetingsListMeetingSummariesResponse):
    pass
