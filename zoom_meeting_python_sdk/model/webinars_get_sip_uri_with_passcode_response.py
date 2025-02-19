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


class WebinarsGetSipUriWithPasscodeResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the webinar's encoded SIP URI.
    """


    class MetaOapg:
        
        class properties:
            sip_dialing = schemas.StrSchema
            paid_crc_plan_participant = schemas.BoolSchema
            participant_identifier_code = schemas.StrSchema
            expire_in = schemas.Int64Schema
            __annotations__ = {
                "sip_dialing": sip_dialing,
                "paid_crc_plan_participant": paid_crc_plan_participant,
                "participant_identifier_code": participant_identifier_code,
                "expire_in": expire_in,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sip_dialing"]) -> MetaOapg.properties.sip_dialing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paid_crc_plan_participant"]) -> MetaOapg.properties.paid_crc_plan_participant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participant_identifier_code"]) -> MetaOapg.properties.participant_identifier_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expire_in"]) -> MetaOapg.properties.expire_in: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sip_dialing", "paid_crc_plan_participant", "participant_identifier_code", "expire_in", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sip_dialing"]) -> typing.Union[MetaOapg.properties.sip_dialing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paid_crc_plan_participant"]) -> typing.Union[MetaOapg.properties.paid_crc_plan_participant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participant_identifier_code"]) -> typing.Union[MetaOapg.properties.participant_identifier_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expire_in"]) -> typing.Union[MetaOapg.properties.expire_in, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sip_dialing", "paid_crc_plan_participant", "participant_identifier_code", "expire_in", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        sip_dialing: typing.Union[MetaOapg.properties.sip_dialing, str, schemas.Unset] = schemas.unset,
        paid_crc_plan_participant: typing.Union[MetaOapg.properties.paid_crc_plan_participant, bool, schemas.Unset] = schemas.unset,
        participant_identifier_code: typing.Union[MetaOapg.properties.participant_identifier_code, str, schemas.Unset] = schemas.unset,
        expire_in: typing.Union[MetaOapg.properties.expire_in, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsGetSipUriWithPasscodeResponse':
        return super().__new__(
            cls,
            *args,
            sip_dialing=sip_dialing,
            paid_crc_plan_participant=paid_crc_plan_participant,
            participant_identifier_code=participant_identifier_code,
            expire_in=expire_in,
            _configuration=_configuration,
            **kwargs,
        )
