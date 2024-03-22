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

from zoom_meeting_python_sdk.type.meetings_create_batch_polls_response_polls_item_questions import MeetingsCreateBatchPollsResponsePollsItemQuestions

class RequiredMeetingsCreateBatchPollsResponsePollsItem(TypedDict):
    pass

class OptionalMeetingsCreateBatchPollsResponsePollsItem(TypedDict, total=False):
    # Title for the Poll
    title: str

    # Whether to allow meeting participants to answer poll questions anonymously:  * `true` &mdash; Anonymous polls enabled.  * `false` &mdash; Participants cannot answer poll questions anonymously.
    anonymous: bool

    # Meeting Poll ID
    id: str

    # The type of poll:  * `1` &mdash; Poll.  * `2` &mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * `3` &mdash; Quiz. This feature must be enabled in your Zoom account.
    poll_type: int

    questions: MeetingsCreateBatchPollsResponsePollsItemQuestions

    # Status of the Meeting Poll:    `notstart` - Poll not started    `started` - Poll started    `ended` - Poll ended    `sharing` - Sharing poll results
    status: str

class MeetingsCreateBatchPollsResponsePollsItem(RequiredMeetingsCreateBatchPollsResponsePollsItem, OptionalMeetingsCreateBatchPollsResponsePollsItem):
    pass
