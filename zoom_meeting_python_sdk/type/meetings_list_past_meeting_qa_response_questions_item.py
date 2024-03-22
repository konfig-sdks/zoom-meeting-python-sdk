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

from zoom_meeting_python_sdk.type.meetings_list_past_meeting_qa_response_questions_item_question_details import MeetingsListPastMeetingQaResponseQuestionsItemQuestionDetails

class RequiredMeetingsListPastMeetingQaResponseQuestionsItem(TypedDict):
    pass

class OptionalMeetingsListPastMeetingQaResponseQuestionsItem(TypedDict, total=False):
    # The user's email address. If the user is **not** part of the host's account, this returns an empty string value, with some exceptions. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for details.
    email: str

    # The user's name. If `anonymous` option is enabled for the Q&amp;A, the participant's information is be kept anonymous and the value of `name` field is `Anonymous Attendee`.
    name: str

    question_details: MeetingsListPastMeetingQaResponseQuestionsItemQuestionDetails

class MeetingsListPastMeetingQaResponseQuestionsItem(RequiredMeetingsListPastMeetingQaResponseQuestionsItem, OptionalMeetingsListPastMeetingQaResponseQuestionsItem):
    pass
