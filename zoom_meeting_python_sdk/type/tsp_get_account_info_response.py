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

from zoom_meeting_python_sdk.type.tsp_get_account_info_response_dial_in_numbers import TspGetAccountInfoResponseDialInNumbers

class RequiredTspGetAccountInfoResponse(TypedDict):
    pass

class OptionalTspGetAccountInfoResponse(TypedDict, total=False):
    # Control restriction on account users adding a TSP number outside of account's dial in numbers.
    dial_in_number_unrestricted: bool

    dial_in_numbers: TspGetAccountInfoResponseDialInNumbers

    # Enable Telephony Service Provider for account users.
    enable: bool

    # For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account.
    master_account_setting_extended: bool

    # Control restriction on account users being able to modify their TSP credentials.
    modify_credential_forbidden: bool

    # Telephony bridge zone
    tsp_bridge: str

    # Enable TSP feature for account. This has to be enabled to use any other tsp settings/features.
    tsp_enabled: bool

    # Telephony Service Provider.
    tsp_provider: str

class TspGetAccountInfoResponse(RequiredTspGetAccountInfoResponse, OptionalTspGetAccountInfoResponse):
    pass
