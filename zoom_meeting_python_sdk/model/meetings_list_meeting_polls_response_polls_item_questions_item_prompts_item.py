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


class MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            prompt_question = schemas.StrSchema
        
            @staticmethod
            def prompt_right_answers() -> typing.Type['MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers']:
                return MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers
            __annotations__ = {
                "prompt_question": prompt_question,
                "prompt_right_answers": prompt_right_answers,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_question"]) -> MetaOapg.properties.prompt_question: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_right_answers"]) -> 'MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["prompt_question", "prompt_right_answers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_question"]) -> typing.Union[MetaOapg.properties.prompt_question, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_right_answers"]) -> typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["prompt_question", "prompt_right_answers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        prompt_question: typing.Union[MetaOapg.properties.prompt_question, str, schemas.Unset] = schemas.unset,
        prompt_right_answers: typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItem':
        return super().__new__(
            cls,
            *args,
            prompt_question=prompt_question,
            prompt_right_answers=prompt_right_answers,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_list_meeting_polls_response_polls_item_questions_item_prompts_item_prompt_right_answers import MeetingsListMeetingPollsResponsePollsItemQuestionsItemPromptsItemPromptRightAnswers
