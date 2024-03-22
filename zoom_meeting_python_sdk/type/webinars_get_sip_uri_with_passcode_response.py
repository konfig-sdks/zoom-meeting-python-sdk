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


class RequiredWebinarsGetSipUriWithPasscodeResponse(TypedDict):
    pass

class OptionalWebinarsGetSipUriWithPasscodeResponse(TypedDict, total=False):
    # The webinar's encoded SIP URI.
    sip_dialing: str

    # Whether the API caller has a Conference Room Connector (CRC) plan.
    paid_crc_plan_participant: bool

    # This value identifies the webinar participant. It is automatically embedded in the SIP URI if the API caller has a CRC plan.
    participant_identifier_code: str

    # The number of seconds the encoded SIP URI is valid before it expires.
    expire_in: int

class WebinarsGetSipUriWithPasscodeResponse(RequiredWebinarsGetSipUriWithPasscodeResponse, OptionalWebinarsGetSipUriWithPasscodeResponse):
    pass
