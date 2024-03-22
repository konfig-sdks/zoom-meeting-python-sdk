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


class MeetingsUpdateDetailsRequestRecurrence(BaseModel):
    # Recurrence meeting types.   `1` - Daily.    `2` - Weekly.    `3` - Monthly.
    type: Literal[1, 2, 3] = Field(alias='type')

    # Select the final date when the meeting recurs before it is canceled. Should be in UTC time, such as 2017-11-25T12:00:00Z. Cannot be used with `end_times`.
    end_date_time: typing.Optional[datetime] = Field(None, alias='end_date_time')

    # Select how many times the meeting should recur before it is canceled. If `end_times` is set to 0, it means there is no end time. The maximum number of recurrences is 60. Cannot be used with `end_date_time`.
    end_times: typing.Optional[int] = Field(None, alias='end_times')

    # Use this field **only if you're scheduling a recurring meeting of type** `3` to state the day in a month when the meeting should recur. The value range is from 1 to 31.  For instance, if the meeting should recur on 23rd of each month, provide `23` as this field's value and `1` as the `repeat_interval` field's value. If the meeting should recur every three months on 23rd of the month, change the `repeat_interval` field's value to `3`.
    monthly_day: typing.Optional[int] = Field(None, alias='monthly_day')

    # Use this field **only if you're scheduling a recurring meeting of type** `3` to state the week of the month when the meeting should recur. If you use this field, you must also use the `monthly_week_day` field to state the day of the week when the meeting should recur.     `-1` - Last week of the month.    `1` - First week of the month.    `2` - Second week of the month.    `3` - Third week of the month.    `4` - Fourth week of the month.
    monthly_week: typing.Optional[Literal[-1, 1, 2, 3, 4]] = Field(None, alias='monthly_week')

    # Use this field only if you're scheduling a recurring meeting of type `3` to state a specific day in a week when a monthly meeting should recur. To use this field, you must also use the `monthly_week` field.       `1` - Sunday.    `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` - Thursday.    `6` - Friday.    `7` - Saturday.
    monthly_week_day: typing.Optional[Literal[1, 2, 3, 4, 5, 6, 7]] = Field(None, alias='monthly_week_day')

    # Define the interval when the meeting should recur. For instance, to schedule a meeting that recurs every two months, set this field's value as `2` and the `type` parameter's value to `3`.   For a daily meeting, the maximum interval is `90` days. For a weekly meeting, the maximum interval is `12` weeks. For a monthly meeting, the maximum value is `3` months.  
    repeat_interval: typing.Optional[int] = Field(None, alias='repeat_interval')

    # This field is required if you're scheduling a recurring meeting of type `2`, to state which days of the week the meeting should repeat.     Thiw field's value could be a number between `1` to `7` in string format. For instance, if the meeting should recur on Sunday, provide `1` as this field's value.         **Note** If you would like the meeting to occur on multiple days of a week, you should provide comma separated values for this field. For instance, if the meeting should recur on Sundays and Tuesdays provide `1,3` as this field's value.       `1`  - Sunday.     `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` -  Thursday.    `6` - Friday.    `7` - Saturday.
    weekly_days: typing.Optional[Literal["1", "2", "3", "4", "5", "6", "7"]] = Field(None, alias='weekly_days')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
