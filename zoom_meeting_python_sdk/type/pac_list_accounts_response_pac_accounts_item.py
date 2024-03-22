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

from zoom_meeting_python_sdk.type.pac_list_accounts_response_pac_accounts_item_dedicated_dial_in_number import PacListAccountsResponsePacAccountsItemDedicatedDialInNumber
from zoom_meeting_python_sdk.type.pac_list_accounts_response_pac_accounts_item_global_dial_in_numbers import PacListAccountsResponsePacAccountsItemGlobalDialInNumbers

class RequiredPacListAccountsResponsePacAccountsItem(TypedDict):
    pass

class OptionalPacListAccountsResponsePacAccountsItem(TypedDict, total=False):
    # The conference ID.
    conference_id: int

    dedicated_dial_in_number: PacListAccountsResponsePacAccountsItemDedicatedDialInNumber

    global_dial_in_numbers: PacListAccountsResponsePacAccountsItemGlobalDialInNumbers

    # The listen-only password, up to six characters in length.
    listen_only_password: str

    # The participant password, up to six characters in length.
    participant_password: str

class PacListAccountsResponsePacAccountsItem(RequiredPacListAccountsResponsePacAccountsItem, OptionalPacListAccountsResponsePacAccountsItem):
    pass
