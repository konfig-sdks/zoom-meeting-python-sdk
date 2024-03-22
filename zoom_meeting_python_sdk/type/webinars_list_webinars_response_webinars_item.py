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


class RequiredWebinarsListWebinarsResponseWebinarsItem(TypedDict):
    pass

class OptionalWebinarsListWebinarsResponseWebinarsItem(TypedDict, total=False):
    # Webinar description. The agenda length gets truncated to 250 characters when you list all webinars for a user. To view the complete agenda, retrieve details for a single webinar, use the [**Get a webinar**](https://developers.zoom.us) API.
    agenda: str

    # The webinar's creation time.
    created_at: datetime

    # The webinar's duration, in minutes.
    duration: int

    # The host's ID.
    host_id: str

    # The webinar ID.
    id: int

    # The URL to join the webinar.
    join_url: str

    # The webinar's start time.
    start_time: datetime

    # The webinar's [timezone](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).
    timezone: str

    # The webinar's topic.
    topic: str

    # The webinar type.  * `5` - A webinar.  * `6` - A recurring webinar without a fixed time.  * `9` - A recurring webinar with a fixed time.
    type: int

    # The webinar's universally unique identifier (UUID). Each webinar instance generates a webinar UUID.
    uuid: str

    # Whether the webinar is `simulive`.
    is_simulive: bool

class WebinarsListWebinarsResponseWebinarsItem(RequiredWebinarsListWebinarsResponseWebinarsItem, OptionalWebinarsListWebinarsResponseWebinarsItem):
    pass
