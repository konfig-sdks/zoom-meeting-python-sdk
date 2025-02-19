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


class MeetingsUpdateRegistrationQuestionsRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Meeting Registrant Questions
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def custom_questions() -> typing.Type['MeetingsUpdateRegistrationQuestionsRequestCustomQuestions']:
                return MeetingsUpdateRegistrationQuestionsRequestCustomQuestions
        
            @staticmethod
            def questions() -> typing.Type['MeetingsUpdateRegistrationQuestionsRequestQuestions']:
                return MeetingsUpdateRegistrationQuestionsRequestQuestions
            __annotations__ = {
                "custom_questions": custom_questions,
                "questions": questions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_questions"]) -> 'MeetingsUpdateRegistrationQuestionsRequestCustomQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["questions"]) -> 'MeetingsUpdateRegistrationQuestionsRequestQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["custom_questions", "questions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_questions"]) -> typing.Union['MeetingsUpdateRegistrationQuestionsRequestCustomQuestions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["questions"]) -> typing.Union['MeetingsUpdateRegistrationQuestionsRequestQuestions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["custom_questions", "questions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        custom_questions: typing.Union['MeetingsUpdateRegistrationQuestionsRequestCustomQuestions', schemas.Unset] = schemas.unset,
        questions: typing.Union['MeetingsUpdateRegistrationQuestionsRequestQuestions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsUpdateRegistrationQuestionsRequest':
        return super().__new__(
            cls,
            *args,
            custom_questions=custom_questions,
            questions=questions,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_update_registration_questions_request_custom_questions import MeetingsUpdateRegistrationQuestionsRequestCustomQuestions
from zoom_meeting_python_sdk.model.meetings_update_registration_questions_request_questions import MeetingsUpdateRegistrationQuestionsRequestQuestions
