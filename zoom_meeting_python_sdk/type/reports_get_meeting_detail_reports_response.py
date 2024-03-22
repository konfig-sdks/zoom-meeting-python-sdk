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

from zoom_meeting_python_sdk.type.reports_get_meeting_detail_reports_response_custom_keys import ReportsGetMeetingDetailReportsResponseCustomKeys
from zoom_meeting_python_sdk.type.reports_get_meeting_detail_reports_response_tracking_fields import ReportsGetMeetingDetailReportsResponseTrackingFields

class RequiredReportsGetMeetingDetailReportsResponse(TypedDict):
    pass

class OptionalReportsGetMeetingDetailReportsResponse(TypedDict, total=False):
    custom_keys: ReportsGetMeetingDetailReportsResponseCustomKeys

    # Department of the host.
    dept: str

    # Meeting duration.
    duration: int

    # Meeting end time.
    end_time: datetime

    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &quot;**long**&quot; format(represented as int64 data type in JSON), also known as the meeting number.
    id: int

    # Number of meeting participants.
    participants_count: int

    # Meeting start time.
    start_time: datetime

    # Meeting topic.
    topic: str

    # Number of meeting minutes. This represents the total amount of meeting minutes attended by each participant including the host, for meetings hosted by the user. For instance if there were one host(named A) and one participant(named B) in a meeting, the value of total_minutes would be calculated as below:  **total_minutes** = Total Meeting Attendance Minutes of A + Total Meeting Attendance Minutes of B
    total_minutes: int

    tracking_fields: ReportsGetMeetingDetailReportsResponseTrackingFields

    # Meeting type.
    type: int

    # User email.
    user_email: str

    # User display name.
    user_name: str

    # Meeting UUID. Each meeting instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). [Double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.
    uuid: str

class ReportsGetMeetingDetailReportsResponse(RequiredReportsGetMeetingDetailReportsResponse, OptionalReportsGetMeetingDetailReportsResponse):
    pass
