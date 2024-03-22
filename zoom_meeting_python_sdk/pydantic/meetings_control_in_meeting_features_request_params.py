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

from zoom_meeting_python_sdk.pydantic.meetings_control_in_meeting_features_request_params_contacts import MeetingsControlInMeetingFeaturesRequestParamsContacts
from zoom_meeting_python_sdk.pydantic.meetings_control_in_meeting_features_request_params_h323_headers import MeetingsControlInMeetingFeaturesRequestParamsH323Headers
from zoom_meeting_python_sdk.pydantic.meetings_control_in_meeting_features_request_params_invite_options import MeetingsControlInMeetingFeaturesRequestParamsInviteOptions
from zoom_meeting_python_sdk.pydantic.meetings_control_in_meeting_features_request_params_sip_headers import MeetingsControlInMeetingFeaturesRequestParamsSipHeaders

class MeetingsControlInMeetingFeaturesRequestParams(BaseModel):
    contacts: typing.Optional[MeetingsControlInMeetingFeaturesRequestParamsContacts] = Field(None, alias='contacts')

    # The user's name to display in the meeting. Use this field if you pass the `participant.invite.callout` value for the `method` field.
    invitee_name: typing.Optional[str] = Field(None, alias='invitee_name')

    # The user's phone number. Use this field if you pass the `participant.invite.callout` value for the `method` field. As a best practice, ensure this includes a country code and area code.
    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    invite_options: typing.Optional[MeetingsControlInMeetingFeaturesRequestParamsInviteOptions] = Field(None, alias='invite_options')

    # The type of call out. Use a value of `h323` or `sip`. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.
    call_type: typing.Optional[str] = Field(None, alias='call_type')

    # The user's device IP address or URI. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.
    device_ip: typing.Optional[str] = Field(None, alias='device_ip')

    h323_headers: typing.Optional[MeetingsControlInMeetingFeaturesRequestParamsH323Headers] = Field(None, alias='h323_headers')

    sip_headers: typing.Optional[MeetingsControlInMeetingFeaturesRequestParamsSipHeaders] = Field(None, alias='sip_headers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
