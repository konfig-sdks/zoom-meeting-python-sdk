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

from zoom_meeting_python_sdk.pydantic.analytics_details_response_analytics_details import AnalyticsDetailsResponseAnalyticsDetails

class AnalyticsDetailsResponse(BaseModel):
    # The queried start date
    from_: typing.Optional[date] = Field(None, alias='from')

    # The queried end date.
    to: typing.Optional[date] = Field(None, alias='to')

    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The number of records returned within a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    # The total number of all the records available across pages.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    analytics_details: typing.Optional[AnalyticsDetailsResponseAnalyticsDetails] = Field(None, alias='analytics_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
