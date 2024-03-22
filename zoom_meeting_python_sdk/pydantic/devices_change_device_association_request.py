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


class DevicesChangeDeviceAssociationRequest(BaseModel):
    # The Zoom Room ID which device is being associated to. The `room_id` is required when `assign` is selected for `action` field.
    room_id: typing.Optional[str] = Field(None, alias='room_id')

    # Specify one of the following values for this field:  `ZR`: Zoom Room Computer.     `ZRC`: Zoom Room Controller.     `ZRP`: Scheduling Display.     `ZRW`: Companion Whiteboard.
    app_type: typing.Optional[Literal["ZR", "ZRC", "ZRP", "ZRW"]] = Field(None, alias='app_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
