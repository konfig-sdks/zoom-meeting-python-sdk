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

from zoom_meeting_python_sdk.type.tsp_add_user_tsp_account_request_dial_in_numbers import TspAddUserTspAccountRequestDialInNumbers

class RequiredTspAddUserTspAccountRequest(TypedDict):
    # Conference code: numeric value, length is less than 16.
    conference_code: str

    # Leader PIN: numeric value, length is less than 16.
    leader_pin: str

class OptionalTspAddUserTspAccountRequest(TypedDict, total=False):
    dial_in_numbers: TspAddUserTspAccountRequestDialInNumbers

    # Telephony bridge
    tsp_bridge: str

class TspAddUserTspAccountRequest(RequiredTspAddUserTspAccountRequest, OptionalTspAddUserTspAccountRequest):
    pass
