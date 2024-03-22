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

from zoom_meeting_python_sdk.pydantic.analytics_summary_response_analytics_summary import AnalyticsSummaryResponseAnalyticsSummary

class AnalyticsSummaryResponse(BaseModel):
    # The queried start date
    from_: typing.Optional[date] = Field(None, alias='from')

    # The queried end date.
    to: typing.Optional[date] = Field(None, alias='to')

    analytics_summary: typing.Optional[AnalyticsSummaryResponseAnalyticsSummary] = Field(None, alias='analytics_summary')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
