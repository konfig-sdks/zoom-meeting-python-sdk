# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class SipPhoneEnableUserSipPhoneResponse(BaseModel):
    # The SIP phone ID.
    id: typing.Optional[str] = Field(None, alias='id')

    # The authorization name of the user that is registered for SIP phone.
    authorization_name: typing.Optional[str] = Field(None, alias='authorization_name')

    # The name or IP address of your provider's SIP domain (example: CDC.WEB). 
    domain: typing.Optional[str] = Field(None, alias='domain')

    # The password generated for the user in the SIP account.
    password: typing.Optional[str] = Field(None, alias='password')

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.
    proxy_server: typing.Optional[str] = Field(None, alias='proxy_server')

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.
    proxy_server2: typing.Optional[str] = Field(None, alias='proxy_server2')

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.
    proxy_server3: typing.Optional[str] = Field(None, alias='proxy_server3')

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server: typing.Optional[str] = Field(None, alias='register_server')

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server2: typing.Optional[str] = Field(None, alias='register_server2')

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server3: typing.Optional[str] = Field(None, alias='register_server3')

    # The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.
    registration_expire_time: typing.Optional[int] = Field(None, alias='registration_expire_time')

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol: typing.Optional[Literal["UDP", "TCP", "TLS", "AUTO"]] = Field(None, alias='transport_protocol')

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol2: typing.Optional[Literal["UDP", "TCP", "TLS", "AUTO"]] = Field(None, alias='transport_protocol2')

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol3: typing.Optional[Literal["UDP", "TCP", "TLS", "AUTO"]] = Field(None, alias='transport_protocol3')

    # The email address of the user to associate with the SIP Phone. Can add `.win`, `.mac`, `.android`, `.ipad`, `.iphone`, `.linux`, `.pc`, `.mobile`, `.pad` at the end of the email (for example, `user@example.com.mac`) to add accounts for different platforms for the same user.
    user_email: typing.Optional[str] = Field(None, alias='user_email')

    # The phone number associated with the user in the SIP account.
    user_name: typing.Optional[str] = Field(None, alias='user_name')

    # The number to dial for checking voicemail.
    voice_mail: typing.Optional[str] = Field(None, alias='voice_mail')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
