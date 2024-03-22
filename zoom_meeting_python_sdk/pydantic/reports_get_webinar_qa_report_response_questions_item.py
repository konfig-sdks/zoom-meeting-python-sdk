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

from zoom_meeting_python_sdk.pydantic.reports_get_webinar_qa_report_response_questions_item_question_details import ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetails

class ReportsGetWebinarQaReportResponseQuestionsItem(BaseModel):
    # The user ID of the user who asked the question. This value returns blank for external users.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # Participant's email. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: typing.Optional[str] = Field(None, alias='email')

    # Participant's display name.       If anonymous [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) option is enabled and if a participant submits the Q&amp;A without providing their name, the value of the `name` field will be &quot;Anonymous Attendee&quot;.
    name: typing.Optional[str] = Field(None, alias='name')

    question_details: typing.Optional[ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetails] = Field(None, alias='question_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
