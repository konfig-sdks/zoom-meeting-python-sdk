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

from zoom_meeting_python_sdk.type.webinars_list_past_instances_response_webinars import WebinarsListPastInstancesResponseWebinars

class RequiredWebinarsListPastInstancesResponse(TypedDict):
    pass

class OptionalWebinarsListPastInstancesResponse(TypedDict, total=False):
    webinars: WebinarsListPastInstancesResponseWebinars

class WebinarsListPastInstancesResponse(RequiredWebinarsListPastInstancesResponse, OptionalWebinarsListPastInstancesResponse):
    pass
