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

from zoom_meeting_python_sdk.type.reports_get_meeting_poll_reports_response_questions_item_question_details import ReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetails

class RequiredReportsGetMeetingPollReportsResponseQuestionsItem(TypedDict):
    pass

class OptionalReportsGetMeetingPollReportsResponseQuestionsItem(TypedDict, total=False):
    # The participant's email address.
    email: str

    # The participant's display name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `name` field will return the &quot;Anonymous Attendee&quot; value.
    name: str

    # The participant's first name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `first_name` field will return the &quot;Anonymous Attendee&quot; value.
    first_name: str

    # The participant's last name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `last_name` field will return the &quot;Anonymous Attendee&quot; value.
    last_name: str

    question_details: ReportsGetMeetingPollReportsResponseQuestionsItemQuestionDetails

class ReportsGetMeetingPollReportsResponseQuestionsItem(RequiredReportsGetMeetingPollReportsResponseQuestionsItem, OptionalReportsGetMeetingPollReportsResponseQuestionsItem):
    pass
