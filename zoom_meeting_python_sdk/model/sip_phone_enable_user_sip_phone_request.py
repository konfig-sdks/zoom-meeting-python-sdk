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


class SipPhoneEnableUserSipPhoneRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "password",
            "user_email",
            "voice_mail",
            "user_name",
            "domain",
            "proxy_server",
            "register_server",
            "authorization_name",
        }
        
        class properties:
            
            
            class authorization_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
            class domain(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            password = schemas.StrSchema
            proxy_server = schemas.StrSchema
            register_server = schemas.StrSchema
            
            
            class user_email(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'email'
                    max_length = 64
            
            
            class user_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
            
            
            class voice_mail(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
            proxy_server2 = schemas.StrSchema
            proxy_server3 = schemas.StrSchema
            register_server2 = schemas.StrSchema
            register_server3 = schemas.StrSchema
            
            
            class registration_expire_time(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 127
                    inclusive_minimum = 1
            
            
            class transport_protocol(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UDP": "UDP",
                        "TCP": "TCP",
                        "TLS": "TLS",
                        "AUTO": "AUTO",
                    }
                
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
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UDP": "UDP",
                        "TCP": "TCP",
                        "TLS": "TLS",
                        "AUTO": "AUTO",
                    }
                
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
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UDP": "UDP",
                        "TCP": "TCP",
                        "TLS": "TLS",
                        "AUTO": "AUTO",
                    }
                
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
            __annotations__ = {
                "authorization_name": authorization_name,
                "domain": domain,
                "password": password,
                "proxy_server": proxy_server,
                "register_server": register_server,
                "user_email": user_email,
                "user_name": user_name,
                "voice_mail": voice_mail,
                "proxy_server2": proxy_server2,
                "proxy_server3": proxy_server3,
                "register_server2": register_server2,
                "register_server3": register_server3,
                "registration_expire_time": registration_expire_time,
                "transport_protocol": transport_protocol,
                "transport_protocol2": transport_protocol2,
                "transport_protocol3": transport_protocol3,
            }
    
    password: MetaOapg.properties.password
    user_email: MetaOapg.properties.user_email
    voice_mail: MetaOapg.properties.voice_mail
    user_name: MetaOapg.properties.user_name
    domain: MetaOapg.properties.domain
    proxy_server: MetaOapg.properties.proxy_server
    register_server: MetaOapg.properties.register_server
    authorization_name: MetaOapg.properties.authorization_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization_name"]) -> MetaOapg.properties.authorization_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy_server"]) -> MetaOapg.properties.proxy_server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["register_server"]) -> MetaOapg.properties.register_server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voice_mail"]) -> MetaOapg.properties.voice_mail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy_server2"]) -> MetaOapg.properties.proxy_server2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["proxy_server3"]) -> MetaOapg.properties.proxy_server3: ...
    
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authorization_name", "domain", "password", "proxy_server", "register_server", "user_email", "user_name", "voice_mail", "proxy_server2", "proxy_server3", "register_server2", "register_server3", "registration_expire_time", "transport_protocol", "transport_protocol2", "transport_protocol3", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization_name"]) -> MetaOapg.properties.authorization_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy_server"]) -> MetaOapg.properties.proxy_server: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["register_server"]) -> MetaOapg.properties.register_server: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_email"]) -> MetaOapg.properties.user_email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_name"]) -> MetaOapg.properties.user_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voice_mail"]) -> MetaOapg.properties.voice_mail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy_server2"]) -> typing.Union[MetaOapg.properties.proxy_server2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["proxy_server3"]) -> typing.Union[MetaOapg.properties.proxy_server3, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authorization_name", "domain", "password", "proxy_server", "register_server", "user_email", "user_name", "voice_mail", "proxy_server2", "proxy_server3", "register_server2", "register_server3", "registration_expire_time", "transport_protocol", "transport_protocol2", "transport_protocol3", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        password: typing.Union[MetaOapg.properties.password, str, ],
        user_email: typing.Union[MetaOapg.properties.user_email, str, ],
        voice_mail: typing.Union[MetaOapg.properties.voice_mail, str, ],
        user_name: typing.Union[MetaOapg.properties.user_name, str, ],
        domain: typing.Union[MetaOapg.properties.domain, str, ],
        proxy_server: typing.Union[MetaOapg.properties.proxy_server, str, ],
        register_server: typing.Union[MetaOapg.properties.register_server, str, ],
        authorization_name: typing.Union[MetaOapg.properties.authorization_name, str, ],
        proxy_server2: typing.Union[MetaOapg.properties.proxy_server2, str, schemas.Unset] = schemas.unset,
        proxy_server3: typing.Union[MetaOapg.properties.proxy_server3, str, schemas.Unset] = schemas.unset,
        register_server2: typing.Union[MetaOapg.properties.register_server2, str, schemas.Unset] = schemas.unset,
        register_server3: typing.Union[MetaOapg.properties.register_server3, str, schemas.Unset] = schemas.unset,
        registration_expire_time: typing.Union[MetaOapg.properties.registration_expire_time, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        transport_protocol: typing.Union[MetaOapg.properties.transport_protocol, str, schemas.Unset] = schemas.unset,
        transport_protocol2: typing.Union[MetaOapg.properties.transport_protocol2, str, schemas.Unset] = schemas.unset,
        transport_protocol3: typing.Union[MetaOapg.properties.transport_protocol3, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SipPhoneEnableUserSipPhoneRequest':
        return super().__new__(
            cls,
            *args,
            password=password,
            user_email=user_email,
            voice_mail=voice_mail,
            user_name=user_name,
            domain=domain,
            proxy_server=proxy_server,
            register_server=register_server,
            authorization_name=authorization_name,
            proxy_server2=proxy_server2,
            proxy_server3=proxy_server3,
            register_server2=register_server2,
            register_server3=register_server3,
            registration_expire_time=registration_expire_time,
            transport_protocol=transport_protocol,
            transport_protocol2=transport_protocol2,
            transport_protocol3=transport_protocol3,
            _configuration=_configuration,
            **kwargs,
        )
