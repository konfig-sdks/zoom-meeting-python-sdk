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

from zoom_meeting_python_sdk.pydantic.tsp_list_user_tsp_accounts_response_tsp_accounts_item_dial_in_numbers import TspListUserTspAccountsResponseTspAccountsItemDialInNumbers

class TspListUserTspAccountsResponseTspAccountsItem(BaseModel):
    # Conference code: numeric value, length is less than 16.
    conference_code: str = Field(alias='conference_code')

    # Leader PIN: numeric value, length is less than 16.
    leader_pin: str = Field(alias='leader_pin')

    dial_in_numbers: typing.Optional[TspListUserTspAccountsResponseTspAccountsItemDialInNumbers] = Field(None, alias='dial_in_numbers')

    # The TSP credential ID.
    id: typing.Optional[Literal["1", "2"]] = Field(None, alias='id')

    # Telephony bridge 
    tsp_bridge: typing.Optional[Literal["US_TSP_TB", "EU_TSP_TB"]] = Field(None, alias='tsp_bridge')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
