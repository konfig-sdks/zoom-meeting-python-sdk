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


class TspAddUserTspAccountResponseDialInNumbers(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    List of dial in numbers.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TspAddUserTspAccountResponseDialInNumbersItem']:
            return TspAddUserTspAccountResponseDialInNumbersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TspAddUserTspAccountResponseDialInNumbersItem'], typing.List['TspAddUserTspAccountResponseDialInNumbersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TspAddUserTspAccountResponseDialInNumbers':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TspAddUserTspAccountResponseDialInNumbersItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.tsp_add_user_tsp_account_response_dial_in_numbers_item import TspAddUserTspAccountResponseDialInNumbersItem
