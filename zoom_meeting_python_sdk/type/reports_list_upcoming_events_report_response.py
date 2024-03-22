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

from zoom_meeting_python_sdk.type.reports_list_upcoming_events_report_response_upcoming_events import ReportsListUpcomingEventsReportResponseUpcomingEvents

RequiredReportsListUpcomingEventsReportResponse = TypedDict("RequiredReportsListUpcomingEventsReportResponse", {
    })

OptionalReportsListUpcomingEventsReportResponse = TypedDict("OptionalReportsListUpcomingEventsReportResponse", {
    # The report's start date. This value must be within the past six months.
    "from": date,

    # The next page token is used to paginate through large result sets. A next page token returns when the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    "next_page_token": str,

    # The number of records returned in a single API call.
    "page_size": int,

    # The report's end date. This value must be within the past six months and cannot exceed a month from the `from` value.
    "to": date,

    "upcoming_events": ReportsListUpcomingEventsReportResponseUpcomingEvents,
    }, total=False)

class ReportsListUpcomingEventsReportResponse(RequiredReportsListUpcomingEventsReportResponse, OptionalReportsListUpcomingEventsReportResponse):
    pass
