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


class RequiredMeetingsCreateMeetingResponseSettingsContinuousMeetingChat(TypedDict):
    pass

class OptionalMeetingsCreateMeetingResponseSettingsContinuousMeetingChat(TypedDict, total=False):
    # Whether to enable the **Enable continuous meeting chat** setting.
    enable: bool

    # Whether to enable the **Automatically add invited external users** setting.
    auto_add_invited_external_users: bool

    # The channel's ID.
    channel_id: str

class MeetingsCreateMeetingResponseSettingsContinuousMeetingChat(RequiredMeetingsCreateMeetingResponseSettingsContinuousMeetingChat, OptionalMeetingsCreateMeetingResponseSettingsContinuousMeetingChat):
    pass
