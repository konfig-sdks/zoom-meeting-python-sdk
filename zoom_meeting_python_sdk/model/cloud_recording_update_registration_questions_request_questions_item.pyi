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


class CloudRecordingUpdateRegistrationQuestionsRequestQuestionsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class field_name(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LAST_NAME(cls):
                    return cls("last_name")
                
                @schemas.classproperty
                def ADDRESS(cls):
                    return cls("address")
                
                @schemas.classproperty
                def CITY(cls):
                    return cls("city")
                
                @schemas.classproperty
                def COUNTRY(cls):
                    return cls("country")
                
                @schemas.classproperty
                def ZIP(cls):
                    return cls("zip")
                
                @schemas.classproperty
                def STATE(cls):
                    return cls("state")
                
                @schemas.classproperty
                def PHONE(cls):
                    return cls("phone")
                
                @schemas.classproperty
                def INDUSTRY(cls):
                    return cls("industry")
                
                @schemas.classproperty
                def ORG(cls):
                    return cls("org")
                
                @schemas.classproperty
                def JOB_TITLE(cls):
                    return cls("job_title")
                
                @schemas.classproperty
                def PURCHASING_TIME_FRAME(cls):
                    return cls("purchasing_time_frame")
                
                @schemas.classproperty
                def ROLE_IN_PURCHASE_PROCESS(cls):
                    return cls("role_in_purchase_process")
                
                @schemas.classproperty
                def NO_OF_EMPLOYEES(cls):
                    return cls("no_of_employees")
                
                @schemas.classproperty
                def COMMENTS(cls):
                    return cls("comments")
            required = schemas.BoolSchema
            __annotations__ = {
                "field_name": field_name,
                "required": required,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_name"]) -> MetaOapg.properties.field_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field_name", "required", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_name"]) -> typing.Union[MetaOapg.properties.field_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field_name", "required", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field_name: typing.Union[MetaOapg.properties.field_name, str, schemas.Unset] = schemas.unset,
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CloudRecordingUpdateRegistrationQuestionsRequestQuestionsItem':
        return super().__new__(
            cls,
            *args,
            field_name=field_name,
            required=required,
            _configuration=_configuration,
            **kwargs,
        )
