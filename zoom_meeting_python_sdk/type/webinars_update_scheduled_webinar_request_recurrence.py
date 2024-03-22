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


class RequiredWebinarsUpdateScheduledWebinarRequestRecurrence(TypedDict):
    # Recurrence meeting types.   `1` - Daily.    `2` - Weekly.    `3` - Monthly.
    type: int

class OptionalWebinarsUpdateScheduledWebinarRequestRecurrence(TypedDict, total=False):
    # Select the final date when the meeting will recur before it is canceled. Should be in UTC time, such as 2017-11-25T12:00:00Z. Cannot be used with `end_times`.
    end_date_time: datetime

    # Select how many times the webinar will recur before it is canceled. The maximum number of recurring is 60. Cannot be used with `end_date_time`.
    end_times: int

    # Use this field **only if you're scheduling a recurring meeting of type** `3` to state which day in a month, the meeting should recur. The value range is from 1 to 31.  If you would like the meeting to recur on 23rd of each month, provide `23` as the value of this field and `1` as the value of the `repeat_interval` field. If you would like the meeting to recur every three months, on 23rd of the month, change the value of the `repeat_interval` field to `3`.
    monthly_day: int

    # Use this field **only if you're scheduling a recurring meeting of type** `3` to state the week of the month when the meeting should recur. If you use this field, **you must also use the `monthly_week_day` field to state the day of the week when the meeting should recur.**     `-1` - Last week of the month.    `1` - First week of the month.    `2` - Second week of the month.    `3` - Third week of the month.    `4` - Fourth week of the month.
    monthly_week: int

    # Use this field **only if you're scheduling a recurring meeting of type** `3` to state a specific day in a week when the monthly meeting should recur. To use this field, you must also use the `monthly_week` field.       `1` - Sunday.    `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` - Thursday.    `6` - Friday.    `7` - Saturday.
    monthly_week_day: int

    # Define the interval when the meeting should recur. If you would like to schedule a meeting that recurs every two months, set the value of this field as `2` and the value of the `type` parameter as `3`.   For a daily meeting, the maximum interval you can set is `90` days. For a weekly meeting the maximum interval that you can set is  of `12` weeks. For a monthly meeting, there is a maximum of `3` months.  
    repeat_interval: int

    # This field is required **if you're scheduling a recurring meeting of type** `2` to state which day(s) of the week the meeting should repeat.           The value for this field could be a number between `1` to `7` in string format. For instance, if the meeting should recur on Sunday, provide `1` as the value of this field.         **Note:** If you would like the meeting to occur on multiple days of a week, you should provide comma separated values for this field. For instance, if the meeting should recur on Sundays and Tuesdays provide `1,3` as the value of this field.       `1`  - Sunday.     `2` - Monday.    `3` - Tuesday.    `4` -  Wednesday.    `5` -  Thursday.    `6` - Friday.    `7` - Saturday.
    weekly_days: str

class WebinarsUpdateScheduledWebinarRequestRecurrence(RequiredWebinarsUpdateScheduledWebinarRequestRecurrence, OptionalWebinarsUpdateScheduledWebinarRequestRecurrence):
    pass
