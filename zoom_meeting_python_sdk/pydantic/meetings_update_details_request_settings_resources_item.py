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


class MeetingsUpdateDetailsRequestSettingsResourcesItem(BaseModel):
    # The resource type.
    resource_type: typing.Optional[Literal["whiteboard"]] = Field(None, alias='resource_type')

    # The resource ID.
    resource_id: typing.Optional[str] = Field(None, alias='resource_id')

    # The permission levels for users to access the whiteboard.  * `editor` - Users with link access can edit the board.  * `commenter` - Users with link access can comment on the board.  * `viewer` - Users with link access can view the board.
    permission_level: typing.Optional[Literal["editor", "commenter", "viewer"]] = Field(None, alias='permission_level')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
