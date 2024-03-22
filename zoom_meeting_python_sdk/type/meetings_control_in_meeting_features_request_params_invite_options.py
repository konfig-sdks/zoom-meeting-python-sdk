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


class RequiredMeetingsControlInMeetingFeaturesRequestParamsInviteOptions(TypedDict):
    pass

class OptionalMeetingsControlInMeetingFeaturesRequestParamsInviteOptions(TypedDict, total=False):
    # Whether to require a greeting before being connected. Use this field if you pass the `participant.invite.callout` value for the `method` field.
    require_greeting: bool

    # Whether to require pressing 1 before being connected. Use this field if you pass the `participant.invite.callout` value for the `method` field.
    require_pressing_one: bool

class MeetingsControlInMeetingFeaturesRequestParamsInviteOptions(RequiredMeetingsControlInMeetingFeaturesRequestParamsInviteOptions, OptionalMeetingsControlInMeetingFeaturesRequestParamsInviteOptions):
    pass
