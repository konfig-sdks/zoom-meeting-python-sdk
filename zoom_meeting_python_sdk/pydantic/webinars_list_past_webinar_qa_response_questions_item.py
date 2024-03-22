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

from zoom_meeting_python_sdk.pydantic.webinars_list_past_webinar_qa_response_questions_item_question_details import WebinarsListPastWebinarQaResponseQuestionsItemQuestionDetails

class WebinarsListPastWebinarQaResponseQuestionsItem(BaseModel):
    # Email address of the user. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: typing.Optional[str] = Field(None, alias='email')

    # Name of the user. If `anonymous` option is enabled for the Q&amp;A, the participant's information will be kept anonymous and the value of `name` field will be `Anonymous Attendee`.
    name: typing.Optional[str] = Field(None, alias='name')

    question_details: typing.Optional[WebinarsListPastWebinarQaResponseQuestionsItemQuestionDetails] = Field(None, alias='question_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
