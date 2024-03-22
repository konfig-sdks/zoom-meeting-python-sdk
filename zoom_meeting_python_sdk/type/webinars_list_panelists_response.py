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

from zoom_meeting_python_sdk.type.webinars_list_panelists_response_panelists import WebinarsListPanelistsResponsePanelists

class RequiredWebinarsListPanelistsResponse(TypedDict):
    pass

class OptionalWebinarsListPanelistsResponse(TypedDict, total=False):
    panelists: WebinarsListPanelistsResponsePanelists

    # Total records.
    total_records: int

class WebinarsListPanelistsResponse(RequiredWebinarsListPanelistsResponse, OptionalWebinarsListPanelistsResponse):
    pass
