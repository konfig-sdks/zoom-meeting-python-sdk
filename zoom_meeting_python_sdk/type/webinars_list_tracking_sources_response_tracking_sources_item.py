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


class RequiredWebinarsListTrackingSourcesResponseTrackingSourcesItem(TypedDict):
    pass

class OptionalWebinarsListTrackingSourcesResponseTrackingSourcesItem(TypedDict, total=False):
    # Unique Identifier of the tracking source.
    id: str

    # Number of registrations made from this source.
    registration_count: int

    # Name of the source (platform) where the registration URL was shared.
    source_name: str

    # Tracking URL. The URL that was shared for the registration.
    tracking_url: str

    # Number of visitors who visited the registration page from this source.
    visitor_count: int

class WebinarsListTrackingSourcesResponseTrackingSourcesItem(RequiredWebinarsListTrackingSourcesResponseTrackingSourcesItem, OptionalWebinarsListTrackingSourcesResponseTrackingSourcesItem):
    pass
