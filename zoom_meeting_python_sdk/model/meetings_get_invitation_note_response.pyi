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


class MeetingsGetInvitationNoteResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Meeting invitation details.
    """


    class MetaOapg:
        
        class properties:
            invitation = schemas.StrSchema
        
            @staticmethod
            def sip_links() -> typing.Type['MeetingsGetInvitationNoteResponseSipLinks']:
                return MeetingsGetInvitationNoteResponseSipLinks
            __annotations__ = {
                "invitation": invitation,
                "sip_links": sip_links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invitation"]) -> MetaOapg.properties.invitation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sip_links"]) -> 'MeetingsGetInvitationNoteResponseSipLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["invitation", "sip_links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invitation"]) -> typing.Union[MetaOapg.properties.invitation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sip_links"]) -> typing.Union['MeetingsGetInvitationNoteResponseSipLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["invitation", "sip_links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        invitation: typing.Union[MetaOapg.properties.invitation, str, schemas.Unset] = schemas.unset,
        sip_links: typing.Union['MeetingsGetInvitationNoteResponseSipLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsGetInvitationNoteResponse':
        return super().__new__(
            cls,
            *args,
            invitation=invitation,
            sip_links=sip_links,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.meetings_get_invitation_note_response_sip_links import MeetingsGetInvitationNoteResponseSipLinks
