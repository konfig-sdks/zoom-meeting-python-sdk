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

from zoom_meeting_python_sdk.pydantic.meetings_get_meeting_summary_response_summary_details_item import MeetingsGetMeetingSummaryResponseSummaryDetailsItem

MeetingsGetMeetingSummaryResponseSummaryDetails = typing.List[MeetingsGetMeetingSummaryResponseSummaryDetailsItem]
