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


class MeetingsGetSipUriWithPasscodeResponse(BaseModel):
    # The meeting's encoded SIP URI.
    sip_dialing: typing.Optional[str] = Field(None, alias='sip_dialing')

    # Whether the API caller has a CRC (Conference Room Connector) plan.
    paid_crc_plan_participant: typing.Optional[bool] = Field(None, alias='paid_crc_plan_participant')

    # This value identifies the meeting participant. It is automatically embedded in the SIP URI if the API caller has a CRC (Conference Room Connector) plan.
    participant_identifier_code: typing.Optional[str] = Field(None, alias='participant_identifier_code')

    # The number of seconds the encoded SIP URI is valid before it expires.
    expire_in: typing.Optional[int] = Field(None, alias='expire_in')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
