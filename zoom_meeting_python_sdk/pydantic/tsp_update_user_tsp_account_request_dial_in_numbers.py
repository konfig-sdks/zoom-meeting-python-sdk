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

from zoom_meeting_python_sdk.pydantic.tsp_update_user_tsp_account_request_dial_in_numbers_item import TspUpdateUserTspAccountRequestDialInNumbersItem

TspUpdateUserTspAccountRequestDialInNumbers = typing.List[TspUpdateUserTspAccountRequestDialInNumbersItem]
