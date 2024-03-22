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

from zoom_meeting_python_sdk.type.meetings_create_poll_request_questions_item_answers import MeetingsCreatePollRequestQuestionsItemAnswers
from zoom_meeting_python_sdk.type.meetings_create_poll_request_questions_item_prompts import MeetingsCreatePollRequestQuestionsItemPrompts
from zoom_meeting_python_sdk.type.meetings_create_poll_request_questions_item_right_answers import MeetingsCreatePollRequestQuestionsItemRightAnswers

class RequiredMeetingsCreatePollRequestQuestionsItem(TypedDict):
    pass

class OptionalMeetingsCreatePollRequestQuestionsItem(TypedDict, total=False):
    # The allowed maximum number of characters. This field only applies to `short_answer` and `long_answer` polls:  * For `short_answer` polls, a maximum of 500 characters.  * For `long_answer` polls, a maximum of 2,000 characters.
    answer_max_character: int

    # The allowed minimum number of characters. This field only applies to `short_answer` and `long_answer` polls. You must provide at least a **one** character minimum value.
    answer_min_character: int

    # Whether participants must answer the question:  * `true` &mdash; The participant must answer the question.  * `false` &mdash; The participant does not need to answer the question.   **Note:**  * When the poll's `type` value is `1` (Poll), this value defaults to `true`.  * When the poll's `type` value is the `2` (Advanced Poll) or `3` (Quiz) values, this value defaults to `false`.
    answer_required: bool

    answers: MeetingsCreatePollRequestQuestionsItemAnswers

    # Whether the correct answer is case sensitive. This field only applies to `fill_in_the_blank` polls:  * `true` &mdash; The answer is case-sensitive.  * `false` &mdash; The answer is not case-sensitive.   This value defaults to `false`.
    case_sensitive: bool

    # The poll question, up to 255 characters.   For `fill_in_the_blank` polls, this field is the poll's question. For each value that the user must fill in, ensure that there are the same number of `right_answers` values.
    name: str

    prompts: MeetingsCreatePollRequestQuestionsItemPrompts

    # The high score label used for the `rating_max_value` field.   This field only applies to the `rating_scale` poll.
    rating_max_label: str

    # The rating scale's maximum value, up to a maximum value of 10.   This field only applies to the `rating_scale` poll.
    rating_max_value: int

    # The low score label used for the `rating_min_value` field.   This field only applies to the `rating_scale` poll.
    rating_min_label: str

    # The rating scale's minimum value. This value cannot be less than zero.   This field only applies to the `rating_scale` poll.
    rating_min_value: int

    right_answers: MeetingsCreatePollRequestQuestionsItemRightAnswers

    # Whether to display the radio selection as a drop-down box:  * `true` &mdash; Show as a drop-down box.  * `false` &mdash; Do not show as a drop-down box.   This value defaults to `false`.
    show_as_dropdown: bool

    # The poll's question and answer type:  * `single` &mdash; Single choice.  * `multiple` &mdash; Multiple choice.  * `matching` &mdash; Matching.  * `rank_order` &mdash; Rank order.  * `short_answer` &mdash; Short answer.  * `long_answer` &mdash; Long answer.  * `fill_in_the_blank` &mdash; Fill in the blank.  * `rating_scale` &mdash; Rating scale.
    type: str

class MeetingsCreatePollRequestQuestionsItem(RequiredMeetingsCreatePollRequestQuestionsItem, OptionalMeetingsCreatePollRequestQuestionsItem):
    pass
