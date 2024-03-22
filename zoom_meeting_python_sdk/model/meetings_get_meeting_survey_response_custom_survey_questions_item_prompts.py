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


class MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPrompts(
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
        def items() -> typing.Type['MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPromptsItem']:
            return MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPromptsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPromptsItem'], typing.List['MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPromptsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPrompts':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPromptsItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.meetings_get_meeting_survey_response_custom_survey_questions_item_prompts_item import MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemPromptsItem
