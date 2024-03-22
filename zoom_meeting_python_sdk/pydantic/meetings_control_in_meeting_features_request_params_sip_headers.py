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

from zoom_meeting_python_sdk.pydantic.meetings_control_in_meeting_features_request_params_sip_headers_additional_headers import MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeaders

class MeetingsControlInMeetingFeaturesRequestParamsSipHeaders(BaseModel):
    # Custom name that will be used within the SIP Header.
    from_display_name: typing.Optional[str] = Field(None, alias='from_display_name')

    # Custom remote name that will be used within the meeting.
    to_display_name: typing.Optional[str] = Field(None, alias='to_display_name')

    # Custom URI that will be used within the SIP Header. The URI must start with 'sip:' or 'sips:' as a valid URI based on parameters defined by the platform.
    from_uri: typing.Optional[str] = Field(None, alias='from_uri')

    additional_headers: typing.Optional[MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeaders] = Field(None, alias='additional_headers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
