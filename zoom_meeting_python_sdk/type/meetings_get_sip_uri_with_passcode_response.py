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


class RequiredMeetingsGetSipUriWithPasscodeResponse(TypedDict):
    pass

class OptionalMeetingsGetSipUriWithPasscodeResponse(TypedDict, total=False):
    # The meeting's encoded SIP URI.
    sip_dialing: str

    # Whether the API caller has a CRC (Conference Room Connector) plan.
    paid_crc_plan_participant: bool

    # This value identifies the meeting participant. It is automatically embedded in the SIP URI if the API caller has a CRC (Conference Room Connector) plan.
    participant_identifier_code: str

    # The number of seconds the encoded SIP URI is valid before it expires.
    expire_in: int

class MeetingsGetSipUriWithPasscodeResponse(RequiredMeetingsGetSipUriWithPasscodeResponse, OptionalMeetingsGetSipUriWithPasscodeResponse):
    pass
