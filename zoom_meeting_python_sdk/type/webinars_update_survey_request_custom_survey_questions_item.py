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

from zoom_meeting_python_sdk.type.webinars_update_survey_request_custom_survey_questions_item_answers import WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemAnswers
from zoom_meeting_python_sdk.type.webinars_update_survey_request_custom_survey_questions_item_prompts import WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPrompts

class RequiredWebinarsUpdateSurveyRequestCustomSurveyQuestionsItem(TypedDict):
    pass

class OptionalWebinarsUpdateSurveyRequestCustomSurveyQuestionsItem(TypedDict, total=False):
    # The survey question, up to 420 characters.
    name: str

    # The survey's question and answer type.  * `single` - Single choice.  * `multiple` - Multiple choice.  * `matching` - Matching.  * `rank_order` - Rank order  * `short_answer` - Short answer  * `long_answer` - Long answer.  * `fill_in_the_blank` - Fill in the blank  * `rating_scale` - Rating scale.
    type: str

    # Whether participants must answer the question.  * `true` - The participant must answer the question.  * `false` - The participant does not need to answer the question.    This value defaults to `false`.
    answer_required: bool

    # Whether to display the radio selection as a drop-down box.  * `true` - Show as a drop-down box.  * `false` - Do not show as a drop-down box.    This value defaults to `false`.
    show_as_dropdown: bool

    answers: WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemAnswers

    prompts: WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPrompts

    # The allowed minimum number of characters. This field only applies to `short_answer` and `long_answer` questions. You must provide at least a **one** character minimum value.
    answer_min_character: int

    # The allowed maximum number of characters. This field only applies to `short_answer` and `long_answer` questions.  * For `short_answer` question, a maximum of 500 characters.  * For `long_answer` question, a maximum of 2,000 characters.
    answer_max_character: int

    # The rating scale's minimum value. This value can't be less than zero.    This field only applies to the `rating_scale` survey.
    rating_min_value: int

    # The rating scale's maximum value, up to a maximum value of 10.    This field only applies to the `rating_scale` survey.
    rating_max_value: int

    # The low score label used for the `rating_min_value` field, up to 50 characters.    This field only applies to the `rating_scale` survey.
    rating_min_label: str

    # The high score label used for the `rating_max_value` field, up to 50 characters.    This field only applies to the `rating_scale` survey.
    rating_max_label: str

class WebinarsUpdateSurveyRequestCustomSurveyQuestionsItem(RequiredWebinarsUpdateSurveyRequestCustomSurveyQuestionsItem, OptionalWebinarsUpdateSurveyRequestCustomSurveyQuestionsItem):
    pass
