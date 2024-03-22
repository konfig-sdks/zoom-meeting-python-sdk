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

from zoom_meeting_python_sdk.pydantic.reports_get_webinar_poll_reports_response_questions_item_question_details import ReportsGetWebinarPollReportsResponseQuestionsItemQuestionDetails

class ReportsGetWebinarPollReportsResponseQuestionsItem(BaseModel):
    # The participant's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    # The participant's display name. **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `name` field will return the &quot;Anonymous Attendee&quot; value.
    name: typing.Optional[str] = Field(None, alias='name')

    # The participant's first name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `first_name` field will return the &quot;Anonymous Attendee&quot; value.
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # The participant's last name. If the **Allow participants to answer questions anonymously** setting is enabled for a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meet), the participant's polling information is kept anonymous and the `last_name` field will return the &quot;Anonymous Attendee&quot; value.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    question_details: typing.Optional[ReportsGetWebinarPollReportsResponseQuestionsItemQuestionDetails] = Field(None, alias='question_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
