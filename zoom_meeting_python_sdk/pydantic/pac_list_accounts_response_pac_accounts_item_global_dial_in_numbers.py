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

from zoom_meeting_python_sdk.pydantic.pac_list_accounts_response_pac_accounts_item_global_dial_in_numbers_item import PacListAccountsResponsePacAccountsItemGlobalDialInNumbersItem

PacListAccountsResponsePacAccountsItemGlobalDialInNumbers = typing.List[PacListAccountsResponsePacAccountsItemGlobalDialInNumbersItem]
