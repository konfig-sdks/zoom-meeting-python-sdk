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

from zoom_meeting_python_sdk.type.reports_get_active_inactive_host_reports_response_users import ReportsGetActiveInactiveHostReportsResponseUsers

RequiredReportsGetActiveInactiveHostReportsResponse = TypedDict("RequiredReportsGetActiveInactiveHostReportsResponse", {
    })

OptionalReportsGetActiveInactiveHostReportsResponse = TypedDict("OptionalReportsGetActiveInactiveHostReportsResponse", {
    # Start date for this report.
    "from": date,

    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    "next_page_token": str,

    # The number of pages returned for the request made.
    "page_count": int,

    # The page number of the current results.
    "page_number": int,

    # The number of records returned with a single API call.
    "page_size": int,

    # End date for this report.
    "to": date,

    # The total number of all the records available across pages.
    "total_records": int,

    # Number of meeting minutes for this range.
    "total_meeting_minutes": int,

    # Number of meetings for this range.
    "total_meetings": int,

    # Number of participants for this range.
    "total_participants": int,

    "users": ReportsGetActiveInactiveHostReportsResponseUsers,
    }, total=False)

class ReportsGetActiveInactiveHostReportsResponse(RequiredReportsGetActiveInactiveHostReportsResponse, OptionalReportsGetActiveInactiveHostReportsResponse):
    pass
