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


class MeetingsUpdateLivestreamRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Meeting live stream.
    """


    class MetaOapg:
        required = {
            "page_url",
            "stream_key",
            "stream_url",
        }
        
        class properties:
            
            
            class page_url(
                schemas.StrSchema
            ):
                pass
            
            
            class stream_key(
                schemas.StrSchema
            ):
                pass
            
            
            class stream_url(
                schemas.StrSchema
            ):
                pass
            resolution = schemas.StrSchema
            __annotations__ = {
                "page_url": page_url,
                "stream_key": stream_key,
                "stream_url": stream_url,
                "resolution": resolution,
            }
    
    page_url: MetaOapg.properties.page_url
    stream_key: MetaOapg.properties.stream_key
    stream_url: MetaOapg.properties.stream_url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_url"]) -> MetaOapg.properties.page_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_key"]) -> MetaOapg.properties.stream_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream_url"]) -> MetaOapg.properties.stream_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolution"]) -> MetaOapg.properties.resolution: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["page_url", "stream_key", "stream_url", "resolution", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_url"]) -> MetaOapg.properties.page_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_key"]) -> MetaOapg.properties.stream_key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream_url"]) -> MetaOapg.properties.stream_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolution"]) -> typing.Union[MetaOapg.properties.resolution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page_url", "stream_key", "stream_url", "resolution", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        page_url: typing.Union[MetaOapg.properties.page_url, str, ],
        stream_key: typing.Union[MetaOapg.properties.stream_key, str, ],
        stream_url: typing.Union[MetaOapg.properties.stream_url, str, ],
        resolution: typing.Union[MetaOapg.properties.resolution, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MeetingsUpdateLivestreamRequest':
        return super().__new__(
            cls,
            *args,
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            resolution=resolution,
            _configuration=_configuration,
            **kwargs,
        )
