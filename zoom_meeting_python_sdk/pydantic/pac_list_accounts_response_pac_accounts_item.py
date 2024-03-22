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

from zoom_meeting_python_sdk.pydantic.pac_list_accounts_response_pac_accounts_item_dedicated_dial_in_number import PacListAccountsResponsePacAccountsItemDedicatedDialInNumber
from zoom_meeting_python_sdk.pydantic.pac_list_accounts_response_pac_accounts_item_global_dial_in_numbers import PacListAccountsResponsePacAccountsItemGlobalDialInNumbers

class PacListAccountsResponsePacAccountsItem(BaseModel):
    # The conference ID.
    conference_id: typing.Optional[int] = Field(None, alias='conference_id')

    dedicated_dial_in_number: typing.Optional[PacListAccountsResponsePacAccountsItemDedicatedDialInNumber] = Field(None, alias='dedicated_dial_in_number')

    global_dial_in_numbers: typing.Optional[PacListAccountsResponsePacAccountsItemGlobalDialInNumbers] = Field(None, alias='global_dial_in_numbers')

    # The listen-only password, up to six characters in length.
    listen_only_password: typing.Optional[str] = Field(None, alias='listen_only_password')

    # The participant password, up to six characters in length.
    participant_password: typing.Optional[str] = Field(None, alias='participant_password')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
