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


class SipPhoneUpdateSpecificPhoneRequest(BaseModel):
    # The authorization name of the user that is registered for SIP phone.
    authorization_name: str = Field(alias='authorization_name')

    # The name or IP address of your provider's SIP domain (example: CDC.WEB). 
    domain: str = Field(alias='domain')

    # The password generated for the user in the SIP account.
    password: str = Field(alias='password')

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.
    proxy_server: str = Field(alias='proxy_server')

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.
    proxy_server2: str = Field(alias='proxy_server2')

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.
    proxy_server3: str = Field(alias='proxy_server3')

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server: str = Field(alias='register_server')

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server2: str = Field(alias='register_server2')

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server3: str = Field(alias='register_server3')

    # The phone number associated with the user in the SIP account.
    user_name: str = Field(alias='user_name')

    # The number to dial for checking voicemail.
    voice_mail: str = Field(alias='voice_mail')

    # The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.
    registration_expire_time: typing.Optional[int] = Field(None, alias='registration_expire_time')

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol: typing.Optional[Literal["UDP", "TCP", "TLS", "AUTO"]] = Field(None, alias='transport_protocol')

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol2: typing.Optional[Literal["UDP", "TCP", "TLS", "AUTO"]] = Field(None, alias='transport_protocol2')

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol3: typing.Optional[Literal["UDP", "TCP", "TLS", "AUTO"]] = Field(None, alias='transport_protocol3')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
