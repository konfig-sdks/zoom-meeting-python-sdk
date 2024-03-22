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


class WebinarsCreatePollResponseQuestions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the poll's questions.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['WebinarsCreatePollResponseQuestionsItem']:
            return WebinarsCreatePollResponseQuestionsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['WebinarsCreatePollResponseQuestionsItem'], typing.List['WebinarsCreatePollResponseQuestionsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WebinarsCreatePollResponseQuestions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'WebinarsCreatePollResponseQuestionsItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.webinars_create_poll_response_questions_item import WebinarsCreatePollResponseQuestionsItem
