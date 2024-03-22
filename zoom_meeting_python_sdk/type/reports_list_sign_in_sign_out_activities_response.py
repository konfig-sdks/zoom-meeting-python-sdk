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

from zoom_meeting_python_sdk.type.reports_list_sign_in_sign_out_activities_response_activity_logs import ReportsListSignInSignOutActivitiesResponseActivityLogs

RequiredReportsListSignInSignOutActivitiesResponse = TypedDict("RequiredReportsListSignInSignOutActivitiesResponse", {
    })

OptionalReportsListSignInSignOutActivitiesResponse = TypedDict("OptionalReportsListSignInSignOutActivitiesResponse", {
    "activity_logs": ReportsListSignInSignOutActivitiesResponseActivityLogs,

    # Start date from which you want the activity logs report to be generated.
    "from": str,

    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    "next_page_token": str,

    # The number of records returned with a single API call.
    "page_size": int,

    # End date until which you want the activity logs report to be generated
    "to": str,
    }, total=False)

class ReportsListSignInSignOutActivitiesResponse(RequiredReportsListSignInSignOutActivitiesResponse, OptionalReportsListSignInSignOutActivitiesResponse):
    pass
