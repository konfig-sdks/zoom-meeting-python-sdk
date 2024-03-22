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


class RequiredMeetingsUpdateDetailsRequestSettingsContinuousMeetingChat(TypedDict):
    pass

class OptionalMeetingsUpdateDetailsRequestSettingsContinuousMeetingChat(TypedDict, total=False):
    # Whether to enable the **Enable continuous meeting chat** setting.
    enable: bool

    # Whether to enable the **Automatically add invited external users** setting.
    auto_add_invited_external_users: bool

class MeetingsUpdateDetailsRequestSettingsContinuousMeetingChat(RequiredMeetingsUpdateDetailsRequestSettingsContinuousMeetingChat, OptionalMeetingsUpdateDetailsRequestSettingsContinuousMeetingChat):
    pass
