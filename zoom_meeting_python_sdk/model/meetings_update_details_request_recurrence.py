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


class MeetingsUpdateDetailsRequestRecurrence(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Recurrence object. Use this object only for a meeting with type `8`, a recurring meeting with fixed time. 
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
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
            end_date_time = schemas.DateTimeSchema
            
            
            class end_times(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 60
            monthly_day = schemas.IntSchema
            
            
            class monthly_week(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        -1: "NEGATIVE_1",
                        1: "POSITIVE_1",
                        2: "POSITIVE_2",
                        3: "POSITIVE_3",
                        4: "POSITIVE_4",
                    }
                
                @schemas.classproperty
                def NEGATIVE_1(cls):
                    return cls(-1)
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
            
            
            class monthly_week_day(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        1: "POSITIVE_1",
                        2: "POSITIVE_2",
                        3: "POSITIVE_3",
                        4: "POSITIVE_4",
                        5: "POSITIVE_5",
                        6: "POSITIVE_6",
                        7: "POSITIVE_7",
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
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls(4)
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls(5)
                
                @schemas.classproperty
                def POSITIVE_6(cls):
                    return cls(6)
                
                @schemas.classproperty
                def POSITIVE_7(cls):
                    return cls(7)
            repeat_interval = schemas.IntSchema
            
            
            class weekly_days(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "1": "POSITIVE_1",
                        "2": "POSITIVE_2",
                        "3": "POSITIVE_3",
                        "4": "POSITIVE_4",
                        "5": "POSITIVE_5",
                        "6": "POSITIVE_6",
                        "7": "POSITIVE_7",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls("1")
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls("2")
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls("3")
                
                @schemas.classproperty
                def POSITIVE_4(cls):
                    return cls("4")
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls("5")
                
                @schemas.classproperty
                def POSITIVE_6(cls):
                    return cls("6")
                
                @schemas.classproperty
                def POSITIVE_7(cls):
                    return cls("7")
            __annotations__ = {
                "type": type,
                "end_date_time": end_date_time,
                "end_times": end_times,
                "monthly_day": monthly_day,
                "monthly_week": monthly_week,
                "monthly_week_day": monthly_week_day,
                "repeat_interval": repeat_interval,
                "weekly_days": weekly_days,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date_time"]) -> MetaOapg.properties.end_date_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_times"]) -> MetaOapg.properties.end_times: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthly_day"]) -> MetaOapg.properties.monthly_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthly_week"]) -> MetaOapg.properties.monthly_week: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["monthly_week_day"]) -> MetaOapg.properties.monthly_week_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repeat_interval"]) -> MetaOapg.properties.repeat_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weekly_days"]) -> MetaOapg.properties.weekly_days: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "end_date_time", "end_times", "monthly_day", "monthly_week", "monthly_week_day", "repeat_interval", "weekly_days", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date_time"]) -> typing.Union[MetaOapg.properties.end_date_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_times"]) -> typing.Union[MetaOapg.properties.end_times, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthly_day"]) -> typing.Union[MetaOapg.properties.monthly_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthly_week"]) -> typing.Union[MetaOapg.properties.monthly_week, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["monthly_week_day"]) -> typing.Union[MetaOapg.properties.monthly_week_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repeat_interval"]) -> typing.Union[MetaOapg.properties.repeat_interval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weekly_days"]) -> typing.Union[MetaOapg.properties.weekly_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "end_date_time", "end_times", "monthly_day", "monthly_week", "monthly_week_day", "repeat_interval", "weekly_days", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, decimal.Decimal, int, ],
        end_date_time: typing.Union[MetaOapg.properties.end_date_time, str, datetime, schemas.Unset] = schemas.unset,
        end_times: typing.Union[MetaOapg.properties.end_times, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        monthly_day: typing.Union[MetaOapg.properties.monthly_day, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        monthly_week: typing.Union[MetaOapg.properties.monthly_week, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        monthly_week_day: typing.Union[MetaOapg.properties.monthly_week_day, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        repeat_interval: typing.Union[MetaOapg.properties.repeat_interval, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        weekly_days: typing.Union[MetaOapg.properties.weekly_days, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsUpdateDetailsRequestRecurrence':
        return super().__new__(
            cls,
            *args,
            type=type,
            end_date_time=end_date_time,
            end_times=end_times,
            monthly_day=monthly_day,
            monthly_week=monthly_week,
            monthly_week_day=monthly_week_day,
            repeat_interval=repeat_interval,
            weekly_days=weekly_days,
            _configuration=_configuration,
            **kwargs,
        )
