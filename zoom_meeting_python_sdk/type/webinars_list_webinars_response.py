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

from zoom_meeting_python_sdk.type.webinars_list_webinars_response_webinars import WebinarsListWebinarsResponseWebinars

class RequiredWebinarsListWebinarsResponse(TypedDict):
    pass

class OptionalWebinarsListWebinarsResponse(TypedDict, total=False):
    # Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: str

    # The number of pages returned for the request made.
    page_count: int

    # WARNING: This property is deprecated
    # **Deprecated** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.
    page_number: int

    # The number of records returned with a single API call.
    page_size: int

    # The total number of all the records available across pages.
    total_records: int

    webinars: WebinarsListWebinarsResponseWebinars

class WebinarsListWebinarsResponse(RequiredWebinarsListWebinarsResponse, OptionalWebinarsListWebinarsResponse):
    pass
