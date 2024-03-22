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


class MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpreters(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the meeting's language interpreters.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpretersItem']:
            return MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpretersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpretersItem'], typing.List['MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpretersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpreters':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpretersItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.meetings_update_details_request_settings_language_interpretation_interpreters_item import MeetingsUpdateDetailsRequestSettingsLanguageInterpretationInterpretersItem
