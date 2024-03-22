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

from zoom_meeting_python_sdk.type.meetings_create_batch_polls_response_polls_item_questions_item_answers import MeetingsCreateBatchPollsResponsePollsItemQuestionsItemAnswers
from zoom_meeting_python_sdk.type.meetings_create_batch_polls_response_polls_item_questions_item_prompts import MeetingsCreateBatchPollsResponsePollsItemQuestionsItemPrompts
from zoom_meeting_python_sdk.type.meetings_create_batch_polls_response_polls_item_questions_item_right_answers import MeetingsCreateBatchPollsResponsePollsItemQuestionsItemRightAnswers

class RequiredMeetingsCreateBatchPollsResponsePollsItemQuestionsItem(TypedDict):
    pass

class OptionalMeetingsCreateBatchPollsResponsePollsItemQuestionsItem(TypedDict, total=False):
    # The allowed maximum number of characters. This field only returns for `short_answer` and `long_answer` polls.
    answer_max_character: int

    # The allowed minimum number of characters. This field only returns for `short_answer` and `long_answer` polls.
    answer_min_character: int

    # Whether participants must answer the question:  * `true` &mdash; The participant must answer the question.  * `false` &mdash; The participant does not need to answer the question.
    answer_required: bool

    answers: MeetingsCreateBatchPollsResponsePollsItemQuestionsItemAnswers

    # Whether the correct answer is case sensitive. This field only returns for `fill_in_the_blank` polls:  * `true` &mdash; The answer is case-sensitive.  * `false` &mdash; The answer is not case-sensitive.
    case_sensitive: bool

    # The poll question's title. For `fill_in_the_blank` polls, this field is the poll's question.
    name: str

    prompts: MeetingsCreateBatchPollsResponsePollsItemQuestionsItemPrompts

    # The high score label used for the `rating_max_value` field. This field only returns for `rating_scale` polls.
    rating_max_label: str

    # The rating scale's maximum value. This field only returns for `rating_scale` polls.
    rating_max_value: int

    # The low score label used for the `rating_min_value` field. This field only returns for `rating_scale` polls.
    rating_min_label: str

    # The rating scale's minimum value. This field only returns for `rating_scale` polls.
    rating_min_value: int

    right_answers: MeetingsCreateBatchPollsResponsePollsItemQuestionsItemRightAnswers

    # Whether to display the radio selection as a drop-down box:  * `true` &mdash; Show as a drop-down box.  * `false` &mdash; Do not show as a drop-down box.
    show_as_dropdown: bool

    # The poll's question and answer type:  * `single` &mdash; Single choice.  * `multiple` &mdash; Multiple choice.  * `matching` &mdash; Matching.  * `rank_order` &mdash; Rank order.  * `short_answer` &mdash; Short answer.  * `long_answer` &mdash; Long answer.  * `fill_in_the_blank` &mdash; Fill in the blank.  * `rating_scale` &mdash; Rating scale.
    type: str

class MeetingsCreateBatchPollsResponsePollsItemQuestionsItem(RequiredMeetingsCreateBatchPollsResponsePollsItemQuestionsItem, OptionalMeetingsCreateBatchPollsResponsePollsItemQuestionsItem):
    pass
