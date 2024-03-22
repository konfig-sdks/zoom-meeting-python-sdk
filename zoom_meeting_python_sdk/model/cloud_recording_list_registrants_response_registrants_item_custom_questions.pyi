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


class CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about custom questions.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestionsItem']:
            return CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestionsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestionsItem'], typing.List['CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestionsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestionsItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.cloud_recording_list_registrants_response_registrants_item_custom_questions_item import CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestionsItem
