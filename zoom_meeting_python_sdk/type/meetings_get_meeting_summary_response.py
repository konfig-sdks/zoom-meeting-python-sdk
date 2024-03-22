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

from zoom_meeting_python_sdk.type.meetings_get_meeting_summary_response_edited_summary import MeetingsGetMeetingSummaryResponseEditedSummary
from zoom_meeting_python_sdk.type.meetings_get_meeting_summary_response_next_steps import MeetingsGetMeetingSummaryResponseNextSteps
from zoom_meeting_python_sdk.type.meetings_get_meeting_summary_response_summary_details import MeetingsGetMeetingSummaryResponseSummaryDetails

class RequiredMeetingsGetMeetingSummaryResponse(TypedDict):
    pass

class OptionalMeetingsGetMeetingSummaryResponse(TypedDict, total=False):
    # The ID of the user who is set as the meeting host.
    meeting_host_id: str

    # The meeting host's email address.
    meeting_host_email: str

    # The unique meeting ID.   Each meeting instance generates its own meeting UUID. After a meeting ends, a new UUID is generated for the next instance of the meeting.   Use the [**List past meeting instances**](https://developers.zoom.us) API to retrieve a list of UUIDs from past meeting instances. [Double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a `/` or contains `//` in it. 
    meeting_uuid: str

    # [The meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-)  The meeting's unique identifier in **long** format, represented as int64 data type in JSON. Also known as the meeting number.
    meeting_id: int

    # The meeting topic.
    meeting_topic: str

    # The meeting's start date and time.
    meeting_start_time: datetime

    # The meeting's end date and time.
    meeting_end_time: datetime

    # The summary's start date and time.
    summary_start_time: datetime

    # The summary's end date and time.
    summary_end_time: datetime

    # The date and time when the meeting summary was created.
    summary_created_time: datetime

    # The date and time when the meeting summary was last modified.
    summary_last_modified_time: datetime

    # The summary title.
    summary_title: str

    # The summary overview.
    summary_overview: str

    summary_details: MeetingsGetMeetingSummaryResponseSummaryDetails

    next_steps: MeetingsGetMeetingSummaryResponseNextSteps

    edited_summary: MeetingsGetMeetingSummaryResponseEditedSummary

class MeetingsGetMeetingSummaryResponse(RequiredMeetingsGetMeetingSummaryResponse, OptionalMeetingsGetMeetingSummaryResponse):
    pass
