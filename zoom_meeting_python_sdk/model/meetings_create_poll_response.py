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


class MeetingsCreatePollResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about meeting and webinar polling.
    """


    class MetaOapg:
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            id = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "notstart": "NOTSTART",
                        "started": "STARTED",
                        "ended": "ENDED",
                        "sharing": "SHARING",
                    }
                
                @schemas.classproperty
                def NOTSTART(cls):
                    return cls("notstart")
                
                @schemas.classproperty
                def STARTED(cls):
                    return cls("started")
                
                @schemas.classproperty
                def ENDED(cls):
                    return cls("ended")
                
                @schemas.classproperty
                def SHARING(cls):
                    return cls("sharing")
            anonymous = schemas.BoolSchema
            
            
            class poll_type(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        1: "POSITIVE_1",
                        2: "POSITIVE_2",
                        3: "POSITIVE_3",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
        
            @staticmethod
            def questions() -> typing.Type['MeetingsCreatePollResponseQuestions']:
                return MeetingsCreatePollResponseQuestions
            __annotations__ = {
                "title": title,
                "id": id,
                "status": status,
                "anonymous": anonymous,
                "poll_type": poll_type,
                "questions": questions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anonymous"]) -> MetaOapg.properties.anonymous: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["poll_type"]) -> MetaOapg.properties.poll_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["questions"]) -> 'MeetingsCreatePollResponseQuestions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "status", "anonymous", "poll_type", "questions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anonymous"]) -> typing.Union[MetaOapg.properties.anonymous, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["poll_type"]) -> typing.Union[MetaOapg.properties.poll_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["questions"]) -> typing.Union['MeetingsCreatePollResponseQuestions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "status", "anonymous", "poll_type", "questions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        anonymous: typing.Union[MetaOapg.properties.anonymous, bool, schemas.Unset] = schemas.unset,
        poll_type: typing.Union[MetaOapg.properties.poll_type, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        questions: typing.Union['MeetingsCreatePollResponseQuestions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsCreatePollResponse':
        return super().__new__(
            cls,
            *args,
            title=title,
            id=id,
            status=status,
            anonymous=anonymous,
            poll_type=poll_type,
            questions=questions,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_create_poll_response_questions import MeetingsCreatePollResponseQuestions
