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

from zoom_meeting_python_sdk.type.meetings_batch_registrants_create_request_registrants import MeetingsBatchRegistrantsCreateRequestRegistrants

class RequiredMeetingsBatchRegistrantsCreateRequest(TypedDict):
    pass

class OptionalMeetingsBatchRegistrantsCreateRequest(TypedDict, total=False):
    # If a meeting was scheduled with approval_type `1` (manual approval), but you would like to automatically approve the registrants that are added via this API, you can set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting  that was originally scheduled with approval_type `0` (automatic approval).
    auto_approve: bool

    # Send confirmation Email to Registrants
    registrants_confirmation_email: bool

    registrants: MeetingsBatchRegistrantsCreateRequestRegistrants

class MeetingsBatchRegistrantsCreateRequest(RequiredMeetingsBatchRegistrantsCreateRequest, OptionalMeetingsBatchRegistrantsCreateRequest):
    pass
