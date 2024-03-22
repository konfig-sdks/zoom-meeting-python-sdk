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


class RequiredWebinarsGetDetailsResponseSettingsFollowUpAbsenteesEmailNotification(TypedDict):
    pass

class OptionalWebinarsGetDetailsResponseSettingsFollowUpAbsenteesEmailNotification(TypedDict, total=False):
    # * `true` - Send follow-up email to absentees.  * `false` - Do not send follow-up email to absentees.
    enable: bool

    # `0` - No plan.    `1` - Send 1 days after the scheduled end date.    `2` - Send 2 days after the scheduled end date.    `3` - Send 3 days after the scheduled end date.    `4` - Send 4 days after the scheduled end date.    `5` - Send 5 days after the scheduled end date.    `6` - Send 6 days after the scheduled end date.    `7` - Send 7 days after the scheduled end date.
    type: int

class WebinarsGetDetailsResponseSettingsFollowUpAbsenteesEmailNotification(RequiredWebinarsGetDetailsResponseSettingsFollowUpAbsenteesEmailNotification, OptionalWebinarsGetDetailsResponseSettingsFollowUpAbsenteesEmailNotification):
    pass
