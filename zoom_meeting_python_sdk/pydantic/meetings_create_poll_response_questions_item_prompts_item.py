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

from zoom_meeting_python_sdk.pydantic.meetings_create_poll_response_questions_item_prompts_item_prompt_right_answers import MeetingsCreatePollResponseQuestionsItemPromptsItemPromptRightAnswers

class MeetingsCreatePollResponseQuestionsItemPromptsItem(BaseModel):
    # The question prompt's title.
    prompt_question: typing.Optional[str] = Field(None, alias='prompt_question')

    prompt_right_answers: typing.Optional[MeetingsCreatePollResponseQuestionsItemPromptsItemPromptRightAnswers] = Field(None, alias='prompt_right_answers')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
