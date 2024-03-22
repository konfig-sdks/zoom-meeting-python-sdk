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


class MeetingsUpdateMeetingStatusRequest(BaseModel):
    # `end` - End a meeting.     `recover` - [Recover](https://support.zoom.us/hc/en-us/articles/360038297111-Recover-a-deleted-meeting) a deleted meeting. 
    action: typing.Optional[Literal["end", "recover"]] = Field(None, alias='action')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
