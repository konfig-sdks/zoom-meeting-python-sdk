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


class WebinarsUpdateScheduledWebinarRequestSettingsQuestionAndAnswer(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Using-Q-A-as-the-webinar-host#:~:text=Overview,and%20upvote%20each%20other's%20questions.) for webinar.
    """


    class MetaOapg:
        
        class properties:
            allow_submit_questions = schemas.BoolSchema
            allow_anonymous_questions = schemas.BoolSchema
            
            
            class answer_questions(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "only": "ONLY",
                        "all": "ALL",
                    }
                
                @schemas.classproperty
                def ONLY(cls):
                    return cls("only")
                
                @schemas.classproperty
                def ALL(cls):
                    return cls("all")
            attendees_can_comment = schemas.BoolSchema
            attendees_can_upvote = schemas.BoolSchema
            allow_auto_reply = schemas.BoolSchema
            auto_reply_text = schemas.StrSchema
            enable = schemas.BoolSchema
            __annotations__ = {
                "allow_submit_questions": allow_submit_questions,
                "allow_anonymous_questions": allow_anonymous_questions,
                "answer_questions": answer_questions,
                "attendees_can_comment": attendees_can_comment,
                "attendees_can_upvote": attendees_can_upvote,
                "allow_auto_reply": allow_auto_reply,
                "auto_reply_text": auto_reply_text,
                "enable": enable,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_submit_questions"]) -> MetaOapg.properties.allow_submit_questions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_anonymous_questions"]) -> MetaOapg.properties.allow_anonymous_questions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["answer_questions"]) -> MetaOapg.properties.answer_questions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendees_can_comment"]) -> MetaOapg.properties.attendees_can_comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attendees_can_upvote"]) -> MetaOapg.properties.attendees_can_upvote: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allow_auto_reply"]) -> MetaOapg.properties.allow_auto_reply: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_reply_text"]) -> MetaOapg.properties.auto_reply_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable"]) -> MetaOapg.properties.enable: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allow_submit_questions", "allow_anonymous_questions", "answer_questions", "attendees_can_comment", "attendees_can_upvote", "allow_auto_reply", "auto_reply_text", "enable", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_submit_questions"]) -> typing.Union[MetaOapg.properties.allow_submit_questions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_anonymous_questions"]) -> typing.Union[MetaOapg.properties.allow_anonymous_questions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["answer_questions"]) -> typing.Union[MetaOapg.properties.answer_questions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendees_can_comment"]) -> typing.Union[MetaOapg.properties.attendees_can_comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attendees_can_upvote"]) -> typing.Union[MetaOapg.properties.attendees_can_upvote, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allow_auto_reply"]) -> typing.Union[MetaOapg.properties.allow_auto_reply, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_reply_text"]) -> typing.Union[MetaOapg.properties.auto_reply_text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable"]) -> typing.Union[MetaOapg.properties.enable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allow_submit_questions", "allow_anonymous_questions", "answer_questions", "attendees_can_comment", "attendees_can_upvote", "allow_auto_reply", "auto_reply_text", "enable", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        allow_submit_questions: typing.Union[MetaOapg.properties.allow_submit_questions, bool, schemas.Unset] = schemas.unset,
        allow_anonymous_questions: typing.Union[MetaOapg.properties.allow_anonymous_questions, bool, schemas.Unset] = schemas.unset,
        answer_questions: typing.Union[MetaOapg.properties.answer_questions, str, schemas.Unset] = schemas.unset,
        attendees_can_comment: typing.Union[MetaOapg.properties.attendees_can_comment, bool, schemas.Unset] = schemas.unset,
        attendees_can_upvote: typing.Union[MetaOapg.properties.attendees_can_upvote, bool, schemas.Unset] = schemas.unset,
        allow_auto_reply: typing.Union[MetaOapg.properties.allow_auto_reply, bool, schemas.Unset] = schemas.unset,
        auto_reply_text: typing.Union[MetaOapg.properties.auto_reply_text, str, schemas.Unset] = schemas.unset,
        enable: typing.Union[MetaOapg.properties.enable, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsUpdateScheduledWebinarRequestSettingsQuestionAndAnswer':
        return super().__new__(
            cls,
            *args,
            allow_submit_questions=allow_submit_questions,
            allow_anonymous_questions=allow_anonymous_questions,
            answer_questions=answer_questions,
            attendees_can_comment=attendees_can_comment,
            attendees_can_upvote=attendees_can_upvote,
            allow_auto_reply=allow_auto_reply,
            auto_reply_text=auto_reply_text,
            enable=enable,
            _configuration=_configuration,
            **kwargs,
        )
