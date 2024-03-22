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

from zoom_meeting_python_sdk.type.sip_phone_list_response_phones import SipPhoneListResponsePhones

class RequiredSipPhoneListResponse(TypedDict):
    pass

class OptionalSipPhoneListResponse(TypedDict, total=False):
    next_page_token: str

    # The number of pages returned for the request made.
    page_count: int

    # The page number of the current results.
    page_number: int

    # The number of records returned within a single API call.
    page_size: int

    phones: SipPhoneListResponsePhones

    # The total number of all the records available across pages.
    total_records: int

class SipPhoneListResponse(RequiredSipPhoneListResponse, OptionalSipPhoneListResponse):
    pass
