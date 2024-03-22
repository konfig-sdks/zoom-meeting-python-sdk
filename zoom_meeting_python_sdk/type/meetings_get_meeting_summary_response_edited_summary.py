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

from zoom_meeting_python_sdk.type.meetings_get_meeting_summary_response_edited_summary_next_steps import MeetingsGetMeetingSummaryResponseEditedSummaryNextSteps

class RequiredMeetingsGetMeetingSummaryResponseEditedSummary(TypedDict):
    pass

class OptionalMeetingsGetMeetingSummaryResponseEditedSummary(TypedDict, total=False):
    # The user edited summary details.
    summary_details: str

    next_steps: MeetingsGetMeetingSummaryResponseEditedSummaryNextSteps

class MeetingsGetMeetingSummaryResponseEditedSummary(RequiredMeetingsGetMeetingSummaryResponseEditedSummary, OptionalMeetingsGetMeetingSummaryResponseEditedSummary):
    pass
