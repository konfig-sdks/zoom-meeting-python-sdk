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


class MeetingsUpdateSurveyRequestCustomSurvey(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the customized meeting survey.
    """


    class MetaOapg:
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
                pass
            anonymous = schemas.BoolSchema
            numbered_questions = schemas.BoolSchema
            show_question_type = schemas.BoolSchema
            
            
            class feedback(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def questions() -> typing.Type['MeetingsUpdateSurveyRequestCustomSurveyQuestions']:
                return MeetingsUpdateSurveyRequestCustomSurveyQuestions
            __annotations__ = {
                "title": title,
                "anonymous": anonymous,
                "numbered_questions": numbered_questions,
                "show_question_type": show_question_type,
                "feedback": feedback,
                "questions": questions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anonymous"]) -> MetaOapg.properties.anonymous: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numbered_questions"]) -> MetaOapg.properties.numbered_questions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_question_type"]) -> MetaOapg.properties.show_question_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feedback"]) -> MetaOapg.properties.feedback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["questions"]) -> 'MeetingsUpdateSurveyRequestCustomSurveyQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "anonymous", "numbered_questions", "show_question_type", "feedback", "questions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anonymous"]) -> typing.Union[MetaOapg.properties.anonymous, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numbered_questions"]) -> typing.Union[MetaOapg.properties.numbered_questions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_question_type"]) -> typing.Union[MetaOapg.properties.show_question_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feedback"]) -> typing.Union[MetaOapg.properties.feedback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["questions"]) -> typing.Union['MeetingsUpdateSurveyRequestCustomSurveyQuestions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "anonymous", "numbered_questions", "show_question_type", "feedback", "questions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        anonymous: typing.Union[MetaOapg.properties.anonymous, bool, schemas.Unset] = schemas.unset,
        numbered_questions: typing.Union[MetaOapg.properties.numbered_questions, bool, schemas.Unset] = schemas.unset,
        show_question_type: typing.Union[MetaOapg.properties.show_question_type, bool, schemas.Unset] = schemas.unset,
        feedback: typing.Union[MetaOapg.properties.feedback, str, schemas.Unset] = schemas.unset,
        questions: typing.Union['MeetingsUpdateSurveyRequestCustomSurveyQuestions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsUpdateSurveyRequestCustomSurvey':
        return super().__new__(
            cls,
            *args,
            title=title,
            anonymous=anonymous,
            numbered_questions=numbered_questions,
            show_question_type=show_question_type,
            feedback=feedback,
            questions=questions,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_update_survey_request_custom_survey_questions import MeetingsUpdateSurveyRequestCustomSurveyQuestions
