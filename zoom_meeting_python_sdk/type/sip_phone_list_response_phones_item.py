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


class RequiredSipPhoneListResponsePhonesItem(TypedDict):
    pass

class OptionalSipPhoneListResponsePhonesItem(TypedDict, total=False):
    # The authorization name of the user that is registered for SIP phone.
    authorization_name: str

    # The name or IP address of your provider's SIP domain.
    domain: str

    # The SIP phone ID.
    id: str

    # The password generated for the user in the SIP account. 
    password: str

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.
    proxy_server: str

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.
    proxy_server2: str

    # The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.
    proxy_server3: str

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server: str

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server2: str

    # The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.
    register_server3: str

    # The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server. 
    registration_expire_time: int

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol: str

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol2: str

    # Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.
    transport_protocol3: str

    # The email address of the user to associate with the SIP Phone. Can add `.win`, `.mac`, `.android`, `.ipad`, `.iphone`, `.linux`, `.pc`, `.mobile`, `.pad` at the end of the email (for example, `user@example.com.mac`) to add accounts for different platforms for the same user.
    user_email: str

    # The phone number associated with the user in the SIP account. 
    user_name: str

    # The number to dial for checking voicemail.
    voice_mail: str

class SipPhoneListResponsePhonesItem(RequiredSipPhoneListResponsePhonesItem, OptionalSipPhoneListResponsePhonesItem):
    pass
