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

from zoom_meeting_python_sdk.pydantic.webinars_update_registrant_status_request_registrants import WebinarsUpdateRegistrantStatusRequestRegistrants

class WebinarsUpdateRegistrantStatusRequest(BaseModel):
    # The registration action to perform.  * `approve` - Approve the registrant.  * `deny` - Reject the registrant.  * `cancel` - Cancel the registrant's approval.
    action: Literal["approve", "deny", "cancel"] = Field(alias='action')

    registrants: typing.Optional[WebinarsUpdateRegistrantStatusRequestRegistrants] = Field(None, alias='registrants')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
