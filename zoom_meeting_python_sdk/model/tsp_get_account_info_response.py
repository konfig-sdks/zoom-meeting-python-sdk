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


class TspGetAccountInfoResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            dial_in_number_unrestricted = schemas.BoolSchema
        
            @staticmethod
            def dial_in_numbers() -> typing.Type['TspGetAccountInfoResponseDialInNumbers']:
                return TspGetAccountInfoResponseDialInNumbers
            enable = schemas.BoolSchema
            master_account_setting_extended = schemas.BoolSchema
            modify_credential_forbidden = schemas.BoolSchema
            
            
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
            tsp_enabled = schemas.BoolSchema
            tsp_provider = schemas.StrSchema
            __annotations__ = {
                "dial_in_number_unrestricted": dial_in_number_unrestricted,
                "dial_in_numbers": dial_in_numbers,
                "enable": enable,
                "master_account_setting_extended": master_account_setting_extended,
                "modify_credential_forbidden": modify_credential_forbidden,
                "tsp_bridge": tsp_bridge,
                "tsp_enabled": tsp_enabled,
                "tsp_provider": tsp_provider,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dial_in_number_unrestricted"]) -> MetaOapg.properties.dial_in_number_unrestricted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dial_in_numbers"]) -> 'TspGetAccountInfoResponseDialInNumbers': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable"]) -> MetaOapg.properties.enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["master_account_setting_extended"]) -> MetaOapg.properties.master_account_setting_extended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["modify_credential_forbidden"]) -> MetaOapg.properties.modify_credential_forbidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tsp_bridge"]) -> MetaOapg.properties.tsp_bridge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tsp_enabled"]) -> MetaOapg.properties.tsp_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tsp_provider"]) -> MetaOapg.properties.tsp_provider: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dial_in_number_unrestricted", "dial_in_numbers", "enable", "master_account_setting_extended", "modify_credential_forbidden", "tsp_bridge", "tsp_enabled", "tsp_provider", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dial_in_number_unrestricted"]) -> typing.Union[MetaOapg.properties.dial_in_number_unrestricted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dial_in_numbers"]) -> typing.Union['TspGetAccountInfoResponseDialInNumbers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable"]) -> typing.Union[MetaOapg.properties.enable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["master_account_setting_extended"]) -> typing.Union[MetaOapg.properties.master_account_setting_extended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["modify_credential_forbidden"]) -> typing.Union[MetaOapg.properties.modify_credential_forbidden, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tsp_bridge"]) -> typing.Union[MetaOapg.properties.tsp_bridge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tsp_enabled"]) -> typing.Union[MetaOapg.properties.tsp_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tsp_provider"]) -> typing.Union[MetaOapg.properties.tsp_provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dial_in_number_unrestricted", "dial_in_numbers", "enable", "master_account_setting_extended", "modify_credential_forbidden", "tsp_bridge", "tsp_enabled", "tsp_provider", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dial_in_number_unrestricted: typing.Union[MetaOapg.properties.dial_in_number_unrestricted, bool, schemas.Unset] = schemas.unset,
        dial_in_numbers: typing.Union['TspGetAccountInfoResponseDialInNumbers', schemas.Unset] = schemas.unset,
        enable: typing.Union[MetaOapg.properties.enable, bool, schemas.Unset] = schemas.unset,
        master_account_setting_extended: typing.Union[MetaOapg.properties.master_account_setting_extended, bool, schemas.Unset] = schemas.unset,
        modify_credential_forbidden: typing.Union[MetaOapg.properties.modify_credential_forbidden, bool, schemas.Unset] = schemas.unset,
        tsp_bridge: typing.Union[MetaOapg.properties.tsp_bridge, str, schemas.Unset] = schemas.unset,
        tsp_enabled: typing.Union[MetaOapg.properties.tsp_enabled, bool, schemas.Unset] = schemas.unset,
        tsp_provider: typing.Union[MetaOapg.properties.tsp_provider, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TspGetAccountInfoResponse':
        return super().__new__(
            cls,
            *args,
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            dial_in_numbers=dial_in_numbers,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.tsp_get_account_info_response_dial_in_numbers import TspGetAccountInfoResponseDialInNumbers
