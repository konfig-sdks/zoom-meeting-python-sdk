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


class WebinarsGetSurveyResponseCustomSurveyQuestionsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            
            
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
            answer_required = schemas.BoolSchema
            show_as_dropdown = schemas.BoolSchema
        
            @staticmethod
            def answers() -> typing.Type['WebinarsGetSurveyResponseCustomSurveyQuestionsItemAnswers']:
                return WebinarsGetSurveyResponseCustomSurveyQuestionsItemAnswers
        
            @staticmethod
            def prompts() -> typing.Type['WebinarsGetSurveyResponseCustomSurveyQuestionsItemPrompts']:
                return WebinarsGetSurveyResponseCustomSurveyQuestionsItemPrompts
            
            
            class answer_min_character(
                schemas.IntSchema
            ):
                pass
            answer_max_character = schemas.IntSchema
            
            
            class rating_min_value(
                schemas.IntSchema
            ):
                pass
            
            
            class rating_max_value(
                schemas.IntSchema
            ):
                pass
            
            
            class rating_min_label(
                schemas.StrSchema
            ):
                pass
            
            
            class rating_max_label(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "type": type,
                "answer_required": answer_required,
                "show_as_dropdown": show_as_dropdown,
                "answers": answers,
                "prompts": prompts,
                "answer_min_character": answer_min_character,
                "answer_max_character": answer_max_character,
                "rating_min_value": rating_min_value,
                "rating_max_value": rating_max_value,
                "rating_min_label": rating_min_label,
                "rating_max_label": rating_max_label,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_required"]) -> MetaOapg.properties.answer_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_as_dropdown"]) -> MetaOapg.properties.show_as_dropdown: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answers"]) -> 'WebinarsGetSurveyResponseCustomSurveyQuestionsItemAnswers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompts"]) -> 'WebinarsGetSurveyResponseCustomSurveyQuestionsItemPrompts': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_min_character"]) -> MetaOapg.properties.answer_min_character: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_max_character"]) -> MetaOapg.properties.answer_max_character: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_min_value"]) -> MetaOapg.properties.rating_min_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_max_value"]) -> MetaOapg.properties.rating_max_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_min_label"]) -> MetaOapg.properties.rating_min_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rating_max_label"]) -> MetaOapg.properties.rating_max_label: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "type", "answer_required", "show_as_dropdown", "answers", "prompts", "answer_min_character", "answer_max_character", "rating_min_value", "rating_max_value", "rating_min_label", "rating_max_label", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_required"]) -> typing.Union[MetaOapg.properties.answer_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_as_dropdown"]) -> typing.Union[MetaOapg.properties.show_as_dropdown, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answers"]) -> typing.Union['WebinarsGetSurveyResponseCustomSurveyQuestionsItemAnswers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompts"]) -> typing.Union['WebinarsGetSurveyResponseCustomSurveyQuestionsItemPrompts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_min_character"]) -> typing.Union[MetaOapg.properties.answer_min_character, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_max_character"]) -> typing.Union[MetaOapg.properties.answer_max_character, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_min_value"]) -> typing.Union[MetaOapg.properties.rating_min_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_max_value"]) -> typing.Union[MetaOapg.properties.rating_max_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_min_label"]) -> typing.Union[MetaOapg.properties.rating_min_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rating_max_label"]) -> typing.Union[MetaOapg.properties.rating_max_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "type", "answer_required", "show_as_dropdown", "answers", "prompts", "answer_min_character", "answer_max_character", "rating_min_value", "rating_max_value", "rating_min_label", "rating_max_label", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        answer_required: typing.Union[MetaOapg.properties.answer_required, bool, schemas.Unset] = schemas.unset,
        show_as_dropdown: typing.Union[MetaOapg.properties.show_as_dropdown, bool, schemas.Unset] = schemas.unset,
        answers: typing.Union['WebinarsGetSurveyResponseCustomSurveyQuestionsItemAnswers', schemas.Unset] = schemas.unset,
        prompts: typing.Union['WebinarsGetSurveyResponseCustomSurveyQuestionsItemPrompts', schemas.Unset] = schemas.unset,
        answer_min_character: typing.Union[MetaOapg.properties.answer_min_character, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        answer_max_character: typing.Union[MetaOapg.properties.answer_max_character, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rating_min_value: typing.Union[MetaOapg.properties.rating_min_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rating_max_value: typing.Union[MetaOapg.properties.rating_max_value, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rating_min_label: typing.Union[MetaOapg.properties.rating_min_label, str, schemas.Unset] = schemas.unset,
        rating_max_label: typing.Union[MetaOapg.properties.rating_max_label, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsGetSurveyResponseCustomSurveyQuestionsItem':
        return super().__new__(
            cls,
            *args,
            name=name,
            type=type,
            answer_required=answer_required,
            show_as_dropdown=show_as_dropdown,
            answers=answers,
            prompts=prompts,
            answer_min_character=answer_min_character,
            answer_max_character=answer_max_character,
            rating_min_value=rating_min_value,
            rating_max_value=rating_max_value,
            rating_min_label=rating_min_label,
            rating_max_label=rating_max_label,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.webinars_get_survey_response_custom_survey_questions_item_answers import WebinarsGetSurveyResponseCustomSurveyQuestionsItemAnswers
from zoom_meeting_python_sdk.model.webinars_get_survey_response_custom_survey_questions_item_prompts import WebinarsGetSurveyResponseCustomSurveyQuestionsItemPrompts
