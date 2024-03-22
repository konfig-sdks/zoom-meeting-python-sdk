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

from zoom_meeting_python_sdk.type.webinars_list_tracking_sources_response_tracking_sources import WebinarsListTrackingSourcesResponseTrackingSources

class RequiredWebinarsListTrackingSourcesResponse(TypedDict):
    pass

class OptionalWebinarsListTrackingSourcesResponse(TypedDict, total=False):
    # The total number of registration records for this Webinar.
    total_records: int

    tracking_sources: WebinarsListTrackingSourcesResponseTrackingSources

class WebinarsListTrackingSourcesResponse(RequiredWebinarsListTrackingSourcesResponse, OptionalWebinarsListTrackingSourcesResponse):
    pass
