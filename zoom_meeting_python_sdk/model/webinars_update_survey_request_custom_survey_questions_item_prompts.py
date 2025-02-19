# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zoom_meeting_python_sdk import schemas  # noqa: F401


class WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPrompts(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the prompt questions. This field only applies to `matching` and `rank_order` questions. You **must** provide a minimum of two prompts, up to a maximum of 10 prompts.
    """


    class MetaOapg:
        max_items = 10
        min_items = 2
        
        @staticmethod
        def items() -> typing.Type['WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPromptsItem']:
            return WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPromptsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPromptsItem'], typing.List['WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPromptsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPrompts':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPromptsItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.webinars_update_survey_request_custom_survey_questions_item_prompts_item import WebinarsUpdateSurveyRequestCustomSurveyQuestionsItemPromptsItem
