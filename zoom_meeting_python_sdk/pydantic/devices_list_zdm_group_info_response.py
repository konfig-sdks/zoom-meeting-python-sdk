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

from zoom_meeting_python_sdk.pydantic.devices_list_zdm_group_info_response_groups import DevicesListZdmGroupInfoResponseGroups

class DevicesListZdmGroupInfoResponse(BaseModel):
    groups: typing.Optional[DevicesListZdmGroupInfoResponseGroups] = Field(None, alias='groups')

    # Use the next page token to paginate through a large set of results. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The total number of records returned from a single API call.
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
