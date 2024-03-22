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


class RequiredReportsGetTelephoneReportsResponseTelephonyUsageItem(TypedDict):
    pass

class OptionalReportsGetTelephoneReportsResponseTelephonyUsageItem(TypedDict, total=False):
    # Caller's call-in number.
    call_in_number: str

    # Country name.
    country_name: str

    # User department.
    dept: str

    # Call leg duration
    duration: int

    # Call leg end time
    end_time: datetime

    # User email.
    host_email: str

    # The user ID of the meeting host.
    host_id: str

    # User display name.
    host_name: str

    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &quot;**long**&quot; format(represented as int64 data type in JSON), also known as the meeting number.
    meeting_id: int

    # Meeting type.
    meeting_type: str

    # Toll-free telephone number. 
    phone_number: str

    # Calling rate for the telephone call.
    rate: typing.Union[int, float]

    # The number that is signaled to Zoom. 
    signaled_number: str

    # Call leg start time
    start_time: datetime

    # Total cost (USD) for Call Out. Calculated as plan rate by duration.
    total: typing.Union[int, float]

    # Call type.
    type: str

    # Meeting UUID.
    uuid: str

class ReportsGetTelephoneReportsResponseTelephonyUsageItem(RequiredReportsGetTelephoneReportsResponseTelephonyUsageItem, OptionalReportsGetTelephoneReportsResponseTelephonyUsageItem):
    pass
