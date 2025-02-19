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


class ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            answer = schemas.StrSchema
            question = schemas.StrSchema
            question_id = schemas.StrSchema
            create_time = schemas.StrSchema
        
            @staticmethod
            def answer_details() -> typing.Type['ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails']:
                return ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails
            __annotations__ = {
                "answer": answer,
                "question": question,
                "question_id": question_id,
                "create_time": create_time,
                "answer_details": answer_details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer"]) -> MetaOapg.properties.answer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question"]) -> MetaOapg.properties.question: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["question_id"]) -> MetaOapg.properties.question_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_details"]) -> 'ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["answer", "question", "question_id", "create_time", "answer_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer"]) -> typing.Union[MetaOapg.properties.answer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question"]) -> typing.Union[MetaOapg.properties.question, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["question_id"]) -> typing.Union[MetaOapg.properties.question_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> typing.Union[MetaOapg.properties.create_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_details"]) -> typing.Union['ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["answer", "question", "question_id", "create_time", "answer_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        answer: typing.Union[MetaOapg.properties.answer, str, schemas.Unset] = schemas.unset,
        question: typing.Union[MetaOapg.properties.question, str, schemas.Unset] = schemas.unset,
        question_id: typing.Union[MetaOapg.properties.question_id, str, schemas.Unset] = schemas.unset,
        create_time: typing.Union[MetaOapg.properties.create_time, str, schemas.Unset] = schemas.unset,
        answer_details: typing.Union['ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItem':
        return super().__new__(
            cls,
            *args,
            answer=answer,
            question=question,
            question_id=question_id,
            create_time=create_time,
            answer_details=answer_details,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.reports_get_webinar_qa_report_response_questions_item_question_details_item_answer_details import ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails
