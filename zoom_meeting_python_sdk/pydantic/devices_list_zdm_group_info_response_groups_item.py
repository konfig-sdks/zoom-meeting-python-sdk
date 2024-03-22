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


class DevicesListZdmGroupInfoResponseGroupsItem(BaseModel):
    # The ZDM group's describe.
    description: typing.Optional[str] = Field(None, alias='description')

    # The ZDM group's unique ID.
    zdm_group_id: typing.Optional[str] = Field(None, alias='zdm_group_id')

    # The ZDM group's name.
    name: typing.Optional[str] = Field(None, alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
