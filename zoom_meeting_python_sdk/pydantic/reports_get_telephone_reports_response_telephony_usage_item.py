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


class ReportsGetTelephoneReportsResponseTelephonyUsageItem(BaseModel):
    # Caller's call-in number.
    call_in_number: typing.Optional[str] = Field(None, alias='call_in_number')

    # Country name.
    country_name: typing.Optional[str] = Field(None, alias='country_name')

    # User department.
    dept: typing.Optional[str] = Field(None, alias='dept')

    # Call leg duration
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Call leg end time
    end_time: typing.Optional[datetime] = Field(None, alias='end_time')

    # User email.
    host_email: typing.Optional[str] = Field(None, alias='host_email')

    # The user ID of the meeting host.
    host_id: typing.Optional[str] = Field(None, alias='host_id')

    # User display name.
    host_name: typing.Optional[str] = Field(None, alias='host_name')

    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &quot;**long**&quot; format(represented as int64 data type in JSON), also known as the meeting number.
    meeting_id: typing.Optional[int] = Field(None, alias='meeting_id')

    # Meeting type.
    meeting_type: typing.Optional[str] = Field(None, alias='meeting_type')

    # Toll-free telephone number. 
    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    # Calling rate for the telephone call.
    rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='rate')

    # The number that is signaled to Zoom. 
    signaled_number: typing.Optional[str] = Field(None, alias='signaled_number')

    # Call leg start time
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Total cost (USD) for Call Out. Calculated as plan rate by duration.
    total: typing.Optional[typing.Union[int, float]] = Field(None, alias='total')

    # Call type.
    type: typing.Optional[Literal["toll-free", "call-out", "call-in", "US toll-number", "global toll-number", "premium", "premium call-in", "Toll"]] = Field(None, alias='type')

    # Meeting UUID.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
