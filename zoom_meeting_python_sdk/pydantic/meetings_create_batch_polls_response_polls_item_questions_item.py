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

from zoom_meeting_python_sdk.pydantic.meetings_create_batch_polls_response_polls_item_questions_item_answers import MeetingsCreateBatchPollsResponsePollsItemQuestionsItemAnswers
from zoom_meeting_python_sdk.pydantic.meetings_create_batch_polls_response_polls_item_questions_item_prompts import MeetingsCreateBatchPollsResponsePollsItemQuestionsItemPrompts
from zoom_meeting_python_sdk.pydantic.meetings_create_batch_polls_response_polls_item_questions_item_right_answers import MeetingsCreateBatchPollsResponsePollsItemQuestionsItemRightAnswers

class MeetingsCreateBatchPollsResponsePollsItemQuestionsItem(BaseModel):
    # The allowed maximum number of characters. This field only returns for `short_answer` and `long_answer` polls.
    answer_max_character: typing.Optional[int] = Field(None, alias='answer_max_character')

    # The allowed minimum number of characters. This field only returns for `short_answer` and `long_answer` polls.
    answer_min_character: typing.Optional[int] = Field(None, alias='answer_min_character')

    # Whether participants must answer the question:  * `true` &mdash; The participant must answer the question.  * `false` &mdash; The participant does not need to answer the question.
    answer_required: typing.Optional[bool] = Field(None, alias='answer_required')

    answers: typing.Optional[MeetingsCreateBatchPollsResponsePollsItemQuestionsItemAnswers] = Field(None, alias='answers')

    # Whether the correct answer is case sensitive. This field only returns for `fill_in_the_blank` polls:  * `true` &mdash; The answer is case-sensitive.  * `false` &mdash; The answer is not case-sensitive.
    case_sensitive: typing.Optional[bool] = Field(None, alias='case_sensitive')

    # The poll question's title. For `fill_in_the_blank` polls, this field is the poll's question.
    name: typing.Optional[str] = Field(None, alias='name')

    prompts: typing.Optional[MeetingsCreateBatchPollsResponsePollsItemQuestionsItemPrompts] = Field(None, alias='prompts')

    # The high score label used for the `rating_max_value` field. This field only returns for `rating_scale` polls.
    rating_max_label: typing.Optional[str] = Field(None, alias='rating_max_label')

    # The rating scale's maximum value. This field only returns for `rating_scale` polls.
    rating_max_value: typing.Optional[int] = Field(None, alias='rating_max_value')

    # The low score label used for the `rating_min_value` field. This field only returns for `rating_scale` polls.
    rating_min_label: typing.Optional[str] = Field(None, alias='rating_min_label')

    # The rating scale's minimum value. This field only returns for `rating_scale` polls.
    rating_min_value: typing.Optional[int] = Field(None, alias='rating_min_value')

    right_answers: typing.Optional[MeetingsCreateBatchPollsResponsePollsItemQuestionsItemRightAnswers] = Field(None, alias='right_answers')

    # Whether to display the radio selection as a drop-down box:  * `true` &mdash; Show as a drop-down box.  * `false` &mdash; Do not show as a drop-down box.
    show_as_dropdown: typing.Optional[bool] = Field(None, alias='show_as_dropdown')

    # The poll's question and answer type:  * `single` &mdash; Single choice.  * `multiple` &mdash; Multiple choice.  * `matching` &mdash; Matching.  * `rank_order` &mdash; Rank order.  * `short_answer` &mdash; Short answer.  * `long_answer` &mdash; Long answer.  * `fill_in_the_blank` &mdash; Fill in the blank.  * `rating_scale` &mdash; Rating scale.
    type: typing.Optional[Literal["single", "multiple", "matching", "rank_order", "short_answer", "long_answer", "fill_in_the_blank", "rating_scale"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
