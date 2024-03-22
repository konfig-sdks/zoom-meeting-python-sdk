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

from zoom_meeting_python_sdk.pydantic.tsp_get_account_info_response_dial_in_numbers import TspGetAccountInfoResponseDialInNumbers

class TspGetAccountInfoResponse(BaseModel):
    # Control restriction on account users adding a TSP number outside of account's dial in numbers.
    dial_in_number_unrestricted: typing.Optional[bool] = Field(None, alias='dial_in_number_unrestricted')

    dial_in_numbers: typing.Optional[TspGetAccountInfoResponseDialInNumbers] = Field(None, alias='dial_in_numbers')

    # Enable Telephony Service Provider for account users.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    # For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account.
    master_account_setting_extended: typing.Optional[bool] = Field(None, alias='master_account_setting_extended')

    # Control restriction on account users being able to modify their TSP credentials.
    modify_credential_forbidden: typing.Optional[bool] = Field(None, alias='modify_credential_forbidden')

    # Telephony bridge zone
    tsp_bridge: typing.Optional[Literal["US_TSP_TB", "EU_TSP_TB"]] = Field(None, alias='tsp_bridge')

    # Enable TSP feature for account. This has to be enabled to use any other tsp settings/features.
    tsp_enabled: typing.Optional[bool] = Field(None, alias='tsp_enabled')

    # Telephony Service Provider.
    tsp_provider: typing.Optional[str] = Field(None, alias='tsp_provider')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
