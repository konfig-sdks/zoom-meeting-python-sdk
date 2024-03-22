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

from zoom_meeting_python_sdk.pydantic.meetings_get_meeting_summary_response_edited_summary import MeetingsGetMeetingSummaryResponseEditedSummary
from zoom_meeting_python_sdk.pydantic.meetings_get_meeting_summary_response_next_steps import MeetingsGetMeetingSummaryResponseNextSteps
from zoom_meeting_python_sdk.pydantic.meetings_get_meeting_summary_response_summary_details import MeetingsGetMeetingSummaryResponseSummaryDetails

class MeetingsGetMeetingSummaryResponse(BaseModel):
    # The ID of the user who is set as the meeting host.
    meeting_host_id: typing.Optional[str] = Field(None, alias='meeting_host_id')

    # The meeting host's email address.
    meeting_host_email: typing.Optional[str] = Field(None, alias='meeting_host_email')

    # The unique meeting ID.   Each meeting instance generates its own meeting UUID. After a meeting ends, a new UUID is generated for the next instance of the meeting.   Use the [**List past meeting instances**](https://developers.zoom.us) API to retrieve a list of UUIDs from past meeting instances. [Double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a `/` or contains `//` in it. 
    meeting_uuid: typing.Optional[str] = Field(None, alias='meeting_uuid')

    # [The meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-)  The meeting's unique identifier in **long** format, represented as int64 data type in JSON. Also known as the meeting number.
    meeting_id: typing.Optional[int] = Field(None, alias='meeting_id')

    # The meeting topic.
    meeting_topic: typing.Optional[str] = Field(None, alias='meeting_topic')

    # The meeting's start date and time.
    meeting_start_time: typing.Optional[datetime] = Field(None, alias='meeting_start_time')

    # The meeting's end date and time.
    meeting_end_time: typing.Optional[datetime] = Field(None, alias='meeting_end_time')

    # The summary's start date and time.
    summary_start_time: typing.Optional[datetime] = Field(None, alias='summary_start_time')

    # The summary's end date and time.
    summary_end_time: typing.Optional[datetime] = Field(None, alias='summary_end_time')

    # The date and time when the meeting summary was created.
    summary_created_time: typing.Optional[datetime] = Field(None, alias='summary_created_time')

    # The date and time when the meeting summary was last modified.
    summary_last_modified_time: typing.Optional[datetime] = Field(None, alias='summary_last_modified_time')

    # The summary title.
    summary_title: typing.Optional[str] = Field(None, alias='summary_title')

    # The summary overview.
    summary_overview: typing.Optional[str] = Field(None, alias='summary_overview')

    summary_details: typing.Optional[MeetingsGetMeetingSummaryResponseSummaryDetails] = Field(None, alias='summary_details')

    next_steps: typing.Optional[MeetingsGetMeetingSummaryResponseNextSteps] = Field(None, alias='next_steps')

    edited_summary: typing.Optional[MeetingsGetMeetingSummaryResponseEditedSummary] = Field(None, alias='edited_summary')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
