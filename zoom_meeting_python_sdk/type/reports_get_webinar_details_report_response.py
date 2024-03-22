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

from zoom_meeting_python_sdk.type.reports_get_webinar_details_report_response_custom_keys import ReportsGetWebinarDetailsReportResponseCustomKeys
from zoom_meeting_python_sdk.type.reports_get_webinar_details_report_response_tracking_fields import ReportsGetWebinarDetailsReportResponseTrackingFields

class RequiredReportsGetWebinarDetailsReportResponse(TypedDict):
    pass

class OptionalReportsGetWebinarDetailsReportResponse(TypedDict, total=False):
    custom_keys: ReportsGetWebinarDetailsReportResponseCustomKeys

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

    # Number of Webinar minutes. This represents the total amount of Webinar minutes attended by each participant including the host, for a Webinar hosted by the user. For instance if there were one host(named A) and one participant(named B) in a Webinar, the value of total_minutes would be calculated as below:  **total_minutes** = Total Webinar Attendance Minutes of A + Total Webinar Attendance Minutes of B
    total_minutes: int

    tracking_fields: ReportsGetWebinarDetailsReportResponseTrackingFields

    # Meeting type.
    type: int

    # User email.
    user_email: str

    # User display name.
    user_name: str

    # Webinar UUID. Each webinar instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated when the next instance of the webinar starts). [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.
    uuid: str

class ReportsGetWebinarDetailsReportResponse(RequiredReportsGetWebinarDetailsReportResponse, OptionalReportsGetWebinarDetailsReportResponse):
    pass
