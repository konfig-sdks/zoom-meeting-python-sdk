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


class SipPhoneListResponsePhonesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            authorization_name = schemas.StrSchema
            domain = schemas.StrSchema
            id = schemas.StrSchema
            password = schemas.StrSchema
            proxy_server = schemas.StrSchema
            proxy_server2 = schemas.StrSchema
            proxy_server3 = schemas.StrSchema
            register_server = schemas.StrSchema
            register_server2 = schemas.StrSchema
            register_server3 = schemas.StrSchema
            registration_expire_time = schemas.IntSchema
            
            
            class transport_protocol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UDP(cls):
                    return cls("UDP")
                
                @schemas.classproperty
                def TCP(cls):
                    return cls("TCP")
                
                @schemas.classproperty
                def TLS(cls):
                    return cls("TLS")
                
                @schemas.classproperty
                def AUTO(cls):
                    return cls("AUTO")
            
            
            class transport_protocol2(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UDP(cls):
                    return cls("UDP")
                
                @schemas.classproperty
                def TCP(cls):
                    return cls("TCP")
                
                @schemas.classproperty
                def TLS(cls):
                    return cls("TLS")
                
                @schemas.classproperty
                def AUTO(cls):
                    return cls("AUTO")
            
            
            class transport_protocol3(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UDP(cls):
                    return cls("UDP")
                
                @schemas.classproperty
                def TCP(cls):
                    return cls("TCP")
                
                @schemas.classproperty
                def TLS(cls):
                    return cls("TLS")
                
                @schemas.classproperty
                def AUTO(cls):
                    return cls("AUTO")
            user_email = schemas.StrSchema
            user_name = schemas.StrSchema
            voice_mail = schemas.StrSchema
            __annotations__ = {
                "authorization_name": authorization_name,
                "domain": domain,
                "id": id,
                "password": password,
                "proxy_server": proxy_server,
                "proxy_server2": proxy_server2,
                "proxy_server3": proxy_server3,
                "register_server": register_server,
                "register_server2": register_server2,
                "register_server3": register_server3,
                "registration_expire_time": registration_expire_time,
                "transport_protocol": transport_protocol,
                "transport_protocol2": transport_protocol2,
                "transport_protocol3": transport_protocol3,
                "user_email": user_email,
                "user_name": user_name,
                "voice_mail": voice_mail,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization_name"]) -> MetaOapg.properties.authorization_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy_server"]) -> MetaOapg.properties.proxy_server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy_server2"]) -> MetaOapg.properties.proxy_server2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy_server3"]) -> MetaOapg.properties.proxy_server3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["register_server"]) -> MetaOapg.properties.register_server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["register_server2"]) -> MetaOapg.properties.register_server2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["register_server3"]) -> MetaOapg.properties.register_server3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registration_expire_time"]) -> MetaOapg.properties.registration_expire_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transport_protocol"]) -> MetaOapg.properties.transport_protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transport_protocol2"]) -> MetaOapg.properties.transport_protocol2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transport_protocol3"]) -> MetaOapg.properties.transport_protocol3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_mail"]) -> MetaOapg.properties.voice_mail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authorization_name", "domain", "id", "password", "proxy_server", "proxy_server2", "proxy_server3", "register_server", "register_server2", "register_server3", "registration_expire_time", "transport_protocol", "transport_protocol2", "transport_protocol3", "user_email", "user_name", "voice_mail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization_name"]) -> typing.Union[MetaOapg.properties.authorization_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union[MetaOapg.properties.domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy_server"]) -> typing.Union[MetaOapg.properties.proxy_server, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy_server2"]) -> typing.Union[MetaOapg.properties.proxy_server2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy_server3"]) -> typing.Union[MetaOapg.properties.proxy_server3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["register_server"]) -> typing.Union[MetaOapg.properties.register_server, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["register_server2"]) -> typing.Union[MetaOapg.properties.register_server2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["register_server3"]) -> typing.Union[MetaOapg.properties.register_server3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registration_expire_time"]) -> typing.Union[MetaOapg.properties.registration_expire_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transport_protocol"]) -> typing.Union[MetaOapg.properties.transport_protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transport_protocol2"]) -> typing.Union[MetaOapg.properties.transport_protocol2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transport_protocol3"]) -> typing.Union[MetaOapg.properties.transport_protocol3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_email"]) -> typing.Union[MetaOapg.properties.user_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_name"]) -> typing.Union[MetaOapg.properties.user_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_mail"]) -> typing.Union[MetaOapg.properties.voice_mail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authorization_name", "domain", "id", "password", "proxy_server", "proxy_server2", "proxy_server3", "register_server", "register_server2", "register_server3", "registration_expire_time", "transport_protocol", "transport_protocol2", "transport_protocol3", "user_email", "user_name", "voice_mail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        authorization_name: typing.Union[MetaOapg.properties.authorization_name, str, schemas.Unset] = schemas.unset,
        domain: typing.Union[MetaOapg.properties.domain, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        proxy_server: typing.Union[MetaOapg.properties.proxy_server, str, schemas.Unset] = schemas.unset,
        proxy_server2: typing.Union[MetaOapg.properties.proxy_server2, str, schemas.Unset] = schemas.unset,
        proxy_server3: typing.Union[MetaOapg.properties.proxy_server3, str, schemas.Unset] = schemas.unset,
        register_server: typing.Union[MetaOapg.properties.register_server, str, schemas.Unset] = schemas.unset,
        register_server2: typing.Union[MetaOapg.properties.register_server2, str, schemas.Unset] = schemas.unset,
        register_server3: typing.Union[MetaOapg.properties.register_server3, str, schemas.Unset] = schemas.unset,
        registration_expire_time: typing.Union[MetaOapg.properties.registration_expire_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transport_protocol: typing.Union[MetaOapg.properties.transport_protocol, str, schemas.Unset] = schemas.unset,
        transport_protocol2: typing.Union[MetaOapg.properties.transport_protocol2, str, schemas.Unset] = schemas.unset,
        transport_protocol3: typing.Union[MetaOapg.properties.transport_protocol3, str, schemas.Unset] = schemas.unset,
        user_email: typing.Union[MetaOapg.properties.user_email, str, schemas.Unset] = schemas.unset,
        user_name: typing.Union[MetaOapg.properties.user_name, str, schemas.Unset] = schemas.unset,
        voice_mail: typing.Union[MetaOapg.properties.voice_mail, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SipPhoneListResponsePhonesItem':
        return super().__new__(
            cls,
            *args,
            authorization_name=authorization_name,
            domain=domain,
            id=id,
            password=password,
            proxy_server=proxy_server,
            proxy_server2=proxy_server2,
            proxy_server3=proxy_server3,
            register_server=register_server,
            register_server2=register_server2,
            register_server3=register_server3,
            registration_expire_time=registration_expire_time,
            transport_protocol=transport_protocol,
            transport_protocol2=transport_protocol2,
            transport_protocol3=transport_protocol3,
            user_email=user_email,
            user_name=user_name,
            voice_mail=voice_mail,
            _configuration=_configuration,
            **kwargs,
        )
