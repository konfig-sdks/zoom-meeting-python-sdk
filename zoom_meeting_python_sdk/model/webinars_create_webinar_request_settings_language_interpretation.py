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


class WebinarsCreateWebinarRequestSettingsLanguageInterpretation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The webinar's [language interpretation settings](https://support.zoom.us/hc/en-us/articles/360034919791-Language-interpretation-in-meetings-and-webinars). Make sure to add the language in the web portal in order to use it in the API. See link for details. 

**Note:** This feature is only available for certain Webinar add-on, Education, and Business and higher plans. If this feature is not enabled on the host's account, this setting will **not** be applied to the webinar. This is not supported for simulive webinars.
    """


    class MetaOapg:
        
        class properties:
            enable = schemas.BoolSchema
        
            @staticmethod
            def interpreters() -> typing.Type['WebinarsCreateWebinarRequestSettingsLanguageInterpretationInterpreters']:
                return WebinarsCreateWebinarRequestSettingsLanguageInterpretationInterpreters
            __annotations__ = {
                "enable": enable,
                "interpreters": interpreters,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable"]) -> MetaOapg.properties.enable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interpreters"]) -> 'WebinarsCreateWebinarRequestSettingsLanguageInterpretationInterpreters': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enable", "interpreters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable"]) -> typing.Union[MetaOapg.properties.enable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interpreters"]) -> typing.Union['WebinarsCreateWebinarRequestSettingsLanguageInterpretationInterpreters', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enable", "interpreters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        enable: typing.Union[MetaOapg.properties.enable, bool, schemas.Unset] = schemas.unset,
        interpreters: typing.Union['WebinarsCreateWebinarRequestSettingsLanguageInterpretationInterpreters', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WebinarsCreateWebinarRequestSettingsLanguageInterpretation':
        return super().__new__(
            cls,
            *args,
            enable=enable,
            interpreters=interpreters,
            _configuration=_configuration,
            **kwargs,
        )

from zoom_meeting_python_sdk.model.webinars_create_webinar_request_settings_language_interpretation_interpreters import WebinarsCreateWebinarRequestSettingsLanguageInterpretationInterpreters
