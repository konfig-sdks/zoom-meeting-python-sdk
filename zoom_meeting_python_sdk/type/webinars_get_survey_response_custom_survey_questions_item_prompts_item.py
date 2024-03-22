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


class RequiredWebinarsGetSurveyResponseCustomSurveyQuestionsItemPromptsItem(TypedDict):
    pass

class OptionalWebinarsGetSurveyResponseCustomSurveyQuestionsItemPromptsItem(TypedDict, total=False):
    # The question prompt's title.
    prompt_question: str

class WebinarsGetSurveyResponseCustomSurveyQuestionsItemPromptsItem(RequiredWebinarsGetSurveyResponseCustomSurveyQuestionsItemPromptsItem, OptionalWebinarsGetSurveyResponseCustomSurveyQuestionsItemPromptsItem):
    pass
