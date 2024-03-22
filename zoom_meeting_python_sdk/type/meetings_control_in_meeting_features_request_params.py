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

from zoom_meeting_python_sdk.type.meetings_control_in_meeting_features_request_params_contacts import MeetingsControlInMeetingFeaturesRequestParamsContacts
from zoom_meeting_python_sdk.type.meetings_control_in_meeting_features_request_params_h323_headers import MeetingsControlInMeetingFeaturesRequestParamsH323Headers
from zoom_meeting_python_sdk.type.meetings_control_in_meeting_features_request_params_invite_options import MeetingsControlInMeetingFeaturesRequestParamsInviteOptions
from zoom_meeting_python_sdk.type.meetings_control_in_meeting_features_request_params_sip_headers import MeetingsControlInMeetingFeaturesRequestParamsSipHeaders

class RequiredMeetingsControlInMeetingFeaturesRequestParams(TypedDict):
    pass

class OptionalMeetingsControlInMeetingFeaturesRequestParams(TypedDict, total=False):
    contacts: MeetingsControlInMeetingFeaturesRequestParamsContacts

    # The user's name to display in the meeting. Use this field if you pass the `participant.invite.callout` value for the `method` field.
    invitee_name: str

    # The user's phone number. Use this field if you pass the `participant.invite.callout` value for the `method` field. As a best practice, ensure this includes a country code and area code.
    phone_number: str

    invite_options: MeetingsControlInMeetingFeaturesRequestParamsInviteOptions

    # The type of call out. Use a value of `h323` or `sip`. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.
    call_type: str

    # The user's device IP address or URI. Use this field if you pass the `participant.invite.room_system_callout` value for the `method` field.
    device_ip: str

    h323_headers: MeetingsControlInMeetingFeaturesRequestParamsH323Headers

    sip_headers: MeetingsControlInMeetingFeaturesRequestParamsSipHeaders

class MeetingsControlInMeetingFeaturesRequestParams(RequiredMeetingsControlInMeetingFeaturesRequestParams, OptionalMeetingsControlInMeetingFeaturesRequestParams):
    pass
