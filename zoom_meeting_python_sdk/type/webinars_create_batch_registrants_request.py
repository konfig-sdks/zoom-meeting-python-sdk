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

from zoom_meeting_python_sdk.type.webinars_create_batch_registrants_request_registrants import WebinarsCreateBatchRegistrantsRequestRegistrants

class RequiredWebinarsCreateBatchRegistrantsRequest(TypedDict):
    pass

class OptionalWebinarsCreateBatchRegistrantsRequest(TypedDict, total=False):
    # If a meeting was scheduled with approval_type `1` (manual approval), but you want to automatically approve registrants added via this API, set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting that was originally scheduled with approval_type `0` (automatic approval).
    auto_approve: bool

    registrants: WebinarsCreateBatchRegistrantsRequestRegistrants

class WebinarsCreateBatchRegistrantsRequest(RequiredWebinarsCreateBatchRegistrantsRequest, OptionalWebinarsCreateBatchRegistrantsRequest):
    pass
