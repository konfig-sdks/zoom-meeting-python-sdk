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

from zoom_meeting_python_sdk.pydantic.reports_list_sign_in_sign_out_activities_response_activity_logs import ReportsListSignInSignOutActivitiesResponseActivityLogs

class ReportsListSignInSignOutActivitiesResponse(BaseModel):
    activity_logs: typing.Optional[ReportsListSignInSignOutActivitiesResponseActivityLogs] = Field(None, alias='activity_logs')

    # Start date from which you want the activity logs report to be generated.
    from_: typing.Optional[str] = Field(None, alias='from')

    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of records returned with a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # End date until which you want the activity logs report to be generated
    to: typing.Optional[str] = Field(None, alias='to')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
