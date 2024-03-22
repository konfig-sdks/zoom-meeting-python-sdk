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


class MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemAnswers(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    The survey question's available answers. This field requires a **minimum** of two answers. 

* For `single` and `multiple` questions, you can only provide a maximum of 50 answers. 
* For `matching` polls, you can only provide a maximum of 16 answers. 
* For `rank_order` polls, you can only provide a maximum of seven answers.
    """


    class MetaOapg:
        
        
        class items(
            schemas.StrSchema
        ):
            pass

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MeetingsGetMeetingSurveyResponseCustomSurveyQuestionsItemAnswers':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
