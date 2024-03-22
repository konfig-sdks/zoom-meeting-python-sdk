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


class RequiredTspUpdateAccountTspInformationRequest(TypedDict):
    pass

class OptionalTspUpdateAccountTspInformationRequest(TypedDict, total=False):
    # Control restriction on account users adding a TSP number outside of account's dial in numbers.
    dial_in_number_unrestricted: bool

    # Enable 3rd party audio conferencing for account users
    enable: bool

    # For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account.
    master_account_setting_extended: bool

    # Control restriction on account users being able to modify their TSP credentials.
    modify_credential_forbidden: bool

    # Telephony bridge
    tsp_bridge: str

    # Enable TSP feature for account. This has to be enabled to use any other tsp settings/features.
    tsp_enabled: bool

    # 3rd party audio conferencing provider
    tsp_provider: str

class TspUpdateAccountTspInformationRequest(RequiredTspUpdateAccountTspInformationRequest, OptionalTspUpdateAccountTspInformationRequest):
    pass
