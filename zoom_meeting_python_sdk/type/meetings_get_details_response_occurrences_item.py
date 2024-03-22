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


class RequiredMeetingsGetDetailsResponseOccurrencesItem(TypedDict):
    pass

class OptionalMeetingsGetDetailsResponseOccurrencesItem(TypedDict, total=False):
    # Duration.
    duration: int

    # Occurrence ID: Unique Identifier that identifies an occurrence of a recurring meeting. [Recurring meetings](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings) can have a maximum of 50 occurrences.
    occurrence_id: str

    # Start time.
    start_time: datetime

    # Occurrence status:   `available` - Available occurrence.    `deleted` -  Deleted occurrence.
    status: str

class MeetingsGetDetailsResponseOccurrencesItem(RequiredMeetingsGetDetailsResponseOccurrencesItem, OptionalMeetingsGetDetailsResponseOccurrencesItem):
    pass
