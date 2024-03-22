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


class MeetingsListMeetingPollsResponsePollsItemQuestionsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            answer_max_character = schemas.IntSchema
            
            
            class answer_min_character(
                schemas.IntSchema
            ):
                pass
            answer_required = schemas.BoolSchema
        
            @staticmethod
            def answers() -> typing.Type['MeetingsListMeetingPollsResponsePollsItemQuestionsItemAnswers']:
                return MeetingsListMeetingPollsResponsePollsItemQuestionsItemAnswers
            case_sensitive = schemas.BoolSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def prompts() -> typing.Type['MeetingsListMeetingPollsResponsePollsItemQuestionsItemPrompts']:
                return MeetingsListMeetingPollsResponsePollsItemQuestionsItemPrompts
            rating_max_label = schemas.StrSchema
            
            
            class rating_max_value(
                schemas.IntSchema
            ):
                pass
            rating_min_label = schemas.StrSchema
            
            
            class rating_min_value(
                schemas.IntSchema
            ):
                pass
        
            @staticmethod
            def right_answers() -> typing.Type['MeetingsListMeetingPollsResponsePollsItemQuestionsItemRightAnswers']:
                return MeetingsListMeetingPollsResponsePollsItemQuestionsItemRightAnswers
            show_as_dropdown = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("single")
                
                @schemas.classproperty
                def MULTIPLE(cls):
                    return cls("multiple")
                
                @schemas.classproperty
                def MATCHING(cls):
                    return cls("matching")
                
                @schemas.classproperty
                def RANK_ORDER(cls):
                    return cls("rank_order")
                
                @schemas.classproperty
                def SHORT_ANSWER(cls):
                    return cls("short_answer")
                
                @schemas.classproperty
                def LONG_ANSWER(cls):
                    return cls("long_answer")
                
                @schemas.classproperty
                def FILL_IN_THE_BLANK(cls):
                    return cls("fill_in_the_blank")
                
                @schemas.classproperty
                def RATING_SCALE(cls):
                    return cls("rating_scale")
            __annotations__ = {
                "answer_max_character": answer_max_character,
                "answer_min_character": answer_min_character,
                "answer_required": answer_required,
                "answers": answers,
                "case_sensitive": case_sensitive,
                "name": name,
                "prompts": prompts,
                "rating_max_label": rating_max_label,
                "rating_max_value": rating_max_value,
                "rating_min_label": rating_min_label,
                "rating_min_value": rating_min_value,
                "right_answers": right_answers,
                "show_as_dropdown": show_as_dropdown,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_max_character"]) -> MetaOapg.properties.answer_max_character: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_min_character"]) -> MetaOapg.properties.answer_min_character: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_required"]) -> MetaOapg.properties.answer_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answers"]) -> 'MeetingsListMeetingPollsResponsePollsItemQuestionsItemAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["case_sensitive"]) -> MetaOapg.properties.case_sensitive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompts"]) -> 'MeetingsListMeetingPollsResponsePollsItemQuestionsItemPrompts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_max_label"]) -> MetaOapg.properties.rating_max_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_max_value"]) -> MetaOapg.properties.rating_max_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_min_label"]) -> MetaOapg.properties.rating_min_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_min_value"]) -> MetaOapg.properties.rating_min_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["right_answers"]) -> 'MeetingsListMeetingPollsResponsePollsItemQuestionsItemRightAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_as_dropdown"]) -> MetaOapg.properties.show_as_dropdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["answer_max_character", "answer_min_character", "answer_required", "answers", "case_sensitive", "name", "prompts", "rating_max_label", "rating_max_value", "rating_min_label", "rating_min_value", "right_answers", "show_as_dropdown", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_max_character"]) -> typing.Union[MetaOapg.properties.answer_max_character, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_min_character"]) -> typing.Union[MetaOapg.properties.answer_min_character, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_required"]) -> typing.Union[MetaOapg.properties.answer_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answers"]) -> typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["case_sensitive"]) -> typing.Union[MetaOapg.properties.case_sensitive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompts"]) -> typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemPrompts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_max_label"]) -> typing.Union[MetaOapg.properties.rating_max_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_max_value"]) -> typing.Union[MetaOapg.properties.rating_max_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_min_label"]) -> typing.Union[MetaOapg.properties.rating_min_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_min_value"]) -> typing.Union[MetaOapg.properties.rating_min_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["right_answers"]) -> typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemRightAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_as_dropdown"]) -> typing.Union[MetaOapg.properties.show_as_dropdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["answer_max_character", "answer_min_character", "answer_required", "answers", "case_sensitive", "name", "prompts", "rating_max_label", "rating_max_value", "rating_min_label", "rating_min_value", "right_answers", "show_as_dropdown", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        answer_max_character: typing.Union[MetaOapg.properties.answer_max_character, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        answer_min_character: typing.Union[MetaOapg.properties.answer_min_character, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        answer_required: typing.Union[MetaOapg.properties.answer_required, bool, schemas.Unset] = schemas.unset,
        answers: typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemAnswers', schemas.Unset] = schemas.unset,
        case_sensitive: typing.Union[MetaOapg.properties.case_sensitive, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        prompts: typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemPrompts', schemas.Unset] = schemas.unset,
        rating_max_label: typing.Union[MetaOapg.properties.rating_max_label, str, schemas.Unset] = schemas.unset,
        rating_max_value: typing.Union[MetaOapg.properties.rating_max_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rating_min_label: typing.Union[MetaOapg.properties.rating_min_label, str, schemas.Unset] = schemas.unset,
        rating_min_value: typing.Union[MetaOapg.properties.rating_min_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        right_answers: typing.Union['MeetingsListMeetingPollsResponsePollsItemQuestionsItemRightAnswers', schemas.Unset] = schemas.unset,
        show_as_dropdown: typing.Union[MetaOapg.properties.show_as_dropdown, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsListMeetingPollsResponsePollsItemQuestionsItem':
        return super().__new__(
            cls,
            *args,
            answer_max_character=answer_max_character,
            answer_min_character=answer_min_character,
            answer_required=answer_required,
            answers=answers,
            case_sensitive=case_sensitive,
            name=name,
            prompts=prompts,
            rating_max_label=rating_max_label,
            rating_max_value=rating_max_value,
            rating_min_label=rating_min_label,
            rating_min_value=rating_min_value,
            right_answers=right_answers,
            show_as_dropdown=show_as_dropdown,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_list_meeting_polls_response_polls_item_questions_item_answers import MeetingsListMeetingPollsResponsePollsItemQuestionsItemAnswers
from zoom_meeting_python_sdk.model.meetings_list_meeting_polls_response_polls_item_questions_item_prompts import MeetingsListMeetingPollsResponsePollsItemQuestionsItemPrompts
from zoom_meeting_python_sdk.model.meetings_list_meeting_polls_response_polls_item_questions_item_right_answers import MeetingsListMeetingPollsResponsePollsItemQuestionsItemRightAnswers
