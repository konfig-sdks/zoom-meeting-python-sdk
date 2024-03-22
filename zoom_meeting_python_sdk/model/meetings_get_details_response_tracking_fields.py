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


class MeetingsGetDetailsResponseTrackingFields(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Tracking fields.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MeetingsGetDetailsResponseTrackingFieldsItem']:
            return MeetingsGetDetailsResponseTrackingFieldsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MeetingsGetDetailsResponseTrackingFieldsItem'], typing.List['MeetingsGetDetailsResponseTrackingFieldsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MeetingsGetDetailsResponseTrackingFields':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MeetingsGetDetailsResponseTrackingFieldsItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.meetings_get_details_response_tracking_fields_item import MeetingsGetDetailsResponseTrackingFieldsItem
