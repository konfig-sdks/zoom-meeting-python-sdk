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

from zoom_meeting_python_sdk.pydantic.reports_get_meeting_detail_reports_response_custom_keys import ReportsGetMeetingDetailReportsResponseCustomKeys
from zoom_meeting_python_sdk.pydantic.reports_get_meeting_detail_reports_response_tracking_fields import ReportsGetMeetingDetailReportsResponseTrackingFields

class ReportsGetMeetingDetailReportsResponse(BaseModel):
    custom_keys: typing.Optional[ReportsGetMeetingDetailReportsResponseCustomKeys] = Field(None, alias='custom_keys')

    # Department of the host.
    dept: typing.Optional[str] = Field(None, alias='dept')

    # Meeting duration.
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Meeting end time.
    end_time: typing.Optional[datetime] = Field(None, alias='end_time')

    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &quot;**long**&quot; format(represented as int64 data type in JSON), also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    # Number of meeting participants.
    participants_count: typing.Optional[int] = Field(None, alias='participants_count')

    # Meeting start time.
    start_time: typing.Optional[datetime] = Field(None, alias='start_time')

    # Meeting topic.
    topic: typing.Optional[str] = Field(None, alias='topic')

    # Number of meeting minutes. This represents the total amount of meeting minutes attended by each participant including the host, for meetings hosted by the user. For instance if there were one host(named A) and one participant(named B) in a meeting, the value of total_minutes would be calculated as below:  **total_minutes** = Total Meeting Attendance Minutes of A + Total Meeting Attendance Minutes of B
    total_minutes: typing.Optional[int] = Field(None, alias='total_minutes')

    tracking_fields: typing.Optional[ReportsGetMeetingDetailReportsResponseTrackingFields] = Field(None, alias='tracking_fields')

    # Meeting type.
    type: typing.Optional[int] = Field(None, alias='type')

    # User email.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # User display name.
    user_name: typing.Optional[str] = Field(None, alias='user_name')

    # Meeting UUID. Each meeting instance will generate its own UUID(i.e., after a meeting ends, a new UUID will be generated for the next instance of the meeting). [Double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) your UUID when using it for API calls if the UUID begins with a '/' or contains '//' in it.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
