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

from zoom_meeting_python_sdk.type.webinars_update_registrant_status_request_registrants import WebinarsUpdateRegistrantStatusRequestRegistrants

class RequiredWebinarsUpdateRegistrantStatusRequest(TypedDict):
    # The registration action to perform.  * `approve` - Approve the registrant.  * `deny` - Reject the registrant.  * `cancel` - Cancel the registrant's approval.
    action: str

class OptionalWebinarsUpdateRegistrantStatusRequest(TypedDict, total=False):
    registrants: WebinarsUpdateRegistrantStatusRequestRegistrants

class WebinarsUpdateRegistrantStatusRequest(RequiredWebinarsUpdateRegistrantStatusRequest, OptionalWebinarsUpdateRegistrantStatusRequest):
    pass
