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


class DevicesCreateNewDeviceRequest(BaseModel):
    # The device's name.
    device_name: str = Field(alias='device_name')

    # The device's mac address.
    mac_address: str = Field(alias='mac_address')

    # The device's serial number.
    serial_number: str = Field(alias='serial_number')

    # The device's manufacturer.
    vendor: str = Field(alias='vendor')

    # The device's model.
    model: str = Field(alias='model')

    # Device type.    `0` - Zoom Rooms computer.    `1` - Zoom Rooms controller.    `5` - Zoom Phone appliance.
    device_type: Literal[0, 1, 5] = Field(alias='device_type')

    # The Zoom Room's ID. Only for Zoom Room devices.
    room_id: typing.Optional[str] = Field(None, alias='room_id')

    # User email for assigning the Zoom Phone device. Only for Zoom Phone devices.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # The name of the tag.
    tag: typing.Optional[str] = Field(None, alias='tag')

    # The ZDM group ID.
    zdm_group_id: typing.Optional[str] = Field(None, alias='zdm_group_id')

    # The extension number.
    extension_number: typing.Optional[str] = Field(None, alias='extension_number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
