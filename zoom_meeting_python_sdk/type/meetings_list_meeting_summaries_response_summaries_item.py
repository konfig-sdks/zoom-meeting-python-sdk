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


class RequiredMeetingsListMeetingSummariesResponseSummariesItem(TypedDict):
    pass

class OptionalMeetingsListMeetingSummariesResponseSummariesItem(TypedDict, total=False):
    # The ID of the user who is set as the meeting host.
    meeting_host_id: str

    # The meeting host's email address.
    meeting_host_email: str

    # Unique meeting ID. Each meeting instance generates its own meeting UUID - after a meeting ends, a new UUID is generated for the next instance of the meeting. Retrieve a list of UUIDs from past meeting instances using the [**List past meeting instances**](https://developers.zoom.us) API. [Double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a `/` or contains `//` in it. 
    meeting_uuid: str

    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-) - the meeting's unique identifier in **long** format, represented as int64 data type in JSON, also known as the meeting number.
    meeting_id: int

    # Meeting topic.
    meeting_topic: str

    # The meeting's start date and time.
    meeting_start_time: datetime

    # The meeting's end date and time.
    meeting_end_time: datetime

    # The summary's start date and time.
    summary_start_time: datetime

    # The summary's end date and time.
    summary_end_time: datetime

    # The date and time at which the meeting summary was created.
    summary_created_time: datetime

    # The date and time at which the meeting summary was last modified.
    summary_last_modified_time: datetime

class MeetingsListMeetingSummariesResponseSummariesItem(RequiredMeetingsListMeetingSummariesResponseSummariesItem, OptionalMeetingsListMeetingSummariesResponseSummariesItem):
    pass
