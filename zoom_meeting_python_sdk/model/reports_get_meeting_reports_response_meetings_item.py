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


class ReportsGetMeetingReportsResponseMeetingsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def custom_keys() -> typing.Type['ReportsGetMeetingReportsResponseMeetingsItemCustomKeys']:
                return ReportsGetMeetingReportsResponseMeetingsItemCustomKeys
            duration = schemas.IntSchema
            end_time = schemas.DateTimeSchema
            id = schemas.IntSchema
            participants_count = schemas.IntSchema
            session_key = schemas.StrSchema
            source = schemas.StrSchema
            start_time = schemas.DateTimeSchema
            topic = schemas.StrSchema
            total_minutes = schemas.IntSchema
            
            
            class type(
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
                        8: "POSITIVE_8",
                        9: "POSITIVE_9",
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
                
                @schemas.classproperty
                def POSITIVE_8(cls):
                    return cls(8)
                
                @schemas.classproperty
                def POSITIVE_9(cls):
                    return cls(9)
            user_email = schemas.StrSchema
            user_name = schemas.StrSchema
            uuid = schemas.StrSchema
            schedule_time = schemas.StrSchema
            join_waiting_room_time = schemas.StrSchema
            join_time = schemas.StrSchema
            leave_time = schemas.StrSchema
            host_organization = schemas.StrSchema
            host_name = schemas.StrSchema
            has_screen_share = schemas.BoolSchema
            has_recording = schemas.BoolSchema
            has_chat = schemas.BoolSchema
            
            
            class meeting_encryption_status(
                schemas.EnumBase,
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        1: "POSITIVE_1",
                        2: "POSITIVE_2",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def POSITIVE_2(cls):
                    return cls(2)
            participants_count_my_account = schemas.IntSchema
            __annotations__ = {
                "custom_keys": custom_keys,
                "duration": duration,
                "end_time": end_time,
                "id": id,
                "participants_count": participants_count,
                "session_key": session_key,
                "source": source,
                "start_time": start_time,
                "topic": topic,
                "total_minutes": total_minutes,
                "type": type,
                "user_email": user_email,
                "user_name": user_name,
                "uuid": uuid,
                "schedule_time": schedule_time,
                "join_waiting_room_time": join_waiting_room_time,
                "join_time": join_time,
                "leave_time": leave_time,
                "host_organization": host_organization,
                "host_name": host_name,
                "has_screen_share": has_screen_share,
                "has_recording": has_recording,
                "has_chat": has_chat,
                "meeting_encryption_status": meeting_encryption_status,
                "participants_count_my_account": participants_count_my_account,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_keys"]) -> 'ReportsGetMeetingReportsResponseMeetingsItemCustomKeys': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participants_count"]) -> MetaOapg.properties.participants_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_key"]) -> MetaOapg.properties.session_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic"]) -> MetaOapg.properties.topic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_minutes"]) -> MetaOapg.properties.total_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule_time"]) -> MetaOapg.properties.schedule_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["join_waiting_room_time"]) -> MetaOapg.properties.join_waiting_room_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["join_time"]) -> MetaOapg.properties.join_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leave_time"]) -> MetaOapg.properties.leave_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_organization"]) -> MetaOapg.properties.host_organization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host_name"]) -> MetaOapg.properties.host_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_screen_share"]) -> MetaOapg.properties.has_screen_share: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_recording"]) -> MetaOapg.properties.has_recording: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_chat"]) -> MetaOapg.properties.has_chat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meeting_encryption_status"]) -> MetaOapg.properties.meeting_encryption_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participants_count_my_account"]) -> MetaOapg.properties.participants_count_my_account: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["custom_keys", "duration", "end_time", "id", "participants_count", "session_key", "source", "start_time", "topic", "total_minutes", "type", "user_email", "user_name", "uuid", "schedule_time", "join_waiting_room_time", "join_time", "leave_time", "host_organization", "host_name", "has_screen_share", "has_recording", "has_chat", "meeting_encryption_status", "participants_count_my_account", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_keys"]) -> typing.Union['ReportsGetMeetingReportsResponseMeetingsItemCustomKeys', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> typing.Union[MetaOapg.properties.end_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participants_count"]) -> typing.Union[MetaOapg.properties.participants_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_key"]) -> typing.Union[MetaOapg.properties.session_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic"]) -> typing.Union[MetaOapg.properties.topic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_minutes"]) -> typing.Union[MetaOapg.properties.total_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_email"]) -> typing.Union[MetaOapg.properties.user_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_name"]) -> typing.Union[MetaOapg.properties.user_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule_time"]) -> typing.Union[MetaOapg.properties.schedule_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["join_waiting_room_time"]) -> typing.Union[MetaOapg.properties.join_waiting_room_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["join_time"]) -> typing.Union[MetaOapg.properties.join_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leave_time"]) -> typing.Union[MetaOapg.properties.leave_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_organization"]) -> typing.Union[MetaOapg.properties.host_organization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host_name"]) -> typing.Union[MetaOapg.properties.host_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_screen_share"]) -> typing.Union[MetaOapg.properties.has_screen_share, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_recording"]) -> typing.Union[MetaOapg.properties.has_recording, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_chat"]) -> typing.Union[MetaOapg.properties.has_chat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meeting_encryption_status"]) -> typing.Union[MetaOapg.properties.meeting_encryption_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participants_count_my_account"]) -> typing.Union[MetaOapg.properties.participants_count_my_account, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["custom_keys", "duration", "end_time", "id", "participants_count", "session_key", "source", "start_time", "topic", "total_minutes", "type", "user_email", "user_name", "uuid", "schedule_time", "join_waiting_room_time", "join_time", "leave_time", "host_organization", "host_name", "has_screen_share", "has_recording", "has_chat", "meeting_encryption_status", "participants_count_my_account", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        custom_keys: typing.Union['ReportsGetMeetingReportsResponseMeetingsItemCustomKeys', schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        end_time: typing.Union[MetaOapg.properties.end_time, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        participants_count: typing.Union[MetaOapg.properties.participants_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        session_key: typing.Union[MetaOapg.properties.session_key, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        topic: typing.Union[MetaOapg.properties.topic, str, schemas.Unset] = schemas.unset,
        total_minutes: typing.Union[MetaOapg.properties.total_minutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user_email: typing.Union[MetaOapg.properties.user_email, str, schemas.Unset] = schemas.unset,
        user_name: typing.Union[MetaOapg.properties.user_name, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        schedule_time: typing.Union[MetaOapg.properties.schedule_time, str, schemas.Unset] = schemas.unset,
        join_waiting_room_time: typing.Union[MetaOapg.properties.join_waiting_room_time, str, schemas.Unset] = schemas.unset,
        join_time: typing.Union[MetaOapg.properties.join_time, str, schemas.Unset] = schemas.unset,
        leave_time: typing.Union[MetaOapg.properties.leave_time, str, schemas.Unset] = schemas.unset,
        host_organization: typing.Union[MetaOapg.properties.host_organization, str, schemas.Unset] = schemas.unset,
        host_name: typing.Union[MetaOapg.properties.host_name, str, schemas.Unset] = schemas.unset,
        has_screen_share: typing.Union[MetaOapg.properties.has_screen_share, bool, schemas.Unset] = schemas.unset,
        has_recording: typing.Union[MetaOapg.properties.has_recording, bool, schemas.Unset] = schemas.unset,
        has_chat: typing.Union[MetaOapg.properties.has_chat, bool, schemas.Unset] = schemas.unset,
        meeting_encryption_status: typing.Union[MetaOapg.properties.meeting_encryption_status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        participants_count_my_account: typing.Union[MetaOapg.properties.participants_count_my_account, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReportsGetMeetingReportsResponseMeetingsItem':
        return super().__new__(
            cls,
            *args,
            custom_keys=custom_keys,
            duration=duration,
            end_time=end_time,
            id=id,
            participants_count=participants_count,
            session_key=session_key,
            source=source,
            start_time=start_time,
            topic=topic,
            total_minutes=total_minutes,
            type=type,
            user_email=user_email,
            user_name=user_name,
            uuid=uuid,
            schedule_time=schedule_time,
            join_waiting_room_time=join_waiting_room_time,
            join_time=join_time,
            leave_time=leave_time,
            host_organization=host_organization,
            host_name=host_name,
            has_screen_share=has_screen_share,
            has_recording=has_recording,
            has_chat=has_chat,
            meeting_encryption_status=meeting_encryption_status,
            participants_count_my_account=participants_count_my_account,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.reports_get_meeting_reports_response_meetings_item_custom_keys import ReportsGetMeetingReportsResponseMeetingsItemCustomKeys
