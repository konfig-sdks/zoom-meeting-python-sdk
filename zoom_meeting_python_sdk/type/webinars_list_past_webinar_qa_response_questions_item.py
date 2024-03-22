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

from zoom_meeting_python_sdk.type.webinars_list_past_webinar_qa_response_questions_item_question_details import WebinarsListPastWebinarQaResponseQuestionsItemQuestionDetails

class RequiredWebinarsListPastWebinarQaResponseQuestionsItem(TypedDict):
    pass

class OptionalWebinarsListPastWebinarQaResponseQuestionsItem(TypedDict, total=False):
    # Email address of the user. If the participant is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: str

    # Name of the user. If `anonymous` option is enabled for the Q&amp;A, the participant's information will be kept anonymous and the value of `name` field will be `Anonymous Attendee`.
    name: str

    question_details: WebinarsListPastWebinarQaResponseQuestionsItemQuestionDetails

class WebinarsListPastWebinarQaResponseQuestionsItem(RequiredWebinarsListPastWebinarQaResponseQuestionsItem, OptionalWebinarsListPastWebinarQaResponseQuestionsItem):
    pass
