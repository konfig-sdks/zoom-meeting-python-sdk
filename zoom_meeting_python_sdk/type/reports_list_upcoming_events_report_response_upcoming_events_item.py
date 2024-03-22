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


class RequiredReportsListUpcomingEventsReportResponseUpcomingEventsItem(TypedDict):
    pass

class OptionalReportsListUpcomingEventsReportResponseUpcomingEventsItem(TypedDict, total=False):
    # The event host's department.
    dept: str

    # The event host's ID.
    host_id: str

    # The event host's name.
    host_name: str

    # The event's unique ID.
    id: str

    # The event's start time.
    start_time: str

    # The event's topic.
    topic: str

class ReportsListUpcomingEventsReportResponseUpcomingEventsItem(RequiredReportsListUpcomingEventsReportResponseUpcomingEventsItem, OptionalReportsListUpcomingEventsReportResponseUpcomingEventsItem):
    pass
