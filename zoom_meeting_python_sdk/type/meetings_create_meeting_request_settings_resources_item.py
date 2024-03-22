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


class RequiredMeetingsCreateMeetingRequestSettingsResourcesItem(TypedDict):
    pass

class OptionalMeetingsCreateMeetingRequestSettingsResourcesItem(TypedDict, total=False):
    # The resource type.
    resource_type: str

    # The resource ID.
    resource_id: str

    # The permission levels for users to access the whiteboard.  * `editor` - Users with link access can edit the board.  * `commenter` - Users with link access can comment on the board.  * `viewer` - Users with link access can view the board.
    permission_level: str

class MeetingsCreateMeetingRequestSettingsResourcesItem(RequiredMeetingsCreateMeetingRequestSettingsResourcesItem, OptionalMeetingsCreateMeetingRequestSettingsResourcesItem):
    pass
