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


class TspAddUserTspAccountResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    List of TSP accounts.
    """


    class MetaOapg:
        required = {
            "conference_code",
            "leader_pin",
        }
        
        class properties:
            
            
            class conference_code(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 16
                    min_length = 1
            
            
            class leader_pin(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 16
                    min_length = 1
            id = schemas.StrSchema
        
            @staticmethod
            def dial_in_numbers() -> typing.Type['TspAddUserTspAccountResponseDialInNumbers']:
                return TspAddUserTspAccountResponseDialInNumbers
            
            
            class tsp_bridge(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "US_TSP_TB": "US_TSP_TB",
                        "EU_TSP_TB": "EU_TSP_TB",
                    }
                
                @schemas.classproperty
                def US_TSP_TB(cls):
                    return cls("US_TSP_TB")
                
                @schemas.classproperty
                def EU_TSP_TB(cls):
                    return cls("EU_TSP_TB")
            __annotations__ = {
                "conference_code": conference_code,
                "leader_pin": leader_pin,
                "id": id,
                "dial_in_numbers": dial_in_numbers,
                "tsp_bridge": tsp_bridge,
            }
    
    conference_code: MetaOapg.properties.conference_code
    leader_pin: MetaOapg.properties.leader_pin
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conference_code"]) -> MetaOapg.properties.conference_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leader_pin"]) -> MetaOapg.properties.leader_pin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dial_in_numbers"]) -> 'TspAddUserTspAccountResponseDialInNumbers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tsp_bridge"]) -> MetaOapg.properties.tsp_bridge: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conference_code", "leader_pin", "id", "dial_in_numbers", "tsp_bridge", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conference_code"]) -> MetaOapg.properties.conference_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leader_pin"]) -> MetaOapg.properties.leader_pin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dial_in_numbers"]) -> typing.Union['TspAddUserTspAccountResponseDialInNumbers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tsp_bridge"]) -> typing.Union[MetaOapg.properties.tsp_bridge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conference_code", "leader_pin", "id", "dial_in_numbers", "tsp_bridge", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conference_code: typing.Union[MetaOapg.properties.conference_code, str, ],
        leader_pin: typing.Union[MetaOapg.properties.leader_pin, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        dial_in_numbers: typing.Union['TspAddUserTspAccountResponseDialInNumbers', schemas.Unset] = schemas.unset,
        tsp_bridge: typing.Union[MetaOapg.properties.tsp_bridge, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TspAddUserTspAccountResponse':
        return super().__new__(
            cls,
            *args,
            conference_code=conference_code,
            leader_pin=leader_pin,
            id=id,
            dial_in_numbers=dial_in_numbers,
            tsp_bridge=tsp_bridge,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.tsp_add_user_tsp_account_response_dial_in_numbers import TspAddUserTspAccountResponseDialInNumbers
