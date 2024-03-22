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

from zoom_meeting_python_sdk.type.tsp_list_user_tsp_accounts_response_tsp_accounts_item_dial_in_numbers_item import TspListUserTspAccountsResponseTspAccountsItemDialInNumbersItem

TspListUserTspAccountsResponseTspAccountsItemDialInNumbers = typing.List[TspListUserTspAccountsResponseTspAccountsItemDialInNumbersItem]
