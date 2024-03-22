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


class RequiredWebinarsAddRegistrantResponseOccurrencesItem(TypedDict):
    pass

class OptionalWebinarsAddRegistrantResponseOccurrencesItem(TypedDict, total=False):
    # Duration.
    duration: int

    # Occurrence ID: Unique identifier that identifies an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences.
    occurrence_id: str

    # Start time.
    start_time: datetime

    # Occurrence status.
    status: str

class WebinarsAddRegistrantResponseOccurrencesItem(RequiredWebinarsAddRegistrantResponseOccurrencesItem, OptionalWebinarsAddRegistrantResponseOccurrencesItem):
    pass
