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

from zoom_meeting_python_sdk.type.reports_get_telephone_reports_response_telephony_usage import ReportsGetTelephoneReportsResponseTelephonyUsage

RequiredReportsGetTelephoneReportsResponse = TypedDict("RequiredReportsGetTelephoneReportsResponse", {
    })

OptionalReportsGetTelephoneReportsResponse = TypedDict("OptionalReportsGetTelephoneReportsResponse", {
    # Start date for this report.
    "from": date,

    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    "next_page_token": str,

    # The number of pages returned for the request made. This field does **not** return if the `query_date_type` parameter is the `meeting_start_time` or `meeting_end_time` value.
    "page_count": int,

    # The number of records returned with a single API call.
    "page_size": int,

    # End date for this report.
    "to": date,

    # The total number of all the records available across pages. This field does **not** return if the `query_date_type` parameter is the `meeting_start_time` or `meeting_end_time` value.
    "total_records": int,

    "telephony_usage": ReportsGetTelephoneReportsResponseTelephonyUsage,
    }, total=False)

class ReportsGetTelephoneReportsResponse(RequiredReportsGetTelephoneReportsResponse, OptionalReportsGetTelephoneReportsResponse):
    pass
