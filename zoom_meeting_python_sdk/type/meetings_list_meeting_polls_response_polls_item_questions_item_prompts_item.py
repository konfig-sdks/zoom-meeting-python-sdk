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

from zoom_meeting_python_sdk.type.meetings_list_meeting_polls_response_polls_item_questions_item_prompts_item_prompt_right_answers import MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers

class RequiredMeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem(TypedDict):
    pass

class OptionalMeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem(TypedDict, total=False):
    # The question prompt's title.
    prompt_question: str

    prompt_right_answers: MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers

class MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem(RequiredMeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem, OptionalMeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem):
    pass
